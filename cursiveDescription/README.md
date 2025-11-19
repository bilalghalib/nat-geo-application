# Cursive: Complete Documentation Package

## Overview

This package contains everything needed to understand, build, and deploy Cursive - a convivial infrastructure for embodied learning through correspondence.

**What is Cursive?** Think of it as "email for learning" - an open protocol for human correspondence that enables learning by doing together.

---

## Core Documents (Start Here)

### 1. [VISION.md](./VISION.md) - Philosophy & Values
**Read first.** Explains what we're building and why.

**Key sections:**
- Core thesis (learning through dialogue + making)
- Problem we're solving (platform lock-in, disembodied learning)
- Six core values (agency, embodiment, privacy, openness, slowness, craft)
- How it works (for participants, facilitators, creators)
- Business model (sustainable without surveillance)

**Time to read:** 30 minutes
**Action:** Understand the vision before anything else

### 2. [ARCHITECTURE.md](./ARCHITECTURE.md) - Technical Design
**Read second.** Shows how values translate to code.

**Key sections:**
- Response to critique (5 pros, 5 cons addressed)
- Core primitives (Letter, Guide, Identity, Instance)
- Database schema (PostgreSQL)
- API architecture (REST + optional WebSocket)
- Federation protocol (Phases 1-3)
- Security & privacy model

**Time to read:** 45 minutes
**Action:** Understand technical foundation

### 3. [ROADMAP.md](./ROADMAP.md) - Implementation Plan
**Read third.** Concrete timeline from MVP to mature system.

**Key sections:**
- Phase 0: Foundation (MVP, 3 months)
- Phase 1: Open Backend (6 months)
- Phase 2: Federation (12 months)
- Phase 3: Context Layer (18 months)
- Resource requirements (team, budget)
- Success metrics

**Time to read:** 30 minutes
**Action:** Understand what to build when

### 4. [CRITIQUE_RESPONSE.md](./CRITIQUE_RESPONSE.md) - Values Codex
**Read fourth.** Detailed response to design critique + values framework.

**Key sections:**
- Response to 5 pros (strengths acknowledged)
- Response to 5 cons (mitigations provided)
- Engagement with supportive theorists (Dewey, Freire, Papert, Wenger, Illich)
- Response to skeptical theorists (Kirschner, Skinner, Luhmann, Zuboff, Postman)
- Answers to 5 critical questions (privacy, IA, openness, friction, embodiment)
- Decision heuristics & non-negotiables

**Time to read:** 60 minutes
**Action:** Understand design decisions and trade-offs

### 5. [GETTING_STARTED.md](./GETTING_STARTED.md) - Developer Guide
**Read when ready to build.** Step-by-step implementation.

**Key sections:**
- Week-by-week breakdown (12 weeks to MVP)
- Database migrations (complete schema)
- Code examples (authentication, editor, facilitation)
- Common issues & solutions
- Deployment guide (Vercel or self-hosted)

**Time to read:** 45 minutes + implementation time
**Action:** Build Phase 0 MVP

---

## Wireframes (Visual Reference)

### Core User Flows

**[1-today-fullwidth-wireframe.html](./1-today-fullwidth-wireframe.html)**
- Today page with three display modes (collapsed/preview/inline)
- Full-width prompt transclusion
- Geocached prompts (locked/unlocked states)
- Single-column, single-focus design

**[2-settings-privacy-wireframe.html](./2-settings-privacy-wireframe.html)**
- Privacy controls (private by default)
- Knowledge graph transparency
- Export/import options
- Federation settings

**[3-cofacilitation-wireframe.html](./3-cofacilitation-wireframe.html)**
- Roles (owner, co-facilitator, participant)
- Permissions matrix
- Activity log
- Invitation workflow

**[4-suggestions-wireframe.html](./4-suggestions-wireframe.html)**
- Participant-initiated prompts
- Bottom-up curriculum
- Facilitator response flow

**[5-embodied-features-wireframe.html](./5-embodied-features-wireframe.html)**
- Geocached prompts (location-based unlocking)
- Margin note comments (not bottom)
- Real-time co-editing modes (shared/turn-taking/forking)

**[6-public-profile-wireframe.html](./6-public-profile-wireframe.html)**
- ActivityPub integration
- RSS/JSON feeds
- Follow options (Mastodon, email, RSS)
- Developer APIs (WebFinger, ActivityPub actor)

**[7-federation-import-wireframe.html](./7-federation-import-wireframe.html)**
- Cross-instance guide browsing
- Import workflow
- Customization options
- Attribution preservation

