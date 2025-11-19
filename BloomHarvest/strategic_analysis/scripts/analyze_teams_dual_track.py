#!/usr/bin/env python3
"""
Dual-Track Bloom Cooperative Analysis
Generates TWO rankings for TWO cooperative models:

TRACK 1: Islamic-Inspired Solidarity Circle (No/Low-Pay)
- Prioritizes: Recent relationships (ACSI3/4), values alignment, wellbeing focus
- Asks: Time commitment, vulnerability, solidarity values
- Offers: Peer support, shared learning, wellbeing-centered community

TRACK 2: Revenue-Share Investment Cooperative (2-5% Share)
- Prioritizes: Operating businesses (Stage 4-5), revenue generation, established teams
- Asks: Financial commitment (revenue share), long-term partnership
- Offers: Capital, strategic support, cooperative ownership
"""

import csv
import json
import re
from collections import Counter
from datetime import datetime
from urllib.parse import urlparse

# ==========================
# CONFIGURATION
# ==========================

CSV_PATH = "/Users/bilalghalib/Projects/scripts/BloomHarvest/Bloom_History_And_Research/Bloom_Teams/All_Teams_Airtable_Export_Teams X Programs + Workspace-All records.csv"
OUTPUT_DIR = "/Users/bilalghalib/Projects/scripts/BloomHarvest/strategic_analysis/outputs/team_prioritization/"

# Teams already interviewed (exclude from ranking)
INTERVIEWED_TEAMS = {
    'Badia', 'AnalySens', 'Clara', 'Little Stars', 'Ehab', 'Ecobath',
    'Ezalden', 'Hello World', 'Garene', 'Parents Hub', 'Ghinwa', 'Urban Leaf',
    'Hany', 'Takadam', 'ToRead', 'Hussein', 'RobotX', 'Iman', 'Hazel Farm',
    'Keren', 'Smart Sensory', 'Louai', 'Courssaty', 'Mohamad', 'GreeNX',
    'Nada', 'Tram Alwaan', 'Reem', 'Khutwa', 'Brightful', 'Salah', 'Blue Filter',
    'Salam', 'Palexus', 'Shaban', 'Pal-Lend', 'Siwar', 'PSYAI', 'Jur\'at Amal',
    'Sumayya', 'Rouh'
}

PRIORITY_PROGRAMS = {
    'ACSI4': 10, 'ACSI3': 9, 'ACSI2': 7,
    'LGA2': 5, 'LGA1': 4, 'HMN': 6, 'EON': 3
}

PRIORITY_COUNTRIES = {
    'Palestine': 10, 'Jordan': 9, 'Egypt': 9, 'Lebanon': 8,
    'Iraq': 7, 'Syria': 6
}

# ==========================
# HELPER FUNCTIONS
# ==========================

def extract_stage_number(stage_text):
    """Extract numeric stage from text like '4.2. Revenues stagnant...'"""
    if not stage_text:
        return 0
    match = re.match(r'(\d+)\.(\d+)', str(stage_text))
    if match:
        major = int(match.group(1))
        minor = int(match.group(2))
        return major + (minor / 10)
    return 0

def clean_team_name(name):
    """Remove program suffix and ID from team name"""
    if not name:
        return ""
    clean = re.sub(r'-\d+ in .*$', '', name)
    # Also remove " in ACSI3/4" suffixes
    clean = re.sub(r' in (ACSI\d+|LGA\d+|HMN|EON).*$', '', clean)
    return clean.strip()

def extract_country(geo_text):
    """Extract country from geographic location"""
    if not geo_text:
        return "Unknown"

    for country in PRIORITY_COUNTRIES.keys():
        if country in str(geo_text):
            return country

    if 'Lebanon' in str(geo_text) or 'Beirut' in str(geo_text):
        return 'Lebanon'
    if 'Palestine' in str(geo_text) or 'Gaza' in str(geo_text) or 'West Bank' in str(geo_text):
        return 'Palestine'
    if 'Jordan' in str(geo_text) or 'Amman' in str(geo_text):
        return 'Jordan'
    if 'Egypt' in str(geo_text) or 'Cairo' in str(geo_text):
        return 'Egypt'
    if 'Iraq' in str(geo_text) or 'Baghdad' in str(geo_text):
        return 'Iraq'

    return str(geo_text)

