
roadmap:
# Cursive: Implementation Roadmap

## Overview

This document outlines the path from current state to Phase 3 (federated, context-aware system).

**Timeline:** 18-24 months
**Approach:** Incremental delivery, user feedback at each phase
**Principle:** Ship early, iterate based on real use

## Current State Assessment

### What Exists (Based on Logs)

**Backend:**
- ✅ PostgreSQL schema (users, profiles, sections, pages, groups)
- ✅ Supabase auth (cookie-based)
- ✅ Mail system (mail_items, today_mail_items view)
- ✅ Groups (facilitator/participant roles)
- ✅ Guides (guide_pages)
- ✅ Whisper system (plugins, cards, runs)
- ✅ Writing sessions tracking

**Frontend:**
- ✅ Today page (with transclusion issues to fix)
- ✅ Facilitation tab (needs consolidation)
- ✅ Page editor (TipTap)
- ✅ Drawing capability (mentioned)
- ⚠️ Dashboard vs FacilitationTab duplication
- ⚠️ PagePicker exists but not exposed
- ⚠️ Vocabulary customization not in UI

**Broken/Missing:**
- ❌ Mail card behavior (cloning vs linking)
- ❌ Custom page sending UI
- ❌ Unified facilitator view
- ❌ Export/import for letters
- ❌ Public profiles
- ❌ Federation protocol
- ❌ Knowledge graph UI

### Technical Debt

**Priority 1 (Blocking):**
1. Fix today_mail_items view (recipient_id issue)
2. Consolidate dashboard.tsx vs FacilitationTab
3. Fix mail card → worksheet linking
4. Restore custom page sending

**Priority 2 (Important):**
1. Add vocabulary customization UI
2. Implement export/import
3. Clean up API auth (convert to createApiClient)
4. Add confirmation window UI

**Priority 3 (Nice to have):**
1. Offline support (service worker)
2. Better error handling
3. Loading states
4. Accessibility improvements

## Phase 0: Foundation (Current - Month 3)

### Goal
**Ship a working MVP where facilitators can send prompts and participants can respond.**

### Week 1-2: Stabilization

**Fix Critical Bugs:**
- [x] today_mail_items.recipient_id (DONE per logs)
- [ ] API auth conversion (released-prompts.ts, submissions.ts, etc.)
- [ ] Mail card linking (not cloning)
- [ ] FacilitationTab consolidation

**Deliverable:** No console errors, all core flows work

### Week 3-4: Core Facilitation Flow

**Build:**
1. Unified facilitator view (delete dashboard.tsx)
2. "Send Next Guide Prompt" button (uses released_prompts)
3. "Send Custom Page" button (PagePicker modal)
4. Vocabulary customization form (SettingsTab)
5. Confirmation window UI (before each send)

**User Flow:**
```
Facilitator:
1. Opens /groups/[id] → sees FacilitationTab
2. Clicks "Send Next" → confirms → letter sent to all
3. Or clicks "Send Custom" → picks page → sends
4. Goes to Review → sees submissions (responses table)
5. Leaves margin comments (not bottom)

Participant:
1. Opens /@username/main/today/YYYY-MM-DD
2. Sees mail card (title, due, status)
3. Clicks "Open worksheet" → goes to /p/[sectionId]
4. Writes response, submits
5. Facilitator sees snapshot in Review
```

**Deliverable:** End-to-end facilitation works

### Week 5-6: Participant Experience

**Build:**
1. Today page with full-width transclusion
2. Three display modes (collapsed/preview/inline)
3. Mail card as reference (not content)
4. Worksheet lives in group folder
5. Status tracking (not started / working / submitted)

**User Flow:**
```
Participant morning routine:
1. Open Today page
2. See prompt card (collapsed)
3. Click "Show preview" or "Show inline"
4. Either:
   a. Quick note in inline editor
   b. "Open worksheet" for full editor
5. Work at own pace
6. Submit when ready
```

**Deliverable:** Participants have clear, calm interface

### Week 7-8: Polish & Test

**Build:**
1. Onboarding flow (first-time users)
2. Help docs (in-app)
3. Error messages (friendly, actionable)
4. Loading states (skeletons)
5. Mobile responsive

**Test:**
1. Run with 2-3 beta groups (10-20 people each)
2. Gather feedback
3. Fix bugs
4. Iterate

**Deliverable:** Production-ready MVP

### Week 9-12: Export/Import Foundation

**Build:**
1. Export letter as JSON
2. Export letter as Markdown + drawings (SVG)
3. Import letter from JSON
4. Export guide as JSON
5. Import guide from JSON (local only, no federation yet)

**Format:**
```json
// letter-export.json
{
  "cursive": "1.0",
  "type": "letter",
  "id": "uuid",
  "title": "...",
  "pages": [...],
  "exported_at": "2025-10-20T10:00:00Z"
}

// guide-export.json
{
  "cursive": "1.0",
  "type": "guide",
  "id": "philosophy-101",
  "author": "dr-chen@cursive.com",
  "letters": [...]
}
```

**UI:**
```
Settings → Export & Data
├── Export all letters (JSON)
├── Export all letters (Markdown)
├── Export guide "Philosophy 101"
└── Import guide from file
```

**Deliverable:** Users can take their data with them

### Phase 0 Success Criteria

**Metrics:**
- [ ] 50+ active users
- [ ] 5+ active groups
- [ ] 100+ letters written
- [ ] <5% error rate
- [ ] <2s p95 response time
- [ ] Positive feedback from beta users

**Qualitative:**
- [ ] Facilitators can run courses without bugs
- [ ] Participants find it calm, not overwhelming
- [ ] Export works (users trust us with their data)
- [ ] Core loop feels good

## Phase 1: Open Backend (Month 4-6)

### Goal
**Open source the core, enable self-hosting, establish protocol.**

### Month 4: Code Organization

**Refactor:**
1. Extract `cursive-core` package
2. Separate frontend (`cursive-app`) from backend
3. Define clean API boundaries
4. Document protocol spec

**Structure:**
```
cursive/
├── cursive-core/          (MIT license)
│   ├── src/
│   │   ├── api/           (REST endpoints)
│   │   ├── models/        (Letter, Guide, Identity)
│   │   ├── db/            (Schema + migrations)
│   │   └── federation/    (Import/export utils)
│   ├── docker-compose.yml
│   ├── README.md
│   └── LICENSE (MIT)
│
└── cursive-app/           (Proprietary for now)
    ├── frontend/          (Next.js)
    ├── whispers/          (AI features)
    └── marketplace/       (Guide marketplace)
```

**Deliverable:** Clean separation, documented

### Month 5: Self-Hosting

**Build:**
1. Docker Compose setup
2. Environment config (`.env` template)
3. Database migrations (Postgres)
4. Self-hosting guide (`docs/self-hosting.md`)
5. Sample nginx config

**Test:**
1. Fresh Ubuntu 24 VPS
2. Follow self-hosting guide
3. Instance runs at `my-school.edu`
4. Can create users, write letters, create groups

**Deliverable:** Anyone can self-host

### Month 6: Protocol Specification

**Document:**
1. Letter format spec (`docs/letter-format.md`)
2. Guide format spec (`docs/guide-format.md`)
3. Federation protocol v1 (`docs/federation.md`)
4. REST API reference (`docs/api.md`)

**Publish:**
1. GitHub repo (cursive/cursive-core)
2. Protocol site (protocol.cursive.com)
3. Announce to community

