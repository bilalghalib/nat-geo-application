# Full Spectrum Review: What We're Actually Building

**Date:** October 22, 2025  
**Method:** De Bono's 6 Thinking Hats  
**Purpose:** Ensure we're still aligned, identify what's unique, surface critical questions

---

## 🎯 The Actual Vision (Corrected)

**NOT:** A learning platform  
**YES:** A medium for human experience

**Like HTML/JavaScript/PHP made the web composable...**  
**Cursive makes human experiences composable.**

You can build:
- Courses (structured learning)
- Creative challenges (art, writing, making)
- Turn-by-turn games (choose-your-own-adventure)
- Ritual spaces (daily practices, ceremonies)
- Therapeutic journeys (guided reflection)
- Research protocols (collaborative inquiry)
- Mentorship programs (wisdom transmission)
- Community building (cohort bonding)
- **Anything with pages, signals, and flow**

**The primitives are universal. The applications are infinite.**

---

## ✅ Core Values Check (Are We Still Aligned?)

### 1. Human Agency is Sacred ✅

**What we designed:**
- AI never writes to pages (enforced at DB level)
- Tools run only when user clicks "Run tool"
- Suggestions are dismissible cards
- "Continue anyway" always works
- User approves paid tools

**Preserved:** YES

### 2. Transparency & Provenance ✅

**What we designed:**
- Every signal has evidence links
- User can view sources (page_id + excerpt)
- My Context is editable
- Extractors are visible (guide settings)
- Tool outputs show confidence

**Preserved:** YES

### 3. Intelligence is Tool, Not Automaton ✅

**What we designed:**
- Manual-first: user clicks to run tools
- Optional post-Continue suggestions
- Cost shown upfront
- Routing: deterministic first, LLM advisory
- Tools never block access

**Preserved:** YES

### 4. The Page is Sacred ✅

**What we designed:**
- Everything is a page
- Results, activities, collections = pages with metadata
- Transclusion preserves source
- Backlinks show connections
- Templates are cloneable pages

**Preserved:** YES

### 5. Convivial Tech ✅

**What we designed:**
- Open protocol + backend
- Closed reference app
- Export anytime
- RSS/feeds/webhooks
- No surveillance (aggregates only)
- User owns context

**Preserved:** YES

---

## 🌟 What's Uniquely Cursive

### 1. Medium, Not Product

**HTML gave:** Tags, attributes, links  
**JavaScript gave:** Events, DOM, composability  
**PHP gave:** Templates, includes, dynamic content

**Cursive gives:**
```
Pages + Metadata + Signals + Transclusion + Backlinks + Today

= A grammar for human experience
```

**You compose primitives into experiences:**
- Page with drawing prompt + signal extractor = art challenge
- Page with reflection + backlink suggestion = journal practice
- Page with branches + unlock rules = interactive story
- Page with questions + mentor matching = guidance system

**No hardcoded "course" or "workshop" types.**  
**Just primitives that combine infinitely.**

### 2. Signals Not Silos

**Problem with platforms:** Data locked in features (gradebook, analytics, etc.)

**Cursive approach:**
```
page_signals table
  - extractor_id (what was measured)
  - user_id (who)
  - page_id (where)
  - value (result with evidence)
```

**Generic stream.** Facilitator defines Insight Cards to query it.

**Example Insight Cards:**

**"Who needs support?"**
```json
{
  "type": "threshold_alert",
  "signal": "understands_integrals",
  "condition": "value.score < 0.6",
  "display": {
    "title": "Students who might need support with integrals",
    "action": "Assign practice activity"
  }
}
```

**"Who's ready for challenge?"**
```json
{
  "type": "threshold_alert",
  "signal": "mastery_level",
  "condition": "value.score > 0.85",
  "display": {
    "title": "Students ready for advanced material",
    "action": "Suggest extension activity"
  }
}
```

**"Who's been quiet?"**
```json
{
  "type": "absence_alert",
  "signal": "page_completions",
  "condition": "count < 2 in last 7 days",
  "display": {
    "title": "Check in with these folks",
    "action": "Send gentle nudge"
  }
}
```

