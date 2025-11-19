#!/usr/bin/env python3
"""
Strategic Transition System - Team Analysis Infrastructure
Processes all teams from Airtable export and generates network insights
"""

import csv
import json
import os
from pathlib import Path
from typing import Dict, List, Any
from collections import defaultdict, Counter
import re

# Paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data" / "teams"
OUTPUT_DIR = BASE_DIR / "outputs" / "network_analysis"
EMBEDDINGS_DIR = BASE_DIR / "outputs" / "embeddings"

class TeamAnalyzer:
    """Analyzes all teams and generates network insights"""

    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.teams = []
        self.sectors = defaultdict(list)
        self.countries = defaultdict(list)
        self.programs = defaultdict(list)
        self.stages = defaultdict(list)

    def load_teams(self):
        """Load and parse teams from CSV"""
        print(f"📊 Loading teams from {self.csv_path}...")

        with open(self.csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                team = self.normalize_team(row)
                self.teams.append(team)

                # Index by sector, country, program
                if team.get('sector'):
                    self.sectors[team['sector']].append(team)
                if team.get('country'):
                    self.countries[team['country']].append(team)
                if team.get('program'):
                    self.programs[team['program']].append(team)
                if team.get('stage'):
                    self.stages[team['stage']].append(team)

        print(f"✅ Loaded {len(self.teams)} teams")
        return self.teams

    def normalize_team(self, row: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize team data from Airtable export"""
        # Airtable exports can have various column names
        # This handles common variations

        team = {
            'id': row.get('Record ID') or row.get('ID') or row.get('id', ''),
            'name': row.get('Team Name') or row.get('Name') or row.get('team_name', ''),
            'sector': self.clean_sector(row.get('Sector') or row.get('Industry') or row.get('sector', '')),
            'country': self.clean_country(row.get('Country') or row.get('Location') or row.get('country', '')),
            'program': self.clean_program(row.get('Program') or row.get('Cohort') or row.get('program', '')),
            'stage': self.clean_stage(row.get('Stage') or row.get('Status') or row.get('stage', '')),
            'description': row.get('Description') or row.get('About') or row.get('description', ''),
            'contact': row.get('Contact') or row.get('Email') or row.get('contact', ''),
            'phone': row.get('Phone') or row.get('Mobile') or row.get('phone', ''),
            'founder': row.get('Founder') or row.get('Founder Name') or row.get('founder', ''),
            'website': row.get('Website') or row.get('URL') or row.get('website', ''),
            'raw_data': row  # Keep original for reference
        }

        return team

    def clean_sector(self, sector: str) -> str:
        """Normalize sector names"""
        if not sector:
            return "Unknown"

        sector = sector.strip().lower()

        # Map common variations
        mapping = {
            'education': 'EdTech',
            'edtech': 'EdTech',
            'ed-tech': 'EdTech',
            'finance': 'FinTech',
            'fintech': 'FinTech',
            'fin-tech': 'FinTech',
            'health': 'HealthTech',
            'healthcare': 'HealthTech',
            'healthtech': 'HealthTech',
            'agriculture': 'AgriTech',
            'agritech': 'AgriTech',
            'agri-tech': 'AgriTech',
            'retail': 'Retail',
            'e-commerce': 'E-Commerce',
            'ecommerce': 'E-Commerce',
            'logistics': 'Logistics',
            'transportation': 'Logistics',
            'energy': 'CleanTech',
            'cleantech': 'CleanTech',
            'environment': 'CleanTech',
        }

        for key, value in mapping.items():
            if key in sector:
                return value

        return sector.title()

    def clean_country(self, country: str) -> str:
        """Normalize country names"""
        if not country:
            return "Unknown"

        country = country.strip()

        # Common variations
        mapping = {
            'lebanon': 'Lebanon',
            'leb': 'Lebanon',
            'lb': 'Lebanon',
            'jordan': 'Jordan',
            'jo': 'Jordan',
            'palestine': 'Palestine',
            'ps': 'Palestine',
            'syria': 'Syria',
            'sy': 'Syria',
            'egypt': 'Egypt',
            'eg': 'Egypt',
            'iraq': 'Iraq',
            'iq': 'Iraq',
        }

        country_lower = country.lower()
        for key, value in mapping.items():
            if key in country_lower:
                return value

        return country.title()

    def clean_program(self, program: str) -> str:
        """Normalize program names"""
        if not program:
            return "Unknown"

        # Extract program codes like ACSI1, ACSI2, etc.
        program = program.strip()

        # Look for ACSI patterns
        acsi_match = re.search(r'ACSI[- ]?(\d+)', program, re.IGNORECASE)
        if acsi_match:
            return f"ACSI{acsi_match.group(1)}"

        # Look for HerMeNow
        if 'hermenow' in program.lower() or 'her me now' in program.lower():
            return "HerMeNow"

        return program

    def clean_stage(self, stage: str) -> str:
        """Normalize stage/status"""
        if not stage:
            return "Unknown"

        stage = stage.strip().lower()

        mapping = {
            'idea': 'Idea',
            'prototype': 'Prototype',
            'mvp': 'MVP',
            'launch': 'Launched',
            'launched': 'Launched',
            'growth': 'Growth',
            'scale': 'Scaling',
            'scaling': 'Scaling',
            'active': 'Active',
            'inactive': 'Inactive',
            'closed': 'Closed',
        }

        for key, value in mapping.items():
            if key in stage:
                return value

        return stage.title()

    def analyze_network(self) -> Dict[str, Any]:
        """Generate comprehensive network analysis"""
        print("\n🔍 Analyzing network...")

        analysis = {
            'total_teams': len(self.teams),
            'by_sector': self.analyze_dimension(self.sectors, 'sector'),
            'by_country': self.analyze_dimension(self.countries, 'country'),
            'by_program': self.analyze_dimension(self.programs, 'program'),
            'by_stage': self.analyze_dimension(self.stages, 'stage'),
            'top_sectors': self.get_top_n(self.sectors, 10),
            'top_countries': self.get_top_n(self.countries, 10),
            'top_programs': self.get_top_n(self.programs, 10),
        }

        return analysis

    def analyze_dimension(self, dimension_dict: Dict, dimension_name: str) -> Dict:
        """Analyze a specific dimension (sector, country, etc.)"""
        return {
            key: {
                'count': len(teams),
                'percentage': round(len(teams) / len(self.teams) * 100, 1),
                'teams': [t['name'] for t in teams[:5]]  # Sample
            }
            for key, teams in sorted(dimension_dict.items(), key=lambda x: len(x[1]), reverse=True)
        }

    def get_top_n(self, dimension_dict: Dict, n: int) -> List[Dict]:
        """Get top N categories by team count"""
        return [
            {
                'category': key,
                'count': len(teams),
                'percentage': round(len(teams) / len(self.teams) * 100, 1)
            }
            for key, teams in sorted(dimension_dict.items(), key=lambda x: len(x[1]), reverse=True)[:n]
        ]

    def calculate_cooperative_projections(self) -> Dict[str, Any]:
        """Calculate cooperative revenue projections"""
        print("\n💰 Calculating cooperative projections...")

        total_teams = len(self.teams)

        # Assumed annual fee per team
        annual_fee = 1000  # $1,000/year per team

        # Different adoption scenarios
        scenarios = {
            'conservative': {
                'adoption_rate': 0.10,
                'teams': int(total_teams * 0.10),
                'annual_revenue': int(total_teams * 0.10 * annual_fee),
                'description': 'Conservative: 10% adoption - early adopters only'
            },
            'moderate': {
                'adoption_rate': 0.30,
                'teams': int(total_teams * 0.30),
                'annual_revenue': int(total_teams * 0.30 * annual_fee),
                'description': 'Moderate: 30% adoption - successful outreach campaign'
            },
            'optimistic': {
                'adoption_rate': 0.50,
                'teams': int(total_teams * 0.50),
                'annual_revenue': int(total_teams * 0.50 * annual_fee),
                'description': 'Optimistic: 50% adoption - strong network effects'
            },
        }

        return {
            'total_addressable_market': total_teams,
            'annual_fee_per_team': annual_fee,
            'scenarios': scenarios,
            'five_year_projection': {
                scenario_name: scenario['annual_revenue'] * 5
                for scenario_name, scenario in scenarios.items()
            }
        }

    def prioritize_outreach(self, top_n: int = 100) -> List[Dict]:
        """Prioritize teams for outreach based on multiple factors"""
        print(f"\n🎯 Prioritizing top {top_n} teams for outreach...")

        scored_teams = []

        for team in self.teams:
            score = 0
            reasons = []

            # Factor 1: High-growth sectors (EdTech, FinTech, HealthTech)
            if team['sector'] in ['EdTech', 'FinTech', 'HealthTech']:
                score += 3
                reasons.append(f"High-growth sector ({team['sector']})")

            # Factor 2: Recent programs (ACSI3, ACSI4, HerMeNow)
            if team['program'] in ['ACSI3', 'ACSI4', 'HerMeNow']:
                score += 3
                reasons.append(f"Recent program ({team['program']})")

            # Factor 3: Active/Growth/Scaling stage
            if team['stage'] in ['Active', 'Growth', 'Scaling', 'Launched']:
                score += 2
                reasons.append(f"Active stage ({team['stage']})")

            # Factor 4: Has contact information
            if team['contact'] or team['phone']:
                score += 1
                reasons.append("Has contact info")

            # Factor 5: Strategic countries (Lebanon, Jordan, Palestine)
            if team['country'] in ['Lebanon', 'Jordan', 'Palestine']:
                score += 2
                reasons.append(f"Strategic market ({team['country']})")

            # Factor 6: Has description (more info = better understanding)
            if team['description'] and len(team['description']) > 50:
                score += 1
                reasons.append("Detailed profile")

            scored_teams.append({
                'team': team,
                'priority_score': score,
                'reasons': reasons
            })

        # Sort by score
        scored_teams.sort(key=lambda x: x['priority_score'], reverse=True)

        return scored_teams[:top_n]

    def identify_partnerships(self) -> List[Dict]:
        """Identify potential partnerships across teams"""
        print("\n🤝 Identifying partnership opportunities...")

        partnerships = []

        # Cross-sector partnerships
        for sector1, teams1 in self.sectors.items():
            for sector2, teams2 in self.sectors.items():
                if sector1 < sector2:  # Avoid duplicates
                    # Find synergies
                    synergy = self.find_synergy(sector1, sector2)
                    if synergy:
                        partnerships.append({
                            'type': 'cross-sector',
                            'sectors': [sector1, sector2],
                            'team_count_1': len(teams1),
                            'team_count_2': len(teams2),
                            'synergy': synergy,
                            'potential_partnerships': min(len(teams1), len(teams2))
                        })

        # Geographic clustering
        for country, teams in self.countries.items():
            if len(teams) >= 5:  # Minimum cluster size
                partnerships.append({
                    'type': 'geographic-cluster',
                    'country': country,
                    'team_count': len(teams),
                    'opportunity': f"Local cooperative chapter in {country}",
                    'teams': [t['name'] for t in teams[:10]]
                })

        return partnerships

    def find_synergy(self, sector1: str, sector2: str) -> str:
        """Find synergies between sectors"""
        synergies = {
            ('EdTech', 'FinTech'): 'Student payment systems, educational financing',
            ('EdTech', 'HealthTech'): 'Health education, medical training platforms',
            ('FinTech', 'AgriTech'): 'Agricultural financing, supply chain payments',
            ('FinTech', 'E-Commerce'): 'Payment processing, merchant services',
            ('HealthTech', 'AgriTech'): 'Nutrition, food safety tracking',
            ('Logistics', 'E-Commerce'): 'Last-mile delivery, fulfillment',
            ('Logistics', 'AgriTech'): 'Farm-to-market distribution',
        }

        key = tuple(sorted([sector1, sector2]))
        return synergies.get(key, '')

    def generate_cluster_report(self) -> str:
        """Generate a human-readable cluster report"""
        report = []
        report.append("=" * 80)
        report.append("BLOOM COOPERATIVE - FULL NETWORK ANALYSIS")
        report.append("=" * 80)
        report.append(f"\nTotal Teams: {len(self.teams)}")
        report.append("\n" + "=" * 80)

        # Sector analysis
        report.append("\n📊 SECTOR DISTRIBUTION")
        report.append("-" * 80)
        for sector, teams in sorted(self.sectors.items(), key=lambda x: len(x[1]), reverse=True)[:10]:
            percentage = len(teams) / len(self.teams) * 100
            report.append(f"{sector:20} {len(teams):4} teams ({percentage:5.1f}%)")

        # Country analysis
        report.append("\n\n🌍 GEOGRAPHIC DISTRIBUTION")
        report.append("-" * 80)
        for country, teams in sorted(self.countries.items(), key=lambda x: len(x[1]), reverse=True)[:10]:
            percentage = len(teams) / len(self.teams) * 100
            report.append(f"{country:20} {len(teams):4} teams ({percentage:5.1f}%)")

        # Program analysis
        report.append("\n\n🎓 PROGRAM DISTRIBUTION")
        report.append("-" * 80)
        for program, teams in sorted(self.programs.items(), key=lambda x: len(x[1]), reverse=True):
            percentage = len(teams) / len(self.teams) * 100
            report.append(f"{program:20} {len(teams):4} teams ({percentage:5.1f}%)")

        report.append("\n" + "=" * 80)

        return "\n".join(report)

    def save_results(self, network_analysis: Dict, projections: Dict,
                     priority_teams: List, partnerships: List):
        """Save all analysis results"""
        print("\n💾 Saving results...")

        # Ensure output directories exist
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        # Save network analysis
        with open(OUTPUT_DIR / "network_analysis.json", 'w') as f:
            json.dump(network_analysis, f, indent=2)
        print(f"✅ Saved: network_analysis.json")

        # Save projections
        with open(OUTPUT_DIR / "cooperative_projections.json", 'w') as f:
            json.dump(projections, f, indent=2)
        print(f"✅ Saved: cooperative_projections.json")

        # Save priority teams
        priority_output = [
            {
                'rank': i + 1,
                'name': team['team']['name'],
                'sector': team['team']['sector'],
                'country': team['team']['country'],
                'program': team['team']['program'],
                'priority_score': team['priority_score'],
                'reasons': team['reasons'],
                'contact': team['team']['contact'],
                'phone': team['team']['phone']
            }
            for i, team in enumerate(priority_teams)
        ]
        with open(OUTPUT_DIR / "priority_outreach_top100.json", 'w') as f:
            json.dump(priority_output, f, indent=2)
        print(f"✅ Saved: priority_outreach_top100.json")

        # Save partnerships
        with open(OUTPUT_DIR / "partnership_opportunities.json", 'w') as f:
            json.dump(partnerships, f, indent=2)
        print(f"✅ Saved: partnership_opportunities.json")

        # Save cluster report
        cluster_report = self.generate_cluster_report()
        with open(OUTPUT_DIR / "cluster_report.txt", 'w') as f:
            f.write(cluster_report)
        print(f"✅ Saved: cluster_report.txt")

        # Save all teams (normalized)
        with open(OUTPUT_DIR / "all_teams_normalized.json", 'w') as f:
            json.dump(self.teams, f, indent=2)
        print(f"✅ Saved: all_teams_normalized.json")


def main():
    """Main processing pipeline"""
    print("🚀 Bloom Cooperative - Strategic Transition System")
    print("=" * 80)

    # Look for CSV file
    csv_candidates = [
        DATA_DIR / "all_teams.csv",
        DATA_DIR / "teams.csv",
        BASE_DIR.parent / "Bloom_History_And_Research" / "Bloom_Teams" / "All_Teams_Airtable_Export_Teams X Programs + Workspace-All records.csv",
    ]

    csv_path = None
    for candidate in csv_candidates:
        if candidate.exists():
            csv_path = candidate
            break

    if not csv_path:
        print("\n❌ ERROR: No teams CSV file found!")
        print("\nPlease upload your CSV to one of these locations:")
        for candidate in csv_candidates:
            print(f"  - {candidate}")
        print("\nExpected columns: Team Name, Sector, Country, Program, Stage, Contact, etc.")
        return

    # Initialize analyzer
    analyzer = TeamAnalyzer(str(csv_path))

    # Load teams
    teams = analyzer.load_teams()

    # Generate network analysis
    network_analysis = analyzer.analyze_network()

    # Calculate projections
    projections = analyzer.calculate_cooperative_projections()

    # Prioritize outreach
    priority_teams = analyzer.prioritize_outreach(top_n=100)

    # Identify partnerships
    partnerships = analyzer.identify_partnerships()

    # Save everything
    analyzer.save_results(network_analysis, projections, priority_teams, partnerships)

    # Print summary
    print("\n" + "=" * 80)
    print("✅ ANALYSIS COMPLETE!")
    print("=" * 80)
    print(f"\n📊 Analyzed {len(teams)} teams")
    print(f"🎯 Identified top {len(priority_teams)} priority teams for outreach")
    print(f"🤝 Found {len(partnerships)} partnership opportunities")
    print(f"\n💰 Cooperative Revenue Projections:")
    for scenario, data in projections['scenarios'].items():
        print(f"  {scenario.title():12} → {data['teams']:4} teams → ${data['annual_revenue']:,}/year")

    print(f"\n📁 All results saved to: {OUTPUT_DIR}")
    print("\nNext steps:")
    print("  1. Review cluster_report.txt for network overview")
    print("  2. Check priority_outreach_top100.json for outreach targets")
    print("  3. Run dashboard generator to create interactive visualizations")


if __name__ == "__main__":
    main()
