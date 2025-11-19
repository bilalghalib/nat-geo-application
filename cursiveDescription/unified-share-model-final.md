# Unified Share & Verification Model - Final Spec

## The Simple Model

**Two share types + Export:**

1. **Share Page** - The finished work (most common)
2. **Share Walkthrough** - The creation process (recorded or live)
3. **Export** - Full data portability (sovereignty)

**Verification is embedded metadata, not a separate share type.**

---

## How It Works: End-to-End Flows

### Flow 1: School Homework Submission

**Student perspective:**
```
1. Write essay in Cursive
   ├─ Background recording captures process automatically
   ├─ Session fingerprint generated
   └─ No action required from student

2. Click "Share page"
   ├─ Copy link
   ├─ Badge visibility: Auto (shows if strong fingerprint)
   └─ URL: /p/my-climate-essay

3. Paste link in LMS submission box
   └─ Done
```

**Teacher perspective:**
```
1. Open student's link → /p/my-climate-essay

2. See finished essay + subtle badge in header
   ✓ Human-made

3. Most of the time: Read, grade, done
   └─ Badge = confidence boost, no action needed

4. If suspicious:
   ├─ Click badge
   ├─ See: "47 min, 312 strokes, 23 revisions, 94% confidence"
   ├─ Optional: "Request walkthrough access"
   └─ Student approves → teacher watches replay

5. If really suspicious:
   ├─ Ask student for export
   ├─ Student: Export → With verification
   ├─ Teacher uploads .cursive file to independent verifier
   └─ Hash matches → confirmed authentic
```

**Why this works:**
- âœ… Student doesn't think about "proof" vs "page"
- âœ… Teacher gets confidence by default
- âœ… Privacy preserved (deep access requires consent)
- âœ… Verification is portable (.cursive export)
- âœ… Works with any LMS (just a link)

---

### Flow 2: Portfolio Showcase

**Designer perspective:**
```
1. Create logo design in Cursive

2. Share to social media:
   ├─ Option A: Share page (finished work)
   │  └─ Shows ✓ Human-made badge → "47 min of craft"
   │
   └─ Option B: Share walkthrough (30s timelapse)
      └─ Viewers watch creation process with audio

3. For client presentation:
   ├─ Export page + sessions
   ├─ Upload to personal website
   └─ Embed HTML viewer (self-hosted)
```

**Viewer perspective:**
```
1. See Twitter post with link

2. Click → opens /p/logo-design
   ├─ See finished logo
   ├─ Notice badge: "⚡ Handcrafted"
   └─ Below: "Watch creation process" button

3. Click button → /w/session-xyz
   └─ 30-second timelapse with designer's narration
```

**Why this works:**
- âœ… Shows off craft without being preachy
- âœ… Badge adds credibility ("this took real work")
- âœ… Walkthrough is optional extra
- âœ… Can self-host (no platform dependency)

---

### Flow 3: Live Teaching Session

**Teacher perspective:**
```
1. Open blank page in Cursive

2. Click "Share" → "Go live"
   ├─ Title: "Office Hours: Calculus Help"
   ├─ Description: "Working through problem set 3"
   └─ [Go live]

3. System generates join link: /w/live/abc-123
   ├─ Copy link
   └─ Paste in Slack channel

4. Work through problems in real-time
   ├─ Students watch as you draw/type
   ├─ See participant count: "12 watching"
   └─ Students can ask questions via chat (future)

5. When done: Click "End live"
   ├─ Session auto-converts to replay
   ├─ Toast: "Session ended. Replay available at [link]"
   └─ Can trim idle segments before sharing
```

**Student perspective:**
```
1. See Slack message: "Join office hours: [link]"

2. Click → /w/live/abc-123
   ├─ See teacher's screen live
   ├─ Watch them work through problem
   └─ See other participants (count only)

3. If arrive late:
   ├─ Session still live → join in progress
   └─ Session ended → redirects to replay
```

**Why this works:**
- âœ… One URL for both live and replay
- âœ… No separate "live" vs "recorded" confusion
- âœ… Students can review later
- âœ… Teacher doesn't need to manage two links

---

### Flow 4: Research Field Notes

**Researcher perspective:**
```
1. Take daily notes during expedition
   ├─ Text, drawings, photos
   ├─ GPS automatically captured
   └─ Works offline

2. At end of month:
   ├─ Export collection → .cursive archive
   ├─ Save to encrypted USB drive
   └─ Upload to institutional repository (when online)

3. Years later:
   ├─ Download from repository
   ├─ Import into new Cursive instance
   └─ All context preserved (dates, locations, sessions)
```

