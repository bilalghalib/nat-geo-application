#!/usr/bin/env python3
"""
Extract insights from interview transcripts
Processes 20 interviews to find themes, quotes, patterns, and actionable learnings
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict, Counter

# Base paths
BASE_DIR = Path(__file__).parent.parent.parent
INTERVIEWS_DIR = BASE_DIR / "Bloom_History_And_Research/Bloom_Teams/Interview_Transcripts"
OUTPUT_DIR = BASE_DIR / "strategic_analysis/outputs/insights"

# Create output directory
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Themes to look for (informed by reading transcripts)
THEMES = {
    "community_support": [
        "support", "community", "network", "connections", "relationships",
        "peer", "help each other", "together", "collective"
    ],
    "sustainability": [
        "sustainable", "sustainability", "donor", "funding", "funds",
        "revenue", "income", "financial", "self-sustaining"
    ],
    "programs_valuable": [
        "program", "accelerator", "boot camp", "training", "learned",
        "supportive", "commitment", "experts", "mentorship"
    ],
    "post_program_needs": [
        "after", "follow up", "ended", "continued", "ongoing",
        "stay connected", "alumni", "maintain"
    ],
    "crisis_context": [
        "crisis", "war", "Lebanon", "Palestine", "conflict", "electricity",
        "economic collapse", "instability", "challenges"
    ],
    "cooperative_interest": [
        "cooperative", "pool", "sharing", "collective", "mutual aid",
        "together", "ubuntu", "collaboration"
    ],
    "pain_points": [
        "struggle", "difficult", "challenge", "problem", "frustration",
        "hard", "barrier", "obstacle"
    ],
    "opportunities": [
        "opportunity", "potential", "possibility", "excited", "interested",
        "curious", "innovative", "experiment"
    ],
    "resources_needed": [
        "need", "lacking", "missing", "require", "want",
        "access", "resources", "capacity"
    ],
    "values": [
        "ubuntu", "values", "ethics", "regenerative", "anti-extractive",
        "wellbeing", "impact", "purpose", "why"
    ]
}

def load_interviews():
    """Load all interview transcripts"""
    interviews = []
    for md_file in sorted(INTERVIEWS_DIR.glob("*.md")):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract name from filename
            name = md_file.stem.replace("[Transcript] ", "").replace("[Transcsript] ", "")
            interviews.append({
                "name": name,
                "file": md_file.name,
                "content": content
            })
    return interviews

def extract_speakers(content):
    """Extract speaker lines from transcript"""
    lines = content.split('\n')
    speakers = defaultdict(list)
    current_speaker = None

    for line in lines:
        # Match speaker pattern: "00:00:00 Name\"
        speaker_match = re.match(r'\d+→\d+:\d+:\d+ (.+?)\\$', line)
        if speaker_match:
            current_speaker = speaker_match.group(1).strip()
        elif current_speaker and line.strip() and not line.startswith('!') and not line.startswith('\\'):
            # Clean up the line
            clean_line = line.strip().replace('\\', '')
            if clean_line:
                speakers[current_speaker].append(clean_line)

    return speakers

def find_theme_quotes(content, theme_name, keywords):
    """Find quotes related to a theme"""
    quotes = []
    lines = content.split('\n')

    for i, line in enumerate(lines):
        # Check if line contains any theme keywords
        line_lower = line.lower()
        if any(keyword.lower() in line_lower for keyword in keywords):
            # Extract context (speaker + quote)
            speaker_match = re.match(r'\d+→\d+:\d+:\d+ (.+?)\\$', line)
            if speaker_match:
                speaker = speaker_match.group(1).strip()
                # Get next few lines as the quote
                quote_lines = []
                for j in range(i+1, min(i+10, len(lines))):
                    if re.match(r'\d+→\d+:\d+:\d+', lines[j]):
                        break
                    quote_line = lines[j].strip().replace('\\', '')
                    if quote_line:
                        quote_lines.append(quote_line)

                if quote_lines:
                    quote = ' '.join(quote_lines)
                    if len(quote) > 50:  # Only keep substantial quotes
                        quotes.append({
                            "speaker": speaker,
                            "quote": quote[:500],  # Truncate very long quotes
                            "keywords_matched": [k for k in keywords if k.lower() in line_lower]
                        })

    return quotes

def extract_bilal_questions(interviews):
    """Extract Bilal's questions to understand what he's exploring"""
    questions = []

    for interview in interviews:
        speakers = extract_speakers(interview['content'])
        if 'Bilal Ghalib' in speakers or 'Bilal' in speakers:
            bilal_lines = speakers.get('Bilal Ghalib', []) + speakers.get('Bilal', [])
            for line in bilal_lines:
                # Look for questions
                if '?' in line and len(line) > 30:
                    questions.append({
                        "interview": interview['name'],
                        "question": line[:300]
                    })

    return questions

def analyze_interviews():
    """Main analysis function"""
    print("🔍 Extracting insights from 20 interviews...")
    print("="*80)

    interviews = load_interviews()
    print(f"✅ Loaded {len(interviews)} interviews\n")

    # 1. Theme analysis
    print("📊 Analyzing themes...")
    theme_analysis = {}
    all_theme_quotes = defaultdict(list)

    for theme_name, keywords in THEMES.items():
        print(f"  - {theme_name}")
        theme_count = 0
        for interview in interviews:
            # Count mentions
            content_lower = interview['content'].lower()
            mentions = sum(content_lower.count(kw.lower()) for kw in keywords)
            theme_count += mentions

            # Extract quotes
            quotes = find_theme_quotes(interview['content'], theme_name, keywords)
            for quote in quotes:
                all_theme_quotes[theme_name].append({
                    **quote,
                    "interview": interview['name']
                })

        theme_analysis[theme_name] = {
            "total_mentions": theme_count,
            "avg_per_interview": round(theme_count / len(interviews), 1),
            "keywords": keywords,
            "top_quotes": all_theme_quotes[theme_name][:10]  # Top 10 quotes per theme
        }

    # 2. Extract Bilal's questions
    print("\n❓ Extracting research questions...")
    questions = extract_bilal_questions(interviews)

    # 3. Speaker analysis
    print("\n👥 Analyzing speakers...")
    all_speakers = defaultdict(int)
    for interview in interviews:
        speakers = extract_speakers(interview['content'])
        for speaker, lines in speakers.items():
            all_speakers[speaker] += len(lines)

    # 4. Interview metadata
    print("\n📝 Compiling interview metadata...")
    interview_summary = []
    for interview in interviews:
        speakers = extract_speakers(interview['content'])
        word_count = len(interview['content'].split())
        interview_summary.append({
            "name": interview['name'],
            "file": interview['file'],
            "word_count": word_count,
            "speakers": list(speakers.keys()),
            "num_speakers": len(speakers)
        })

    # 5. Compile results
    results = {
        "metadata": {
            "total_interviews": len(interviews),
            "total_words": sum(i['word_count'] for i in interview_summary),
            "analysis_date": "2025-11-18"
        },
        "themes": theme_analysis,
        "bilal_questions": questions[:50],  # Top 50 questions
        "interviews": interview_summary,
        "speaker_stats": dict(sorted(all_speakers.items(), key=lambda x: x[1], reverse=True))
    }

    # Save results
    output_file = OUTPUT_DIR / "interview_insights.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Saved: {output_file}")

    # Generate human-readable reports
    generate_reports(results)

    return results

def generate_reports(results):
    """Generate human-readable insight reports"""

    # 1. Themes Report
    themes_report = OUTPUT_DIR / "themes_report.md"
    with open(themes_report, 'w', encoding='utf-8') as f:
        f.write("# Interview Themes Analysis\n\n")
        f.write(f"**Based on {results['metadata']['total_interviews']} interviews**\n\n")
        f.write("---\n\n")

        # Sort themes by mentions
        sorted_themes = sorted(
            results['themes'].items(),
            key=lambda x: x[1]['total_mentions'],
            reverse=True
        )

        for theme_name, data in sorted_themes:
            f.write(f"## {theme_name.replace('_', ' ').title()}\n\n")
            f.write(f"**Mentions:** {data['total_mentions']} ({data['avg_per_interview']} per interview)\n\n")
            f.write(f"**Keywords:** {', '.join(data['keywords'][:10])}\n\n")

            if data['top_quotes']:
                f.write("**Key Quotes:**\n\n")
                for i, quote in enumerate(data['top_quotes'][:5], 1):
                    f.write(f"{i}. *\"{quote['quote'][:200]}...\"*\n")
                    f.write(f"   — {quote['speaker']} ({quote['interview']})\n\n")

            f.write("---\n\n")

    print(f"✅ Saved: {themes_report}")

    # 2. Questions Report
    questions_report = OUTPUT_DIR / "research_questions.md"
    with open(questions_report, 'w', encoding='utf-8') as f:
        f.write("# Research Questions from Bilal\n\n")
        f.write("**Questions Bilal asked during interviews - shows what he's exploring**\n\n")
        f.write("---\n\n")

        for i, q in enumerate(results['bilal_questions'][:30], 1):
            f.write(f"{i}. *{q['question']}*\n")
            f.write(f"   (from {q['interview']})\n\n")

    print(f"✅ Saved: {questions_report}")

    # 3. Summary Report
    summary_report = OUTPUT_DIR / "insights_summary.md"
    with open(summary_report, 'w', encoding='utf-8') as f:
        f.write("# Interview Insights Summary\n\n")
        f.write("## Overview\n\n")
        f.write(f"- **Total interviews:** {results['metadata']['total_interviews']}\n")
        f.write(f"- **Total words:** {results['metadata']['total_words']:,}\n")
        f.write(f"- **Avg words/interview:** {results['metadata']['total_words']//results['metadata']['total_interviews']:,}\n\n")

        f.write("## Top Themes (by mentions)\n\n")
        sorted_themes = sorted(
            results['themes'].items(),
            key=lambda x: x[1]['total_mentions'],
            reverse=True
        )
        for i, (theme, data) in enumerate(sorted_themes[:5], 1):
            f.write(f"{i}. **{theme.replace('_', ' ').title()}** - {data['total_mentions']} mentions\n")

        f.write("\n## What We're Learning\n\n")
        f.write("See `themes_report.md` for detailed quotes and patterns.\n\n")
        f.write("See `research_questions.md` for questions Bilal is exploring.\n\n")
        f.write("---\n\n")
        f.write("*Generated from interview transcript analysis*\n")

    print(f"✅ Saved: {summary_report}")

if __name__ == "__main__":
    results = analyze_interviews()
    print("\n" + "="*80)
    print("✅ INSIGHTS EXTRACTION COMPLETE")
    print("="*80)
    print("\n📁 Check outputs:")
    print(f"  - {OUTPUT_DIR}/interview_insights.json")
    print(f"  - {OUTPUT_DIR}/themes_report.md")
    print(f"  - {OUTPUT_DIR}/research_questions.md")
    print(f"  - {OUTPUT_DIR}/insights_summary.md")
    print()