**Deliverable:** Open standard established

### Phase 1 Success Criteria

**Technical:**
- [ ] cursive-core repo public
- [ ] MIT license
- [ ] Docker Compose works
- [ ] 3+ self-hosted instances
- [ ] Protocol spec published

**Community:**
- [ ] 10+ GitHub stars
- [ ] 3+ external contributors
- [ ] 2+ forks
- [ ] Active discussions (issues, PRs)

## Phase 2: Federation (Month 7-12)

### Goal
**Instances can share guides, subscribe to feeds, discover across network.**

### Month 7-8: Instance Registry

**Build:**
1. Federation API endpoints
2. Instance registration
3. Trust relationships (public keys)
4. Webhook system

**Flow:**
```
1. westwood.edu registers with cursive.com
POST cursive.com/api/federation/register
{
  "instance": "westwood.edu",
  "admin": "admin@westwood.edu",
  "public_key": "..."
}

2. cursive.com stores trust relationship
3. Can now federate
```

**UI:**
```
Settings → Federation
├── Your instance: cursive.com
├── Connected instances:
│   └── westwood.edu (verified)
└── [+ Connect to new instance]
```

**Deliverable:** Instances can register relationships

### Month 9-10: Guide Marketplace

**Build:**
1. Browse guides (local + federated)
2. Import guide from other instance
3. Customize imported guide
4. Publish guide to marketplace

**User Flow:**
```
Facilitator at westwood.edu:
1. Browse → Federated Guides
2. Search: "philosophy embodiment"
3. Find: "Embodied Philosophy" by dr-chen@cursive.com
4. Click "Preview & Import"
5. See full guide contents
6. Customize vocabulary, schedule
7. Import to westwood.edu
8. Create group using imported guide
```

**UI:**
```
/guides/marketplace
├── Local guides (5)
├── From cursive.com (23)
├── From stanford.edu (12)
└── [Search across all instances]
```

**Deliverable:** Guides flow between instances

### Month 11-12: Public Profiles & RSS

**Build:**
1. Public profile page (/username)
2. RSS feed (/username/feed.rss)
3. JSON Feed (/username/feed.json)
4. Profile customization
5. WebFinger (/.well-known/webfinger)

**User Flow:**
```
Alex publishes letter:
1. Write letter, toggle "Make public"
2. Letter appears at cursive.com/alex/truth-shadows
3. Also appears in RSS feed
4. Sarah at westwood.edu subscribes to RSS
5. Gets notified of new letters
```

**Formats:**
```xml
<!-- RSS 2.0 -->
<rss version="2.0">
  <channel>
    <title>Alex Chen</title>
    <link>https://cursive.com/alex</link>
    <item>
      <title>On Truth and Shadows</title>
      <link>https://cursive.com/alex/truth-shadows</link>
      <pubDate>Mon, 20 Oct 2025 14:30:00 GMT</pubDate>
    </item>
  </channel>
</rss>
```

```json
// JSON Feed
{
  "version": "https://jsonfeed.org/version/1",
  "title": "Alex Chen",
  "home_page_url": "https://cursive.com/alex",
  "feed_url": "https://cursive.com/alex/feed.json",
  "items": [
    {
      "id": "uuid",
      "url": "https://cursive.com/alex/truth-shadows",
      "title": "On Truth and Shadows",
      "date_published": "2025-10-20T14:30:00Z"
    }
  ]
}
```

**Deliverable:** Public presence, standard feeds

### Phase 2 Success Criteria

**Technical:**
- [ ] 10+ instances in federation
- [ ] 100+ guides shared cross-instance
- [ ] RSS feeds working
- [ ] Webhook delivery <1s p95

**Usage:**
- [ ] 500+ active users across all instances
- [ ] 50+ guides in marketplace
- [ ] 20+ cross-instance imports

## Phase 3: Context Layer (Month 13-18)

### Goal
**Privacy-preserving discovery, knowledge graph, advanced whispers.**

### Month 13-14: Knowledge Graph Foundation

**Build:**
1. Entity extraction (from letters)
2. Knowledge graph storage
3. User-visible graph UI
4. Opt-in/opt-out controls

**Flow:**
```
1. User writes letter mentioning "Plato", "shadows", "embodiment"
2. System extracts entities (locally)
3. Shows in Settings → Your Knowledge Graph:
   - People: Plato, Sarah Parker
   - Concepts: embodiment, perception
   - Places: Westwood Sculpture Garden
4. User can delete any node
5. User can opt in to "Make discoverable"
```

**Privacy:**
- Default: OFF (no graph)
- Opt-in: Local only (graph for personal whispers)
- Opt-in: Discoverable (cross-instance connections)

**Deliverable:** Knowledge graph working, privacy-first

### Month 15-16: Semantic Discovery

**Build:**
1. Embeddings-based search
2. Cross-instance query protocol
3. Connection requests
4. Consent flow

**Flow:**
```
Sarah at westwood.edu:
1. Enabled "Discoverable"
2. Writes about "phenomenology of walking"
3. System publishes embeddings (not full text)

Alex at cursive.com:
1. Enabled "Discoverable"
2. Writes about "embodied knowledge"
3. Gets whisper: "Sarah at westwood.edu writes about related topics"
4. Clicks "Request to connect"
5. Sarah gets notification: "Alex wants to read your letters"
6. Sarah approves
7. They can now correspond
```

**Privacy Model:**
```javascript
// What gets shared cross-instance:
{
  "user_id": "sarah@westwood.edu",
  "embedding": [...vector...],
  "entities": ["phenomenology", "walking", "Merleau-Ponty"],
  "preview": "First 100 characters...",
  "request_url": "westwood.edu/api/connection-request"
}

// What does NOT get shared:
- Full letter content
- Private metadata
- User location
- Reading patterns
```

**Deliverable:** Discovery works, privacy preserved

### Month 17-18: ActivityPub Integration

**Build:**
1. ActivityPub actor (user profile)
2. Inbox/outbox endpoints
3. Follow from Mastodon
4. Publish letters to fediverse
5. Reply handling (becomes correspondence)

**User Flow:**
```
Alex at cursive.com:
1. Publishes letter "On Truth and Shadows"
2. Letter posted to ActivityPub outbox
3. Followers on Mastodon see it in their timeline
4. They can reply (becomes letter in Alex's inbox)
5. Alex can respond (turns into correspondence)
```

**Technical:**
```javascript
// ActivityPub Actor
GET cursive.com/users/alex
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Person",
  "id": "https://cursive.com/users/alex",
  "inbox": "https://cursive.com/users/alex/inbox",
  "outbox": "https://cursive.com/users/alex/outbox",
  "followers": "https://cursive.com/users/alex/followers",
  "following": "https://cursive.com/users/alex/following"
}

// Create activity (publish letter)
POST cursive.com/users/alex/outbox
{
  "type": "Create",
  "object": {
    "type": "Article",
    "name": "On Truth and Shadows",
    "content": "...",
    "url": "https://cursive.com/alex/truth-shadows"
  }
}
```

**Deliverable:** Cursive is a fediverse citizen

### Phase 3 Success Criteria

**Technical:**
- [ ] Knowledge graph opt-in rate >20%
- [ ] Cross-instance connections working
- [ ] ActivityPub verified by Mastodon community
- [ ] Privacy audit passed (no leaks)