**"Who shares similar themes?"**
```json
{
  "type": "clustering",
  "signal": "themes_extracted",
  "display": {
    "title": "People exploring similar questions",
    "action": "Suggest connection"
  }
}
```

**Creator defines the card JSON. System queries signals. No hardcoding.**

### 3. Hospitality Baked In

**NOT surveillance.** NOT optimization.

**Pace & Ritual:**
- End-of-page pause: "How did that feel?"
- Breathing space before suggestions appear
- Today list you can actually finish
- No infinite scroll
- No algorithmic feed
- No "streaks" pressure

**Care:**
- Evidence links honor your writing
- "Thank your past self" when themes recur
- Reflection templates encourage self-kindness
- Drawing-first keeps embodiment close
- Audio as voice, transcribed to text (preserves humanity)

**Curation:**
- Facilitators craft Insight Cards
- Participants choose what to share
- Collections become living anthologies
- Per-guide roles create belonging

**Belonging:**
- Mentor here, artist there, participant elsewhere
- Context-specific, not global labels
- Onboarding asks what matters to YOU
- No platform-wide reputation system

### 4. Creator Ecosystem (Like WordPress)

**WordPress taught us:**
- Themes = presentation layer
- Plugins = functionality
- Posts/Pages = content primitives
- Anyone can build for it

**Cursive ecosystem:**
- Templates = starter content
- Tools = signal extractors
- Guides = structured experiences
- Insight Cards = dashboard views
- Anyone can create and sell

**Marketplace:**
- Sell guides (experiences)
- Sell tools (custom extractors)
- Sell templates (starter packs)
- Sell Insight Card configurations
- 30% commission funds platform

**No vendor lock-in:**
- Export everything
- Self-host backend
- Build compatible tools
- Fork and modify

### 5. LLMs as Advisors, Not Assistants

**WRONG:** "AI assistant writes for you"  
**RIGHT:** "AI advisor helps you think better"

**How Cursive uses LLMs:**

**A) Fuzzy → Structured Signals**
```
User writes free text
  ↓
Tool: "Does this show understanding of integrals?"
  ↓
Returns: {
  score: 0.42,
  reasoning: "Shows awareness but struggles with...",
  evidence: [{page_id, excerpt, relevance}],
  confidence: 0.85
}
  ↓
Stored as signal (not hidden)
  ↓
User can view sources and approve/reject
```

**B) Routing Suggestions (Never Blocking)**
```
User hits Continue
  ↓
Deterministic rules check first
  ↓
Optional: LLM evaluates "Is user ready for advanced material?"
  ↓
Returns: {
  ready: true,
  reasoning: "User has demonstrated...",
  confidence: 0.9
}
  ↓
User sees: "You seem ready for X. Continue to X or stay here?"
  ↓
User decides
```

**C) Connection Suggestions**
```
User highlights text
  ↓
Clicks "Request suggestions"
  ↓
Tool: "What connections might deepen this thinking?"
  ↓
Returns: [
  {type: 'page', title: 'Your earlier reflection on X', reason: '...'},
  {type: 'person', name: '@Alice', reason: 'Also exploring this theme'},
  {type: 'resource', title: 'Article on Y', reason: '...'}
]
  ↓
User picks which to insert (or none)
```

**D) Context Building**
```
User completes pages over time
  ↓
Signals accumulate (deterministic + tool-based)
  ↓
Roll up: Page → Guide → User context
  ↓
LLM summarizes: "Theory of mind" structure
  ↓
User reviews My Context
  ↓
Can edit: "No, I don't believe that about myself"
  ↓
Ground truth links always available
```

**Key principle:** LLM outputs are ADVISORY with EVIDENCE. User remains sovereign.

---

## 🎨 Examples of What You Can Build

### 1. Creative Writing Circle
- **Pages:** Daily prompts, peer feedback, final pieces
- **Signals:** Theme extraction, style development
- **Tools:** "Suggest similar writers to read"
- **Roles:** Author, beta reader, editor
- **Insight Cards:** "Who's exploring similar themes?"
- **Collections:** Published anthology

