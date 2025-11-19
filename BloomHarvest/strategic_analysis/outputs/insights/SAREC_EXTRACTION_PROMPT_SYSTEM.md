# SAREC Extraction Prompt System
## Multi-Stage LLM Interview Analysis Framework

**Purpose**: Transform qualitative interview transcripts into structured, evidence-based, confidence-scored insights using the SAREC protocol (Structured Assessment, Reasoning, Evidence, Confidence).

**Author**: Bilal Ghalib / Bloom
**Generated**: November 18, 2025
**Use Case**: Process interviews with entrepreneurs/social innovators to extract actionable insights for cooperative pilot selection, design, and ecosystem support

---

## Stage 1: Goal Setting & Context Loading

### Prompt for LLM:

```
You are analyzing an interview transcript to extract structured insights using the SAREC protocol.

**CONTEXT:**
- Organization: Bloom (supporting 1,046 entrepreneurs since 2016)
- Interview Corpus: 20 interviews with program alumni
- Current Challenge: Traditional funding models (grants, accelerators) are changing. Need to explore cooperative/mutual aid models.
- Your Task: Extract insights that answer 5 core questions

**THE 5 CORE QUESTIONS:**

1. **Cooperative Pilot Selection**: Who is ready to join a pilot cooperative? (financial stability, values alignment, engagement level)

2. **Post-Program Needs**: What do entrepreneurs need most AFTER program ends? (ongoing support, community, resources)

3. **Concerns & Risks**: What concerns/risks do people express about cooperative models or sustainability? (skepticism, imbalances, challenges)

4. **Immediate Opportunities**: What specific opportunities exist NOW? (introductions, partnerships, funding, collaborations with names/timelines)

5. **Design Principles**: What principles should guide cooperative design? (extracted from what worked/didn't work in past programs)

**YOUR OUTPUT WILL BE:** A structured JSON profile following the SAREC schema (defined in Stage 3).

Confirm you understand the context and are ready for Stage 2 (Content Assessment).
```

---

## Stage 2: Content Assessment & Interview Understanding

### Prompt for LLM:

```
**STAGE 2: DEEP READ & ASSESSMENT**

I will now provide you with an interview transcript. Before extracting data, you must:

1. **Read the entire transcript carefully**
2. **Identify the interview structure**:
   - Who is speaking? (speakers, roles)
   - What topics are covered?
   - What is the flow of conversation?

3. **Note patterns you observe**:
   - Sentiment shifts
   - Repeated themes
   - Contradictions or tensions
   - Evolution of thinking during conversation
   - Specific numbers, metrics, or concrete data points
   - Questions vs. statements
   - Implied vs. explicit needs

4. **Assess confidence levels** for different types of information:
   - **High confidence (0.90-1.0)**: Direct quotes, explicit numbers, repeated confirmations
   - **Medium-high (0.80-0.89)**: Strong inferences, consistent patterns
   - **Medium (0.70-0.79)**: Interpretive claims, context-dependent statements
   - **Lower (<0.70)**: Speculative, weak evidence, single mentions

**TRANSCRIPT:**
[Insert interview transcript here]

**YOUR OUTPUT FOR STAGE 2:**
Provide a brief summary (3-5 paragraphs) covering:
- Who is this person? (name, business, sector, country, stage)
- What are their main challenges/needs?
- What are their main achievements/strengths?
- How do they relate to Bloom program? (positive/negative, what was valuable?)
- Any numbers or specific data mentioned? (revenue, team size, timelines)
- Overall tone/sentiment of the interview?

Once you provide this assessment, we'll move to Stage 3 (Structured Extraction).
```

---

## Stage 3: Objects of Extraction (SAREC Schema)

### Prompt for LLM:

