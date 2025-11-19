# Cursive Vision

## 1. What We Are Building

Cursive is the first implementation of a convivial protocol for human-curated creation. Hosts (teachers, editors, facilitators) craft invitations, guests respond with their own words and drawings, and the interface shows the provenance of every contribution. Education is our beachhead, but the protocol is designed for salons, book clubs, newsrooms, art collectives, and anyone who wants depth over algorithmic distribution.

**Thesis:** the internet has feeds (algorithm-curated) and generators (machine-authored), but almost no infrastructure for *human* curation. Cursive fills that gap.

## 2. Design Principles

| Principle | Description | Concrete Practices |
| --- | --- | --- |
| Human Craft over Automation | Pages are sacred, human-authored artifacts. | Editors never auto-complete; Thinking Nodes tool from the chrome. |
| Disappearing Infrastructure | The interface gets out of the way so craft is visible. | Press Enter to add space, no modal gymnastics, typography stays calm. |
| Slow Correspondence | Work unfolds over days, not minutes. | Folded invitations, scheduled deliveries, optional dawn releases. |
| Convivial Technology | Tools should strengthen community bonds. | Hosts curate taste; groups rename primitives; provenance is transparent. |
| Connection to Self/Others/World/Truth | Suggestions help people notice meaning, not chase metrics. | Patterns in journals, relevant peers, geocached prompts, cited texts. |

## 3. Vocabulary & Renamable Primitives

We keep a small set of canonical concepts and let each group rename them to fit its culture:

- **Host** → facilitator, editor, teacher, librarian.
- **Series** → guide, collection, journey, season.
- **Invitation** → prompt, challenge, letter, mission.
- **Response** → page, folio, artifact, study.
- **Curations** → gallery, anthology, bulletin, exhibition.
- **Thinking Node** → tool, partner, studio assistant.

Renamability is a first-class product requirement: the protocol exposes neutral keys; the UI lets communities supply human language.

## 4. Architecture Overview

### Layer A – Human Notebook
- TipTap `doc` JSON with human-only content.
- Drawings stored as Konva stroke batches in `ink_strokes`.
- Replay events (optional) captured in `text_events`.
- `ensureValidDocument` enforces structural integrity before persistence.

### Layer B – Invitation & Curation
- `mail_items` queue invitations with schedule, vocabulary, and optional geofences.
- `notebook_tabs` represent spaces; `assignment_metadata` tracks status (`pending`, `begun`, `submitted`, `reviewed`).
- `assignment_snapshots` freeze entire sections for curation, gifts, or archival.
- Curations reference responses and keep a transparent audit trail (who selected what, when, and why).

### Layer C – Thinking Nodes
- Semantic context stored in `user_context`/`group_context`.
- Suggestions rendered as dismissible cards; no inline writing.
- LLMs can connect people, cite texts, unlock geocached prompts, and invite embodied exploration.

## 5. Education is the Beachhead

We launch with classrooms because teachers already perform human curation daily. Schools provide:
- Clear rituals (mail arrives, work begins, submissions happen).
- Natural scale (30–150 people per host).
- Budget for tools that honour craft.

Our roadmap expands the same protocol to:
- Creative studios (collaborative fiction, illustration telegrams).
- Newsrooms (editorial saloons and reader correspondences).
- Community learning circles (book clubs, public philosophy).
- Research labs (slow peer review).

## 6. LLM Participation Rules

1. **Observer, not Author:** models may notice, recall, and connect—but never type within the document.
2. **Invoked or Tooled:** suggestions appear on the periphery and require explicit human acceptance.
3. **Transparent Provenance:** every suggestion is tagged with “machine notice”; human decisions remain primary.
4. **Embodied Bias:** default suggestions nudge toward place-based experiences (walks, museums, cafés) rather than more screen time.
5. **Data Belongs to Humans:** students own their notebooks and replay windows; sharing is always opt-in.

## 7. Proof of Craft (formerly “Proof of Human”)

We prefer “proof of craft” to avoid arms-race language. The system records:
- Carried context (who invited whom, which guide version).
- Crafted response (who wrote/drew what).
- Curatorial decisions (who selected it, when, and why).
- Optional process trail (replay window, ink strokes).

Hosts can request this metadata when authenticity matters; guests can withhold when privacy is paramount.

## 8. Embodiment & Place

Cursive should insist on real-world experiences when possible:
- Geocached invitations that unlock at particular locations.
- Location boards for neighbourhood studios/cafés.
- Nature identification prompts that transform photos into reflections.
- Field assignments that require walking, visiting, or observing.

These features keep the protocol anchored to the world, not trapped in the browser.

## 9. Strategy & Phases

1. **Phase 0 – Product-Ready Classroom Loop (in progress)**  
   Mail → Invitation → Response → Submission → Curation.  
   Finish the Section Editor, Submission Panel, replay capture, and curator galleries.

2. **Phase 1 – Guide Publishing & Adoption**  
   Make it effortless for hosts to publish a series, remix others, and share galleries back to the commons.

3. **Phase 2 – Thinking Node Platform**  
   Ship semantic search, collaborator suggestions, and embodied tools. Define public APIs.

4. **Phase 3 – Creative Community Expansion**  
   Pilot with writing collectives, art salons, and small editorial teams. Validate vocabulary flexibility.

5. **Phase 4 – Protocol Packaging**  
   Publish the “Convivial Protocol” spec (identity, invitations, responses, curation, provenance). Offer hosted implementation plus federated options.

## 10. What Success Looks Like

- Hosts describe Cursive as “the space where language stays human.”
- Students and guests treat their notebooks as lifelong studios, not disposable homework bins.
- Invitations, responses, and curations can move between instances without losing context or provenance.
- A New York Times editor, a high-school teacher, and a community art facilitator can all run their gatherings on the same protocol.
- “Let’s Cursive this” becomes shorthand for “let’s curate a human, beautiful exchange together.”
