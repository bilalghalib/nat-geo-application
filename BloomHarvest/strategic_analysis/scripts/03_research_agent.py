#!/usr/bin/env python3
"""
LLM Research Agent - Automated team research and outreach prioritization
Can be extended to search web, LinkedIn, company databases for current status
"""
import json
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict

@dataclass
class TeamResearchProfile:
    """Enriched team profile with research findings"""
    company_name: str
    founder: str
    program: str
    stage: str
    sector: Optional[str]

    # Research findings
    current_status: str  # active, scaling, pivoted, dormant, unknown
    linkedin_activity: Optional[str] = None
    recent_achievements: List[str] = None
    funding_raised: Optional[str] = None
    team_size: Optional[str] = None

    # Outreach strategy
    outreach_priority: int = 0  # 1-10
    outreach_approach: str = ""
    talking_points: List[str] = None
    potential_value: str = ""

    # Cooperative fit
    cooperative_readiness: int = 0  # 1-10
    can_contribute: List[str] = None
    needs_from_coop: List[str] = None

    def __post_init__(self):
        if self.recent_achievements is None:
            self.recent_achievements = []
        if self.talking_points is None:
            self.talking_points = []
        if self.can_contribute is None:
            self.can_contribute = []
        if self.needs_from_coop is None:
            self.needs_from_coop = []

def generate_outreach_strategy(team: Dict) -> Dict[str, any]:
    """
    Generate personalized outreach strategy for each team
    Based on their profile, program participation, sector
    """

    company = team['company_name']
    founder = team['founder']
    program = team['program']
    sector = team.get('sector', 'unknown')
    partnerships_needed = team.get('partnerships_needed', False)

    strategy = {
        'priority': 5,  # Default medium priority
        'approach': '',
        'talking_points': [],
        'cooperative_value_prop': []
    }

    # High priority if seeking partnerships
    if partnerships_needed:
        strategy['priority'] += 3
        strategy['talking_points'].append(
            f"You mentioned seeking partnerships during your ACSI interview - we've identified {8} teams in similar sectors who could collaborate"
        )

    # Sector-specific approach
    if sector == 'edtech':
        strategy['approach'] = "Educational ecosystem collaboration"
        strategy['talking_points'].extend([
            f"We have 12 EdTech teams from Bloom programs who could form a powerful collective",
            "Shared platform for educational content distribution",
            "Joint go-to-market strategy for schools and institutions"
        ])
        strategy['cooperative_value_prop'].extend([
            "Access to shared educational content library",
            "Collective bargaining with school systems",
            "Joint marketing to reduce customer acquisition costs"
        ])

    elif sector == 'fintech':
        strategy['approach'] = "Financial services integration"
        strategy['talking_points'].extend([
            "4 FinTech teams that could integrate services",
            "Shared compliance and regulatory resources",
            "Payment infrastructure partnerships"
        ])
        strategy['cooperative_value_prop'].extend([
            "Shared compliance/regulatory expertise",
            "Cross-platform payment integration",
            "Joint fundraising for larger financial infrastructure"
        ])

    elif sector == 'health':
        strategy['approach'] = "Healthcare impact collective"
        strategy['talking_points'].extend([
            "3 health-focused teams that could align on clinical partnerships",
            "Shared access to healthcare providers and institutions"
        ])
        strategy['cooperative_value_prop'].extend([
            "Joint clinical validation studies",
            "Shared relationships with hospitals/clinics",
            "Collective impact measurement"
        ])

    # Program-specific insights
    if 'ACSI4' in program or 'ACSI3' in program:
        strategy['talking_points'].append(
            "Recent ACSI graduates have momentum - perfect time to join cooperative"
        )
        strategy['priority'] += 1

    # Universal cooperative benefits
    strategy['cooperative_value_prop'].extend([
        "Shared back-office services (accounting, legal, HR) at 30-40% savings",
        "Joint fundraising support and grant writing",
        "Collective purchasing power for software and infrastructure",
        "Knowledge sharing community across 1,011+ teams"
    ])

    return strategy