**Usage:**
- [ ] 1000+ users opted into discovery
- [ ] 100+ cross-instance connections made
- [ ] 50+ Mastodon instances following Cursive users
- [ ] Positive feedback on privacy model

## Beyond Phase 3

### Potential Features (Month 19+)

**Co-Editing:**
- Real-time collaboration (Yjs + WebSocket)
- Turn-taking mode
- Forking mode

**Geocaching:**
- Location-based prompt unlocking
- Place-tagging
- Spatial discovery

**Mobile Apps:**
- Native iOS (Swift)
- Native Android (Kotlin)
- Or: Progressive Web App (PWA)

**Advanced Whispers:**
- Framework plugin (detect which thinking framework user is using)
- Gap plugin (identify knowledge gaps)
- Connection plugin (suggest related concepts)
- Parliament plugin (critique from different perspectives)

**Analytics (for facilitators):**
- Engagement patterns
- Common struggles
- Effective prompts
- (Privacy-preserving, aggregated only)

## Resource Requirements

### Team

**Phase 0 (MVP):**
- 1 full-stack engineer
- 1 designer (part-time)
- Beta testers (volunteers)

**Phase 1-2 (Federation):**
- 2 full-stack engineers
- 1 designer
- 1 DevOps/infrastructure
- Community manager (part-time)

**Phase 3 (Context Layer):**
- 3 full-stack engineers
- 1 ML engineer (for embeddings)
- 1 designer
- 1 DevOps
- Community manager (full-time)

### Budget (Estimated)

**Phase 0 (3 months):**
- Engineering: $50K
- Design: $10K
- Infrastructure: $500/mo
- Total: ~$62K

**Phase 1-2 (6 months):**
- Engineering: $150K
- Design: $20K
- DevOps: $40K
- Infrastructure: $1K/mo
- Total: ~$216K

**Phase 3 (6 months):**
- Engineering: $200K
- ML: $60K
- Design: $20K
- DevOps: $40K
- Infrastructure: $2K/mo
- Total: ~$332K

**Grand Total (18 months): ~$610K**

### Funding Strategy

**Bootstrap (Phase 0):**
- Personal funds or small angel round
- Goal: Prove concept, get first customers

**Seed Round (Phase 1-2):**
- $500K-1M
- Use: Build team, ship federation
- Milestones: 10 institutions, 1000 users

**Series A (Phase 3+):**
- $3-5M
- Use: Scale, marketing, enterprise features
- Milestones: 100 institutions, 10K users

## Risk Management

### Technical Risks

**Risk: Federation protocol too complex**
- Mitigation: Start simple (files), iterate
- Fallback: Stay single-instance longer

**Risk: ActivityPub integration breaks**
- Mitigation: Minimal implementation first
- Fallback: RSS feeds work without ActivityPub

**Risk: Knowledge graph privacy leaks**
- Mitigation: External audit before launch
- Fallback: Disable cross-instance discovery

### Business Risks

**Risk: Schools don't pay**
- Mitigation: Free tier proves value first
- Fallback: Focus on individual creators

**Risk: Open source cannibalizes revenue**
- Mitigation: Managed hosting is convenience
- Fallback: Enterprise features only in paid

**Risk: Competition from big platforms**
- Mitigation: Open protocol can't be killed
- Fallback: Niche community is enough

### Operational Risks

**Risk: Can't hire fast enough**
- Mitigation: Start small, contractors
- Fallback: Slower timeline, cut scope

**Risk: Instance admin abuse**
- Mitigation: Clear terms, moderation tools
- Fallback: Block abusive instances

**Risk: Spam/abuse in marketplace**
- Mitigation: Review process, reports
- Fallback: Curated marketplace only

## Success Metrics

### North Star Metric
**Letters written per week** (across all instances)

### Supporting Metrics

**Engagement:**
- Daily/weekly/monthly active users
- Letters per user
- Groups per facilitator
- Response rate (participants replying to prompts)

**Network:**
- Federated instances
- Cross-instance guide imports
- Cross-instance connections
- ActivityPub followers

**Revenue:**
- MRR (Monthly Recurring Revenue)
- Institutions paying
- Marketplace transactions
- Average LTV (Lifetime Value)

**Quality:**
- NPS (Net Promoter Score)
- Retention (30/60/90 day)
- Public letters ratio (opt-in rate)
- Self-hosted instances (protocol adoption)

## Decision Framework

### When to Build

Build if:
- [ ] Users asking for it repeatedly
- [ ] Aligns with core values
- [ ] Feasible in <1 month
- [ ] Moves needle on north star metric

Don't build if:
- [ ] Only 1 user requested
- [ ] Violates values (e.g., adds surveillance)
- [ ] Would take >3 months
- [ ] Distracts from core loop

### When to Open Source

Open source if:
- [ ] Core to protocol
- [ ] Benefits from community review
- [ ] Not competitive advantage
- [ ] Well-documented

Keep proprietary if:
- [ ] UI/UX differentiation
- [ ] Revenue-generating feature
- [ ] Not stable yet
- [ ] Security-sensitive

### When to Federate

Federate if:
- [ ] Multiple instances want to share
- [ ] Clear use case emerges
- [ ] Privacy model solid
- [ ] Technical capacity exists

Don't federate if:
- [ ] No demand yet
- [ ] Privacy unclear
- [ ] Would break things
- [ ] Too complex for value

## Conclusion

**The path is clear:**

1. **Phase 0:** Ship MVP, prove core loop works
2. **Phase 1:** Open source, establish protocol
3. **Phase 2:** Federation, network effects
4. **Phase 3:** Discovery, context layer

**The timeline is realistic:**

- 3 months to MVP (usable)
- 6 months to open source (protocol)
- 12 months to federation (network)
- 18 months to discovery (context)

**The approach is parsimonious:**

Build only what's needed, when it's needed, for people who need it.

No speculation. No premature optimization. Just steady progress toward the vision.

Insha'Allah.
architecture: 
# Cursive: Technical Architecture

## Responding to the Critique

### Acknowledged Issues

**From the 5 Cons:**

1. **Surface sprawl risk** (Today, Mail, Group, Library, Profile, Gallery)
   - **Response:** Ruthless IA rules established (see below)
   - **Solution:** One canonical home per action, explicit navigation hierarchy

2. **Two inbox problem** (Participants and facilitators juggle Today + Mail)
   - **Response:** Mail is notification center only, never workspace
   - **Solution:** Default=Today, escalation rules clear

3. **Protocol ambition vs v1 capacity** (Identity + Federation + Knowledge Graph)
   - **Response:** Phased implementation (0→1→2→3)
   - **Solution:** Layer 1 & 2 in v1, Layer 3 & 4 later

4. **Privacy edges** (Public profiles + magic links + cross-instance discovery)
   - **Response:** Private by default, explicit opt-in for everything
   - **Solution:** Binary states, no gradual exposure

5. **State split complexity** (Transclusion + external worksheets + migration semantics)
   - **Response:** Letters are atomic, references are thin
   - **Solution:** Move/postpone/archive = simple state transitions

### Integration with Skeptical Theorists

**Niklas Luhmann (Systems Complexity):**
- **Warning:** Identity/federation coupling creates unpredictable feedback loops
- **Our Response:** Loose coupling via TTL caching, explicit instance boundaries in UI, atomic operations only
- **Implementation:** Letters self-contained, instances cache read-only, opt-out invalidates immediately

