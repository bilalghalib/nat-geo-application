#!/usr/bin/env python3
"""
Process the full 1,011 teams CSV from Airtable export
Expands the analysis to the complete Bloom network
"""
import json
import csv
from pathlib import Path
from typing import List, Dict
from dataclasses import dataclass, asdict
import sys

@dataclass
class FullTeamProfile:
    """Extended team profile with all Airtable fields"""
    # Core fields
    team_name: str
    program: str = ""
    status: str = ""

    # Contact info
    founder_name: str = ""
    email: str = ""
    phone: str = ""

    # Business details
    sector: str = ""
    location: str = ""
    country: str = ""
    cohort: str = ""

    # Metadata
    application_date: str = ""
    graduation_date: str = ""

    # Analysis fields (will be computed)
    cluster: str = ""
    outreach_priority: int = 0
    partnerships_potential: str = ""
    cooperative_fit: int = 0

def parse_csv_file(csv_path: Path) -> List[Dict]:
    """
    Parse the Airtable CSV export
    Handles various column name formats
    """
    teams = []

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            # Map Airtable columns to our schema
            # This will need to be adjusted based on actual column names
            team = {
                'team_name': row.get('Name', row.get('Team Name', row.get('Company', ''))),
                'program': row.get('Program', row.get('Programs', '')),
                'status': row.get('Status', ''),
                'founder_name': row.get('Founder', row.get('Contact Name', '')),
                'email': row.get('Email', row.get('Contact Email', '')),
                'phone': row.get('Phone', ''),
                'sector': row.get('Sector', row.get('Industry', '')),
                'location': row.get('Location', row.get('City', '')),
                'country': row.get('Country', ''),
                'cohort': row.get('Cohort', row.get('Year', '')),
                'application_date': row.get('Application Date', ''),
                'graduation_date': row.get('Graduation Date', ''),
            }

            # Only add if has a name
            if team['team_name']:
                teams.append(team)

    return teams

def cluster_teams_by_sector(teams: List[Dict]) -> Dict[str, List[Dict]]:
    """Cluster teams by sector"""
    clusters = {}

    for team in teams:
        sector = team.get('sector', 'Other').strip() or 'Other'
        if sector not in clusters:
            clusters[sector] = []
        clusters[sector].append(team)

    return clusters

def cluster_teams_by_country(teams: List[Dict]) -> Dict[str, List[Dict]]:
    """Cluster teams by country"""
    clusters = {}

    for team in teams:
        country = team.get('country', 'Unknown').strip() or 'Unknown'
        if country not in clusters:
            clusters[country] = []
        clusters[country].append(team)

    return clusters

def cluster_teams_by_program(teams: List[Dict]) -> Dict[str, List[Dict]]:
    """Cluster teams by program"""
    clusters = {}

    for team in teams:
        program = team.get('program', 'Unknown').strip() or 'Unknown'
        if program not in clusters:
            clusters[program] = []
        clusters[program].append(team)

    return clusters

def generate_network_insights(teams: List[Dict]) -> Dict:
    """Generate insights across the full network"""

    total_teams = len(teams)

    # Cluster by different dimensions
    sector_clusters = cluster_teams_by_sector(teams)
    country_clusters = cluster_teams_by_country(teams)
    program_clusters = cluster_teams_by_program(teams)

    # Find largest clusters
    largest_sector = max(sector_clusters.items(), key=lambda x: len(x[1]))
    largest_country = max(country_clusters.items(), key=lambda x: len(x[1]))
    largest_program = max(program_clusters.items(), key=lambda x: len(x[1]))

    # Calculate cooperative opportunities
    insights = {
        'total_teams': total_teams,
        'by_sector': {k: len(v) for k, v in sector_clusters.items()},
        'by_country': {k: len(v) for k, v in country_clusters.items()},
        'by_program': {k: len(v) for k, v in program_clusters.items()},
        'largest_clusters': {
            'sector': {'name': largest_sector[0], 'size': len(largest_sector[1])},
            'country': {'name': largest_country[0], 'size': len(largest_country[1])},
            'program': {'name': largest_program[0], 'size': len(largest_program[1])}
        },
        'network_effects': {
            'potential_partnerships': total_teams * (total_teams - 1) // 2,
            'avg_cluster_size_sector': total_teams / len(sector_clusters) if sector_clusters else 0,
            'avg_cluster_size_country': total_teams / len(country_clusters) if country_clusters else 0
        },
        'cooperative_potential': {
            'conservative_members': int(total_teams * 0.10),  # 10%
            'moderate_members': int(total_teams * 0.30),      # 30%
            'optimistic_members': int(total_teams * 0.50),    # 50%
            'conservative_revenue': int(total_teams * 0.10 * 2000),
            'moderate_revenue': int(total_teams * 0.30 * 2500),
            'optimistic_revenue': int(total_teams * 0.50 * 3000)
        }
    }

    return insights, sector_clusters, country_clusters, program_clusters

