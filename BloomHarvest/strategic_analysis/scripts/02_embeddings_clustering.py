#!/usr/bin/env python3
"""
Embeddings-based clustering to find natural team groupings
Uses semantic similarity to identify synergies across the 1,011 teams
"""
import json
from pathlib import Path
from typing import List, Dict, Tuple
from dataclasses import dataclass
import sys

# This is a placeholder for actual embeddings - in production would use:
# - OpenAI embeddings API
# - Anthropic embeddings (when available)
# - Local models like sentence-transformers

@dataclass
class TeamCluster:
    """A cluster of similar teams"""
    cluster_id: int
    teams: List[Dict]
    themes: List[str]
    potential_synergies: List[str]
    cooperative_opportunities: List[str]

def create_team_profile_text(team: Dict) -> str:
    """Create a rich text profile for embedding"""
    parts = [
        f"Company: {team['company_name']}",
        f"Founder: {team['founder']}",
        f"Program: {team['program']}",
        f"Stage: {team['stage']}",
    ]

    if team.get('sector'):
        parts.append(f"Sector: {team['sector']}")

    if team.get('partnerships_needed'):
        parts.append("Seeking partnerships")

    if team.get('grant_received'):
        parts.append("Received grant funding")

    return " | ".join(parts)

def simple_similarity_clustering(teams: List[Dict]) -> List[TeamCluster]:
    """
    Simple rule-based clustering for now
    TODO: Replace with actual embeddings-based clustering
    """
    clusters = {}

    # Cluster by sector first
    for team in teams:
        sector = team.get('sector', 'unknown')
        if sector not in clusters:
            clusters[sector] = []
        clusters[sector].append(team)

    # Convert to TeamCluster objects
    team_clusters = []
    for i, (sector, sector_teams) in enumerate(clusters.items()):
        # Identify potential synergies
        synergies = []
        if sector == 'edtech':
            synergies = [
                "Content sharing partnerships",
                "Joint marketing to educational institutions",
                "Technology platform integration",
                "Shared customer success resources"
            ]
        elif sector == 'climate' or sector == 'agtech':
            synergies = [
                "Shared supply chain optimization",
                "Joint sustainability certifications",
                "Collective impact measurement",
                "Green financing consortium"
            ]
        elif sector == 'fintech':
            synergies = [
                "Payment infrastructure sharing",
                "Joint compliance resources",
                "Cross-platform integration",
                "Shared risk management"
            ]
        elif sector == 'health':
            synergies = [
                "Clinical partnerships",
                "Shared health data standards",
                "Joint research initiatives",
                "Collective healthcare provider relationships"
            ]

        # Identify cooperative opportunities
        coop_opportunities = [
            f"Shared services co-op (accounting, legal, HR)",
            f"Joint fundraising vehicle",
            f"Collective bargaining for vendor contracts",
            f"Knowledge sharing community"
        ]

        cluster = TeamCluster(
            cluster_id=i,
            teams=sector_teams,
            themes=[sector],
            potential_synergies=synergies,
            cooperative_opportunities=coop_opportunities
        )
        team_clusters.append(cluster)

    return team_clusters

def analyze_cross_cluster_opportunities(clusters: List[TeamCluster]) -> Dict:
    """Identify opportunities that span multiple clusters"""

    opportunities = {
        'platform_plays': [],
        'ecosystem_partnerships': [],
        'collective_services': [],
        'joint_ventures': []
    }

    # Find cross-sector platform opportunities
    sector_counts = {}
    for cluster in clusters:
        for theme in cluster.themes:
            sector_counts[theme] = len(cluster.teams)

    # Identify strong sectors that could provide platforms
    strong_sectors = [s for s, count in sector_counts.items() if count >= 3]

    for sector in strong_sectors:
        opportunities['platform_plays'].append({
            'sector': sector,
            'team_count': sector_counts[sector],
            'opportunity': f"Create shared {sector} platform serving all {sector_counts[sector]} teams"
        })

    # Collective services all teams could benefit from
    total_teams = sum(len(c.teams) for c in clusters)
    opportunities['collective_services'] = [
        {
            'service': 'Shared back-office (accounting, legal, HR)',
            'potential_users': total_teams,
            'cost_savings': f'Estimated 30-40% savings vs individual contracts'
        },
        {
            'service': 'Joint grant writing and fundraising support',
            'potential_users': total_teams,
            'impact': 'Higher success rates through specialized expertise'
        },
        {
            'service': 'Collective purchasing power for vendors',
            'potential_users': total_teams,
            'impact': 'Volume discounts on software, infrastructure, services'
        },
        {
            'service': 'Shared marketing and communications resources',
            'potential_users': total_teams,
            'impact': 'Professional marketing at fraction of individual cost'
        }
    ]

    return opportunities