**Institutional repository:**
```
1. Receive .cursive file

2. Extract:
   ├─ pages/ → index in search system
   ├─ index.html → browsable web view
   ├─ fingerprints.json → authenticity metadata
   └─ assets/ → photos, audio

3. Serve at: repository.edu/researchers/alice/expedition-2025

4. Researchers worldwide can:
   ├─ Browse notes (no Cursive account needed)
   ├─ Download full archive
   └─ Verify authenticity via hash
```

**Why this works:**
- âœ… Data survives platform changes
- âœ… Institutional systems can ingest
- âœ… Works offline (critical for field work)
- âœ… Open format, no vendor lock-in

---

### Flow 5: Collaborative Review

**Writer perspective:**
```
1. Draft article in Cursive

2. Share with editor:
   ├─ Click "Share page"
   ├─ Enable comments: Yes
   ├─ Copy link
   └─ Send to editor@magazine.com

3. Editor leaves inline comments

4. Writer addresses feedback

5. When final:
   ├─ Turn off comments
   └─ Export → PDF for publication
```

**Editor perspective:**
```
1. Open link → /p/article-draft

2. See finished article + badge
   └─ Badge shows: "2 hours, 3 sessions"
   └─ Gives context: "This is early draft" vs "Polished final"

3. Leave comments inline
   ├─ "This needs a citation"
   ├─ "Expand this section"
   └─ "Great metaphor here"

4. Writer addresses → notifications

5. Optional: Request walkthrough
   └─ "Show me how you arrived at this argument"
   └─ Watch session recording to understand thought process
```