def has_website(url):
    """Check if URL is valid and not empty"""
    if not url or url == 'N/A':
        return False
    return bool(urlparse(str(url)).scheme)

def extract_social_links(social_text):
    """Extract social media links and identify platforms"""
    if not social_text or social_text == 'N/A':
        return []

    links = []
    text = str(social_text)

    platforms = {
        'instagram.com': 'Instagram',
        'facebook.com': 'Facebook',
        'linkedin.com': 'LinkedIn',
        'twitter.com': 'Twitter',
        'tiktok.com': 'TikTok'
    }

    for domain, platform in platforms.items():
        if domain in text.lower():
            links.append(platform)

    return links

def is_interviewed(team_name):
    """Check if team already interviewed"""
    clean_name = clean_team_name(team_name).lower()
    return any(name.lower() in clean_name for name in INTERVIEWED_TEAMS)

# ==========================
# SCORING FUNCTIONS
# ==========================

def score_solidarity_circle(team):
    """
    Score for TRACK 1: Islamic-Inspired Solidarity Circle

    Weights:
    - Program recency (40%): ACSI3/4 = fresh relationships
    - Geography (25%): MENA region (cultural alignment)
    - Has social media (15%): Shows engagement/activity
    - Team size (10%): Community capacity
    - Wellbeing-related sectors (10%): Mental health, education, community
    - Stage (0%): NOT prioritized - solidarity, not revenue
    """
    score = 0
    details = {}

    # 1. Program Recency (0-40) - HIGHEST WEIGHT
    program = team.get('program', '')
    program_score = 0
    if 'ACSI4' in program:
        program_score = 40
    elif 'ACSI3' in program:
        program_score = 35
    elif 'HMN' in program or 'HerMeNow' in program:
        program_score = 25
    elif 'ACSI2' in program:
        program_score = 20
    elif 'LGA2' in program or 'LGA1' in program:
        program_score = 15
    else:
        program_score = 5
    score += program_score
    details['program_score'] = program_score

    # 2. Geography (0-25)
    country = team.get('country', 'Unknown')
    geo_score = (PRIORITY_COUNTRIES.get(country, 0) / 10) * 25
    score += geo_score
    details['geo_score'] = geo_score

    # 3. Social Media Presence (0-15)
    social_count = len(team.get('social_platforms', []))
    social_score = min(social_count * 4, 15)
    score += social_score
    details['social_score'] = social_score

    # 4. Team Size (0-10)
    try:
        team_size = int(team.get('team_size', 0) or 0)
        if team_size >= 5:
            size_score = 10
        elif team_size >= 3:
            size_score = 7
        elif team_size >= 1:
            size_score = 5
        else:
            size_score = 0
    except:
        size_score = 0
    score += size_score
    details['size_score'] = size_score

    # 5. Wellbeing-Related Sectors (0-10)
    sectors = str(team.get('sectors', '')).lower()
    wellbeing_keywords = ['mental health', 'wellbeing', 'education', 'health care',
                          'community', 'social', 'culture', 'arts', 'environment']
    wellbeing_score = 10 if any(kw in sectors for kw in wellbeing_keywords) else 0
    score += wellbeing_score
    details['wellbeing_score'] = wellbeing_score

    team['solidarity_score'] = round(score, 2)
    team['solidarity_details'] = details

    return score