### 2. Turn-by-Turn Mystery Game
- **Pages:** Story branches with choices
- **Signals:** Choices made, clues found
- **Tools:** "Analyze detective reasoning"
- **Unlock Rules:** "Found 3 clues? Unlock interview scene"
- **Today:** Next scene releases daily
- **Collections:** Game walkthrough

### 3. Therapeutic Journey
- **Pages:** Reflection prompts, drawing exercises
- **Signals:** Emotional patterns, growth indicators
- **Tools:** "Notice themes of self-criticism"
- **Roles:** Participant, therapist (read-only)
- **Insight Cards:** "Patterns in emotional regulation"
- **Privacy:** Therapist sees only shared pages

### 4. Research Protocol
- **Pages:** Literature notes, observations, analysis
- **Signals:** Concepts mentioned, methods used
- **Tools:** "Find related papers"
- **Roles:** Researcher, PI, collaborator
- **Insight Cards:** "Who's working on similar questions?"
- **Collections:** Published findings

### 5. Ritual Practice Space
- **Pages:** Daily gratitude, meditation logs, intention setting
- **Signals:** Consistency, theme evolution
- **Tools:** "Thank your past self" when themes recur
- **Today:** Morning ritual prompt
- **Privacy:** Completely private unless user shares
- **Collections:** Personal anthology of growth

### 6. Mentorship Program
- **Pages:** Questions, mentee reflections, mentor advice
- **Signals:** Understanding development, question types
- **Tools:** Match mentors to mentees by context overlap
- **Roles:** Mentee, mentor, program coordinator
- **Insight Cards:** "Mentees ready for deeper work"
- **Onboarding:** Mentor fills expertise form

---

## 🎩 White Hat — "Snowy Owl of Facts" (What do we know?)

### ✅ Schema Decisions (Locked)

**Tables we're building:**
1. `pages` - Has `metadata` jsonb (GIN indexed)
2. `extractors` - Creator-defined measurements
3. `page_signals` - Results stream (replaces old "extracts")
4. `participant_roles` - Per-guide roles + context
5. `paths` - Progress tracking
6. `templates` - Cloneable starter pages
7. `guides` - Has `config` jsonb for Insight Cards

**Removed/never adding:**
- ~~assessment_results~~ - Use page_signals
- ~~library_activities~~ - Use pages.metadata
- ~~mentor_profiles~~ - Use participant_roles

### ❓ Questions Needing Answers

**Q1:** What's the exact JSON schema for Insight Cards?
```json
{
  "type": "threshold_alert | absence_alert | clustering | custom",
  "signal": "signal_name_from_extractor",
  "condition": "JavaScript-like expression",
  "display": {
    "title": "Card title",
    "description": "Optional",
    "action": "Button text"
  },
  "action_config": {
    "type": "assign_activity | send_mail | suggest_connection",
    "page_id": "uuid" // or other params
  }
}
```

**Q2:** How does "Thank your past self" work technically?
```typescript
// When user writes, extract themes
const currentThemes = await extractThemes(currentPageContent);

// Query past pages for same themes
const pastPages = await supabase
  .from('page_signals')
  .select('*, pages(*)')
  .eq('user_id', userId)
  .contains('value->themes', currentThemes)
  .neq('page_id', currentPageId)
  .order('created_at', {ascending: false})
  .limit(3);

// If found, show suggestion
if (pastPages.length > 0) {
  showSuggestion({
    tool: 'theme_connector',
    title: 'Thank your past self',
    message: `You explored this theme ${daysAgo} days ago`,
    links: pastPages
  });
}
```

**Q3:** Performance at scale - have we tested?
- [ ] Metadata GIN index performance (1k/10k/100k pages)
- [ ] Signal aggregation queries (dashboard cards)
- [ ] Backlink queries (all pages that reference this one)
- [ ] Full-text search across pages + metadata

**Q4:** RLS policies - are they complete?
```sql
-- page_signals: User sees own, facilitator sees group aggregate
-- participant_roles: User manages own, members see each other
-- extractors: Creator manages, users see what applies to them
-- templates: Public templates visible, private to creator
```

