# 🌸 Bloom Cooperative - Strategic Transition System

## Full Network Analysis Infrastructure (1,011+ Teams)

This is a **persistent, reusable analysis system** (not ephemeral chat outputs) designed to process ALL your teams and generate actionable insights for the cooperative transition.

---

## 🎯 What This System Does

### Phase 1: Foundation (Complete ✅)
1. **Convert interviews to markdown** → Enable text analysis
2. **Create unified data schema** → Structure for all 1,011 teams
3. **Build embeddings pipeline** → Cluster teams by similarity
4. **Set up persistent outputs** → JSON/HTML dashboards that persist

### Phase 2: Intelligence (Ready to Run 🚀)
1. **Process full teams CSV** → Analyze all 1,011 teams
2. **Generate network insights** → Sectors, countries, programs
3. **Calculate revenue projections** → Conservative, Moderate, Optimistic
4. **Prioritize outreach** → Top 100 teams to contact first
5. **Identify partnerships** → Cross-sector and geographic synergies

---

## 📁 Directory Structure

```
strategic_analysis/
├── data/
│   └── teams/                    # Upload your CSV here
│       └── all_teams.csv         # Your Airtable export
│
├── scripts/
│   ├── process_all_teams.py      # Main analysis engine
│   ├── generate_embeddings.py    # Similarity clustering
│   └── generate_dashboard.py     # Interactive visualization
│
├── outputs/
│   ├── network_analysis/         # All analysis results
│   │   ├── network_analysis.json           # Full network breakdown
│   │   ├── cooperative_projections.json    # Revenue scenarios
│   │   ├── priority_outreach_top100.json   # Top targets
│   │   ├── partnership_opportunities.json  # Synergies
│   │   ├── cluster_report.txt              # Human-readable summary
│   │   └── all_teams_normalized.json       # Clean data
│   │
│   └── embeddings/               # Similarity analysis
│       ├── team_embeddings.json           # Team vectors
│       ├── similarity_clusters.json       # Clustered teams
│       └── cluster_insights.json          # Patterns found
│
├── dashboards/
│   └── full_network_dashboard.html   # Interactive explorer
│
└── run_full_analysis.sh          # Master pipeline script
```

---

## 🚀 Quick Start

### Step 1: Upload Your Teams CSV

Place your Airtable export at:
```bash
strategic_analysis/data/teams/all_teams.csv
```

**Expected columns** (flexible - will auto-detect):
- Team Name / Name
- Sector / Industry
- Country / Location
- Program / Cohort
- Stage / Status
- Description / About
- Contact / Email
- Phone / Mobile
- Founder / Founder Name
- Website / URL

### Step 2: Run the Analysis

```bash
cd strategic_analysis
chmod +x run_full_analysis.sh
./run_full_analysis.sh
```

This will:
1. ✅ Process all teams
2. ✅ Generate network analysis
3. ✅ Calculate revenue projections
4. ✅ Prioritize outreach targets
5. ✅ Create interactive dashboard

### Step 3: Explore Results

Open in your browser:
```bash
open dashboards/full_network_dashboard.html
```

---

## 📊 What You'll Get

### 1. Network Analysis (`outputs/network_analysis/`)

**network_analysis.json**
- Total teams count
- Breakdown by sector (EdTech, FinTech, HealthTech, etc.)
- Breakdown by country (Lebanon, Jordan, Palestine, etc.)
- Breakdown by program (ACSI1-4, HerMeNow, etc.)
- Top sectors, countries, programs

**cooperative_projections.json**
```json
{
  "scenarios": {
    "conservative": {
      "adoption_rate": 0.10,
      "teams": 101,
      "annual_revenue": 101000
    },
    "moderate": {
      "adoption_rate": 0.30,
      "teams": 303,
      "annual_revenue": 303000
    },
    "optimistic": {
      "adoption_rate": 0.50,
      "teams": 505,
      "annual_revenue": 505000
    }
  }
}
```

