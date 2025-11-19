#!/usr/bin/env python3
"""
Interactive Dashboard Generator
Creates an HTML dashboard for exploring all teams, sectors, and clusters
"""

import json
from pathlib import Path
from typing import Dict, List, Any

BASE_DIR = Path(__file__).parent.parent
NETWORK_DIR = BASE_DIR / "outputs" / "network_analysis"
EMBEDDINGS_DIR = BASE_DIR / "outputs" / "embeddings"
DASHBOARD_DIR = BASE_DIR / "dashboards"


class DashboardGenerator:
    """Generate interactive HTML dashboards"""

    def __init__(self):
        self.network_data = {}
        self.projections = {}
        self.priority_teams = []
        self.partnerships = []
        self.clusters = {}
        self.insights = {}

    def load_data(self):
        """Load all analysis data"""
        print("📊 Loading analysis data...")

        # Load network analysis
        with open(NETWORK_DIR / "network_analysis.json", 'r') as f:
            self.network_data = json.load(f)

        # Load projections
        with open(NETWORK_DIR / "cooperative_projections.json", 'r') as f:
            self.projections = json.load(f)

        # Load priority teams
        with open(NETWORK_DIR / "priority_outreach_top100.json", 'r') as f:
            self.priority_teams = json.load(f)

        # Load partnerships
        with open(NETWORK_DIR / "partnership_opportunities.json", 'r') as f:
            self.partnerships = json.load(f)

        # Load embeddings data (if available)
        clusters_file = EMBEDDINGS_DIR / "similarity_clusters.json"
        if clusters_file.exists():
            with open(clusters_file, 'r') as f:
                self.clusters = json.load(f)

            with open(EMBEDDINGS_DIR / "cluster_insights.json", 'r') as f:
                self.insights = json.load(f)

        print("✅ Data loaded successfully")

    def generate_main_dashboard(self) -> str:
        """Generate main dashboard HTML"""
        total_teams = self.network_data['total_teams']

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bloom Cooperative - Strategic Transition Dashboard</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            padding: 20px;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}

        .header {{
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            margin-bottom: 30px;
            text-align: center;
        }}

        h1 {{
            color: #667eea;
            font-size: 3em;
            margin-bottom: 10px;
        }}

        .subtitle {{
            color: #666;
            font-size: 1.2em;
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}

        .stat-card {{
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.3s;
        }}

        .stat-card:hover {{
            transform: translateY(-5px);
        }}

        .stat-number {{
            font-size: 3em;
            font-weight: bold;
            color: #667eea;
            margin-bottom: 10px;
        }}

        .stat-label {{
            color: #666;
            font-size: 1.1em;
        }}

        .section {{
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }}

        .section h2 {{
            color: #667eea;
            margin-bottom: 20px;
            font-size: 2em;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }}

        .chart-container {{
            margin: 20px 0;
        }}

        .bar-chart {{
            margin: 15px 0;
        }}

        .bar {{
            display: flex;
            align-items: center;
            margin: 10px 0;
        }}

        .bar-label {{
            min-width: 150px;
            font-weight: 600;
            color: #333;
        }}

        .bar-fill {{
            flex: 1;
            display: flex;
            align-items: center;
        }}

        .bar-inner {{
            height: 30px;
            background: linear-gradient(90deg, #667eea, #764ba2);
            border-radius: 5px;
            transition: width 0.5s;
            display: flex;
            align-items: center;
            padding: 0 10px;
            color: white;
            font-weight: bold;
        }}

        .revenue-projections {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}

        .projection-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }}

        .projection-card h3 {{
            font-size: 1.5em;
            margin-bottom: 15px;
            text-transform: uppercase;
        }}

        .projection-amount {{
            font-size: 2.5em;
            font-weight: bold;
            margin: 10px 0;
        }}

        .projection-details {{
            opacity: 0.9;
            margin-top: 10px;
        }}

        .priority-list {{
            max-height: 600px;
            overflow-y: auto;
        }}

        .priority-item {{
            background: #f8f9fa;
            padding: 20px;
            margin: 10px 0;
            border-radius: 10px;
            border-left: 5px solid #667eea;
            transition: background 0.3s;
        }}

        .priority-item:hover {{
            background: #e9ecef;
        }}

        .priority-rank {{
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            margin-right: 10px;
        }}

        .priority-score {{
            float: right;
            background: #764ba2;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
        }}

        .team-name {{
            font-size: 1.3em;
            font-weight: bold;
            margin: 10px 0;
            color: #333;
        }}

        .team-details {{
            color: #666;
            margin: 5px 0;
        }}

        .reasons {{
            margin-top: 10px;
        }}

        .reason-tag {{
            display: inline-block;
            background: #e9ecef;
            padding: 5px 10px;
            border-radius: 5px;
            margin: 3px;
            font-size: 0.9em;
        }}

        .nav-tabs {{
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            border-bottom: 2px solid #e9ecef;
        }}

        .nav-tab {{
            padding: 15px 30px;
            background: #f8f9fa;
            border: none;
            border-radius: 10px 10px 0 0;
            cursor: pointer;
            font-size: 1.1em;
            transition: all 0.3s;
        }}

        .nav-tab:hover {{
            background: #e9ecef;
        }}

        .nav-tab.active {{
            background: #667eea;
            color: white;
        }}

        .tab-content {{
            display: none;
        }}

        .tab-content.active {{
            display: block;
        }}

        .partnership-card {{
            background: #f8f9fa;
            padding: 20px;
            margin: 15px 0;
            border-radius: 10px;
            border-left: 5px solid #28a745;
        }}

        .partnership-type {{
            display: inline-block;
            background: #28a745;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            margin-bottom: 10px;
        }}

        @media (max-width: 768px) {{
            .stats-grid {{
                grid-template-columns: 1fr;
            }}

            h1 {{
                font-size: 2em;
            }}

            .revenue-projections {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌸 Bloom Cooperative</h1>
            <p class="subtitle">Strategic Transition Dashboard - Full Network Analysis</p>
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">{total_teams}</div>
                <div class="stat-label">Total Teams</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(self.network_data['by_sector'])}</div>
                <div class="stat-label">Sectors</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(self.network_data['by_country'])}</div>
                <div class="stat-label">Countries</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(self.priority_teams)}</div>
                <div class="stat-label">Priority Targets</div>
            </div>
        </div>

        <div class="section">
            <h2>💰 Cooperative Revenue Projections</h2>
            <div class="revenue-projections">
