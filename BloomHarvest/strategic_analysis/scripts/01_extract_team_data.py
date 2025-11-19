#!/usr/bin/env python3
"""
Extract structured data from interview transcripts
Handles multilingual content (Arabic/English)
"""
import re
import json
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional
import sys

@dataclass
class TeamProfile:
    """Structured team data"""
    name: str
    founder: str
    program: str  # ACSI4 Accel, HMN 2023, etc.
    date: str
    company_name: str
    stage: str  # Bootcamp, Accelerator, Sprint
    location: Optional[str] = None
    sector: Optional[str] = None
    challenges: List[str] = None
    outcomes: List[str] = None
    partnerships_needed: bool = False
    grant_received: bool = False
    key_learnings: List[str] = None
    transcript_file: str = ""

    def __post_init__(self):
        if self.challenges is None:
            self.challenges = []
        if self.outcomes is None:
            self.outcomes = []
        if self.key_learnings is None:
            self.key_learnings = []

def parse_filename(filename: str) -> Dict[str, str]:
    """Extract metadata from interview filename"""
    # Pattern: [Transcript] Name Date Company (Program).md
    pattern = r'\[Trans[c]?ript\]\s+([^0-9]+)\s+(\d+\s+\w+)\s+(.+?)\s+\((.+?)\)\.md'
    match = re.match(pattern, filename)

    if match:
        founder = match.group(1).strip()
        date = match.group(2).strip()
        company = match.group(3).strip()
        program = match.group(4).strip()

        # Extract stage from program
        if 'Accel' in program:
            stage = 'Accelerator'
        elif 'Bootcamp' in program:
            stage = 'Bootcamp'
        elif 'Sprint' in program:
            stage = 'Sprint'
        elif 'Applied' in program:
            stage = 'Applied'
        else:
            stage = 'Unknown'

        return {
            'founder': founder,
            'date': date,
            'company': company,
            'program': program,
            'stage': stage
        }

    return {}

def extract_keywords(text: str) -> Dict[str, any]:
    """Extract key information from transcript text"""
    text_lower = text.lower()

    # Detect partnerships mentioned
    partnerships_keywords = ['partnership', 'partner', 'collaboration', 'بارتنرشيب', 'بارتنر']
    partnerships_needed = any(kw in text_lower for kw in partnerships_keywords)

    # Detect grant mentioned
    grant_keywords = ['grant', 'جرانت', 'funding', 'تمويل']
    grant_received = any(kw in text_lower for kw in grant_keywords)

    # Detect sectors (example keywords)
    sectors = {
        'edtech': ['education', 'learning', 'school', 'teacher', 'student', 'تعليم', 'مدرسة'],
        'health': ['health', 'therapy', 'medical', 'صحة', 'علاج'],
        'agtech': ['agriculture', 'farm', 'زراعة', 'مزرعة'],
        'fintech': ['finance', 'payment', 'مالي', 'دفع'],
        'climate': ['climate', 'environment', 'green', 'sustainability', 'بيئة', 'مناخ'],
        'ecommerce': ['ecommerce', 'marketplace', 'platform', 'تجارة']
    }

    detected_sector = None
    for sector, keywords in sectors.items():
        if any(kw in text_lower for kw in keywords):
            detected_sector = sector
            break

    return {
        'partnerships_needed': partnerships_needed,
        'grant_received': grant_received,
        'sector': detected_sector
    }

def process_transcript(file_path: Path) -> TeamProfile:
    """Process a single transcript and extract structured data"""

    # Parse filename
    metadata = parse_filename(file_path.name)

    # Read content
    content = file_path.read_text(encoding='utf-8')

    # Extract keywords
    keywords = extract_keywords(content)

    # Create team profile
    team = TeamProfile(
        name=metadata.get('company', 'Unknown'),
        founder=metadata.get('founder', 'Unknown'),
        program=metadata.get('program', 'Unknown'),
        date=metadata.get('date', 'Unknown'),
        company_name=metadata.get('company', 'Unknown'),
        stage=metadata.get('stage', 'Unknown'),
        sector=keywords.get('sector'),
        partnerships_needed=keywords['partnerships_needed'],
        grant_received=keywords['grant_received'],
        transcript_file=str(file_path)
    )

    return team

def main():
    """Main extraction pipeline"""

    # Paths
    base_dir = Path("/home/user/BloomHarvest")
    interview_dir = base_dir / "Bloom_s Research/Bloom_s Interviews/converted_markdown"
    output_dir = base_dir / "strategic_analysis/data"

    # Process all transcripts
    teams = []
    for transcript_file in sorted(interview_dir.glob("*.md")):
        try:
            team = process_transcript(transcript_file)
            teams.append(team)
            print(f"✓ {team.company_name} ({team.program})")
        except Exception as e:
            print(f"✗ {transcript_file.name}: {e}")

    # Save structured data
    output_file = output_dir / "teams_structured.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump([asdict(t) for t in teams], f, indent=2, ensure_ascii=False)

    print(f"\n✅ Extracted {len(teams)} team profiles")
    print(f"📄 Saved to: {output_file}")

    # Generate summary statistics
    stats = {
        'total_teams': len(teams),
        'by_program': {},
        'by_stage': {},
        'by_sector': {},
        'partnerships_needed': sum(1 for t in teams if t.partnerships_needed),
        'grants_received': sum(1 for t in teams if t.grant_received)
    }

    for team in teams:
        # Count by program
        stats['by_program'][team.program] = stats['by_program'].get(team.program, 0) + 1
        # Count by stage
        stats['by_stage'][team.stage] = stats['by_stage'].get(team.stage, 0) + 1
        # Count by sector
        if team.sector:
            stats['by_sector'][team.sector] = stats['by_sector'].get(team.sector, 0) + 1

    stats_file = output_dir / "teams_summary.json"
    with open(stats_file, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2)

    print(f"\n📊 Summary Statistics:")
    print(f"   Total teams: {stats['total_teams']}")
    print(f"   Partnerships needed: {stats['partnerships_needed']}")
    print(f"   Grants received: {stats['grants_received']}")
    print(f"   By stage: {stats['by_stage']}")

    return teams

if __name__ == "__main__":
    main()