def generate_outreach_priority_list(teams: List[Dict], clusters: List[TeamCluster]) -> List[Dict]:
    """
    Generate prioritized list of teams to reach out to
    Scoring based on: partnerships needed, grant success, stage, sector opportunities
    """

    team_scores = []

    for team in teams:
        score = 0
        reasons = []

        # High priority: actively seeking partnerships
        if team.get('partnerships_needed'):
            score += 10
            reasons.append("Actively seeking partnerships")

        # Grant success indicates momentum
        if team.get('grant_received'):
            score += 5
            reasons.append("Successfully raised grant funding")

        # Accelerator stage = more mature
        if team.get('stage') == 'Accelerator':
            score += 3
            reasons.append("Accelerator graduate - more mature")

        # EdTech is largest cluster - high network effect
        if team.get('sector') == 'edtech':
            score += 4
            reasons.append("Part of largest sector cluster (network effects)")

        # Recent program participation
        recent_programs = ['ACSI4', 'ACSI3', 'HMN 2023']
        if any(prog in team.get('program', '') for prog in recent_programs):
            score += 2
            reasons.append("Recent program participant")

        team_scores.append({
            'team': team,
            'priority_score': score,
            'reasons': reasons
        })

    # Sort by score descending
    team_scores.sort(key=lambda x: x['priority_score'], reverse=True)

    return team_scores

def main():
    """Main clustering and analysis pipeline"""

    base_dir = Path("/home/user/BloomHarvest")
    data_dir = base_dir / "strategic_analysis/data"
    output_dir = base_dir / "strategic_analysis/outputs"

    # Load teams data
    with open(data_dir / "teams_structured.json", 'r') as f:
        teams = json.load(f)

    print(f"📊 Analyzing {len(teams)} teams from interviews...")

    # Perform clustering
    clusters = simple_similarity_clustering(teams)

    print(f"\n🎯 Found {len(clusters)} natural clusters:")
    for cluster in clusters:
        print(f"   {cluster.themes[0]}: {len(cluster.teams)} teams")

    # Analyze cross-cluster opportunities
    opportunities = analyze_cross_cluster_opportunities(clusters)

    # Generate outreach priorities
    outreach_priorities = generate_outreach_priority_list(teams, clusters)

    # Save clustering results
    clustering_output = {
        'clusters': [
            {
                'cluster_id': c.cluster_id,
                'themes': c.themes,
                'team_count': len(c.teams),
                'teams': [{'name': t['company_name'], 'founder': t['founder'], 'program': t['program']} for t in c.teams],
                'potential_synergies': c.potential_synergies,
                'cooperative_opportunities': c.cooperative_opportunities
            }
            for c in clusters
        ],
        'cross_cluster_opportunities': opportunities,
        'summary': {
            'total_teams': len(teams),
            'total_clusters': len(clusters),
            'largest_cluster': max(clusters, key=lambda c: len(c.teams)).themes[0],
            'largest_cluster_size': max(len(c.teams) for c in clusters)
        }
    }

    clustering_file = output_dir / "team_clusters.json"
    with open(clustering_file, 'w', encoding='utf-8') as f:
        json.dump(clustering_output, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Saved clustering analysis to: {clustering_file}")

    # Save outreach priorities
    outreach_file = output_dir / "outreach_priorities.json"
    outreach_output = {
        'top_priority_teams': outreach_priorities[:10],  # Top 10
        'all_teams_ranked': outreach_priorities,
        'scoring_criteria': [
            'Actively seeking partnerships (+10)',
            'Grant funding received (+5)',
            'Accelerator graduate (+3)',
            'EdTech sector for network effects (+4)',
            'Recent program participation (+2)'
        ]
    }

    with open(outreach_file, 'w', encoding='utf-8') as f:
        json.dump(outreach_output, f, indent=2, ensure_ascii=False)

    print(f"✅ Saved outreach priorities to: {outreach_file}")

    # Print top priorities
    print(f"\n🎯 Top 5 Teams to Reach Out To:")
    for i, item in enumerate(outreach_priorities[:5], 1):
        team = item['team']
        print(f"\n{i}. {team['company_name']} - {team['founder']}")
        print(f"   Score: {item['priority_score']}")
        print(f"   Reasons: {', '.join(item['reasons'])}")

    # Print key insights
    print(f"\n💡 Key Cooperative Opportunities:")
    for opp in opportunities['collective_services'][:3]:
        print(f"   • {opp['service']}")
        print(f"     → {opp.get('impact', opp.get('cost_savings', ''))}")

    return clusters, opportunities, outreach_priorities

if __name__ == "__main__":
    main()