"""

        for scenario, data in self.projections['scenarios'].items():
            html += f"""
                <div class="projection-card">
                    <h3>{scenario.title()}</h3>
                    <div class="projection-amount">${data['annual_revenue']:,}</div>
                    <div class="projection-details">
                        {data['teams']} teams ({data['adoption_rate']*100:.0f}% adoption)<br>
                        {data['description']}
                    </div>
                </div>
"""

        html += """
            </div>
        </div>

        <div class="section">
            <div class="nav-tabs">
                <button class="nav-tab active" onclick="showTab('sectors')">Sectors</button>
                <button class="nav-tab" onclick="showTab('countries')">Countries</button>
                <button class="nav-tab" onclick="showTab('programs')">Programs</button>
                <button class="nav-tab" onclick="showTab('priority')">Top 100 Priority</button>
                <button class="nav-tab" onclick="showTab('partnerships')">Partnerships</button>
            </div>

            <div id="sectors" class="tab-content active">
                <h2>📊 Teams by Sector</h2>
                <div class="bar-chart">
"""

        max_sector_count = max(data['count'] for data in self.network_data['by_sector'].values())
        for sector, data in list(self.network_data['by_sector'].items())[:15]:
            width_pct = (data['count'] / max_sector_count * 100)
            html += f"""
                    <div class="bar">
                        <div class="bar-label">{sector}</div>
                        <div class="bar-fill">
                            <div class="bar-inner" style="width: {width_pct}%">
                                {data['count']} teams ({data['percentage']}%)
                            </div>
                        </div>
                    </div>
"""

        html += """
                </div>
            </div>

            <div id="countries" class="tab-content">
                <h2>🌍 Teams by Country</h2>
                <div class="bar-chart">
"""

        max_country_count = max(data['count'] for data in self.network_data['by_country'].values())
        for country, data in list(self.network_data['by_country'].items())[:15]:
            width_pct = (data['count'] / max_country_count * 100)
            html += f"""
                    <div class="bar">
                        <div class="bar-label">{country}</div>
                        <div class="bar-fill">
                            <div class="bar-inner" style="width: {width_pct}%">
                                {data['count']} teams ({data['percentage']}%)
                            </div>
                        </div>
                    </div>
"""

        html += """
                </div>
            </div>

            <div id="programs" class="tab-content">
                <h2>🎓 Teams by Program</h2>
                <div class="bar-chart">
"""

        max_program_count = max(data['count'] for data in self.network_data['by_program'].values())
        for program, data in self.network_data['by_program'].items():
            width_pct = (data['count'] / max_program_count * 100)
            html += f"""
                    <div class="bar">
                        <div class="bar-label">{program}</div>
                        <div class="bar-fill">
                            <div class="bar-inner" style="width: {width_pct}%">
                                {data['count']} teams ({data['percentage']}%)
                            </div>
                        </div>
                    </div>