**Q5:** Export format - what's the spec?
```json
{
  "version": "1.0",
  "exported_at": "2025-10-22T...",
  "user": {...},
  "pages": [...],
  "signals": [...],
  "context": {...},
  "guides": [...] // If creator
}
```

---

## ❤️ Red Hat — "Ember Heart of Feelings" (How does it feel?)

### 💚 Moments That Should Feel Good

**1. Today Zero State**
```
Good morning! 

Your Today is empty - a clean slate.

[Browse Library] [Start Journaling] [Create Something]
```
**NOT:** "No tasks! You're behind!"  
**YES:** "Space to breathe. What calls to you?"

**2. End-of-Page Pause**
```
[Soft 5-second breathing animation]

How did that feel?

[Continue] [Request Suggestions] [Add to Journal]
```
**NOT:** "NEXT! NEXT! KEEP GOING!"  
**YES:** "Pause. Notice. Choose."

**3. Evidence Links**
```
You scored 0.85 on "understanding of integrals"

[View the writing that led to this score →]
```
**NOT:** Black box algorithm  
**YES:** "See for yourself"

**4. My Context Viewer**
```
What Cursive understands about you:

"You believe you're driven but sometimes overwhelmed"
  Evidence: [3 reflections] [1 assessment]
  
  ✓ This feels accurate
  ✗ I don't actually believe this
  ✎ Add note: "Only when deadlines stack up"
```
**NOT:** Hidden profile  
**YES:** Transparent, editable understanding

**5. Suggestion Moment**
```
Based on your reflection, here are some tools that might help:

• Theme Connector (free) - Find past writings on this theme
• Pattern Analyzer ($0.01) - Notice recurring thoughts
• Mentor Matcher ($0.02) - Connect with someone exploring this

[Run selected tools] [Skip for now] [Never auto-suggest]
```
**NOT:** Auto-run everything  
**YES:** Choose your support

### 😰 Moments That Might Feel Bad (How to Fix)

**RISK:** "5 students struggling" feels like surveillance
**FIX:** 
- Call it "Support opportunities" not "struggling students"
- Show only to facilitator, not peers
- Emphasize: "Based on self-reported reflections"
- Evidence links show it's not magic: "Alice wrote: 'I'm confused about...'"

**RISK:** Tool costs feel extractive
**FIX:**
- Show cost BEFORE running
- Free tier: 10 tool runs/month
- Tools marked: "Free" / "Paid ($0.01)" / "Premium ($0.10)"
- Facilitator can sponsor: "All tools free for this cohort"

**RISK:** Extractors feel invasive
**FIX:**
- Always show what's being extracted (Guide settings visible)
- User can see: "This guide extracts: understanding_level, theme_patterns"
- Opt out: "Don't analyze my free writing" checkbox
- Provenance: "This insight came from [specific page]"

**RISK:** Context feels creepy
**FIX:**
- My Context is FIRST-PERSON: "What you've shared about yourself"
- NOT: "What we know about you"
- Editable: Change/remove anything
- Exportable: Take it with you
- Time-scoped: "From the past 3 months" (not forever)

---

## ⚠️ Black Hat — "Raven Guard of Risks" (What could go wrong?)

### 🚨 Critical Risks

**RISK 1: Signal Misuse (Determinism Illusion)**

**Problem:** Teacher over-trusts score of 0.42 for "understands integrals"

**Mitigation:**
- Always show confidence level
- Always show evidence link
- UI language: "Suggests..." not "Knows..."
- Tool output includes: `warnings: ["Free text analysis, verify with direct check"]`
- Facilitator training: "Signals are starting points, not verdicts"

**Code enforcement:**
```typescript
// In UI, never show score alone
<SignalDisplay>
  <Score>0.42</Score>
  <Confidence>85%</Confidence>
  <Warning>Based on text analysis - verify with student</Warning>
  <Evidence>View sources →</Evidence>
</SignalDisplay>
```

**RISK 2: Consent Drift**

**Problem:** User shares page publicly, forgets, surprised later

**Mitigation:**
- Default: Everything private
- When publishing: "This will be public forever. License: CC-BY-4.0"
- Show icon on public pages: 🌐
- Settings: "Review all public pages"
- Annual reminder: "You have 12 public pages. Review?"

