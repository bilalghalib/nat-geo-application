# Deep Interview Extraction Design

**Using SAREC (Structured Assessment, Reasoning, Evidence, Confidence) protocol**

---

## 5 Core Questions Guiding Extraction

### Q1: Who is ready for cooperative pilot?
**Why:** Need 10-15 founding members who are stable, values-aligned, and engaged
**Extract:**
- Revenue stability (monthly, growth trend)
- Team health (size, turnover, satisfaction signals)
- Values alignment (ubuntu, cooperation, anti-extractive)
- Engagement level (enthusiasm in interview, follow-up interest)
- Readiness signals ("I would love to be part of this")

### Q2: What do people need most (post-program)?
**Why:** Design services around actual needs, not assumptions
**Extract:**
- Explicit needs (directly stated: "I need mentorship")
- Implicit needs (inferred from problems: "overwhelmed" → delegation support)
- Frequency ranking (what's mentioned most across interviews)
- Willingness to pay (would they pay for sustained support?)
- Current gaps (what they can't get elsewhere)

### Q3: What concerns/risks did people raise about cooperative model?
**Why:** Address objections proactively in design
**Extract:**
- Fairness concerns ("What about imbalance?")
- Feasibility doubts ("How would this actually work?")
- Trust issues ("Money ruins relationships")
- Complexity worries ("Sounds complicated")
- Eligibility questions ("What's the baseline?")

### Q4: What specific opportunities exist RIGHT NOW?
**Why:** Actionable next steps with names, dates, organizations
**Extract:**
- Connections to make (people, orgs)
- Markets to enter (Kuwait, Iraq, etc.)
- Partnerships possible (across alumni)
- Funding sources (billionaire friend, programs)
- Timing windows ("meeting next week")

### Q5: What design principles should guide the cooperative?
**Why:** Build model from actual insights, not theory
**Extract:**
- What worked in Bloom programs
- What didn't work (or was missing)
- Suggested improvements from founders
- Recurring patterns (flexibility > rigidity)
- Contradictions to resolve (scale vs. humane)

---

## Extraction Categories (Comprehensive)

### 1. FINANCIAL DATA
**Structured fields:**
```json
{
  "entity_id": "hussein_robotx",
  "metrics": {
    "monthly_revenue": {"value": 10000, "currency": "USD", "month": "2024-07"},
    "team_size": {"full_time": 2, "contractors": 5, "total": 7},
    "growth_rate": "positive",
    "profitability": "profitable",
    "runway": null
  },
  "evidence": ["interview_line_91", "interview_line_97"],
  "confidence": 0.95
}
```

### 2. SENTIMENT ANALYSIS
**Per person, per topic:**
```json
{
  "entity_id": "garene_parentshub",
  "topic": "cooperative_model",
  "sentiment": {
    "score": 0.85,  // -1 to +1
    "label": "very_positive",
    "intensity": "enthusiastic"
  },
  "evidence": [
    "This is very refreshing, honestly",
    "I would love to be part of it",
    "You're disrupting the norm"
  ],
  "confidence": 0.92
}
```

### 3. READINESS ASSESSMENT (SAREC)
```json
{
  "id": "readiness.cooperative_pilot.garene_parentshub.v1",
  "score": 0.88,
  "reasoning": "High enthusiasm + stable revenue + values-aligned + engaged in co-design during interview",
  "evidence": [
    {"type": "quote", "text": "I would love to be part of this", "loc": "line_310"},
    {"type": "metric", "name": "revenue_stability", "value": "stable"},
    {"type": "pattern", "name": "co_design_engagement", "instances": 8}
  ],
  "confidence": 0.85,
  "assessor": {"type": "llm", "id": "claude-sonnet-4.5", "timestamp": "2025-11-18"},
  "dimensions": {
    "financial_stability": 0.75,
    "values_alignment": 0.95,
    "engagement_level": 0.92,
    "growth_mindset": 0.88
  }
}
```

### 4. NEEDS TAXONOMY
```json
{
  "entity_id": "hussein_robotx",
  "needs": [
    {
      "category": "mentorship",
      "type": "explicit",
      "priority": "high",
      "evidence": "I'm thinking of starting again with a mentor",
      "willingness_to_pay": "implied_yes",
      "confidence": 0.90
    },
    {
      "category": "delegation_support",
      "type": "implied",
      "priority": "high",
      "evidence": "I'm very overwhelmed with all the work I have to manage",
      "willingness_to_pay": "unknown",
      "confidence": 0.75
    }
  ]
}
```

### 5. CONCERNS & OBJECTIONS
```json
{
  "topic": "cooperative_fairness",
  "concern": "revenue_imbalance",
  "raised_by": ["garene_parentshub"],
  "quote": "Someone like me I'm on the lower range... someone like Janna that's a whole different level. Isn't there an imbalance?",
  "severity": "medium",
  "addressable": true,
  "suggested_resolution": "Running average mechanism + pools by revenue tier",
  "confidence": 0.88
}
```

### 6. SPECIFIC OPPORTUNITIES
```json
{
  "opportunity_id": "iraq_mosul_reconstruction",
  "type": "market_expansion",
  "source": "mohamad_greenx",
  "specifics": {
    "organization": "ITC (International Trade Center)",
    "project": "Mosul rebuild - 200 homes",
    "search_terms": "Beit Mosul Iraq ITC",
    "product_fit": "GreeNX battery boxes + solar systems",
    "timeline": "immediate",
    "action_required": "email_introduction"
  },
  "potential_impact": "high",
  "effort_required": "medium",
  "confidence": 0.82
}
```

### 7. VALUES & PHILOSOPHY
```json
{
  "entity_id": "bilal_bloom",
  "values": [
    {
      "value": "relationships_over_revenue",
      "evidence": "We have 1,011 teams that we love. You can't buy that.",
      "strength": "core",
      "consistency": "high",
      "confidence": 0.95
    },
    {
      "mental_model": "aikido_principle",
      "description": "Use other's energy with least harm to both",
      "application": "Working with funders who have different philosophy",
      "confidence": 0.88
    }
  ]
}
```

### 8. EVOLUTION OF THINKING
```json
{
  "topic": "cooperative_structure",
  "timeline": [
    {"stage": "start", "concept": "100 people in one pool", "timestamp_estimate": "early_interview"},
    {"stage": "middle", "concept": "Fractal: 7 teams of 10 = 70", "timestamp_estimate": "mid_interview"},
    {"stage": "end", "concept": "15 people → delegates → 10-person council = 150 total", "timestamp_estimate": "late_interview"}
  ],
  "co_designed_with": "garene_parentshub",
  "evolution_type": "refinement_through_dialogue",
  "confidence": 0.91
}
```

### 9. META-PATTERNS (Cross-Interview)
```json
{
  "pattern_id": "crisis_drives_innovation",
  "instances": [
    {"entity": "mohamad_greenx", "crisis": "electricity_collapse", "innovation": "solar_wind_biogas"},
    {"entity": "garene_parentshub", "crisis": "war_disruption", "innovation": "online_education_pivot"},
    {"entity": "all_founders", "crisis": "usaid_cuts", "innovation": "rethinking_funding_models"}
  ],
  "frequency": "universal",
  "confidence": 0.96
}
```

### 10. NETWORK GRAPH
```json
{
  "connections": [
    {
      "node_a": "bilal_bloom",
      "node_b": "duo_security_founder",
      "relationship": "personal_friend",
      "strength": "high",
      "potential": "funding_source",
      "next_interaction": "paris_meeting_next_week",
      "confidence": 0.94
    },
    {
      "node_a": "hussein_robotx",
      "node_b": "razan_kuwait_education",
      "relationship": "potential_collaboration",
      "strength": "to_be_established",
      "opportunity": "kuwait_market_entry",
      "confidence": 0.70
    }
  ]
}
```

---

## Output Structure (Database-Ready)

### Master Schema:
```
bloom_insights/
├── entities/
│   ├── hussein_robotx.json
│   ├── garene_parentshub.json
│   └── mohamad_greenx.json
├── assessments/
│   ├── readiness_cooperative_pilot.json
│   ├── needs_analysis.json
│   └── concerns_risks.json
├── opportunities/
│   ├── iraq_reconstruction.json
│   ├── kuwait_expansion.json
│   └── billionaire_connection.json
├── patterns/
│   ├── meta_patterns.json
│   ├── design_principles.json
│   └── value_alignment.json
└── network/
    ├── connections_graph.json
    └── collaboration_opportunities.json
```

Each JSON file uses SAREC structure:
- **Assessment**: The claim/insight
- **Reasoning**: Why this conclusion
- **Evidence**: Quotes, metrics, patterns (dereferenceable)
- **Confidence**: 0-1 score

---

## Confidence Calibration

**0.95-1.0**: Direct quote, unambiguous, corroborated across multiple mentions
- Example: "Monthly revenue = $10K" (Hussein stated explicitly)

**0.85-0.94**: Strong inference from clear evidence, minimal ambiguity
- Example: Garene very interested in cooperative (multiple enthusiastic statements)

**0.70-0.84**: Reasonable inference, some interpretation required
- Example: Implied needs from problem descriptions

**0.50-0.69**: Suggestive evidence, higher uncertainty
- Example: Willingness to pay (not directly asked in all cases)

**<0.50**: Speculative, insufficient evidence
- Generally exclude from final database unless flagged as hypothesis

---

## Extraction Process

### Phase 1: Entity Extraction (Per Interview)
For each person interviewed:
1. Financial metrics
2. Sentiment scores
3. Needs (explicit + implicit)
4. Values/philosophy
5. Concerns raised
6. Opportunities mentioned

### Phase 2: Cross-Interview Analysis
1. Meta-patterns (what everyone mentions)
2. Contradictions (split opinions)
3. Evolution (how ideas changed)
4. Network graph (who connects to whom)

### Phase 3: SAREC Assessment Generation
1. Readiness scores (for pilot selection)
2. Priority ranking (who to contact first)
3. Risk assessment (what could go wrong)
4. Design principles (how to structure cooperative)

### Phase 4: Actionable Outputs
1. Top 10 pilot candidates (ranked with reasoning)
2. Immediate opportunities (with contacts/deadlines)
3. Design specifications (from collective insights)
4. FAQ (from questions people asked)

---

## Validation & Quality Checks

### Internal Consistency:
- Do sentiment scores align with readiness scores?
- Do stated needs match implied needs?
- Are financial claims consistent across interview?

### Cross-Interview Validation:
- Do multiple people corroborate same pattern?
- Are there contradictory claims?
- What's consensus vs. outlier opinion?

### Evidence Quality:
- Is quote exact or paraphrased?
- Is number explicit or estimated?
- Is inference justified by evidence?

---

## Next Steps

1. **Execute Deep Read** (20 interviews)
2. **Generate SAREC Objects** (all categories)
3. **Output to JSON** (structured database)
4. **Create Summary Reports** (human-readable)
5. **Build Query Interface** (for exploring data)

---

**Ready to execute?**

This will produce:
- ~300-500 SAREC assessment objects
- 20 entity profiles (full financial, sentiment, needs)
- 10-15 meta-patterns
- 20-30 specific opportunities
- Top 10 pilot candidate ranking
- Design blueprint from collective insights

All machine-readable, confidence-scored, evidence-backed.

**Estimated processing time: Next response (I'll do it all)**
