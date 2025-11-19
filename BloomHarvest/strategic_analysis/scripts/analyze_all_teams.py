#!/usr/bin/env python3
"""
Bloom Teams Analysis & Prioritization Script
Analyzes ~1000 teams from Airtable export to identify next interview candidates

Scoring Criteria:
1. Stage (4-5 = operating businesses prioritized)
2. Has website/social media (indicates active)
3. Geography (MENA region focus)
4. Program (ACSI3/4 = most recent)
5. Team size (indicates scale)
6. Not yet interviewed (exclude 19 completed)
"""

import csv
import json
import re
from collections import Counter, defaultdict
from datetime import datetime
from urllib.parse import urlparse

# ==========================
# CONFIGURATION
# ==========================

CSV_PATH = "/Users/bilalghalib/Projects/scripts/BloomHarvest/Bloom_History_And_Research/Bloom_Teams/All_Teams_Airtable_Export_Teams X Programs + Workspace-All records.csv"
OUTPUT_DIR = "/Users/bilalghalib/Projects/scripts/BloomHarvest/strategic_analysis/outputs/team_prioritization/"

# Teams already interviewed (exclude from ranking)
INTERVIEWED_TEAMS = {
    'Badia', 'AnalySens',
    'Clara', 'Little Stars',
    'Ehab', 'Ecobath',
    'Ezalden', 'Hello World',
    'Garene', 'Parents Hub',
    'Ghinwa', 'Urban Leaf',
    'Hany', 'Takadam', 'ToRead',
    'Hussein', 'RobotX',
    'Iman', 'Hazel Farm',
    'Keren', 'Smart Sensory',
    'Louai', 'Courssaty',
    'Mohamad', 'GreeNX',
    'Nada', 'Tram Alwaan',
    'Reem', 'Khutwa', 'Brightful',
    'Salah', 'Blue Filter',
    'Salam', 'Palexus',
    'Shaban', 'Pal-Lend',
    'Siwar', 'PSYAI', 'Jur\'at Amal',
    'Sumayya', 'Rouh'
}

# Priority programs (most recent)
PRIORITY_PROGRAMS = {
    'ACSI4': 10,
    'ACSI3': 9,
    'ACSI2': 7,
    'LGA2': 5,
    'LGA1': 4,
    'HMN': 6,
    'EON': 3
}