"""

        html += """
                </div>
            </div>

            <div id="priority" class="tab-content">
                <h2>🎯 Top 100 Priority Teams for Outreach</h2>
                <div class="priority-list">
"""

        for team in self.priority_teams[:100]:
            html += f"""
                    <div class="priority-item">
                        <span class="priority-rank">#{team['rank']}</span>
                        <span class="priority-score">Score: {team['priority_score']}</span>
                        <div class="team-name">{team['name']}</div>
                        <div class="team-details">
                            {team['sector']} | {team['country']} | {team['program']}
                        </div>
"""
            if team.get('contact'):
                html += f"""<div class="team-details">📧 {team['contact']}</div>"""
            if team.get('phone'):
                html += f"""<div class="team-details">📱 {team['phone']}</div>"""

            html += """<div class="reasons">"""
            for reason in team['reasons']:
                html += f"""<span class="reason-tag">✓ {reason}</span>"""
            html += """</div></div>"""

        html += """
                </div>
            </div>

            <div id="partnerships" class="tab-content">
                <h2>🤝 Partnership Opportunities</h2>
"""

        for partnership in self.partnerships[:20]:
            if partnership['type'] == 'cross-sector':
                html += f"""
                    <div class="partnership-card">
                        <span class="partnership-type">Cross-Sector</span>
                        <h3>{partnership['sectors'][0]} ↔ {partnership['sectors'][1]}</h3>
                        <p><strong>Synergy:</strong> {partnership['synergy']}</p>
                        <p>{partnership['team_count_1']} teams × {partnership['team_count_2']} teams = {partnership['potential_partnerships']} potential partnerships</p>
                    </div>
"""
            elif partnership['type'] == 'geographic-cluster':
                html += f"""
                    <div class="partnership-card">
                        <span class="partnership-type">Geographic Cluster</span>
                        <h3>{partnership['country']}</h3>
                        <p><strong>Opportunity:</strong> {partnership['opportunity']}</p>
                        <p>{partnership['team_count']} teams across {partnership.get('sector_count', 'multiple')} sectors</p>
                    </div>
"""

        html += """
            </div>
        </div>
    </div>

    <script>
        function showTab(tabName) {
            // Hide all tabs
            const tabs = document.querySelectorAll('.tab-content');
            tabs.forEach(tab => tab.classList.remove('active'));

            // Deactivate all nav tabs
            const navTabs = document.querySelectorAll('.nav-tab');
            navTabs.forEach(tab => tab.classList.remove('active'));

            // Show selected tab
            document.getElementById(tabName).classList.add('active');

            // Activate corresponding nav tab
            event.target.classList.add('active');
        }

        // Animate bars on load
        window.addEventListener('load', () => {
            const bars = document.querySelectorAll('.bar-inner');
            bars.forEach((bar, index) => {
                setTimeout(() => {
                    bar.style.opacity = '1';
                }, index * 50);
            });
        });
    </script>
</body>
</html>
"""

        return html

    def save_dashboard(self):
        """Save dashboard HTML"""
        print("\n📱 Generating dashboard...")

        DASHBOARD_DIR.mkdir(parents=True, exist_ok=True)

        # Generate main dashboard
        dashboard_html = self.generate_main_dashboard()

        # Save
        dashboard_path = DASHBOARD_DIR / "full_network_dashboard.html"
        with open(dashboard_path, 'w') as f:
            f.write(dashboard_html)

        print(f"✅ Dashboard saved to: {dashboard_path}")

        return dashboard_path


def main():
    """Main pipeline"""
    print("📱 Dashboard Generator")
    print("=" * 80)

    generator = DashboardGenerator()

    try:
        # Load data
        generator.load_data()

        # Generate and save dashboard
        dashboard_path = generator.save_dashboard()

        print("\n" + "=" * 80)
        print("✅ DASHBOARD COMPLETE!")
        print("=" * 80)
        print(f"\n🌐 Open in browser: {dashboard_path}")
        print("\nNext steps:")
        print("  1. Open the dashboard in your browser")
        print("  2. Explore sectors, countries, and programs")
        print("  3. Review top 100 priority teams for outreach")
        print("  4. Identify partnership opportunities")

    except FileNotFoundError as e:
        print(f"\n❌ ERROR: {e}")
        print("\nPlease run process_all_teams.py first to generate analysis data")


if __name__ == "__main__":
    main()
