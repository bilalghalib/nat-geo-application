# 📤 Upload Your Teams CSV Here

## Quick Instructions

1. **Export your teams from Airtable** as CSV
2. **Upload to**: `strategic_analysis/data/teams/all_teams.csv`
3. **Run**: `./run_full_analysis.sh`
4. **View results**: Open `dashboards/full_network_dashboard.html`

---

## Expected CSV Format

Your Airtable export should have columns like:

| Column Name | Alternative Names | Description |
|------------|------------------|-------------|
| Team Name | Name, team_name | Company/team name |
| Sector | Industry, sector | EdTech, FinTech, etc. |
| Country | Location, country | Lebanon, Jordan, etc. |
| Program | Cohort, program | ACSI1, ACSI2, HerMeNow |
| Stage | Status, stage | Idea, MVP, Launched, etc. |
| Description | About, description | What the team does |
| Contact | Email, contact | Email address |
| Phone | Mobile, phone | Phone number |
| Founder | Founder Name, founder | Founder's name |
| Website | URL, website | Team website |

**Don't worry about exact column names** - the system auto-detects common variations!

---

## Alternative Upload Locations

If you can't use the default location, you can also upload to:

1. `strategic_analysis/data/teams/teams.csv`
2. `Bloom_History_And_Research/Bloom_Teams/All_Teams_Airtable_Export_Teams X Programs + Workspace-All records.csv`

The system will automatically find it.

---

## What Happens Next?

Once you upload and run `./run_full_analysis.sh`, you'll get:

✅ Network analysis (sectors, countries, programs)
✅ Revenue projections (3 scenarios)
✅ Top 100 priority teams for outreach
✅ Partnership opportunities
✅ Similarity clusters
✅ Interactive dashboard

**Processing time**: ~30-60 seconds for 1,011 teams

---

## Need Help?

Read `TEAM_ANALYSIS_README.md` for full documentation.

Ready? **Upload your CSV and let's analyze 1,011 teams! 🚀**