**priority_outreach_top100.json**
Top 100 teams ranked by:
- High-growth sectors (EdTech, FinTech, HealthTech) = +3 points
- Recent programs (ACSI3, ACSI4, HerMeNow) = +3 points
- Active stage (Growth, Scaling, Launched) = +2 points
- Strategic markets (Lebanon, Jordan, Palestine) = +2 points
- Has contact info = +1 point
- Detailed profile = +1 point

**partnership_opportunities.json**
- Cross-sector synergies (EdTech + FinTech, etc.)
- Geographic clusters (local cooperative chapters)
- Complementary capabilities

### 2. Embeddings Analysis (`outputs/embeddings/`)

**similarity_clusters.json**
Teams grouped by:
- Shared keywords
- Similar sectors
- Common challenges
- Complementary capabilities

**cluster_insights.json**
- Largest clusters
- Cross-sector opportunities
- Geographic hubs

### 3. Interactive Dashboard (`dashboards/`)

**full_network_dashboard.html**
- 📊 Visual breakdown by sector, country, program
- 💰 Revenue projections (3 scenarios)
- 🎯 Top 100 priority teams (with contact info)
- 🤝 Partnership opportunities
- 🔍 Filterable, sortable, explorable

---

## 💡 Use Cases

### For Bilal (Transition Planning)
1. **Contact Priority Teams**: Use `priority_outreach_top100.json` to call teams ranked by strategic fit
2. **Prepare Pitches**: Customize by sector/country/program
3. **Track Progress**: Update team status as you contact them
4. **Find Champions**: Identify early adopters in each cluster

### For Investors
1. **Show Network Size**: 1,011 teams across multiple sectors
2. **Demonstrate Revenue Potential**: Conservative = $100K/yr, Optimistic = $500K/yr
3. **Highlight Synergies**: Cross-sector partnerships increase value
4. **Geographic Strategy**: Regional hubs in Lebanon, Jordan, Palestine

### For Team Members (Future)
1. **Find Partners**: Search by sector/country/keywords
2. **Join Clusters**: Connect with similar teams
3. **Access Resources**: Shared tools, knowledge, networks
4. **Collaborate**: Find complementary capabilities

---

## 🔄 Updating the Analysis

As you contact teams and gather new data:

1. **Update the CSV** with new information
2. **Re-run the analysis**:
   ```bash
   ./run_full_analysis.sh
   ```
3. **Dashboard auto-refreshes** with latest data

---

## 🎯 Next Steps After Running

### Immediate Actions
1. ✅ Open `dashboards/full_network_dashboard.html`
2. ✅ Review `outputs/network_analysis/cluster_report.txt`
3. ✅ Check `outputs/network_analysis/priority_outreach_top100.json`
4. ✅ Call top 10 teams TODAY

### This Week
1. Contact top 50 priority teams
2. Pitch cooperative benefits by sector
3. Identify 10-20 champions
4. Schedule follow-up calls

### This Month
1. Launch pilot with 30-50 teams
2. Refine value proposition based on feedback
3. Create sector-specific cooperative benefits
4. Build member dashboard (Phase 3)

---

## 🛠️ Technical Details

### Data Normalization
The system automatically:
- Cleans sector names (education → EdTech)
- Normalizes country names (lb → Lebanon)
- Extracts program codes (ACSI 1 → ACSI1)
- Standardizes stages (launch → Launched)

### Scoring Algorithm
Priority score = sector_points + program_points + stage_points + market_points + contact_points + profile_points

### Clustering Method
- TF-IDF keyword extraction
- Jaccard similarity
- Sector/country bonuses
- Minimum cluster size = 3 teams

---

## 📞 Support

Questions? Issues? Ideas?

1. Check `outputs/network_analysis/cluster_report.txt` for summary
2. Review this README
3. Examine the scripts for customization

---

## 🎉 You're Ready!

Upload your CSV and run:
```bash
./run_full_analysis.sh
```

**Transform 1,011 teams into a cooperative network. Let's go! 🚀**