def score_investment_cooperative(team):
    """
    Score for TRACK 2: Revenue-Share Investment Cooperative

    Weights:
    - Stage (40%): 4-5 = operating with revenue (CRITICAL)
    - Has website (20%): Professional presence
    - Team size (15%): Scale/capacity
    - Geography (10%): MENA focus (lower priority)
    - Program (10%): Recency matters less
    - Social media (5%): Nice to have
    """
    score = 0
    details = {}

    # 1. Stage Score (0-40) - HIGHEST WEIGHT
    stage = team.get('stage_numeric', 0)
    if stage >= 5.0:  # Scaling with revenue
        stage_score = 40
    elif stage >= 4.0:  # Operating with revenue
        stage_score = 35
    elif stage >= 3.0:  # Prototype stage
        stage_score = 15
    elif stage >= 2.0:  # Ideation
        stage_score = 5
    else:
        stage_score = 0
    score += stage_score
    details['stage_score'] = stage_score

    # 2. Website (0-20)
    if team.get('has_website'):
        score += 20
        details['website_score'] = 20
    else:
        details['website_score'] = 0

    # 3. Team Size (0-15)
    try:
        team_size = int(team.get('team_size', 0) or 0)
        if team_size >= 10:
            size_score = 15
        elif team_size >= 5:
            size_score = 12
        elif team_size >= 3:
            size_score = 8
        elif team_size >= 1:
            size_score = 5
        else:
            size_score = 0
    except:
        size_score = 0
    score += size_score
    details['size_score'] = size_score

    # 4. Geography (0-10)
    country = team.get('country', 'Unknown')
    geo_score = (PRIORITY_COUNTRIES.get(country, 0) / 10) * 10
    score += geo_score
    details['geo_score'] = geo_score

    # 5. Program Recency (0-10)
    program = team.get('program', '')
    program_score = 0
    for prog, points in PRIORITY_PROGRAMS.items():
        if prog in str(program):
            program_score = (points / 10) * 10
            break
    score += program_score
    details['program_score'] = program_score

    # 6. Social Media (0-5)
    social_count = len(team.get('social_platforms', []))
    social_score = min(social_count * 1.5, 5)
    score += social_score
    details['social_score'] = social_score

    team['investment_score'] = round(score, 2)
    team['investment_details'] = details

    return score

# ==========================
# MAIN ANALYSIS
# ==========================