# Priority countries
PRIORITY_COUNTRIES = {
    'Palestine': 10,
    'Jordan': 9,
    'Egypt': 9,
    'Lebanon': 8,
    'Iraq': 7,
    'Syria': 6
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
    # Remove patterns like "-434 in LGA1 Accelerator"
    clean = re.sub(r'-\d+ in .*$', '', name)
    return clean.strip()

def extract_country(geo_text):
    """Extract country from geographic location"""
    if not geo_text:
        return "Unknown"

    # Check for priority countries
    for country in PRIORITY_COUNTRIES.keys():
        if country in str(geo_text):
            return country

    # Extract from common patterns
    if 'Lebanon' in str(geo_text) or 'Beirut' in str(geo_text) or 'Mount Lebanon' in str(geo_text):
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
    # Basic validation
    return bool(urlparse(str(url)).scheme)

def extract_social_links(social_text):
    """Extract social media links and identify platforms"""
    if not social_text or social_text == 'N/A':
        return []

    links = []
    text = str(social_text)

    # Common social platforms
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

def calculate_score(team):
    """
    Calculate priority score for team (0-100)

    Weights:
    - Stage (30%): 4-5 = operating businesses
    - Has website (15%): Shows activity
    - Has social media (10%): Shows activity
    - Program recency (20%): ACSI3/4 prioritized
    - Geography (15%): MENA region
    - Team size (10%): Indicates scale
    """
    score = 0
    details = {}

    # 1. Stage Score (0-30)
    stage = team.get('stage_numeric', 0)
    if stage >= 4.0:  # Operating with revenue
        stage_score = 30
    elif stage >= 3.0:  # Prototype stage
        stage_score = 20
    elif stage >= 2.0:  # Ideation
        stage_score = 10
    else:
        stage_score = 5
    score += stage_score
    details['stage_score'] = stage_score

    # 2. Website (0-15)
    if team.get('has_website'):
        score += 15
        details['website_score'] = 15
    else:
        details['website_score'] = 0

    # 3. Social Media (0-10)
    social_count = len(team.get('social_platforms', []))
    social_score = min(social_count * 3, 10)  # Max 10 points
    score += social_score
    details['social_score'] = social_score

    # 4. Program Recency (0-20)
    program = team.get('program', '')
    program_score = 0
    for prog, points in PRIORITY_PROGRAMS.items():
        if prog in str(program):
            program_score = (points / 10) * 20  # Normalize to 0-20
            break
    score += program_score
    details['program_score'] = program_score

    # 5. Geography (0-15)
    country = team.get('country', 'Unknown')
    geo_score = (PRIORITY_COUNTRIES.get(country, 0) / 10) * 15  # Normalize to 0-15
    score += geo_score
    details['geo_score'] = geo_score

    # 6. Team Size (0-10)
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

    team['score'] = round(score, 2)
    team['score_details'] = details

    return score

# ==========================
# MAIN ANALYSIS
# ==========================

def analyze_teams():
    """Main analysis function"""

    print("=" * 70)
    print("BLOOM TEAMS ANALYSIS & PRIORITIZATION")
    print("=" * 70)
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

            # Extract key fields
            team_name = row.get('Name', '')
            if not team_name:
                continue

            # Skip if already interviewed
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

            # Calculate score
            calculate_score(team)

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

    # Sort by score (descending)
    teams_sorted = sorted(teams, key=lambda x: x['score'], reverse=True)

    # ==========================
    # STATISTICS SUMMARY
    # ==========================

    print("=" * 70)
    print("STATISTICS SUMMARY")
    print("=" * 70)
    print()

    print(f"Total teams: {len(teams)}")
    print(f"Has website: {stats['has_website']} ({stats['has_website']/len(teams)*100:.1f}%)")
    print(f"Has social media: {stats['has_social']} ({stats['has_social']/len(teams)*100:.1f}%)")
    print()

    print("Top 10 Countries:")
    for country, count in stats['by_country'].most_common(10):
        print(f"  {country}: {count}")
    print()

    print("Top 10 Programs:")
    for program, count in stats['by_program'].most_common(10):
        if program:  # Skip empty
            print(f"  {program}: {count}")
    print()

    print("By Stage:")
    for stage, count in sorted(stats['by_stage'].items()):
        print(f"  {stage}: {count}")
    print()

    # ==========================
    # TOP 50 PRIORITIZED TEAMS
    # ==========================

    print("=" * 70)
    print("TOP 50 TEAMS FOR NEXT INTERVIEWS")
    print("=" * 70)
    print()

    print(f"{'Rank':<6} {'Score':<7} {'Name':<40} {'Country':<12} {'Stage':<7} {'Web':<5} {'Social':<8} {'Program'}")
    print("-" * 140)

    for i, team in enumerate(teams_sorted[:50], 1):
        web_icon = "✓" if team['has_website'] else "-"
        social_icon = ",".join(team['social_platforms'][:2]) if team['social_platforms'] else "-"
        stage_display = f"{team['stage_numeric']:.1f}" if team['stage_numeric'] > 0 else "-"

        print(f"{i:<6} {team['score']:<7.1f} {team['name'][:38]:<40} {team['country'][:10]:<12} {stage_display:<7} {web_icon:<5} {social_icon[:6]:<8} {team['program'][:20]}")

    print()

    # ==========================
    # EXPORT DATA
    # ==========================

    import os
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Export top 200 to CSV
    csv_output = f"{OUTPUT_DIR}top_200_teams_ranked.csv"
    with open(csv_output, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['rank', 'score', 'name', 'email', 'country', 'program', 'stage_numeric',
                      'has_website', 'website', 'social_platforms', 'social_media', 'team_size',
                      'sectors', 'geographic_location', 'workspace_link', 'score_details']
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()

        for i, team in enumerate(teams_sorted[:200], 1):
            row = team.copy()
            row['rank'] = i
            row['social_platforms'] = ','.join(team['social_platforms'])
            row['score_details'] = json.dumps(team['score_details'])
            writer.writerow(row)

    print(f"✓ Exported top 200 teams to: {csv_output}")

    # Export full teams to JSON
    json_output = f"{OUTPUT_DIR}all_teams_scored.json"
    with open(json_output, 'w', encoding='utf-8') as f:
        json.dump({
            'metadata': {
                'generated': datetime.now().isoformat(),
                'total_teams': len(teams),
                'already_interviewed': stats['interviewed'],
                'stats': {
                    'has_website': stats['has_website'],
                    'has_social': stats['has_social'],
                    'by_country': dict(stats['by_country'].most_common(20)),
                    'by_program': dict(stats['by_program'].most_common(20))
                }
            },
            'teams': teams_sorted
        }, f, indent=2, ensure_ascii=False)

    print(f"✓ Exported all teams (scored) to: {json_output}")
    print()

    # ==========================
    # RECOMMENDATIONS
    # ==========================

    print("=" * 70)
    print("RECOMMENDATIONS FOR NEXT CALLS")
    print("=" * 70)
    print()

    # Group top teams by criteria
    top_50 = teams_sorted[:50]

    # High stage + active online
    high_priority = [t for t in top_50 if t['stage_numeric'] >= 4.0 and (t['has_website'] or t['social_platforms'])]
    print(f"✓ HIGH PRIORITY (Operating + Active Online): {len(high_priority)} teams")
    print("  Recommended: Interview top 10-15 from this group")
    print()

    # Palestine/Jordan focus
    priority_geo = [t for t in top_50 if t['country'] in ['Palestine', 'Jordan', 'Egypt']]
    print(f"✓ PRIORITY GEOGRAPHY (Palestine/Jordan/Egypt): {len(priority_geo)} teams")
    print()

    # Recent programs
    recent_programs = [t for t in top_50 if any(p in t['program'] for p in ['ACSI4', 'ACSI3', 'HMN'])]
    print(f"✓ RECENT PROGRAMS (ACSI3/4, HMN): {len(recent_programs)} teams")
    print()

    # Suggested next 20 calls
    print("SUGGESTED NEXT 20 CALLS (in order):")
    print()
    for i, team in enumerate(teams_sorted[:20], 1):
        print(f"{i:2}. {team['name'][:45]:<45} | Score: {team['score']:.1f} | {team['country'][:12]:<12} | {team['email']}")

    print()
    print("=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)

if __name__ == '__main__':
    analyze_teams()