**Why this works:**
- âœ… Badge provides effort context (don't be too harsh on early drafts)
- âœ… Comments are native to page view
- âœ… Walkthrough helps understand reasoning
- âœ… Export means writer owns final version

---

### Flow 6: Student Portfolio for College Apps

**Student perspective:**
```
1. Throughout senior year:
   ├─ Write essays in Cursive
   ├─ Keep journal
   └─ Document projects

2. Apply to college:
   ├─ Share page: Personal statement essay
   ├─ Share walkthrough: "How I solved this math problem"
   └─ Export collection: Full senior year journal

3. Optional: Enable badge on all shared pages
   └─ Shows authenticity across portfolio
```

**Admissions officer perspective:**
```
1. Click portfolio link → /p/personal-statement

2. See well-written essay + badge
   └─ ✓ Human-made (87% confidence)
   └─ Reassuring in age of ChatGPT

3. Click supplemental link → /w/math-problem-solving
   └─ 2-minute video of student working through problem
   └─ Demonstrates actual understanding, not memorization

4. For verification (rare):
   ├─ Request .cursive export from student
   ├─ Upload to university's verification system
   └─ Hash confirms authenticity
```

**Why this works:**
- âœ… Badge provides baseline trust
- âœ… Walkthroughs show actual competence
- âœ… University can verify independently
- âœ… Student owns portfolio data

---

## Comparison: Before vs After

### Before (your original presets idea)

```
Share →
├─ Choose preset: "Submit Proof"
├─ Configure tabs: Static | Deep | Replay
├─ Copy link: /share/abc-123?token=xyz
└─ Viewer sees tabs, clicks around
   └─ Confusion: "Which tab should I look at?"
```

**Problems:**
- Too much configuration
- URL doesn't communicate intent
- Tabs hide what's actually shared
- Same link for everyone (can't customize)

### After (this spec)

```
Share →
├─ Share page (default)
│  ├─ Badge: Auto-shown if verified
│  ├─ URL: /p/abc-123
│  └─ Simple settings: Visibility, Comments
│
├─ Share walkthrough
│  ├─ URL: /w/session-xyz
│  └─ Simple options: Audio, Comments
│
└─ Export
   ├─ With verification (.cursive)
   └─ Plain formats (HTML, PDF, Markdown)
```

**Advantages:**
- âœ… Clear URLs communicate intent
- âœ… Less configuration (smart defaults)
- âœ… Verification embedded, not separate
- âœ… Can share different links to different people
- âœ… Export provides escape hatch

---

## Technical Implementation Summary

### Database schema additions

```sql
-- Verification badges (auto-generated from sessions)
CREATE TABLE page_verifications (
  page_id UUID PRIMARY KEY REFERENCES pages(id),
  fingerprint_hash TEXT NOT NULL,
  confidence_score INTEGER NOT NULL,  -- 0-100
  badge_visibility TEXT DEFAULT 'auto',  -- 'auto' | 'always' | 'never'
  metrics JSONB NOT NULL,  -- stroke_count, revision_count, etc.
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Access requests (teacher → student)
CREATE TABLE verification_access_requests (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  page_id UUID REFERENCES pages(id) NOT NULL,
  requester_id UUID REFERENCES users(id) NOT NULL,
  owner_id UUID REFERENCES users(id) NOT NULL,
  message TEXT,
  status TEXT DEFAULT 'pending',  -- 'pending' | 'approved' | 'declined'
  expires_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  responded_at TIMESTAMPTZ
);

-- Export jobs (for async large exports)
CREATE TABLE export_jobs (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES users(id) NOT NULL,
  export_type TEXT NOT NULL,  -- 'page' | 'collection' | 'account'
  resource_id UUID,
  status TEXT DEFAULT 'processing',  -- 'processing' | 'completed' | 'failed'
  download_url TEXT,
  expires_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### API routes

```typescript
// Share endpoints (existing, no changes)
GET  /p/:pageId                    // Static page view
GET  /w/:sessionId                 // Walkthrough replay
GET  /w/live/:sessionId            // Live session

// Verification endpoints (new)
GET  /api/pages/:id/verification   // Get badge data
POST /api/verification/request     // Request walkthrough access
POST /api/verification/respond     // Approve/decline request

// Export endpoints (new)
POST /api/export/page/:id          // Start page export
POST /api/export/page/:id/with-sessions
POST /api/export/collection/:id
POST /api/export/account
GET  /api/export/jobs/:jobId       // Poll export status

// Import endpoints (new)
POST /api/import                   // Upload .cursive file
GET  /api/import/jobs/:jobId       // Poll import status
```

### React components

```typescript
// Share button + menu (modified)
<ShareButton 
  page={page}
  options={['page', 'walkthrough', 'export']}
/>

// Verification badge (new)
<VerificationBadge 
  page={page}
  onClick={openVerificationModal}
/>

// Verification modal (new)
<VerificationDetailsModal 
  fingerprint={fingerprint}
  sessions={sessions}
  onRequestAccess={handleRequest}
/>

// Export dialog (new)
<ExportDialog 
  resource={page | collection}
  type="page" // or "collection" or "account"
/>

// Import dialog (new)
<ImportDialog 
  onUpload={handleFileUpload}
/>
```

---

## Migration Path (if you've built presets already)

**Week 1:**
1. Keep Share button
2. Remove preset chooser
3. Change menu to: Page | Walkthrough | Export
4. Remove tabs from viewer

**Week 2:**
1. Add verification badge to page view
2. Implement badge click → modal
3. Calculate fingerprints on-demand

**Week 3:**
1. Add access request flow
2. Teacher → Student → Approve → Link to walkthrough

**Week 4:**
1. Implement export system
2. HTML, PDF, JSON formats
3. .cursive archive format

**Week 5:**
1. Implement import system
2. Manifest validation
3. Conflict resolution

---

## FAQ

**Q: Isn't this just hiding the "proof" view instead of removing it?**

A: No—there's no separate view. The "proof" is metadata (fingerprint, confidence score, metrics) that's shown in a modal. The viewer still sees the page, just with additional context available on-demand.

**Q: What if a teacher wants to see the Deep view (all strokes, no audio) without requesting walkthrough access?**

A: The verification modal shows aggregate metrics (stroke count, revision count, idle gaps). If the teacher needs the full timeline, they request walkthrough access—but that includes audio if it was recorded. For purely non-audio timeline data, we could add a "Request session data" option that gives JSON export without audio. But this is an edge case.

**Q: What if someone wants to share the walkthrough but not the finished page?**

A: They can share the walkthrough link (`/w/session-xyz`) directly. The walkthrough view can show "View finished page" button at the end, but it's optional.

**Q: Can I share a page with some people and a walkthrough with others?**

A: Yes—they're different URLs. Share `/p/page-abc` to general audience, share `/w/session-xyz` to collaborators who want to see the process.

**Q: What if I want to prove I made something without revealing the content?**

A: Export the fingerprint only (future feature). The certificate PDF could show metrics + hash without showing the page content. This would be useful for patenting/copyright scenarios.

**Q: How does this work with institutional requirements (e.g., schools that mandate verification)?**

A: Schools can set policy: `require_verification_badge: true, minimum_confidence_score: 70`. If a student tries to share a page with low/no fingerprint, system prompts: "Your teacher requires verification. Please work on this page in Cursive to generate a fingerprint, or upload an existing document with citation."

---

## Summary: The Core Insight

**Don't create separate share types for verification—embed verification as inspectable metadata.**

This means:
- âœ… Simpler mental model (one page, one link)
- âœ… Progressive disclosure (badge → modal → request access)
- âœ… Works for all use cases (schools, portfolios, collaboration)
- âœ… Privacy-preserving (opt-in deep access)
- âœ… Portable (export includes fingerprint)
- âœ… Open web (HTML + JSON = no lock-in)

The three-part system (Share Page / Share Walkthrough / Export) gives you:
- **Static view** for finished work
- **Process view** for teaching/showcasing
- **Full portability** for sovereignty

And the verification badge provides trust without creating a separate "proof" workflow.

---

**This is the final architecture. It's simpler, more flexible, and more aligned with your protocol values than the preset approach.**