def main():
    """Main processing pipeline for full teams dataset"""

    base_dir = Path("/home/user/BloomHarvest")
    data_dir = base_dir / "strategic_analysis/data"
    output_dir = base_dir / "strategic_analysis/outputs"

    # Look for CSV file in multiple locations
    csv_locations = [
        data_dir / "all_teams.csv",
        data_dir / "teams.csv",
        base_dir / "Bloom_s Research" / "all_teams.csv",
        base_dir / "all_teams.csv",
    ]

    csv_path = None
    for loc in csv_locations:
        if loc.exists():
            csv_path = loc
            break

    if not csv_path:
        print("❌ CSV file not found. Please place it in one of these locations:")
        for loc in csv_locations:
            print(f"   - {loc}")
        print("\nOr specify the path as an argument:")
        print("   python3 04_process_full_teams_csv.py /path/to/teams.csv")

        if len(sys.argv) > 1:
            csv_path = Path(sys.argv[1])
            if not csv_path.exists():
                print(f"\n❌ File not found: {csv_path}")
                return
        else:
            return

    print(f"📂 Found CSV: {csv_path}")
    print(f"📊 Processing full teams dataset...")

    # Parse CSV
    teams = parse_csv_file(csv_path)
    print(f"\n✅ Loaded {len(teams)} teams")

    # Generate insights
    insights, sector_clusters, country_clusters, program_clusters = generate_network_insights(teams)

    # Save full teams data
    full_teams_file = data_dir / "all_teams_structured.json"
    with open(full_teams_file, 'w', encoding='utf-8') as f:
        json.dump(teams, f, indent=2, ensure_ascii=False)
    print(f"✅ Saved to: {full_teams_file}")

    # Save network insights
    insights_file = output_dir / "network_insights_full.json"
    with open(insights_file, 'w', encoding='utf-8') as f:
        json.dump(insights, f, indent=2, ensure_ascii=False)
    print(f"✅ Saved insights to: {insights_file}")

    # Save sector clusters
    sector_file = output_dir / "clusters_by_sector_full.json"
    with open(sector_file, 'w', encoding='utf-8') as f:
        json.dump({k: [t['team_name'] for t in v] for k, v in sector_clusters.items()},
                  f, indent=2, ensure_ascii=False)

    # Save country clusters
    country_file = output_dir / "clusters_by_country_full.json"
    with open(country_file, 'w', encoding='utf-8') as f:
        json.dump({k: [t['team_name'] for t in v] for k, v in country_clusters.items()},
                  f, indent=2, ensure_ascii=False)

    # Print summary
    print(f"\n{'='*60}")
    print(f"🌸 BLOOM NETWORK ANALYSIS - FULL DATASET")
    print(f"{'='*60}\n")

    print(f"📊 Total Teams: {insights['total_teams']:,}")
    print(f"\n🏆 Largest Clusters:")
    print(f"   Sector: {insights['largest_clusters']['sector']['name']} ({insights['largest_clusters']['sector']['size']} teams)")
    print(f"   Country: {insights['largest_clusters']['country']['name']} ({insights['largest_clusters']['country']['size']} teams)")
    print(f"   Program: {insights['largest_clusters']['program']['name']} ({insights['largest_clusters']['program']['size']} teams)")

    print(f"\n🌐 Network Effects:")
    print(f"   Potential partnerships: {insights['network_effects']['potential_partnerships']:,}")
    print(f"   Avg teams per sector: {insights['network_effects']['avg_cluster_size_sector']:.1f}")

    print(f"\n💰 Cooperative Revenue Potential:")
    print(f"   Conservative (10%): {insights['cooperative_potential']['conservative_members']} members → ${insights['cooperative_potential']['conservative_revenue']:,}/year")
    print(f"   Moderate (30%): {insights['cooperative_potential']['moderate_members']} members → ${insights['cooperative_potential']['moderate_revenue']:,}/year")
    print(f"   Optimistic (50%): {insights['cooperative_potential']['optimistic_members']} members → ${insights['cooperative_potential']['optimistic_revenue']:,}/year")

    print(f"\n📋 Top 5 Sectors:")
    sorted_sectors = sorted(insights['by_sector'].items(), key=lambda x: x[1], reverse=True)
    for sector, count in sorted_sectors[:5]:
        print(f"   {sector}: {count} teams")

    print(f"\n🌍 Top 5 Countries:")
    sorted_countries = sorted(insights['by_country'].items(), key=lambda x: x[1], reverse=True)
    for country, count in sorted_countries[:5]:
        print(f"   {country}: {count} teams")

    print(f"\n{'='*60}")
    print(f"✅ Full network analysis complete!")
    print(f"{'='*60}\n")

    return teams, insights

if __name__ == "__main__":
    main()