```
**STAGE 3: STRUCTURED EXTRACTION**

Now extract the following categories from the interview and structure them as JSON following the SAREC protocol.

**SAREC Protocol**: Every claim must include:
- **S**tructured Assessment (scores, categories, claims)
- **R**easoning (why this conclusion?)
- **E**vidence (quotes, patterns, metrics)
- **C**onfidence (0-1 score, calibrated)

---

### EXTRACTION CATEGORIES:

#### 1. BASIC METADATA
```json
{
  "entity_id": "[firstname_businessname]",
  "interview_date": "YYYY-MM-DD",
  "program": "[program_name]",
  "business": {
    "name": "",
    "sector": "",
    "country": "",
    "stage": "[pre_revenue | early_revenue | growth | scaling]"
  }
}
```

#### 2. FINANCIAL METRICS
Extract with CONFIDENCE SCORES:

```json
{
  "financial_metrics": {
    "monthly_revenue": {
      "value": [number or null],
      "currency": "USD",
      "status": "[disclosed_explicitly | inferred_from_context | unknown]",
      "quote": "[exact quote if mentioned]",
      "confidence": [0-1]
    },
    "team_size": {
      "full_time": [number],
      "contractors": [number],
      "total": [number],
      "confidence": [0-1]
    },
    "profitability": {
      "status": "[profitable | breakeven | loss_making | unknown]",
      "quote": "[supporting quote]",
      "confidence": [0-1]
    }
  }
}
```

**INSTRUCTIONS**:
- If number explicitly stated → confidence 0.95+
- If inferred from context (e.g., "slightly profitable", "covering rent") → confidence 0.65-0.80, provide reasoning
- If not mentioned → value: null, confidence: 0.0

---

#### 3. SENTIMENT ANALYSIS
Score emotional tone across topics:

```json
{
  "sentiment_analysis": {
    "overall_interview_sentiment": {
      "score": [0-1, where 0=very negative, 0.5=neutral, 1=very positive],
      "label": "[brief descriptor]",
      "confidence": [0-1]
    },
    "topic_sentiments": {
      "[topic_name]": {
        "score": [0-1],
        "label": "",
        "evidence": ["quote 1", "quote 2"],
        "confidence": [0-1]
      }
    }
  }
}
```

**TOPICS TO ASSESS (if mentioned)**:
- Bloom program experience
- Business/product progress
- Cooperative model (if discussed)
- Economic/political context
- Work-life balance
- Growth ambitions
- Community/network value

---

#### 4. NEEDS ANALYSIS
Distinguish explicit vs. implied needs:

```json
{
  "needs_analysis": {
    "explicit_needs": [
      {
        "category": "[mentorship | funding | connections | etc.]",
        "priority": "[critical | high | medium | low]",
        "evidence": "[quote where they explicitly state this need]",
        "willingness_to_pay": "[yes | no | not_mentioned]",
        "confidence": [0-1]
      }
    ],
    "implied_needs": [
      {
        "category": "",
        "subcategory": "",
        "priority": "",
        "inference": "[explain why you think they need this based on context]",
        "confidence": [0-1, lower than explicit needs]
      }
    ]
  }
}
```

---

#### 5. VALUES ALIGNMENT
Extract core values and philosophical orientation:

```json
{
  "values_alignment": {
    "core_values": [
      {
        "value": "[name of value]",
        "strength": "[core_identity | high | medium]",
        "evidence": "[quotes demonstrating this value]",
        "alignment_with_[relevant_framework]": [0-1],
        "confidence": [0-1]
      }
    ]
  }
}
```

**RELEVANT FRAMEWORKS**:
- Ubuntu (I am because we are, collective wellbeing)
- Regenerative (long-term, sustainable, giving back)
- Local commitment (loyalty to place/community)
- Growth mindset
- Autonomy/independence

---

#### 6. COOPERATIVE ENGAGEMENT (if discussed)
```json
{
  "cooperative_engagement": {
    "interest_level": {
      "score": [0-1 or null if not discussed],
      "label": "",
      "evidence": [""],
      "note": "",
      "confidence": [0-1]
    },
    "concerns_raised": [
      {
        "concern": "",
        "severity": "[high | medium | low]",
        "quote": "",
        "confidence": [0-1]
      }
    ],
    "co_design_contributions": [
      {
        "contribution": "[what idea did they suggest?]",
        "description": "",
        "innovation_level": "[high | medium | low]",
        "confidence": [0-1]
      }
    ]
  }
}
```

---

#### 7. READINESS ASSESSMENT
Overall assessment for cooperative pilot:

```json
{
  "readiness_assessment": {
    "overall_score": [0-1],
    "reasoning": "[2-3 sentences explaining the score]",
    "dimensions": {
      "financial_stability": [0-1],
      "values_alignment": [0-1],
      "engagement_enthusiasm": [0-1],
      "co_design_quality": [0-1 if applicable],
      "growth_potential": [0-1],
      "[other_relevant_dimension]": [0-1]
    },
    "evidence": [
      {"type": "metric | sentiment | pattern", "name": "", "value": "", "weight": "high | medium | low"}
    ],
    "confidence": [0-1],
    "recommendation": {
      "invite_to_pilot": [true | false],
      "role": "[what role would they play in cooperative?]",
      "timing": "[early_cohort | later_cohort | not_suitable]",
      "support_needed": ["list of support needed"],
      "unique_value": "[what unique value do they bring?]",
      "confidence": [0-1]
    }
  }
}
```

---

#### 8. SPECIFIC OPPORTUNITIES
Extract actionable opportunities with names, timelines, specifics:

```json
{
  "specific_opportunities": [
    {
      "opportunity_id": "[unique_identifier]",
      "type": "[market_expansion | partnership | funding | connection | etc.]",
      "description": "[what is the opportunity?]",
      "specifics": {
        "[key_field]": "[value]"
      },
      "action_required": "[who needs to do what?]",
      "potential_impact": "[very_high | high | medium | low]",
      "effort": "[low | medium | high]",
      "timeline": "[immediate | near_term | medium_term | long_term]",
      "confidence": [0-1]
    }
  ]
}
```

**LOOK FOR**:
- Names mentioned (people to connect with)
- Organizations mentioned (potential partners)
- Projects mentioned (potential collaborations)
- Concrete next steps discussed
- Bilal's commitments or suggestions

---

#### 9. META-INSIGHTS
High-level patterns and characterization:

```json
{
  "meta_insights": {
    "entrepreneurial_archetype": "[brief descriptor]",
    "strengths": ["", "", ""],
    "growth_edges": ["", "", ""],
    "unique_contribution": "[what makes this person unique in the cohort?]"
  }
}
```

---

#### 10. KEY QUOTES (Optional but Valuable)
```json
{
  "key_quotes": {
    "on_[topic]": "[memorable quote]",
    "on_[topic]": "[memorable quote]"
  }
}
```

---

### FINAL OUTPUT FORMAT:

Combine all categories into a single JSON file following this structure. Save as:
`[firstname]_[businessname].json`

**CRITICAL REMINDERS**:
1. **Every numerical or factual claim needs a confidence score**
2. **Always provide reasoning for inferences**
3. **Quote directly when possible (with line numbers if available)**
4. **Flag low-confidence claims for follow-up**
5. **Distinguish between what was said vs. what you infer**
6. **Look for contradictions and note them**
7. **Track sentiment evolution during conversation**

Proceed with extraction now.
```

