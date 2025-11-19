#!/usr/bin/env python3
"""
Team Similarity Analysis using Embeddings
Clusters teams by similarity to find synergies and patterns
"""

import json
import os
from pathlib import Path
from typing import List, Dict, Any
from collections import defaultdict
import re

# For embeddings, we'll use a simple TF-IDF approach
# For production, could use OpenAI embeddings or sentence-transformers

BASE_DIR = Path(__file__).parent.parent
NETWORK_DIR = BASE_DIR / "outputs" / "network_analysis"
EMBEDDINGS_DIR = BASE_DIR / "outputs" / "embeddings"


class TeamEmbeddings:
    """Generate and analyze team embeddings for similarity clustering"""

    def __init__(self):
        self.teams = []
        self.embeddings = {}
        self.clusters = defaultdict(list)

    def load_teams(self):
        """Load normalized teams from network analysis"""
        teams_file = NETWORK_DIR / "all_teams_normalized.json"

        if not teams_file.exists():
            raise FileNotFoundError(
                f"Teams file not found: {teams_file}\n"
                "Please run process_all_teams.py first"
            )

        with open(teams_file, 'r') as f:
            self.teams = json.load(f)

        print(f"✅ Loaded {len(self.teams)} teams for embedding analysis")
        return self.teams

    def create_team_description(self, team: Dict) -> str:
        """Create a text description for embedding"""
        parts = []

        if team.get('name'):
            parts.append(team['name'])
        if team.get('sector'):
            parts.append(f"sector: {team['sector']}")
        if team.get('description'):
            parts.append(team['description'])
        if team.get('country'):
            parts.append(f"country: {team['country']}")
        if team.get('program'):
            parts.append(f"program: {team['program']}")

        return " ".join(parts)

    def generate_simple_embeddings(self):
        """Generate simple keyword-based embeddings"""
        print("\n🔮 Generating embeddings...")

        for team in self.teams:
            description = self.create_team_description(team)

            # Simple keyword extraction
            keywords = self.extract_keywords(description)

            self.embeddings[team['id']] = {
                'team_id': team['id'],
                'team_name': team['name'],
                'keywords': keywords,
                'sector': team['sector'],
                'country': team['country'],
                'program': team['program']
            }

        print(f"✅ Generated embeddings for {len(self.embeddings)} teams")

    def extract_keywords(self, text: str) -> List[str]:
        """Extract meaningful keywords from text"""
        # Convert to lowercase
        text = text.lower()

        # Remove special characters
        text = re.sub(r'[^a-z0-9\s]', ' ', text)

        # Split into words
        words = text.split()

        # Filter out common words
        stopwords = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been',
            'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
            'could', 'should', 'may', 'might', 'must', 'can', 'this', 'that',
            'these', 'those', 'we', 'our', 'us', 'you', 'your', 'they', 'their'
        }

        keywords = [w for w in words if w not in stopwords and len(w) > 3]

        return keywords

    def cluster_by_similarity(self):
        """Cluster teams by keyword similarity"""
        print("\n🎯 Clustering teams by similarity...")

        # Keyword-based clustering
        keyword_clusters = defaultdict(list)

        for team_id, embedding in self.embeddings.items():
            keywords = embedding['keywords']

            # Find top keywords for this team
            for keyword in keywords[:5]:  # Top 5 keywords
                keyword_clusters[keyword].append({
                    'team_id': team_id,
                    'team_name': embedding['team_name'],
                    'sector': embedding['sector'],
                    'country': embedding['country']
                })

        # Filter clusters with at least 3 teams
        significant_clusters = {
            keyword: teams
            for keyword, teams in keyword_clusters.items()
            if len(teams) >= 3
        }

        # Sort by cluster size
        sorted_clusters = sorted(
            significant_clusters.items(),
            key=lambda x: len(x[1]),
            reverse=True
        )

        self.clusters = dict(sorted_clusters[:50])  # Top 50 clusters

        print(f"✅ Found {len(self.clusters)} significant clusters")

        return self.clusters

    def find_similar_teams(self, team_id: str, top_n: int = 10) -> List[Dict]:
        """Find most similar teams to a given team"""
        if team_id not in self.embeddings:
            return []

        target_embedding = self.embeddings[team_id]
        target_keywords = set(target_embedding['keywords'])

        # Calculate similarity scores
        similarities = []

        for other_id, other_embedding in self.embeddings.items():
            if other_id == team_id:
                continue

            other_keywords = set(other_embedding['keywords'])

            # Jaccard similarity
            intersection = len(target_keywords & other_keywords)
            union = len(target_keywords | other_keywords)

            if union > 0:
                similarity = intersection / union

                # Bonus for same sector
                if other_embedding['sector'] == target_embedding['sector']:
                    similarity += 0.2

                # Bonus for same country
                if other_embedding['country'] == target_embedding['country']:
                    similarity += 0.1

                similarities.append({
                    'team_id': other_id,
                    'team_name': other_embedding['team_name'],
                    'sector': other_embedding['sector'],
                    'country': other_embedding['country'],
                    'similarity_score': round(similarity, 3),
                    'common_keywords': list(target_keywords & other_keywords)[:5]
                })

        # Sort by similarity
        similarities.sort(key=lambda x: x['similarity_score'], reverse=True)

        return similarities[:top_n]

    def generate_cluster_insights(self) -> Dict:
        """Generate insights from clusters"""
        insights = {
            'total_clusters': len(self.clusters),
            'largest_clusters': [],
            'cross_sector_clusters': [],
            'geographic_clusters': []
        }

        # Largest clusters
        for keyword, teams in list(self.clusters.items())[:10]:
            sectors = defaultdict(int)
            countries = defaultdict(int)

            for team in teams:
                sectors[team['sector']] += 1
                countries[team['country']] += 1

            insights['largest_clusters'].append({
                'keyword': keyword,
                'team_count': len(teams),
                'sectors': dict(sectors),
                'countries': dict(countries),
                'sample_teams': [t['team_name'] for t in teams[:5]]
            })

        # Cross-sector clusters (clusters with teams from 3+ sectors)
        for keyword, teams in self.clusters.items():
            sectors = set(team['sector'] for team in teams)
            if len(sectors) >= 3:
                insights['cross_sector_clusters'].append({
                    'keyword': keyword,
                    'sectors': list(sectors),
                    'team_count': len(teams),
                    'opportunity': f"Cross-sector collaboration around '{keyword}'"
                })

        # Geographic clusters (same country, different sectors)
        country_groups = defaultdict(lambda: defaultdict(list))
        for team_id, embedding in self.embeddings.items():
            country = embedding['country']
            sector = embedding['sector']
            country_groups[country][sector].append(embedding['team_name'])

        for country, sectors in country_groups.items():
            if len(sectors) >= 3:  # At least 3 different sectors
                insights['geographic_clusters'].append({
                    'country': country,
                    'sector_count': len(sectors),
                    'total_teams': sum(len(teams) for teams in sectors.values()),
                    'sectors': {sector: len(teams) for sector, teams in sectors.items()},
                    'opportunity': f"Regional cooperative hub in {country}"
                })

        return insights

    def save_results(self):
        """Save embeddings and clustering results"""
        print("\n💾 Saving embeddings and clusters...")

        EMBEDDINGS_DIR.mkdir(parents=True, exist_ok=True)

        # Save embeddings
        with open(EMBEDDINGS_DIR / "team_embeddings.json", 'w') as f:
            json.dump(self.embeddings, f, indent=2)
        print("✅ Saved: team_embeddings.json")

        # Save clusters
        clusters_output = {
            keyword: {
                'team_count': len(teams),
                'teams': teams
            }
            for keyword, teams in self.clusters.items()
        }
        with open(EMBEDDINGS_DIR / "similarity_clusters.json", 'w') as f:
            json.dump(clusters_output, f, indent=2)
        print("✅ Saved: similarity_clusters.json")

        # Save cluster insights
        insights = self.generate_cluster_insights()
        with open(EMBEDDINGS_DIR / "cluster_insights.json", 'w') as f:
            json.dump(insights, f, indent=2)
        print("✅ Saved: cluster_insights.json")

        # Generate similarity matrix for sample teams (first 50)
        sample_teams = list(self.embeddings.keys())[:50]
        similarity_matrix = {}

        for team_id in sample_teams:
            similar = self.find_similar_teams(team_id, top_n=10)
            similarity_matrix[self.embeddings[team_id]['team_name']] = similar

        with open(EMBEDDINGS_DIR / "similarity_matrix_sample.json", 'w') as f:
            json.dump(similarity_matrix, f, indent=2)
        print("✅ Saved: similarity_matrix_sample.json")


def main():
    """Main pipeline"""
    print("🔮 Team Similarity Analysis - Embeddings Pipeline")
    print("=" * 80)

    embedder = TeamEmbeddings()

    try:
        # Load teams
        embedder.load_teams()

        # Generate embeddings
        embedder.generate_simple_embeddings()

        # Cluster by similarity
        embedder.cluster_by_similarity()

        # Save results
        embedder.save_results()

        print("\n" + "=" * 80)
        print("✅ EMBEDDINGS COMPLETE!")
        print("=" * 80)
        print(f"\n📊 Generated embeddings for {len(embedder.embeddings)} teams")
        print(f"🎯 Identified {len(embedder.clusters)} similarity clusters")
        print(f"\n📁 Results saved to: {EMBEDDINGS_DIR}")

    except FileNotFoundError as e:
        print(f"\n❌ ERROR: {e}")
        print("\nPlease run process_all_teams.py first to generate normalized team data")


if __name__ == "__main__":
    main()