**[8-complete-architecture-wireframe.html](./8-complete-architecture-wireframe.html)**
- System overview (all primitives)
- Complete user flows (participant, facilitator, creator)
- Values in action
- Implementation phases

### Additional Wireframes

**Early explorations (reference only):**
- today-wireframe.html
- today-transclusion-wireframe.html
- guide-wireframe.html
- guide-scheduling-wireframe.html
- group-wireframe.html
- group-hybrid-review-wireframe.html

---

## Document Relationships

```
VISION.md (Philosophy)
    ↓
ARCHITECTURE.md (Technical Design)
    ↓
ROADMAP.md (Implementation Timeline)
    ↓
CRITIQUE_RESPONSE.md (Design Decisions)
    ↓
GETTING_STARTED.md (Code Implementation)
    ↓
Wireframes (Visual Reference)
```

---

## Quick Start Paths

### Path 1: Executive/Investor (30 minutes)

Read in this order:
1. VISION.md (core thesis + business model)
2. ROADMAP.md (timeline + resources)
3. Browse wireframes (visual understanding)

**Result:** Understand what, why, when, and how much

### Path 2: Designer/UX (60 minutes)

Read in this order:
1. VISION.md (values + design principles)
2. CRITIQUE_RESPONSE.md (design decisions)
3. All 8 wireframes (implementation)

**Result:** Understand design philosophy and UX patterns

### Path 3: Developer (2-3 hours)