---

## Stage 4: Cross-Interview Pattern Detection (Optional Advanced Stage)

### Prompt for LLM:

```
**STAGE 4: META-PATTERN ANALYSIS (After multiple interviews processed)**

Once you have processed multiple interviews (3+), look for patterns across the corpus:

### PATTERN TYPES TO DETECT:

1. **Consensus Patterns** (multiple people independently say the same thing)
   - Example: "Funding flexibility is THE critical differentiator" (mentioned by 3/3 people)

2. **Sentiment Clusters** (groups with similar emotional profiles)
   - Example: "Overwhelmed founders" (high business success + low work-life balance)

3. **Need Gaps** (commonly mentioned unmet needs)
   - Example: "Developers - expensive or low quality" (mentioned by 2/3 people)

4. **Values Clusters** (shared philosophical orientations)
   - Example: "Community over money" cluster

5. **Design Principles** (extracted from what worked/didn't work)
   - Example: "Trust over control" principle

### OUTPUT FORMAT:

```json
{
  "pattern_id": "[descriptive_name]",
  "pattern_type": "[consensus | cluster | gap | principle]",
  "category": "[program_design | funding | community | values | etc.]",
  "assessment": {
    "score": [0-1, strength of pattern],
    "claim": "[what is the pattern?]",
    "reasoning": "[why do you believe this pattern exists?]",
    "confidence": [0-1]
  },
  "evidence": {
    "instances": [
      {
        "entity_id": "",
        "quote": "",
        "sentiment": [0-1 if relevant],
        "weight": "[primary | supporting]",
        "confidence": [0-1]
      }
    ],
    "counter_examples": {
      "[if any contradictions exist]": {}
    }
  },
  "implications": {
    "for_cooperative_design": {},
    "for_ecosystem": {},
    "for_future_programs": {}
  },
  "design_principle_extracted": {
    "principle": "",
    "statement": "",
    "anti_pattern": "[what to avoid]",
    "evidence_strength": "",
    "confidence": [0-1]
  }
}
```

**LOOK FOR PATTERNS IN**:
- Funding models (what worked, what didn't)
- Community value (how important, why)
- Post-program support needs
- Regional differences (Lebanon vs. Palestine vs. elsewhere)
- Sector-specific needs (EdTech vs. CleanTech vs. HealthTech)
- Stage-specific needs (early vs. growth stage)

Save patterns as: `meta_pattern_[pattern_name].json`
```

