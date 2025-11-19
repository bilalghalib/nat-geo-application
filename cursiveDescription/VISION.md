# Cursive Vision

**Last updated:** November 17, 2025

---

## One Paragraph

Cursive is a convivial notebook: a place where humans craft the page, software prepares the workshop, and context gives the work long memory. Every artifact is a page. Pages live inside collections and folders, can be transcluded, and carry provenance (how, when, by whom). Hosts curate invitations, participants respond in their own workspace, and the chrome around each page surfaces suggestions, history, and hospitality without ever writing for you.

---

## What We Are Building

Cursive is the first implementation of a convivial protocol for human-curated creation. Hosts (creators, curators, editors) craft invitations, participants respond with their own words and drawings, and the interface shows the provenance of every contribution. Our initial beachheads are education and creative communities, but the protocol is designed for any context that values human curation: salons, book clubs, newsrooms, art collectives, research labs, and anyone who wants depth over algorithmic distribution.

**Thesis:** The internet has feeds (algorithm-curated) and generators (machine-authored), but almost no infrastructure for *human* curation. Cursive fills that gap.

---

## Core Principles

### 1. Human Craft Over Automation

Pages hold only what the person typed, drew, or recorded. Tools whisper from the edges (prompts, suggestions, insights) and always cite source + cost. Provenance is explicit: we can tell which actions were human, which were suggested, and when.

**Editors never auto-complete. Tools work from the chrome, never inline.**

### 2. Prepared Workshop

- **Prepare:** Clean schema, deterministic onboarding (`handle_new_user`), lint/type gates.
- **Practice:** A focused editor with URL helpers, Today/journal flow, hosting tools.
- **Clean:** Replay logs, docs, and migrations stay accurate so every contributor lands in the same space.

### 3. Composed Context

- Collections/folders/pages are the only hard primitives.
- Questions, analytics, and prompts are layered through schema (questions/answers/aggregations, mail_items, released_prompts).
- Context flows upward: page → folder → collection → host/analytics dashboards, always editable by the people involved.

### 4. Slow Correspondence

Mail, Today, and groups encourage thoughtful pacing (scheduled prompts, replay, gallery curation). Hosts can see patterns without surveilling individuals; participants choose what to publish or keep private.

**Work unfolds over days, not minutes.** Folded invitations, scheduled deliveries, optional dawn releases.

### 5. Disappearing Infrastructure

The interface gets out of the way so craft is visible. Press Enter to add space, no modal gymnastics, typography stays calm.

### 6. Convivial Technology

Tools should strengthen community bonds. Hosts curate taste; groups rename primitives; provenance is transparent. Suggestions help people notice meaning, not chase metrics.

### 7. Open Protocol, Polished Reference App

- Protocol specs live in `protocol/` (MIT).
- Reference app demonstrates best practices (Supabase schema, URL contract, replay logging).
- Others can implement or fork, but we keep our hosted experience opinionated, warm, and well-documented.

---

## Why This Matters

Salons, studios, classrooms—any space that values reflection over throughput—needs tools that honor the page, resist extraction, and still help hosts notice patterns. Cursive makes the notebook the first-class citizen. Everything else (mail, analytics, tools) orbits the page without disturbing it.

The vision is a network of hosts and participants who can remix guides, share Today prompts, and export exhibitions while keeping authorship crystal clear.

---

## Vocabulary & Renamable Primitives

We keep a small set of canonical concepts and let each group rename them to fit its culture:

- **Host** → facilitator, editor, teacher, curator, librarian
- **Participant** → student, member, guest, contributor
- **Collection** → notebook, guide, journey, season, course
- **Invitation** → prompt, challenge, letter, mission, assignment
- **Response** → page, folio, artifact, study, submission
- **Curations** → gallery, anthology, bulletin, exhibition
- **Tool** → assistant, lens, companion, helper, analyzer

**Renamability is a first-class requirement:** The protocol exposes neutral keys; the UI lets communities supply human language.

---

## Architecture Layers

### Layer A – Human Notebook

- TipTap `doc` JSON with human-only content.
- Drawings stored as Konva stroke batches.
- Audio recordings (future) with voice fingerprints.
- `ensureValidDocument` enforces structural integrity before persistence.

**See:** [protocol/specs/page-content.md](../../protocol/specs/page-content.md)

### Layer B – Invitation & Curation

- `mail_items` queue invitations with schedule, vocabulary, and optional geofences.
- Collections represent spaces; folders organize within them.
- Response metadata tracks status (`pending`, `begun`, `shared`, `reviewed`).
- Curations keep a transparent audit trail (who selected what, when, and why).

**See:** [protocol/specs/notebook.md](../../protocol/specs/notebook.md)

### Layer C – Tools (Intelligence)

- Tools analyze content and emit structured signals.
- Suggestions rendered as dismissible cards in chrome; no inline writing.
- Tools can connect people, cite texts, unlock geocached prompts, and invite embodied exploration.
- Tools whisper, routes decide, users confirm.

**See:** [protocol/specs/tools.md](../../protocol/specs/tools.md) | [protocol/specs/routing.md](../../protocol/specs/routing.md)

---

## LLM Participation Rules