def generate_talking_points(team: Dict, strategy: Dict) -> str:
    """Generate personalized email/call script"""

    founder = team['founder']
    company = team['company_name']

    script = f"""
OUTREACH SCRIPT FOR: {founder} - {company}

Opening:
"Hi {founder.split()[0]}, it's David from Bloom. I've been reviewing our interview from {team['date']} and wanted to share something exciting with you..."

Hook:
{strategy['talking_points'][0] if strategy['talking_points'] else 'Bloom is transitioning to a cooperative model'}

Value Proposition:
"We're bringing together the {1011} teams we've trained into a cooperative structure where we're stronger together. Here's what this means for {company}:"

Specific Benefits:
{chr(10).join('• ' + vp for vp in strategy['cooperative_value_prop'][:4])}

Sector-Specific Angle:
{strategy['approach']}

Call to Action:
"Would you be open to a 20-minute call to explore this? I think there are some specific partnerships that could accelerate {company}'s growth."

Follow-up:
"I'll send over a one-pager on the cooperative structure and some initial ideas for {company}."
"""

    return script

def prioritize_all_teams(teams: List[Dict]) -> List[TeamResearchProfile]:
    """Process all teams and create prioritized research profiles"""

    profiles = []

    for team in teams:
        # Generate strategy
        strategy = generate_outreach_strategy(team)

        # Create research profile
        profile = TeamResearchProfile(
            company_name=team['company_name'],
            founder=team['founder'],
            program=team['program'],
            stage=team['stage'],
            sector=team.get('sector'),
            current_status='active',  # Would be researched via LinkedIn/web
            outreach_priority=strategy['priority'],
            outreach_approach=strategy['approach'],
            talking_points=strategy['talking_points'],
            potential_value=f"Part of {strategy['approach']} cluster",
            cooperative_readiness=7,  # Default - would assess via research
            can_contribute=["Sector expertise", "Network connections"],
            needs_from_coop=strategy['cooperative_value_prop'][:3]
        )

        profiles.append(profile)

    # Sort by priority
    profiles.sort(key=lambda p: p.outreach_priority, reverse=True)

    return profiles

def main():
    """Main research agent pipeline"""

    base_dir = Path("/home/user/BloomHarvest")
    data_dir = base_dir / "strategic_analysis/data"
    output_dir = base_dir / "strategic_analysis/outputs"

    # Load teams
    with open(data_dir / "teams_structured.json", 'r') as f:
        teams = json.load(f)

    print(f"🔍 Researching {len(teams)} teams and generating outreach strategies...")

    # Generate research profiles
    profiles = prioritize_all_teams(teams)

    # Save profiles
    profiles_file = output_dir / "team_research_profiles.json"
    with open(profiles_file, 'w', encoding='utf-8') as f:
        json.dump([asdict(p) for p in profiles], f, indent=2, ensure_ascii=False)

    print(f"✅ Generated {len(profiles)} research profiles")
    print(f"📄 Saved to: {profiles_file}")

    # Generate outreach scripts for top 10
    scripts_dir = output_dir / "outreach_scripts"
    scripts_dir.mkdir(exist_ok=True)

    print(f"\n📝 Generating personalized outreach scripts for top 10 teams...")

    for profile in profiles[:10]:
        # Find original team data
        team = next(t for t in teams if t['company_name'] == profile.company_name)
        strategy = generate_outreach_strategy(team)
        script = generate_talking_points(team, strategy)

        # Save script
        safe_name = profile.company_name.replace(' ', '_').replace('/', '_')
        script_file = scripts_dir / f"{safe_name}_outreach.txt"
        script_file.write_text(script, encoding='utf-8')

        print(f"   ✓ {profile.company_name} (Priority: {profile.outreach_priority})")

    print(f"\n✅ Scripts saved to: {scripts_dir}")

    # Generate summary report
    print(f"\n📊 OUTREACH PRIORITY SUMMARY")
    print(f"{'='*60}")

    for i, profile in enumerate(profiles[:10], 1):
        print(f"\n{i}. {profile.company_name} - {profile.founder}")
        print(f"   Priority: {profile.outreach_priority}/10")
        print(f"   Approach: {profile.outreach_approach}")
        print(f"   Value: {profile.potential_value}")

    return profiles

if __name__ == "__main__":
    main()