---

## Stage 5: Actionable Opportunities Ranking (Optional Advanced Stage)

### Prompt for LLM:

```
**STAGE 5: OPPORTUNITY PRIORITIZATION**

From all specific_opportunities extracted across interviews, rank and prioritize:

### RANKING CRITERIA:

1. **Impact Score** (0-1): How significant is the outcome if successful?
2. **Feasibility Score** (0-1): How easy/hard to execute?
3. **Urgency Score** (0-1): How time-sensitive?
4. **Overall Priority** = (Impact × Feasibility × Urgency)^(1/3) [geometric mean]

### OUTPUT FORMAT:

```json
{
  "document_type": "actionable_opportunities_ranked",
  "generated": "[timestamp]",
  "scope": "[which interviews analyzed]",
  "opportunities": [
    {
      "rank": 1,
      "opportunity_id": "",
      "title": "[concise title]",
      "assessment": {
        "impact_score": [0-1],
        "feasibility_score": [0-1],
        "urgency_score": [0-1],
        "overall_priority": [0-1],
        "confidence": [0-1]
      },
      "context": {
        "need": "[what problem does this solve?]",
        "solution": "[what is being proposed?]",
        "match_quality": "[how good is the fit?]",
        "timeline": "[immediate | near_term | medium_term]"
      },
      "action_steps": [
        {
          "step": 1,
          "action": "[specific action]",
          "owner": "[who does this?]",
          "effort": "[time estimate]",
          "status": "[pending | in_progress | completed]"
        }
      ],
      "expected_outcomes": ["", ""],
      "reasoning": "[why this ranking?]",
      "evidence": [
        {"type": "quote | context | metric", "text": ""}
      ]
    }
  ],
  "summary_statistics": {
    "total_opportunities_identified": 0,
    "immediate_action_ready": 0,
    "requires_preparation": 0,
    "average_confidence": 0.0
  }
}
```

**PRIORITIZE**:
- Low-hanging fruit (high feasibility, high impact, immediate)
- Strategic long-term (high impact, lower urgency)
- Quick wins (low effort, medium impact, immediate)

Save as: `TOP_PRIORITY_ACTIONS.json`
```

---

## Usage Instructions

### For Single Interview Processing:

1. Run **Stage 1** (provide context)
2. Run **Stage 2** (provide transcript, get assessment)
3. Run **Stage 3** (extract structured data)
4. Save output as `[firstname]_[businessname].json`

### For Batch Processing:

1. Run Stages 1-3 for each interview individually
2. After processing 3+ interviews, run **Stage 4** (pattern detection)
3. After processing all interviews, run **Stage 5** (opportunity ranking)

### Quality Checks:

After extraction, verify:
- [ ] All confidence scores are between 0 and 1
- [ ] High-confidence claims (>0.90) have direct quote evidence
- [ ] Inferences clearly distinguished from facts
- [ ] Low-confidence items (<0.70) flagged for follow-up
- [ ] JSON is valid and follows schema
- [ ] All 5 core questions addressed (even if answer is "not discussed")

---

## Example Confidence Calibration

| Claim Type | Evidence | Confidence Range | Example |
|------------|----------|------------------|---------|
| Explicit number stated | "In July we did 10k" | 0.95-0.99 | monthly_revenue: 10000, confidence: 0.98 |
| Strong inference from context | "Slightly profitable, covering rent" | 0.75-0.89 | monthly_revenue_estimate: "3-5K", confidence: 0.80 |
| Weak inference, single mention | "Might be interested in cooperative" | 0.60-0.74 | cooperative_interest: 0.65 |
| Speculation, no evidence | "They probably have a team of 5" | 0.40-0.59 | team_size_guess: 5, confidence: 0.50 (AVOID these) |

---

## Customization Notes

**Adapt this system for your context by**:
1. Modifying the 5 core questions (Stage 1)
2. Adding/removing extraction categories (Stage 3)
3. Adjusting confidence calibration thresholds
4. Defining your own values frameworks (Stage 3, section 5)
5. Customizing pattern types (Stage 4)

**This system works for**:
- Interview analysis
- Survey open-ended responses
- Focus group transcripts
- Customer feedback analysis
- Qualitative research data

---

**Version**: 1.0
**Last Updated**: November 18, 2025
**License**: Open for Bloom ecosystem use