**Shoshana Zuboff (Surveillance Capitalism):**
- **Warning:** Knowledge graph = surveillance infrastructure even with good intentions
- **Our Response:** No graph without consent, transparent extraction, user owns nodes, no predictive modeling
- **Implementation:** Discovery opt-in only, visible graph with delete buttons, mutual consent for connections

**Neil Postman (Technopoly):**
- **Warning:** Calling it "OS" makes tool totalizing—learning precedes any tool
- **Our Response:** Tool as threshold, not container; no completion metrics; offline-first; analog escape hatches
- **Implementation:** Free tier fully functional, export to PDF/print, no gamification, low-tech mode

## The Parsimonious OS Approach

### What "OS" Means Here

**NOT an operating system** (we're not Linux or MacOS)

**YES an operating standard** (like HTTP is for web)

**The metaphor:**
- **Kernel** = Core primitives (Letter, Guide, Identity, Instance)
- **System calls** = API for extensions (plugins, integrations)
- **File system** = How letters/guides are stored and addressed
- **User space** = Apps built on Cursive protocol

**Like:**
- Email (SMTP/IMAP/POP3) = protocol, Gmail/Outlook = apps
- Web (HTTP/HTML) = protocol, browsers = apps
- ActivityPub = protocol, Mastodon/Pixelfed = apps

**Not like:**
- macOS (closed, proprietary, single vendor)
- Windows (bundled apps, locked ecosystem)
- iOS (walled garden, app store monopoly)

### Parsimonious = Minimal, Sufficient, Composable

**Minimal:** Only essential primitives. No "nice-to-haves" in core.

**Sufficient:** Covers 80% use cases without extension.

**Composable:** Primitives combine to create complex behaviors.

**Example:**
- **Bad (not parsimonious):** "Assignment" as separate primitive with submissions, grades, rubrics, deadlines, etc.
- **Good (parsimonious):** Letter + Mail + Group = assignments emerge from composition

## Core Primitives (The Kernel)

### 1. Letter

**Definition:** A self-contained unit of writing (1+ pages)

**Format:**
```json
{
  "cursive": "1.0",
  "type": "letter",
  "id": "uuid",
  "author": {
    "id": "alex@cursive.com",
    "name": "Alex Chen",
    "instance": "cursive.com"
  },
  "created": "2025-10-20T14:30:00Z",
  "updated": "2025-10-20T16:45:00Z",
  "title": "On Truth and Shadows",
  "pages": [
    {
      "order": 1,
      "content": {...tiptap json...},
      "drawings": [...stroke data...],
      "metadata": {...}
    }
  ],
  "context": {
    "entities": ["Plato", "shadows", "perception"],
    "places": [{"name": "sculpture garden", "lat": 34.05, "lng": -118.24}],
    "connections": ["letter-uuid-2", "letter-uuid-5"]
  },
  "access": {
    "visibility": "private",  // private | public | magic-link
    "discoverable": false,     // if public, can be found via search?
    "url": null                // if public, what URL?
  },
  "provenance": {
    "derived_from": null,       // if forked/copied
    "co_authors": [],           // if collaborative
    "ai_assisted": false        // if whispers were used
  },
  "signature": "..."            // cryptographic signature
}
```

**Properties:**
- **Atomic:** Contains everything needed to render
- **Portable:** Import/export as single file
- **Addressable:** Has UUID + optional URL
- **Versionable:** Changes tracked
- **Signable:** Author can cryptographically sign

**Operations:**
```
create_letter(author, title) → letter
update_letter(letter_id, changes) → letter
delete_letter(letter_id) → void
export_letter(letter_id, format) → file
import_letter(file) → letter
fork_letter(letter_id) → new_letter
sign_letter(letter_id, private_key) → signature
verify_letter(letter_id, signature, public_key) → boolean
```

### 2. Guide

**Definition:** A curriculum template (sequence + schedule + facilitation settings)

**Format:**
```json
{
  "cursive": "1.0",
  "type": "guide",
  "id": "philosophy-101",
  "author": "dr-chen@cursive.com",
  "title": "Foundations of Philosophy",
  "description": "...",
  "license": "CC-BY-SA-4.0",
  "letters": [
    {
      "template_id": "letter-1-uuid",
      "order": 1,
      "offset_days": 0,
      "title": "The Cave Allegory",
      "geofence": {
        "type": "circle",
        "center": {"lat": 34.05, "lng": -118.24},
        "radius": 100
      }
    }
  ],
  "schedule": {
    "frequency": "weekly",
    "confirmation_window_days": 1,
    "default_time": "09:00"
  },
  "vocabulary": {
    "letter": "Reflection",
    "submit": "Share",
    "guide": "Journey",
    "facilitator": "Guide"
  },
  "facilitation": {
    "review_required": true,
    "gallery_enabled": true,
    "suggestions_enabled": true
  }
}
```

**Properties:**
- **Template-based:** References letter templates, doesn't embed them
- **Importable:** Can be imported to any instance
- **Customizable:** Vocabulary and schedule editable
- **Licensed:** CC, proprietary, or custom

**Operations:**
```
create_guide(author, title, letters) → guide
import_guide(guide_json, instance) → guide
customize_guide(guide_id, vocabulary, schedule) → guide
export_guide(guide_id) → json
publish_guide(guide_id, marketplace) → listing
```

### 3. Identity

**Definition:** A person using Cursive across instances

**Format:**
```
alex@cursive.com
└── username: alex
└── instance: cursive.com
```

**Properties:**
- **Federated:** Works across all instances (like email)
- **Portable:** Can migrate to different instance
- **Discoverable:** Has WebFinger endpoint
- **ActivityPub-compatible:** Can be followed from Mastodon

**Operations:**
```
create_identity(username, instance) → identity
authenticate(username, password) → session
migrate_identity(old_instance, new_instance) → identity
lookup_identity(username@instance) → profile
```

### 4. Instance

**Definition:** A server running Cursive protocol

**Format:**
```
cursive.com
├── users/
│   ├── alex/
│   │   ├── profile.json
│   │   ├── letters/
│   │   └── guides/
│   └── sarah/
├── groups/
└── federation/
    ├── known_instances.json
    └── trust_keys/
```

**Properties:**
- **Self-hostable:** Run your own (like WordPress)
- **Federated:** Can share guides with other instances
- **Isolated:** Data lives locally, not centrally
- **Customizable:** Themes, vocabulary, plugins

**Operations:**
```
register_instance(domain, admin) → instance
federate_with(other_instance) → trust_relationship
import_guide_from(other_instance, guide_id) → guide
export_user_data(user_id) → archive
```

## Data Architecture

### Database Schema (PostgreSQL)

**Core Tables:**
```sql
-- IDENTITY & AUTH
users (id, username, instance, created_at)
profiles (user_id, display_name, bio, avatar_url)

-- CONTENT
letters (id, author_id, title, content, access, created_at, updated_at)
letter_pages (id, letter_id, order, content, drawings)
letter_versions (id, letter_id, version, changes, created_at)

-- CURRICULUM
guides (id, author_id, title, description, license, settings)
guide_letters (id, guide_id, template_letter_id, order, offset_days, geofence)

-- ORGANIZATION
groups (id, guide_id, facilitator_id, instance, settings)
group_members (group_id, user_id, role)  -- role: owner, co-facilitator, participant
group_invitations (id, group_id, letter_id, scheduled_for, status)

-- DELIVERY
mail_items (id, recipient_id, sender_id, letter_id, scheduled_for, status)
worksheets (id, letter_id, group_id, user_id, submitted_at, snapshot_id)

-- DISCOVERY (opt-in)
knowledge_graph_nodes (user_id, entity_type, entity_name, source_letters)
knowledge_graph_edges (from_node, to_node, relationship_type)

-- FEDERATION
federated_instances (domain, trust_level, public_key, last_seen)
federated_guides (local_id, remote_id, source_instance, imported_at)

-- WHISPERS (plugins)
whisper_plugins (id, name, version, enabled_for_groups)
whisper_cards (id, user_id, letter_id, card_type, shown_at, status)
```

### File Storage

**Letters stored as files:**
```
/data/users/alex@cursive.com/
├── letters/
│   ├── uuid-1.json
│   ├── uuid-2.json
│   └── uuid-3.json
├── drawings/
│   ├── uuid-1-page-1.svg
│   └── uuid-2-page-1.svg
└── exports/
    └── 2025-10-20-backup.tar.gz
```

**Why files + database:**
- **Database** = metadata, relationships, queries
- **Files** = actual content, easy backup/export
- **Hybrid** = fast queries + portable content

## API Architecture

### REST API (cursive-core)

**Authentication:**
```
POST /api/auth/login
POST /api/auth/logout
GET  /api/auth/session
```

**Letters:**
```
POST   /api/letters                    # create
GET    /api/letters/:id                # read
PUT    /api/letters/:id                # update
DELETE /api/letters/:id                # delete
GET    /api/letters/:id/export?format  # export
POST   /api/letters/import             # import
POST   /api/letters/:id/fork           # fork
```

**Guides:**
```
POST /api/guides                       # create
GET  /api/guides/:id                   # read
GET  /api/guides/:id/export            # export
POST /api/guides/import                # import
```

**Groups:**
```
POST /api/groups                       # create
GET  /api/groups/:id                   # read
POST /api/groups/:id/invitations       # send letter to group
GET  /api/groups/:id/worksheets        # list submissions
POST /api/groups/:id/members           # add co-facilitator
```

**Federation:**
```
GET  /.well-known/webfinger            # identity discovery
GET  /users/:username                  # ActivityPub actor
GET  /users/:username/inbox            # ActivityPub inbox
POST /users/:username/outbox           # ActivityPub outbox
GET  /federation/guides                # list importable guides
POST /federation/guides/:id/import     # import from other instance
```

### WebSocket (real-time, optional)

**For co-editing:**
```
ws://cursive.com/letters/:id/edit
└── Sends operational transforms (OT) for collaborative editing
```

**For presence:**
```
ws://cursive.com/groups/:id/presence
└── Shows who's online in group
```

## Federation Protocol

### Phase 1: Import/Export (v1)

**Simple file-based federation:**

1. **Export guide:**
   ```bash
   GET cursive.com/api/guides/philosophy-101/export
   → philosophy-101.cursive.json
   ```

2. **Import guide:**
   ```bash
   POST westwood.edu/api/guides/import
   Body: philosophy-101.cursive.json
   → Creates local copy at westwood.edu
   ```

3. **Attribution preserved:**
   - Original author: dr-chen@cursive.com
   - Imported to: westwood.edu
   - Modified by: prof-martinez@westwood.edu

### Phase 2: Webhooks (v1.5)

**Instance-to-instance notification:**

```javascript
// Instance A registers with Instance B
POST cursive.com/api/federation/register
{
  "instance": "westwood.edu",
  "callback": "westwood.edu/api/federation/inbox",
  "public_key": "..."
}

// When guide published at cursive.com
POST westwood.edu/api/federation/inbox
{
  "type": "guide.published",
  "guide_id": "philosophy-101",
  "author": "dr-chen@cursive.com",
  "url": "cursive.com/guides/philosophy-101"
}

// westwood.edu can then import
GET cursive.com/api/guides/philosophy-101/export
```

### Phase 3: ActivityPub (v2)

**Full fediverse integration:**

```javascript
// User publishes letter
POST cursive.com/users/alex/outbox
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Create",
  "actor": "https://cursive.com/users/alex",
  "object": {
    "type": "Article",
    "name": "On Truth and Shadows",
    "content": "...",
    "url": "https://cursive.com/alex/letters/truth-shadows"
  }
}

// Followers on Mastodon receive notification
→ Shows in their timeline
→ Can reply (becomes correspondence)
```

## Implementation Phases

### Phase 0: Foundation (Now - 3 months)

**Goal:** Ship MVP with core loop working

**Build:**
1. Letter editor (TipTap + Konva for drawing)
2. Today page (single-column journal + prompt transclusion)
3. Group facilitation (send letters, review worksheets)
4. Mail system (in-app + email notifications)
5. Export/import (JSON, Markdown)

**Tech Stack:**
- **Frontend:** Next.js, React, TypeScript
- **Backend:** Next.js API routes, PostgreSQL, Supabase
- **Storage:** Supabase Storage (S3-compatible)
- **Auth:** Supabase Auth (OAuth + magic links)

**Not yet built:**
- Federation (just export/import files)
- Knowledge graph (no discovery yet)
- ActivityPub (comes later)
- Plugins (use built-in features only)

**Result:** Functional app at cursive.com

### Phase 1: Open Backend (3-6 months)

**Goal:** Open source core, enable self-hosting

**Build:**
1. Extract `cursive-core` as standalone package
2. MIT license the backend
3. Docker Compose setup
4. Self-hosting docs
5. REST API stabilized

**Open Source:**
```
cursive-core/
├── src/
│   ├── api/         # REST endpoints
│   ├── models/      # Letter, Guide, Identity, Instance
│   ├── federation/  # Import/export
│   └── db/          # Schema + migrations
├── docker-compose.yml
├── README.md
├── LICENSE (MIT)
└── docs/
    ├── self-hosting.md
    ├── api.md
    └── federation.md
```

**Keep Proprietary (for now):**
```
cursive-app/
├── frontend/         # Next.js UI
├── whispers/         # AI features
├── analytics/        # Premium features
└── marketplace/      # Guide marketplace
```

**Result:** Schools can self-host, devs can extend

### Phase 2: Federation (6-12 months)

**Goal:** Instances can share guides, subscribe to feeds

**Build:**
1. Instance registry (cursive.com knows about westwood.edu)
2. Webhook system (cross-instance notifications)
3. Guide marketplace (browse federated guides)
4. RSS feeds (public profiles)
5. OAuth (cursive.com as identity provider)

**Protocol:**
```
# Register instance
POST cursive.com/api/federation/register
{
  "instance": "westwood.edu",
  "admin": "admin@westwood.edu"
}

# Import guide from another instance
GET cursive.com/api/guides/philosophy-101/export
POST westwood.edu/api/guides/import

# Subscribe to public feed
GET cursive.com/users/alex/feed.rss
```

**Result:** Network effects, cross-instance value

### Phase 3: Context Layer (Year 2)

**Goal:** Privacy-preserving discovery across instances

**Build:**
1. Knowledge graph (entities extracted from letters)
2. Semantic search (embeddings-based)
3. Discovery (find people writing about similar things)
4. ActivityPub (full fediverse integration)
5. Advanced whispers (context-aware suggestions)

**Privacy Model:**
```
1. User opts in to "discoverable"
2. Extract entities locally (Plato, shadows, embodiment)
3. Publish embeddings only (not full content)
4. Other instances can query: "Who writes about X?"
5. Results show preview + request access link
6. User approves or denies connection
```

**Result:** Unique value that open source alone can't replicate

## Security & Privacy

### Threat Model

**What we protect against:**

1. **Platform surveillance:** User can opt out of all tracking
2. **Content extraction:** Letters private by default, requires consent to share
3. **Identity theft:** Cryptographic signatures on letters
4. **Instance compromise:** Data encrypted at rest, regular backups
5. **Cross-instance leakage:** TTL on cached data, explicit boundaries

**What we don't protect against:**

1. **Malicious instance admin:** If you self-host, admin has database access
2. **Compromised device:** If someone steals your laptop, they can read your letters
3. **Social engineering:** If you approve a connection, that person can read what you shared

### Privacy Guarantees

**Strong guarantees:**
- Private letters never leave your instance
- Knowledge graph opt-in only (default: disabled)
- Export your data anytime
- Delete account = all data deleted

**Weak guarantees:**
- Once you share via magic link, recipient controls that copy
- Public letters cached by other instances (30-day TTL)
- Federated guides retain attribution (can't anonymize)

### Encryption

**At rest:**
- Database encrypted (AES-256)
- File storage encrypted (S3 server-side)
- Backups encrypted

**In transit:**
- HTTPS everywhere (TLS 1.3)
- WebSocket over WSS
- API keys rotated regularly

**End-to-end (future):**
- Private letters can be E2E encrypted
- User holds private key
- Instance stores encrypted blob
- Can't read on web, only in desktop app with key

## Performance & Scale

### Target Performance

**Response times:**
- Page load: < 1s (p95)
- Letter save: < 200ms (p95)
- Search: < 500ms (p95)

**Offline capability:**
- All reads work offline
- Writes queued, sync when online
- Conflict resolution automatic

**Scalability:**
- 10,000 users per instance (single server)
- 100,000 letters per user (PostgreSQL limits)
- 1MB per letter (reasonable for text + drawings)

### Caching Strategy

**Browser:**
- Service worker caches letters (IndexedDB)
- Images cached (browser cache)
- Offline-first architecture

**Server:**
- Redis for session data
- PostgreSQL for metadata
- S3 for letter content

**Federation:**
- 30-day TTL on cached profiles
- 7-day TTL on cached guides
- Invalidate on opt-out

## Monitoring & Observability

### What We Track

**System metrics:**
- Response times, error rates
- Database query performance
- Storage usage

**Usage metrics (opt-in only):**
- Letters created per day
- Groups active
- Guides imported

**What we DON'T track:**
- Letter content
- Time spent writing
- Reading patterns
- Social graph

### Logging

**Server logs:**
- API requests (no bodies)
- Errors (with context)
- Federation events

**User logs:**
- Export history
- Account changes
- Consent changes

**Retention:**
- 30 days for server logs
- Indefinite for user audit logs
- No third-party analytics

## Extensibility

### Plugin System (Whispers)

**Plugin format:**
```json
{
  "id": "connection-whisper",
  "version": "1.0",
  "name": "Connection Whisper",
  "description": "Suggests connections between ideas",
  "triggers": ["manual", "on_glow"],
  "permissions": ["read_letter_content", "query_knowledge_graph"],
  "code": "..."  // WebAssembly or sandboxed JS
}
```

**Installation:**
```bash
# Install plugin for group
POST /api/groups/:id/plugins
{
  "plugin_id": "connection-whisper",
  "enabled": true,
  "settings": {
    "min_confidence": 0.7
  }
}
```

**Execution:**
```javascript
// Sandboxed environment
const plugin = loadPlugin('connection-whisper');
const suggestions = await plugin.run({
  letter: currentLetter,
  context: userGraph
});

// Returns whisper cards
[
  {
    type: "connection",
    title: "This relates to your earlier letter about Plato",
    reason: "Both discuss the gap between appearance and reality",
    actions: [
      { label: "View letter", url: "/letters/uuid" },
      { label: "Dismiss", action: "dismiss" }
    ]
  }
]
```

### API for Extensions

**Third-party apps can:**
- Read/write letters (with OAuth consent)
- Import/export guides
- Subscribe to RSS feeds
- Query public profiles

**Example: Mobile app**
```javascript
// OAuth flow
const token = await oauthLogin('cursive.com');

// Fetch user's letters
const letters = await fetch('cursive.com/api/letters', {
  headers: { Authorization: `Bearer ${token}` }
});

// Create new letter
await fetch('cursive.com/api/letters', {
  method: 'POST',
  headers: { Authorization: `Bearer ${token}` },
  body: JSON.stringify({
    title: "Morning thoughts",
    content: "..."
  })
});
```

## Testing Strategy

### Unit Tests

**Core primitives:**
- Letter creation, update, export
- Guide import/export
- Identity resolution
- Federation webhooks

**Coverage target:** 80%+ for core

### Integration Tests

**User flows:**
- Create letter → publish → share via magic link
- Import guide → create group → send invitation
- Opt in to discovery → connect cross-instance

### E2E Tests (Playwright)

**Critical paths:**
- New user onboarding
- Facilitator creates course
- Participant responds to prompt
- Federation import

### Performance Tests

**Load testing:**
- 1000 concurrent users
- 100 requests/sec
- Database query performance

## Deployment

### cursive.com (Managed Hosting)

**Infrastructure:**
- Vercel (Next.js hosting)
- Supabase (PostgreSQL + Storage + Auth)
- Cloudflare (CDN + DDoS protection)

**Auto-scaling:**
- Vercel Edge Functions (serverless)
- Supabase connection pooling
- Read replicas for queries

### Self-Hosted (Docker)

**Requirements:**
- 2 CPU cores, 4GB RAM
- 100GB SSD storage
- PostgreSQL 14+
- Node.js 18+

**Setup:**
```bash
# Clone repo
git clone https://github.com/cursive/cursive-core
cd cursive-core

# Configure
cp .env.example .env
# Edit .env with your domain, database, etc.

# Start
docker-compose up -d

# Access at https://your-domain.com
```

## Open Questions

### To Resolve Before v1

1. **Offline conflict resolution:** How do we handle two devices editing same letter offline?
   - **Option A:** Last-write-wins (simple, lossy)
   - **Option B:** Operational transforms (complex, preserves all edits)
   - **Leaning:** A for v1, B for v2

2. **ActivityPub depth:** Full implementation or minimal?
   - **Option A:** Full ActivityPub (can reply, like, boost)
   - **Option B:** Minimal (just publish letters to outbox)
   - **Leaning:** B for v1 (publish only), A for v2

3. **Knowledge graph storage:** Centralized or distributed?
   - **Option A:** Each instance stores its own graph
   - **Option B:** Federated query protocol (instances share embeddings)
   - **Leaning:** A for v1, B for v2

4. **Co-editing real-time:** Required for v1?
   - **Option A:** Yes, use Yjs + WebSocket
   - **Option B:** No, use turn-taking or forking
   - **Leaning:** B for v1 (simpler), A for v2

### To Explore Post-v1

1. **Blockchain for provenance:** Immutable authorship records?
2. **P2P federation:** Instances communicate directly (no central registry)?
3. **Local-first:** Run entirely on device, sync optional?
4. **Mobile app:** Native iOS/Android or PWA?

## Conclusion

This architecture is **parsimonious** because:

1. **Minimal primitives:** Letter, Guide, Identity, Instance (4 core concepts)
2. **Composable:** Complex behaviors emerge from combinations
3. **Portable:** Export/import as JSON files
4. **Extensible:** Plugin system for new features
5. **Federated:** Open protocol, not closed platform

It's **sufficient** because:

1. Covers 80% of correspondence-based learning
2. Works for individuals, groups, and institutions
3. Supports private, shared, and public work
4. Enables both synchronous and asynchronous

It's **OS-like** because:

1. Provides core services (identity, storage, delivery)
2. Defines standard formats (Letter JSON)
3. Enables extensions (plugins, API)
4. Runs anywhere (managed hosting or self-hosted)

We build this **slowly**, **carefully**, and **openly**.

Insha'Allah.
vision:
# Cursive: Vision & Philosophy

## Core Thesis

**Learning happens through dialogue, making things together, and being present in the world.** Digital tools should support this, not replace it.

We're not building a platform. We're building **convivial infrastructure**—a protocol for human correspondence that enables learning by doing together.

## The Problem We're Solving

### What's Broken in Digital Learning

**Platform lock-in:** Your writing, your courses, your relationships trapped behind proprietary walls. When the platform dies, your work dies.

**Disembodied learning:** Everything happens at a screen. The body, the world, the physical experience of understanding—excluded.

**Extractive models:** Free tools that monetize attention. "Engagement metrics" that gamify learning. Surveillance infrastructure disguised as personalization.

**Isolation:** Learning alone at screens, submitting to invisible algorithms, receiving grades from black boxes.

**Manufactured urgency:** Notifications, streaks, badges, completion percentages. The opposite of contemplative learning.

## What We're Building Instead

### Cursive as Infrastructure

**Not an app.** A protocol. Like email for thoughtful correspondence.

**Not a platform.** An open standard. Like HTML for long-form writing.

**Not social media.** A space for depth, not breadth. For letters, not posts.

### The Metaphor: Correspondence

Think of Cursive like **postal infrastructure for the mind:**

- **Letters** = portable, authored, addressable thoughts
- **Guides** = curriculum as shareable templates
- **Groups** = cohorts learning together
- **Mail** = delivery system (in-app + email)
- **Federation** = instances can share and subscribe
- **Profiles** = your work at a URL you control

You write letters. Sometimes to yourself (journal), sometimes to others (correspondence), sometimes to groups (facilitation).

Letters can be private, shared via magic link, or published to your profile. They live in folders you organize. They export as JSON, Markdown, PDF, HTML.

## Core Values

### 1. Human Agency & Consent

**Every action requires explicit choice.**

- Letters private by default
- Gallery curation requires approval
- Prompts can be postponed
- Discovery requires opt-in
- Export data anytime

**Why:** People should control their work, their schedule, their attention. No dark patterns, no "nudges", no surveillance.

### 2. Embodiment

**Learning happens in the world, not just at screens.**

- Geocached prompts (unlock at location)
- Location tagging (where was this written?)
- Drawing and handwriting (body as interface)
- "Go outside" task patterns
- Offline-first (works on plane, syncs later)

**Why:** Understanding comes through physical presence, through walking, through making with hands. The body knows things the mind doesn't.

### 3. Human Craft

**AI suggests, humans author.**

- Whispers in chrome, never in content
- Facilitators must confirm before sending
- Curation is explicit, not algorithmic
- Sacred pages = only human writing lives here

**Why:** Authorship matters. Thinking is made through writing, not generated. AI as tool, not replacement.

### 4. Openness & Portability

**You own your work, you can take it with you.**

- Open source core (MIT license)
- Portable formats (JSON, Markdown, HTML)
- Federation protocol (ActivityPub)
- Self-hostable (like WordPress, Mastodon)
- Custom domains (your.school.edu)

**Why:** Platforms die. Standards persist. Your work should outlive any single service.

### 5. Slowness & Contemplation

**Depth over speed, quality over quantity.**

- No gamification (no streaks, badges, points)
- No engagement metrics visible to facilitators
- Confirmation windows prevent set-and-forget
- Low-tech mode (disable all AI features)
- Print-friendly (your letters as physical objects)

**Why:** Learning takes time. Insight emerges slowly. Fast is not always better.

### 6. Transparency & Trust

**Everything visible, nothing hidden.**

- Knowledge graph visible to users
- Provenance always shown
- Attribution required
- Data export/audit anytime
- No behavioral profiling

**Why:** You should know what the system knows about you. No asymmetric information, no hidden models, no predictions.

## How It Works

### For Participants (Learners)

**Morning:**
- Open Today page (your daily journal)
- See new prompt (full-width in your writing flow)
- Prompt might be geocached → go to sculpture garden to unlock
- Write your response (drawing + text)
- Submit when ready → snapshot goes to facilitator

**Anytime:**
- Write personal letters in your journal
- Correspond with others (send via magic link)
- Publish to your profile (optional, explicit)
- Export everything (portable formats)

### For Facilitators (Teachers)

**Setup:**
- Create guide (sequence of letters + schedule)
- Customize vocabulary ("Exercise" → "Reflection")
- Set confirmation window (stay involved, don't automate)
- Invite co-facilitators (shared responsibility)

**Ongoing:**
- Confirm before each send ("Should I send tomorrow?")
- Review submissions (in Group workspace)
- Leave margin notes (contextual feedback)
- Request to feature work (with consent)
- Respond to suggestions (participants can propose prompts)

### For Creators (Curriculum Designers)

**Create:**
- Design guide with 6-12 letters
- Include embodied activities (location-based, making projects)
- Set license (CC-BY-SA, All Rights Reserved, etc.)
- Publish to marketplace

**Share:**
- Guide spreads across instances (federation)
- Others import and customize (vocabulary, timing)
- You earn from institutional licenses ($10-50/use)
- Network effects = good guides become standards

## The Four Layers

### Layer 1: Content (Portable)

**Letter** = atomic unit of writing (1+ pages, text + drawing)
- Format: JSON (portable, versionable, signable)
- States: Private, Public, Shared via magic link
- Location: Lives in your folders, exported anytime

**Guide** = curriculum as template (sequence + schedule + facilitation)
- Format: JSON manifest + letter templates
- Importable/exportable across instances
- Customizable (vocabulary, timing, content)

### Layer 2: Identity (Federated)

**Identity** = you@instance (alex@cursive.com, sarah@school.edu)
- Works across all Cursive instances
- ActivityPub compatible (Mastodon can follow you)
- Portable (can migrate to different instance)

**Instance** = server running Cursive (cursive.com, school.edu)
- Self-hostable (open source core)
- Federated (can share guides, subscribe to feeds)
- Custom domains (your brand, your data)

### Layer 3: Organization (Groups)

**Group** = cohort using a guide together
- Has facilitators (owner + co-facilitators)
- Has participants
- Lives on one instance, but can use guides from others

**Mail** = delivery system for letters
- Can be in-app notifications, actual email, or both
- Supports scheduling, magic links, postponing
- Not a workspace—just notification + link

### Layer 4: Context (Knowledge Graph)

**Knowledge Graph** = entities extracted from letters (opt-in)
- People, concepts, places mentioned in your writing
- Privacy-preserving (you see what's extracted, can delete)
- Enables discovery (find others writing about similar things)

**Whispers** = AI suggestions in chrome (not content)
- Connection suggestions ("Sarah writes about similar ideas")
- Related concepts ("This connects to Dewey's pragmatism")
- Embodied activities ("Visit the sculpture garden")
- Always dismissible, always optional

## Business Model

### Why This Matters

We need to be sustainable without surveillance, extraction, or lock-in.

### Revenue Streams

**1. Managed Hosting for Institutions ($500-2000/month)**
- Custom domain (school.edu)
- SSO integration
- White-label UI
- Dedicated support
- Advanced analytics
- Most revenue comes from here

**2. Creator Tier ($10/month)**
- Unlimited guides
- Sell in marketplace (we take 15% fee)
- Advanced whispers (knowledge graph)
- Priority support

**3. Guide Marketplace (15% transaction fee)**
- Creators sell guides ($10-50 each)
- We handle payments, licensing, attribution
- Like Gumroad for learning experiences

**4. Professional Services**
- Curriculum design consulting
- Facilitator training
- Custom implementation
- Research partnerships

### What's Free Forever

- Unlimited personal writing (letters, journal)
- Public profile at cursive.com/username
- Basic guide creation (up to 3 active guides)
- Magic link sharing
- All core features (writing, drawing, mail)

### Why This Works

**Schools have budget** and need:
- Reliable hosting
- Support
- Compliance (SSO, data security)
- Training for faculty

**Individuals want free** and get:
- Full writing functionality
- Public presence
- Can self-host if they want

**Creators want income** and can:
- Monetize their expertise
- Build reputation
- Reach institutions

**We avoid:**
- Selling user data (never)
- Restricting core features (open source)
- Locking people in (export anytime)
- Engagement manipulation (no metrics)

## Design Principles

### Ruthless Information Architecture

**Rule 1: One canonical home per action**
- Journaling → Always Today page
- Reviewing → Always Group workspace
- Sending → Always Group/Facilitate tab

**Rule 2: Mail is notification only, never workspace**
- Shows "you have X", links to workspace
- Never do work in Mail, only learn about work

**Rule 3: Today is single-column, single-focus**
- No sidebars
- Prompts inline (full-width transclusion)
- One thing at a time

**Rule 4: Public/Private is binary, not gradual**
- Every letter is Private or Public
- No "unlisted" or "semi-private"
- Explicit toggle, no ambiguity

**Rule 5: Federation at content level, not user level**
- Share guides (templates)
- Share letters (via magic link)
- Don't "follow" users across instances (that's social media)

### UI/UX Philosophy

**Minimize chrome, maximize canvas**
- Your writing is the interface
- Tools appear on hover/selection
- Whispers in margins, not center

**Respect attention**
- No notification spam
- Batch updates daily
- Email digest, not push

**Progressive disclosure**
- Simple by default
- Advanced features appear when needed
- Expert mode for power users

**Offline first**
- Everything works without internet
- Syncs in background
- Conflicts resolved gracefully

## What Makes This Different

### vs. Notion/Roam/Obsidian

**Them:** Personal knowledge management, notes for yourself
**Us:** Correspondence and learning, writing for others (and yourself)

**Them:** Closed ecosystems (even if data is exportable)
**Us:** Open protocol, federated, ActivityPub native

**Them:** Individual productivity
**Us:** Collective learning through dialogue

### vs. Canvas/Blackboard/Moodle

**Them:** LMS for institutions, assignment submission
**Us:** Correspondence infrastructure, learning by doing together

**Them:** Grades, completion tracking, compliance
**Us:** Reflection, dialogue, craft

**Them:** Institution-centric (teacher controls everything)
**Us:** Learner-centric (participants have agency)

### vs. Substack/Medium/Ghost

**Them:** Publishing platforms, audience building
**Us:** Learning infrastructure, cohort facilitation

**Them:** Public by default, metrics-driven
**Us:** Private by default, depth-driven

**Them:** Monetize through subscriptions
**Us:** Monetize through institutions + marketplace

### vs. Mastodon/ActivityPub

**Them:** Social network, short posts, public timeline
**Us:** Long-form correspondence, private by default

**Them:** Follows, favorites, boosts
**Us:** Letters, correspondence, curation

**Them:** Built for social, adapted for publishing
**Us:** Built for learning, happens to be social

## Critical Decisions

### 1. Private by Default

**Decision:** All letters start private. You must explicitly make them public.

**Why:** Writing is thinking. Thinking should be safe. You share when ready, not by default.

### 2. Today as Canonical Home

**Decision:** Your daily journal is the primary interface. Everything else is secondary.

**Why:** Learning is continuous. The journal is where you think, where prompts appear, where life happens. Not a dashboard, not a task list—a page.

### 3. Facilitators Stay Involved

**Decision:** Confirmation windows before each send. No set-and-forget automation.

**Why:** Facilitation is a living practice. You respond to the group, adjust timing, skip prompts when needed. Automation removes human judgment.

### 4. Federation from Day 1

**Decision:** Even v1 supports export/import. Open source core. Portable formats.

**Why:** Lock-in is unethical. If we're not around in 5 years, your work should still exist. Protocol > Platform.

### 5. Offline Capable

**Decision:** Everything works without internet. Sync is background operation.

**Why:** Learning happens on planes, in parks, in places without wifi. The tool shouldn't require constant connection.

## What Success Looks Like

### Year 1

- 1000 active writers at cursive.com (free tier)
- 10 schools running their own instances
- 50 guides in marketplace
- Open source community forming
- ActivityPub federation working

### Year 3

- 50 institutions (schools, companies, communities)
- 10,000+ active participants
- 500+ guides across all instances
- Sustainable revenue (break-even)
- Known as "email for learning"

### Year 5

- 200+ instances in federation
- 100,000+ active participants
- Standard protocol for correspondence-based learning
- Guides as open educational resources
- Protocol adopted by other tools

### Ultimate Vision

Cursive becomes infrastructure—like email, like HTTP, like RSS.

When someone wants to facilitate learning through correspondence, Cursive is the obvious choice because:
- It's open (you're not locked in)
- It's federated (works across institutions)
- It's proven (real people learning real things)
- It's sustainable (business model aligns with values)

## Non-Goals

**We are NOT building:**

- Social network (no timeline, no viral, no influencers)
- Productivity tool (no task management, no project tracking)
- Knowledge base (no wiki, no documentation system)
- LMS replacement (no compliance features, no grade books)
- Note-taking app (Obsidian exists, we're complementary)
- Publishing platform (Substack exists, we're different)

**Why these are non-goals:**

Other tools do these things well. We're focused on one thing: **correspondence-based learning through writing, making, and being present.**

## The Metaphor That Guides Everything

**Think of Cursive like a postal service:**

- You write letters (in your hand, at your pace)
- You send them to specific people (not broadcast)
- They live at addresses (URLs you control)
- The infrastructure is shared (like postal roads)
- But your letters are yours (portable, private)

**Not like:**
- A library (browsing others' work)
- A classroom (one-to-many instruction)
- A social network (following, liking, sharing)
- A workspace (collaboration on shared documents)

**The postal metaphor means:**
- Letters are atomic (self-contained)
- Addressing matters (who, when, why)
- Stamps = intentionality (you choose to send)
- Envelopes = privacy (sealed until opened)
- Postcards = public letters (anyone can read)

When in doubt, ask: "What would the postal service do?"

## Begin

With these values, these principles, and this vision, we build Cursive.

Not quickly. Not perfectly. But **parsimoniously**—with only what's needed, in service of learning.

Insha'Allah.
readme:
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