Read in this order:
1. VISION.md (what we're building)
2. ARCHITECTURE.md (technical foundation)
3. GETTING_STARTED.md (implementation guide)
4. Reference wireframes as needed

**Result:** Ready to start coding

### Path 4: Educator/Facilitator (45 minutes)

Read in this order:
1. VISION.md (core thesis + how it works)
2. CRITIQUE_RESPONSE.md (pedagogical alignment)
3. Wireframes 1, 3, 4 (participant and facilitator flows)

**Result:** Understand how to use Cursive for teaching

### Path 5: Researcher/Theorist (90 minutes)

Read in this order:
1. VISION.md (theoretical foundation)
2. CRITIQUE_RESPONSE.md (engagement with theorists)
3. ARCHITECTURE.md (how theory becomes practice)

**Result:** Understand theoretical grounding

---

## What You Get

### Documentation (5 core documents)
- **VISION.md** (16KB, ~30 min read)
- **ARCHITECTURE.md** (24KB, ~45 min read)
- **ROADMAP.md** (19KB, ~30 min read)
- **CRITIQUE_RESPONSE.md** (34KB, ~60 min read)
- **GETTING_STARTED.md** (22KB, ~45 min + implementation)

**Total reading time:** ~3.5 hours for complete mastery

### Wireframes (8 interactive HTML files)
- Complete user flows (participant, facilitator, creator)
- All major features (today, groups, federation, settings)
- Visual design direction
- Interaction patterns

**Total:** 136KB of HTML, viewable in any browser

### Code Examples
- Database schema (complete PostgreSQL migrations)
- Authentication (Supabase + magic links)
- Letter editor (TipTap + Konva)
- API endpoints (REST with TypeScript)
- React components (Next.js App Router)

---

## Core Principles (Immutable)

**1. Human Agency** - Every action requires explicit choice
**2. Embodiment** - Learning in world, not just at screens
**3. Privacy** - Private by default, user owns data
**4. Openness** - Open protocol, portable formats
**5. Slowness** - Depth over speed, no gamification
**6. Human Craft** - AI suggests, humans author

**When in doubt:**
- Choose privacy over convenience
- Choose depth over engagement
- Choose craft over automation
- Choose openness over control

---

## Non-Negotiables (Will Never Build)

We will NEVER:
- Sell user data
- Use dark patterns
- Gamify learning (points, streaks, badges)
- Auto-send without confirmation
- Make letters public by default
- Use predictive analytics on users
- Lock users in (export always available)

**Why:** These violate core values and harm users

---

## Success Metrics

**North Star Metric:** Letters written per week (across all instances)

**Supporting Metrics:**
- Daily/weekly/monthly active users
- Federated instances
- Cross-instance guide imports
- MRR (institutions + creators)
- NPS (user satisfaction)

**NOT metrics:**
- Time on site
- Engagement score
- Completion percentage
- Social graph size

**Why:** We optimize for learning, not engagement

---

## Timeline Summary

**Phase 0 (Months 1-3):** MVP
- Core loop working
- Export/import
- Magic link sharing
- **Milestone:** 50 users, 5 groups

**Phase 1 (Months 4-6):** Open Backend
- Open source core (MIT)
- Self-hosting guide
- Protocol spec published
- **Milestone:** 10 self-hosted instances

**Phase 2 (Months 7-12):** Federation
- Cross-instance guide sharing
- Public profiles + RSS
- ActivityPub integration
- **Milestone:** 10 institutions, 1000 users

**Phase 3 (Months 13-18):** Context Layer
- Knowledge graph (opt-in)
- Semantic discovery
- Advanced whispers
- **Milestone:** 100 institutions, 10K users

---

## Resource Requirements

**Team:**
- Phase 0: 1-2 developers
- Phase 1-2: 4-5 people (dev, design, DevOps)
- Phase 3: 6-7 people (+ ML engineer)

**Budget:**
- Phase 0: ~$62K (3 months)
- Phase 1-2: ~$216K (6 months)
- Phase 3: ~$332K (6 months)
- **Total (18 months): ~$610K**

**Funding:**
- Bootstrap Phase 0 (personal/angel)
- Seed round for Phase 1-2 ($500K-1M)
- Series A for Phase 3 ($3-5M)

---

## Tech Stack

**Frontend:**
- Next.js 14 (App Router)
- React 18
- TypeScript
- Tailwind CSS
- TipTap (editor)
- Konva (drawing)

**Backend:**
- Next.js API routes
- PostgreSQL 14+
- Supabase (managed hosting)
- Or: Self-hosted Postgres

**Deployment:**
- Vercel (recommended)
- Or: Docker Compose (self-hosted)

**Storage:**
- Supabase Storage (S3-compatible)
- Or: Local filesystem

---

## Getting Help

**Documentation:**
- All docs in this package
- Start with VISION.md

**Code:**
- GETTING_STARTED.md has step-by-step guide
- Copy-paste examples included

**Questions:**
- Check CRITIQUE_RESPONSE.md for design decisions
- Check ARCHITECTURE.md for technical details
- Check ROADMAP.md for timeline

**Community (future):**
- GitHub Discussions (when open sourced)
- Discord server (if created)
- Email: support@cursive.com

---

## Contributing

**Phase 0 (Now):**
- This is pre-open-source
- Core team only

**Phase 1 (Months 4+):**
- Open source backend released
- Contributions welcome
- Governance model TBD

**Phase 2-3:**
- Full community participation
- Federation protocol developed collaboratively

---

## License

**Current Status:**
- Documentation: Open (read, share, reference)
- Code: Not yet released
- Protocol: Will be open standard

**Future:**
- Core backend: MIT License
- Frontend: TBD (likely proprietary or AGPL)
- Protocol spec: Public domain or CC0

---

## The Vision (TL;DR)

**We're building correspondence infrastructure for learning.**

Not a platform. A protocol.

Like email, but for thoughtful correspondence that enables learning through dialogue, making, and being present in the world.

Open source. Federated. Privacy-first. Human-authored.

Letters are portable. Guides are shareable. Identity is federated. Instances are self-hostable.

We compete on quality, not lock-in. We monetize through institutions and creators, not surveillance.

If we fail in 5 years, your work survives. That's not a bug—it's the design.

---

## Begin

You have everything you need:

- ✅ Vision (philosophy, values, business model)
- ✅ Architecture (technical design, database, API)
- ✅ Roadmap (timeline, milestones, resources)
- ✅ Critique Response (design decisions, trade-offs)
- ✅ Getting Started (code examples, step-by-step)
- ✅ Wireframes (visual reference, interaction patterns)

Read. Understand. Build.

Slowly. Carefully. Openly.

**Insha'Allah.**

---

## Package Contents

**Documents (5):**
1. VISION.md
2. ARCHITECTURE.md
3. ROADMAP.md
4. CRITIQUE_RESPONSE.md
5. GETTING_STARTED.md

**Wireframes (8 main + 6 reference):**
1. Today page (full-width transclusion)
2. Settings (privacy & federation)
3. Co-facilitation
4. Suggestions (participant prompts)
5. Embodied features (geocaching, comments, co-editing)
6. Public profile (ActivityPub)
7. Federation import
8. Complete architecture

**Total package size:** ~450KB
**Est. reading time:** 3.5 hours for complete mastery
**Implementation time:** 12 weeks for Phase 0 MVP

---

**Version:** 1.0
**Date:** October 20, 2025
**Status:** Ready for Implementation

**Let's build Cursive.** 🚀
