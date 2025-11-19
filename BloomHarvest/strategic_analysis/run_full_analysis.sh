#!/bin/bash
# Strategic Transition System - Master Pipeline
# Run complete analysis on all teams

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  🌸 BLOOM COOPERATIVE - STRATEGIC TRANSITION SYSTEM 🌸        ║"
echo "║  Full Network Analysis Pipeline                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if Python3 is available
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ ERROR: Python 3 is not installed${NC}"
    exit 1
fi

echo -e "${BLUE}📂 Checking for teams CSV...${NC}"

# Look for CSV file
CSV_PATH=""
if [ -f "data/teams/all_teams.csv" ]; then
    CSV_PATH="data/teams/all_teams.csv"
elif [ -f "data/teams/teams.csv" ]; then
    CSV_PATH="data/teams/teams.csv"
elif [ -f "../Bloom_History_And_Research/Bloom_Teams/All_Teams_Airtable_Export_Teams X Programs + Workspace-All records.csv" ]; then
    CSV_PATH="../Bloom_History_And_Research/Bloom_Teams/All_Teams_Airtable_Export_Teams X Programs + Workspace-All records.csv"
fi

if [ -z "$CSV_PATH" ]; then
    echo -e "${RED}❌ ERROR: No teams CSV found!${NC}"
    echo ""
    echo "Please upload your Airtable export CSV to one of these locations:"
    echo "  - strategic_analysis/data/teams/all_teams.csv"
    echo "  - strategic_analysis/data/teams/teams.csv"
    echo ""
    echo "Expected columns: Team Name, Sector, Country, Program, Stage, Contact, etc."
    exit 1
fi

echo -e "${GREEN}✅ Found CSV: $CSV_PATH${NC}"
echo ""

# Step 1: Process all teams
echo -e "${BLUE}Step 1/3: Processing all teams and generating network analysis...${NC}"
python3 scripts/process_all_teams.py

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ ERROR: Team processing failed${NC}"
    exit 1
fi
echo ""

# Step 2: Generate embeddings and clusters
echo -e "${BLUE}Step 2/3: Generating embeddings and similarity clusters...${NC}"
python3 scripts/generate_embeddings.py

if [ $? -ne 0 ]; then
    echo -e "${YELLOW}⚠️  WARNING: Embeddings failed, but continuing...${NC}"
fi
echo ""

# Step 3: Generate dashboard
echo -e "${BLUE}Step 3/3: Generating interactive dashboard...${NC}"
python3 scripts/generate_dashboard.py

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ ERROR: Dashboard generation failed${NC}"
    exit 1
fi
echo ""

# Success!
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  ✅ ANALYSIS COMPLETE!                                        ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
echo -e "${GREEN}📊 Results available in:${NC}"
echo "  • outputs/network_analysis/     - Network insights, projections, priorities"
echo "  • outputs/embeddings/            - Similarity clusters and insights"
echo "  • dashboards/                    - Interactive HTML dashboard"
echo ""
echo -e "${YELLOW}🚀 Next Steps:${NC}"
echo "  1. Open dashboards/full_network_dashboard.html in your browser"
echo "  2. Review outputs/network_analysis/priority_outreach_top100.json"
echo "  3. Read outputs/network_analysis/cluster_report.txt"
echo "  4. Check outputs/network_analysis/partnership_opportunities.json"
echo ""
echo -e "${BLUE}Ready to transform 1,011 teams into a cooperative network!${NC}"