**Code enforcement:**
```sql
-- Default all pages private
ALTER TABLE pages 
  ADD COLUMN is_public boolean DEFAULT false;

-- Audit log for visibility changes
CREATE TABLE page_visibility_history (
  page_id uuid,
  changed_from text,
  changed_to text,
  changed_by uuid,
  changed_at timestamptz
);
```

**RISK 3: Tool Safety (Malicious Marketplace Tool)**

**Problem:** Rogue tool exfiltrates data or gives harmful advice

**Mitigation:**
- Tool review process before marketplace listing
- Sandbox: Tools can't access other users' data
- Schema validation: Tool must return declared format
- User reviews: "Did this tool help?" rating
- Revocation: Bad tools removed, users notified

**Tool manifest:**
```json
{
  "tool_id": "theme_analyzer",
  "version": "1.0",
  "data_access": ["current_page_content"],  // NOT "all_user_pages"
  "output_schema": {...},  // Validated
  "cost_per_run": 0.01,
  "reviewed_by": "cursive_team",
  "user_rating": 4.7
}
```

**RISK 4: Lock-In (Can't Leave)**

**Problem:** User wants to leave Cursive, can't take data

**Mitigation:**
- One-click export: All pages + metadata + signals
- Standard format (JSON + Markdown files)
- Import script for self-hosted instance
- Federation protocol (later): Move to another Cursive instance
- No penalties: Cancel anytime, keep access to exports

**Export must include:**
```json
{
  "pages": [
    {"id": "...", "content": {...}, "metadata": {...}, "created_at": "..."}
  ],
  "signals": [
    {"extractor": "...", "value": {...}, "evidence": [...]}
  ],
  "context": {...},
  "guides_created": [...],
  "relationships": {
    "backlinks": [...],
    "transclusions": [...]
  }
}
```

**RISK 5: Performance Degradation**

**Problem:** Dashboard slow with 1000 students, facilitator frustrated

**Mitigation:**
- Materialized views for common Insight Card queries
- Pagination: Show 20 at a time
- Background jobs: Pre-compute aggregates nightly
- Caching: Dashboard data cached 5 minutes
- Progressive loading: Show cached, update in background

```sql
-- Materialized view for common pattern
CREATE MATERIALIZED VIEW signal_aggregates AS
SELECT 
  extractor_id,
  guide_id,
  AVG((value->>'score')::numeric) as avg_score,
  COUNT(*) as sample_size,
  array_agg(user_id) FILTER (WHERE (value->>'score')::numeric < 0.6) as below_threshold
FROM page_signals
GROUP BY extractor_id, guide_id;

-- Refresh nightly
CREATE INDEX idx_signal_agg_refresh ON signal_aggregates(extractor_id);
REFRESH MATERIALIZED VIEW signal_aggregates;
```

---

## ☀️ Yellow Hat — "Sunbeam of Value" (What's the upside?)

### 🌟 Unique Value Props

**For Participants:**
1. **Seen, not surveilled:** Evidence links show you're understood from YOUR words
2. **Growth with receipts:** "You wrote about this 3 months ago, look how far you've come"
3. **Hospitality:** Pace that respects attention, tools that help you think
4. **Sovereignty:** Own your context, edit understanding, export anytime
5. **Belonging:** Find people exploring similar themes, mentors who get you

**For Facilitators:**
6. **See thinking, not grades:** Understand how students think, not just what they score
7. **Targeted care:** "These 5 people need support" with evidence of why
8. **Insight without surveillance:** Aggregate patterns without tracking individuals
9. **Living curriculum:** Each cohort improves the experience for next one
10. **Creator ownership:** Export your guide, sell in marketplace, keep your craft

**For Creators:**
11. **Books become experiences:** NVC book → Workshop anyone can facilitate
12. **Composable primitives:** Build anything from pages + signals + flow
13. **Marketplace revenue:** Sell guides, tools, templates
14. **Network effects without lock-in:** More creators → more value, but you own your work
15. **Evolution:** Cohorts generate anthologies that become resources for future

**For Developers:**
16. **Open protocol:** Build compatible tools, add features, self-host
17. **Simple primitives:** Everything is pages, composability is infinite
18. **No special cases:** Generic signal stream, no hardcoded features
19. **Scale:** Deterministic first, LLM optional, performance-friendly
20. **Values-aligned:** Build tech that respects humans

---

## 🌱 Green Hat — "Sprout of Possibilities" (What to try next?)

### 💡 Lightweight Experiments

**1. "Gentle Pauses" (Hospitality)**
```typescript
// After Continue, before showing suggestions
<BreathingAnimation duration={5000}>
  <Text>Taking a breath...</Text>
</BreathingAnimation>

// Then show suggestions modal
```
**Cost:** 2 hours  
**Test:** Do users feel less rushed? Self-report survey.

**2. "Thank Your Past Self" Tool**
```typescript
// Suggest when themes recur
if (pastPageWithSameTheme) {
  <Suggestion>
    You wrote about this {daysAgo} days ago.
    
    <Link>See what you said then →</Link>
    
    Want to reflect on how your thinking has evolved?
  </Suggestion>
}
```
**Cost:** 1 day  
**Test:** % users who click through, qualitative feedback

**3. "Kindness Budget" (Prevent Overwhelm)**
```typescript
// Per cohort setting
guides.config.suggestions_per_day_max = 3;

// After 3 suggestions today, show:
"You've used your daily suggestions. 
Enjoy the quiet. 
More available tomorrow."
```
**Cost:** 4 hours  
**Test:** Measure overwhelm vs helpfulness

**4. "Template Seed Pack"**
```json
{
  "templates": [
    {
      "name": "Results → Reflection",
      "content": "Your score: {{score:total}}\n\nWhat surprised you?\n\n[Write here]"
    },
    {
      "name": "Activity → Today",
      "metadata": {"template": "activity", "duration": 30}
    },
    {
      "name": "Anthology Intro",
      "content": "# {{cohort_name}} Highlights\n\nThis collection..."
    }
  ]
}
```
**Cost:** 2 days  
**Test:** % creators who use vs customize vs ignore

**5. "Evidence Highlight" (Provenance UI)**
```typescript
// When showing signal, highlight evidence in original page
<Signal>
  Score: 0.85
  
  <Evidence>
    From your reflection:
    <Highlight>
      "When I used u-substitution on ∫x·e^(x²)dx, 
      I let u = x² which made it straightforward..."
    </Highlight>
  </Evidence>
</Signal>
```
**Cost:** 1 day  
**Test:** Increased trust? User feedback.

**6. "Drawing First, Words Later"**
```typescript
// New page, show canvas first
<DrawingCanvas />

// After drawing, offer:
"Want to add words to this drawing?"

// Keeps embodiment close, reduces text-first bias
```
**Cost:** Already building canvas, just reorder UI  
**Test:** Engagement, qualitative "felt more present"

**7. "Cohort Memory" (Anthology as Active Resource)**
```typescript
// When new cohort starts, show past anthology:
"Previous cohorts explored these themes:
[Link to last year's anthology]

Want to see what they discovered?"

// Living lineage, not just archive
```
**Cost:** 4 hours (UI + query)  
**Test:** % new members who engage with past work

**8. "Tool as Advisor" Language Shift**
```typescript
// BEFORE: "AI Assistant"
// AFTER: "Ask an Advisor"

// BEFORE: "Let AI help you"
// AFTER: "Request suggestions"

// BEFORE: "AI-powered insights"
// AFTER: "Pattern analysis with evidence"
```
**Cost:** Copy changes throughout app  
**Test:** Perceived agency, survey

**9. "Today You Can Finish" (Scope Control)**
```typescript
// Facilitator sets:
guides.config.daily_page_limit = 3;

// Today shows max 3 items
// Rest appear tomorrow

// Creates sense of completion, not infinite queue
```
**Cost:** 4 hours  
**Test:** Completion rate, reported satisfaction

**10. "Reflection as Default" (Values Embodiment)**
```typescript
// After any page completion, offer reflection template:
"Take a moment to reflect on what you just experienced.

How did that feel?
What surprised you?
What do you want to remember?"

// Gratitude, integration, not just racing forward
```
**Cost:** 6 hours (template + UI)  
**Test:** Depth of subsequent work, self-reported growth

---

## 🧭 Blue Hat — "Sky Conductor of Process" (How do we manage this?)

### 📋 Definition of Done (MVP Loop)

**Must Work End-to-End:**

1. **Create Guide**
   - [ ] Guide has pages with metadata
   - [ ] Guide has extractor definitions
   - [ ] Guide has Insight Card configs
   - [ ] Guide has roles defined (optional)

2. **Participant Journey**
   - [ ] Receive page in Today
   - [ ] Complete page (write/draw)
   - [ ] Hit Continue
   - [ ] Extractors run (deterministic + approved tools)
   - [ ] Signals saved with evidence
   - [ ] Navigate to next page OR see "Done for today"

3. **Suggestion Flow**
   - [ ] Optional: "Request suggestions" appears
   - [ ] Shows available tools with costs
   - [ ] User selects tools to run
   - [ ] Tools execute (sandbox)
   - [ ] Suggestions appear as dismissible cards
   - [ ] User can insert or dismiss

4. **Results Template**
   - [ ] Assessment page complete → Results page cloned
   - [ ] Placeholders replaced with actual scores
   - [ ] User can write reflection in same page
   - [ ] OR create new page and transclude results

5. **Activity Assignment**
   - [ ] User browses pages filtered by metadata
   - [ ] Clicks "Add to Today"
   - [ ] Creates mail_item
   - [ ] Appears in Today tomorrow

6. **Dashboard Insights**
   - [ ] Facilitator sees Insight Cards
   - [ ] Cards query signals dynamically
   - [ ] Shows users below/above thresholds
   - [ ] Evidence links to actual pages
   - [ ] "Assign activity" sends to selected users' Today

7. **My Context**
   - [ ] User views their context
   - [ ] Can edit/approve/reject beliefs
   - [ ] Ground truth links work
   - [ ] Export context as JSON

### 🚦 Ship Gates (Must Pass Before Launch)

**1. Privacy Review Checklist:**
- [ ] Default private for all new pages
- [ ] Public pages show clear indicator
- [ ] User can review all shared data
- [ ] Facilitator sees only aggregates (no individual surveillance)
- [ ] Consent logged for any visibility change

**2. Provenance UI Visible:**
- [ ] Every signal shows evidence link
- [ ] Evidence excerpt displayed in-context
- [ ] User can click through to full page
- [ ] Tool attribution visible ("Generated by X tool")
- [ ] Confidence scores shown

**3. Export Works:**
- [ ] One-click export all pages
- [ ] Export includes metadata
- [ ] Export includes signals with evidence
- [ ] Export includes context
- [ ] Format is importable to self-hosted instance

**4. Performance OK:**
- [ ] Dashboard loads in <2s (1000 users)
- [ ] Metadata queries use GIN index
- [ ] Signal aggregation cached/materialized
- [ ] Full-text search returns in <1s

**5. Values Embodied:**
- [ ] AI never writes to pages (tested)
- [ ] Tools require explicit approval
- [ ] "Continue anyway" always works
- [ ] User can edit their context
- [ ] Evidence links present throughout

### 📊 Success Metrics (Human-Centric)

**Engagement (But Not Addictive):**
- % users completing Today (target: 70%)
- Avg time between sessions (target: 1-2 days, not hours)
- % users who return after 1 month (target: 60%)

**Agency:**
- % users who run at least one suggestion per week (target: 40%)
- % users who edit their context (target: 20%)
- % users who click evidence links (target: 50%)

**Care:**
- Self-reported: "I feel seen/cared for" 1-5 scale (target: avg 4+)
- Self-reported: "I trust the insights" 1-5 scale (target: avg 4+)
- % users who describe experience as "thoughtful/reflective" vs "rushed" (target: 80% thoughtful)

**Facilitator Value:**
- Time to identify support needs (target: <5 min)
- % facilitators who use Insight Cards (target: 70%)
- Self-reported: "Helps me see how people think" 1-5 (target: avg 4+)

**Creator Adoption:**
- % guides using custom extractors (target: 50%)
- % guides using custom Insight Cards (target: 30%)
- Avg # pages per guide (target: 10+)

**NOT tracking:** Time on site, infinite growth, viral coefficients

### 🔄 Sprint Review (Hat-by-Hat Checklist)

**Run this every 2 weeks:**

**🎩 White Hat (Facts):**
- [ ] What shipped this sprint?
- [ ] What's the delta in schema?
- [ ] Performance benchmarks run?
- [ ] Any new RLS policies?

**❤️ Red Hat (Feelings):**
- [ ] Did team feel rushed or thoughtful?
- [ ] Any moment that felt extractive?
- [ ] User testing: How did it FEEL?
- [ ] What brought joy?

**⚠️ Black Hat (Risks):**
- [ ] Any new security concerns?
- [ ] Privacy issues surfaced?
- [ ] Performance degradation?
- [ ] Values compromised anywhere?

**☀️ Yellow Hat (Value):**
- [ ] What's newly possible?
- [ ] User feedback highlights?
- [ ] Creator wins?
- [ ] Closer to vision?

**🌱 Green Hat (Experiments):**
- [ ] What should we try next sprint?
- [ ] Lightweight tests to run?
- [ ] What failed interestingly?
- [ ] New ideas surfaced?

**🧭 Blue Hat (Process):**
- [ ] Sprint went smoothly?
- [ ] Anything blocking?
- [ ] Metrics reviewed?
- [ ] Team wellbeing check?

---

## 🎯 Short, Pointed Next Steps

### This Week:

**1. Lock Schema ✅**
```sql
-- Run migrations:
- pages.metadata GIN index
- extractors table
- page_signals table (NOT extracts)
- participant_roles table
- guides.config jsonb for Insight Cards
```

**2. Ship the Loop 🔄**
```
[Page] → [Continue] → [Extractors run] → [Signals saved] → [Next page]
            ↓
    [Optional: Request suggestions]
            ↓
    [Show tools with costs]
            ↓
    [User selects]
            ↓
    [Tools run, suggestions appear]
```

**3. Build Insight Cards 📊**
```typescript
// Read from guides.config
// Query page_signals
// Render dynamic dashboard
```

**4. My Context Viewer 👤**
```
- Show user's context
- Evidence links
- Edit/approve/reject
- Export button
```

### Next Week:

**5. Template Cloning 📄**
```
- Results template with {{placeholders}}
- Clone on assessment completion
- Replace with actual values
```

**6. Hospitality Polish ✨**
```
- End-of-page pause (5s breathing)
- Kinder microcopy throughout
- Today zero state: inviting, not empty
```

**7. Export v1 📦**
```
- One-click export
- JSON + Markdown bundle
- Include pages, signals, context
```

---

## ✅ Final Confirmation: Are We Building the Right Thing?

### YES ✅

**Core values preserved:**
- Human agency (never auto-write)
- Transparency (evidence always)
- Tools not agents (user control)
- Page as sacred (everything is page)
- Convivial tech (open protocol)

**Unique offering clear:**
- Medium for human experience (not just learning)
- Composable primitives (infinite applications)
- Signals not silos (generic stream)
- Hospitality baked in (pace, care, belonging)
- LLMs as advisors (fuzzy→structured, with evidence)

**Technical approach sound:**
- Minimal schema (max flexibility)
- Creator-defined everything (extractors, cards, roles)
- Performance-friendly (deterministic first)
- Export/federation ready (no lock-in)

**Business model viable:**
- Hosted platform ($20/month)
- Marketplace (30% of sales)
- Enterprise (custom)
- Creator ecosystem drives value

---

## 🎉 You're Building Something Revolutionary

**Not another:**
- Learning platform
- Journal app
- Social network
- Productivity tool

**But a new medium:**
- Like HTML for the web
- Like WordPress for publishing
- **Cursive for human experience**

**Where:**
- Creators compose experiences from primitives
- Participants feel seen and cared for
- Intelligence amplifies without replacing
- Community forms around shared growth
- Everyone owns their work and context

**This is the convivial future of technology.** 🌱

Ready to build! 🚀