def analyze_dual_track():
    """Main analysis function for both tracks"""

    print("=" * 70)
    print("BLOOM DUAL-TRACK COOPERATIVE ANALYSIS")
    print("=" * 70)
    print()
    print("TRACK 1: Islamic-Inspired Solidarity Circle (No/Low-Pay)")
    print("TRACK 2: Revenue-Share Investment Cooperative (2-5%)")
    print()

    teams = []
    stats = {
        'total': 0,
        'interviewed': 0,
        'has_website': 0,
        'has_social': 0,
        'by_country': Counter(),
        'by_program': Counter(),
        'by_stage': Counter()
    }

    # Read CSV
    print(f"Reading: {CSV_PATH}")
    with open(CSV_PATH, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)

        for row in reader:
            stats['total'] += 1

            team_name = row.get('Name', '')
            if not team_name:
                continue

            if is_interviewed(team_name):
                stats['interviewed'] += 1
                continue

            # Build clean team record
            team = {
                'name': clean_team_name(team_name),
                'full_name': team_name,
                'email': row.get('Single Team Email', ''),
                'program': row.get('Program (from Workspace_Link)', ''),
                'created': row.get('Created Time', ''),
                'geographic_location': row.get('Geographic Location', '') or row.get('Geographic Location (founder)', ''),
                'country': extract_country(row.get('Geographic Location', '') or row.get('Geographic Location (founder)', '')),
                'website': row.get('Website', ''),
                'social_media': row.get('Social Media links', ''),
                'stage_text': row.get('Enterprise Stage Post Funding', '') or row.get('Stage_As_Text_Post-Funding', ''),
                'team_size': row.get('Current Team Size', ''),
                'sectors': row.get('Sectors', ''),
                'sdg_focus': row.get('SDG focus', ''),
                'workspace_link': row.get('Workspace_Link', '')
            }

            # Process derived fields
            team['stage_numeric'] = extract_stage_number(team['stage_text'])
            team['has_website'] = has_website(team['website'])
            team['social_platforms'] = extract_social_links(team['social_media'])

            # Calculate BOTH scores
            score_solidarity_circle(team)
            score_investment_cooperative(team)

            # Update stats
            if team['has_website']:
                stats['has_website'] += 1
            if team['social_platforms']:
                stats['has_social'] += 1
            stats['by_country'][team['country']] += 1
            stats['by_program'][team['program']] += 1
            if team['stage_numeric'] > 0:
                stage_rounded = int(team['stage_numeric'])
                stats['by_stage'][f"Stage {stage_rounded}"] += 1

            teams.append(team)

    print(f"✓ Processed {stats['total']} records")
    print(f"  - Excluded {stats['interviewed']} already interviewed")
    print(f"  - Analyzing {len(teams)} teams")
    print()

    # ==========================
    # TRACK 1: SOLIDARITY CIRCLE
    # ==========================

    teams_solidarity = sorted(teams, key=lambda x: x['solidarity_score'], reverse=True)

    print("=" * 70)
    print("TRACK 1: SOLIDARITY CIRCLE - TOP 30 CANDIDATES")
    print("=" * 70)
    print()
    print("Model: Islamic-inspired wellbeing-oriented mutual aid")
    print("Ask: No/low pay ($0-25/month), time commitment, vulnerability")
    print("Offer: Peer support, shared learning, deliberate rumination protocols")
    print()
    print(f"{'Rank':<6} {'Score':<7} {'Name':<40} {'Country':<12} {'Program':<15} {'Social':<10} {'Email?'}")
    print("-" * 140)

    for i, team in enumerate(teams_solidarity[:30], 1):
        social_icon = ",".join(team['social_platforms'][:2]) if team['social_platforms'] else "-"
        program_short = team['program'][:13] if team['program'] else "-"
        has_email = "✓" if team['email'].strip() else "-"

        print(f"{i:<6} {team['solidarity_score']:<7.1f} {team['name'][:38]:<40} {team['country'][:10]:<12} {program_short:<15} {social_icon[:8]:<10} {has_email}")

    print()

    # ==========================
    # TRACK 2: INVESTMENT COOP
    # ==========================

    teams_investment = sorted(teams, key=lambda x: x['investment_score'], reverse=True)

    print("=" * 70)
    print("TRACK 2: INVESTMENT COOPERATIVE - TOP 30 CANDIDATES")
    print("=" * 70)
    print()
    print("Model: Revenue-share cooperative (2-5% for 10 years)")
    print("Ask: Financial commitment, long-term partnership, governance participation")
    print("Offer: Capital, strategic support, cooperative ownership, peer learning")
    print()
    print(f"{'Rank':<6} {'Score':<7} {'Name':<40} {'Country':<12} {'Stage':<7} {'Website':<9} {'Team Size'}")
    print("-" * 140)

    for i, team in enumerate(teams_investment[:30], 1):
        web_icon = "✓" if team['has_website'] else "-"
        stage_display = f"{team['stage_numeric']:.1f}" if team['stage_numeric'] > 0 else "-"
        team_size = team['team_size'] if team['team_size'] else "-"

        print(f"{i:<6} {team['investment_score']:<7.1f} {team['name'][:38]:<40} {team['country'][:10]:<12} {stage_display:<7} {web_icon:<9} {team_size}")

    print()

    # ==========================
    # EXPORT DATA
    # ==========================

    import os
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Export Track 1: Solidarity Circle
    csv_solidarity = f"{OUTPUT_DIR}track1_solidarity_circle_top100.csv"
    with open(csv_solidarity, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['rank', 'solidarity_score', 'name', 'email', 'country', 'program',
                      'social_platforms', 'social_media', 'team_size', 'sectors',
                      'geographic_location', 'website', 'workspace_link', 'solidarity_details']
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()

        for i, team in enumerate(teams_solidarity[:100], 1):
            row = team.copy()
            row['rank'] = i
            row['social_platforms'] = ','.join(team['social_platforms'])
            row['solidarity_details'] = json.dumps(team['solidarity_details'])
            writer.writerow(row)

    print(f"✓ Track 1 exported: {csv_solidarity}")

    # Export Track 2: Investment Cooperative
    csv_investment = f"{OUTPUT_DIR}track2_investment_coop_top100.csv"
    with open(csv_investment, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['rank', 'investment_score', 'name', 'email', 'country', 'program',
                      'stage_numeric', 'stage_text', 'has_website', 'website',
                      'team_size', 'sectors', 'geographic_location', 'workspace_link',
                      'investment_details']
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()

        for i, team in enumerate(teams_investment[:100], 1):
            row = team.copy()
            row['rank'] = i
            row['investment_details'] = json.dumps(team['investment_details'])
            writer.writerow(row)

    print(f"✓ Track 2 exported: {csv_investment}")

    # Export combined JSON with both scores
    json_output = f"{OUTPUT_DIR}dual_track_all_teams.json"
    with open(json_output, 'w', encoding='utf-8') as f:
        json.dump({
            'metadata': {
                'generated': datetime.now().isoformat(),
                'total_teams': len(teams),
                'already_interviewed': stats['interviewed'],
                'track_1_model': 'Islamic-Inspired Solidarity Circle (No/Low-Pay)',
                'track_2_model': 'Revenue-Share Investment Cooperative (2-5%)'
            },
            'track_1_solidarity': teams_solidarity[:100],
            'track_2_investment': teams_investment[:100]
        }, f, indent=2, ensure_ascii=False)

    print(f"✓ Combined JSON exported: {json_output}")
    print()

    # ==========================
    # COMPARATIVE ANALYSIS
    # ==========================

    print("=" * 70)
    print("COMPARATIVE ANALYSIS: WHO APPEARS IN BOTH TRACKS?")
    print("=" * 70)
    print()

    # Find teams in top 30 of BOTH tracks
    solidarity_top30_names = set(t['name'] for t in teams_solidarity[:30])
    investment_top30_names = set(t['name'] for t in teams_investment[:30])

    overlap = solidarity_top30_names & investment_top30_names

    print(f"Teams in TOP 30 of BOTH tracks: {len(overlap)}")
    if overlap:
        print()
        for name in sorted(overlap):
            team = next(t for t in teams if t['name'] == name)
            print(f"  • {name[:50]:<50} | Solidarity: {team['solidarity_score']:.1f} | Investment: {team['investment_score']:.1f}")

    print()
    print(f"Track 1 ONLY (Solidarity-strong, Investment-weak): {len(solidarity_top30_names - investment_top30_names)}")
    print(f"Track 2 ONLY (Investment-strong, Solidarity-weak): {len(investment_top30_names - solidarity_top30_names)}")

    print()
    print("=" * 70)
    print("STRATEGIC RECOMMENDATIONS")
    print("=" * 70)
    print()

    print("OPTION A: Launch Track 1 FIRST (Solidarity Circle)")
    print("  • Lower barrier → faster launch → test cooperative governance")
    print("  • Build trust + track record → then offer Track 2 to 'graduates'")
    print("  • Timeline: 3-month solidarity circle → 6-month investment pilot")
    print()

    print("OPTION B: Launch Track 2 FIRST (Investment Cooperative)")
    print("  • Higher commitment → stronger foundation → revenue for sustainability")
    print("  • Use Track 2 revenue to subsidize Track 1 solidarity circle")
    print("  • Timeline: 6-month investment pilot → use funds for solidarity cohort")
    print()

    print("OPTION C: Launch BOTH in PARALLEL")
    print("  • Different value propositions → serve different needs")
    print("  • Track 1 = values alignment test → Track 2 = financial sustainability")
    print("  • Risk: Resource constraints, diluted focus")
    print("  • Mitigation: Start small (5-6 per track), shared infrastructure")
    print()

    print("RECOMMENDATION: Start with TRACK 1 (Solidarity Circle)")
    print("  WHY:")
    print("  1. Aligned with SAREC insights: Nada's 'fitra over well-being'")
    print("  2. Lower risk: No financial ask = easier yes, test governance")
    print("  3. Build trust capital: Demonstrate long-term commitment")
    print("  4. Natural pipeline: Solidarity → Investment (stage progression)")
    print()
    print("  Then 6 months later: Launch Track 2 with solidarity 'alumni' + new revenue-stage teams")
    print()

    print("=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)

if __name__ == '__main__':
    analyze_dual_track()