1. **Observer, not Author:** Models may notice, recall, and connect—but never type within the document.
2. **Invoked or Tooled:** Suggestions appear on the periphery and require explicit human acceptance.
3. **Transparent Provenance:** Every suggestion is tagged with "machine notice"; human decisions remain primary.
4. **Embodied Bias:** Default suggestions nudge toward place-based experiences (walks, museums, cafés) rather than more screen time.
5. **Data Belongs to Humans:** People own their notebooks and replay windows; sharing is always opt-in.

---

## Proof of Craft

We prefer "proof of craft" to avoid arms-race language. The system records:

- **Carried context:** Who invited whom, which guide version.
- **Crafted response:** Who wrote/drew/spoke what.
- **Curatorial decisions:** Who selected it, when, and why.
- **Optional process trail:** Replay window, ink strokes, keystroke patterns.

Hosts can request this metadata when authenticity matters; participants can withhold when privacy is paramount.

**See:** [protocol/specs/page-content.md#craft-verification](../../protocol/specs/page-content.md#craft-verification)

---

## Embodiment & Place

Cursive should insist on real-world experiences when possible:

- Geocached invitations that unlock at particular locations.
- Location boards for neighbourhood studios/cafés.
- Nature identification prompts that transform photos into reflections.
- Invitations that require walking, visiting, or observing.

These features keep the protocol anchored to the world, not trapped in the browser.

---

## Beachhead Markets

### Education

We start with education because teachers already perform human curation daily. Educational contexts provide:

- Clear rituals (invitations arrive, work begins, sharing happens)
- Natural scale (30–150 people per host)
- Budget for tools that honor craft
- Immediate need for alternatives to extractive platforms

**Use cases:** Courses, workshops, guided reflection, portfolio building

### Creative Communities

Writers, artists, and makers need spaces for critique, collaboration, and exhibition.

- Writing circles (shared prompts, peer feedback, anthology curation)
- Art collectives (process documentation, group exhibitions)
- Creative workshops (structured exercises, portfolio development)

**Use cases:** Writing workshops, illustration telegrams, creative portfolios

### Research & Learning

Researchers and informal learning communities value depth and provenance.

- Book clubs (reading schedules, discussion prompts, shared annotations)
- Research labs (literature review, peer commentary, slow review)
- Public philosophy (guided inquiry, Socratic dialogue)

**Use cases:** Book clubs, research collaboration, public philosophy circles

Our roadmap expands the same protocol across all these contexts.

---

## Strategy & Phases

### Phase 0 – Core Product Loop (in progress)

Invitation → Response → Sharing → Curation.

Finish the Section Editor, Sharing Panel, replay capture, and curator galleries.

### Phase 1 – Guide Publishing & Adoption

Make it effortless for hosts to publish a collection, remix others, and share galleries back to the commons.

### Phase 2 – Tool Platform

Ship semantic search, collaborator suggestions, and embodied tools. Define public APIs for tool creators.

**See:** [protocol/specs/tools.md](../../protocol/specs/tools.md)

### Phase 3 – Creative Community Expansion

Pilot with writing collectives, art salons, and small editorial teams. Validate vocabulary flexibility and renamable primitives.

### Phase 4 – Protocol Packaging

Publish the "Convivial Protocol" spec (identity, invitations, responses, curation, provenance). Offer hosted implementation plus federated options.

---

## North Star Conditions

- People trust the notebook because it never writes for them.
- Hosts can run multi-week sequences using only the primitives in this repo (collections, folders, pages, questions, mail, groups).
- Anyone can inspect an artifact and know how it came to be (human edits, replay log, tool prompts).
- The protocol is simple enough to reimplement, and the reference app feels like a lovingly tended studio.

**Stay aligned with these; everything else is tactics.**

---

## What Success Looks Like

- Hosts describe Cursive as "the space where language stays human."
- Participants treat their notebooks as lifelong studios, not disposable output bins.
- Invitations, responses, and curations can move between instances without losing context or provenance.
- A newsroom editor, a writing workshop host, and a philosophy study group can all run their gatherings on the same protocol.
- "Let's Cursive this" becomes shorthand for "let's curate a human, beautiful exchange together."

---

## Connection to Self/Others/World/Truth

Cursive helps people deepen connection to:

- **Self** – Journaling, reflection, embodied handwriting.
- **Others** – Shared prompts, cohorts, curated galleries.
- **World** – Situated practice: "look up," capture a leaf, walk outside.
- **Truth** – Doubt, exploration, provenance, open-mindedness.

Tools surface patterns in journals, connect to relevant peers, unlock geocached prompts, and cite texts—always as suggestions, never as commands.

---

## See Also

### Protocol Specifications
- [protocol/VALUES.md](../../protocol/VALUES.md) - Six core values
- [protocol/MANIFESTO.md](../../protocol/MANIFESTO.md) - Public-facing vision
- [protocol/specs/](../../protocol/specs/) - Technical protocol specs

### Implementation
- [CANONICAL_ARCHITECTURE.md](../../CANONICAL_ARCHITECTURE.md) - How we implement the protocol
- [IMPLEMENTATION_ROADMAP.md](../../IMPLEMENTATION_ROADMAP.md) - Current work

---

**Built with intention. Designed for depth. Optimized for humanity.**
