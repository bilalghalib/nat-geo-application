# Export System: Data Sovereignty & Portability

## Core Principle

Every user must be able to extract their complete digital presence—pages, sessions, metadata, verification proofs—in an open format that can be re-imported elsewhere or archived independently.

---

## Export Types

### 1. Single Page Export
**Use case:** Share one piece of work outside the platform

**Format options:**
- HTML (standalone, styled)
- Markdown (plain text with metadata)
- PDF (printable, with verification badge)
- JSON (full TipTap structure + metadata)

**What's included:**
```json
{
  "cursive_version": "1.0",
  "export_type": "single_page",
  "exported_at": "2025-10-30T14:30:00Z",
  "page": {
    "id": "abc-123",
    "title": "Essay on Climate Change",
    "author": {
      "id": "user-456",
      "name": "Alice",
      "canonical_id": "alice@cursive.edu"
    },
    "content": { /* TipTap JSON */ },
    "metadata": {
      "created_at": "2025-10-29T10:00:00Z",
      "updated_at": "2025-10-30T14:00:00Z",
      "word_count": 1234,
      "tags": ["climate", "essay"],
      "visibility": "private"
    },
    "fields": {
      "assignment_id": "hw-001",
      "grade": null,
      "submitted_at": "2025-10-30T14:30:00Z"
    }
  }
}
```

**UI:**
```
Export this page →
├─ HTML (for web)
├─ Markdown (for notes apps)
├─ PDF (for printing)
└─ JSON (for re-import)
```

---

### 2. Page + Sessions Export
**Use case:** Include proof-of-work for verification

**Format:** `.cursive` archive (ZIP)

**Contents:**
```
my-essay.cursive/
├─ manifest.json          # Export metadata
├─ page.json              # Page content + metadata
├─ page.html              # Human-readable version
├─ sessions/
│  ├─ session-1.json      # Timeline events
│  ├─ session-2.json
│  └─ session-3.json
├─ fingerprint.json       # Verification data
├─ certificate.pdf        # Human-readable proof
└─ assets/
   ├─ audio-1.mp3         # If recorded with audio
   └─ image-1.png         # Embedded images
```

**manifest.json:**
```json
{
  "cursive_version": "1.0",
  "export_type": "page_with_sessions",
  "exported_at": "2025-10-30T14:30:00Z",
  "exported_by": {
    "id": "user-456",
    "canonical_id": "alice@cursive.edu"
  },
  "contents": {
    "page": "page.json",
    "sessions": ["sessions/session-1.json", "sessions/session-2.json"],
    "fingerprint": "fingerprint.json",
    "certificate": "certificate.pdf",
    "assets": ["assets/audio-1.mp3"]
  },
  "verification": {
    "hash": "sha256:abc123...",
    "signature": "...",  // Optional: cryptographic signature
    "public_key": "..."  // Optional: for verification
  }
}
```

**session-1.json:**
```json
{
  "session_id": "session-xyz",
  "page_id": "page-abc",
  "session_type": "background",
  "started_at": "2025-10-29T10:00:00Z",
  "ended_at": "2025-10-29T10:47:00Z",
  "active_duration_ms": 2820000,
  "events": [
    {
      "timestamp_ms": 0,
      "event_type": "typing",
      "data": {
        "position": 0,
        "content": "The climate crisis is..."
      }
    },
    {
      "timestamp_ms": 1500,
      "event_type": "ink_stroke",
      "data": {
        "points": [[100, 200, 0.5], [102, 205, 0.6]],
        "tool": "pen",
        "color": "#000000"
      }
    },
    // ... more events
  ],
  "metadata": {
    "device": "iPad Pro",
    "browser": "Safari",
    "locale": "en-US",
    "timezone": "America/New_York"
  }
}
```

**fingerprint.json:**
```json
{
  "page_id": "page-abc",
  "sessions": ["session-xyz", "session-def"],
  "hash": "sha256:a7b3c4d2...",
  "confidence_score": 94,
  "metrics": {
    "total_active_ms": 2820000,
    "stroke_count": 312,
    "revision_count": 23,
    "session_count": 3
  },
  "temporal_markers": {
    "idle_gaps": [5234, 8932, 12456],
    "burst_speeds": [45, 52, 38],
    "revision_clusters": [3, 5, 2, 7, 6]
  },
  "behavioral_signals": {
    "stroke_variance_ms": 456,
    "correction_rate": 0.12,
    "device_switches": 1
  },
  "verification_url": "https://cursive.edu/verify/abc123"
}
```

**UI:**
```
Export with proof →
├─ Download .cursive archive
└─ [Preview contents before download]
```

---

### 3. Collection Export
**Use case:** Backup a journal, course, or project

**Format:** `.cursive` archive (ZIP)

**Contents:**
```
my-journal.cursive/
├─ manifest.json
├─ collection.json        # Collection metadata
├─ pages/
│  ├─ 2025-10-29.json
│  ├─ 2025-10-30.json
│  └─ ...
├─ sessions/
│  ├─ session-1.json
│  ├─ session-2.json
│  └─ ...
├─ folders/
│  └─ structure.json      # Folder hierarchy
├─ assets/
│  └─ ...
└─ index.html             # Browsable archive
```

**collection.json:**
```json
{
  "id": "collection-123",
  "title": "My Daily Journal",
  "kind": "workspace",
  "owner": {
    "id": "user-456",
    "canonical_id": "alice@cursive.edu"
  },
  "created_at": "2025-01-01T00:00:00Z",
  "metadata": {
    "tags": ["journal", "personal"],
    "page_count": 243,
    "settings": {
      "default_visibility": "private",
      "allow_comments": false
    }
  }
}
```

**index.html:**
```html
<!DOCTYPE html>
<html>
<head>
  <title>My Daily Journal - Archive</title>
  <style>/* Cursive styles */</style>
</head>
<body>
  <header>
    <h1>My Daily Journal</h1>
    <p>Exported from Cursive on October 30, 2025</p>
  </header>
  
  <nav>
    <h2>Pages</h2>
    <ul>
      <li><a href="pages/2025-10-29.html">October 29, 2025</a></li>
      <li><a href="pages/2025-10-30.html">October 30, 2025</a></li>
      <!-- ... -->
    </ul>
  </nav>
  
  <main>
    <p>This is a portable archive of your Cursive collection.</p>
    <p>You can browse it offline or import it into another Cursive instance.</p>
  </main>
</body>
</html>
```

---

### 4. Full Account Export
**Use case:** Complete data portability, account migration

**Format:** `.cursive` archive (ZIP)

**Contents:**
```
alice-cursive-backup.cursive/
├─ manifest.json
├─ user.json              # Profile, settings
├─ collections/
│  ├─ journal/
│  │  ├─ collection.json
│  │  ├─ pages/
│  │  └─ sessions/
│  ├─ essays/
│  └─ ...
├─ shared/                # Pages shared with you
├─ comments/              # Comments you've made
├─ relationships/         # Following/followers
└─ verification/
   ├─ fingerprints.json   # All verification data
   └─ certificates/       # PDF proofs
```

**user.json:**
```json
{
  "id": "user-456",
  "canonical_id": "alice@cursive.edu",
  "display_name": "Alice",
  "created_at": "2025-01-15T00:00:00Z",
  "settings": {
    "email": "alice@cursive.edu",
    "timezone": "America/New_York",
    "locale": "en-US",
    "preferences": {
      "default_visibility": "private",
      "enable_verification_badges": true,
      "default_editor_mode": "handwriting"
    }
  },
  "stats": {
    "total_pages": 243,
    "total_collections": 5,
    "total_sessions": 892,
    "total_active_time_ms": 52340000
  }
}
```

---

## Import System

### Import a .cursive archive

**Flow:**
1. User uploads `.cursive` file
2. System validates manifest
3. Shows preview: "Import 243 pages, 5 collections, 892 sessions?"
4. User confirms
5. System creates pages, preserves IDs (or remaps if conflicts)
6. Verification fingerprints are preserved

**UI:**
```
Import from .cursive →
├─ Upload file
├─ [Preview shows structure]
├─ Options:
│  ├─ Preserve original IDs (if no conflicts)
│  ├─ Merge with existing collections
│  └─ Keep all pages private
└─ [Import] [Cancel]
```

**Conflict resolution:**
```
If page IDs conflict:
├─ Option 1: Create new IDs, preserve content
├─ Option 2: Skip duplicates
└─ Option 3: Overwrite existing (warn first)
```

---

## Scheduled Exports (Advanced)

**Use case:** Automatic backups for peace of mind

**Settings:**
```
Automatic backups:
├─ Frequency: Weekly / Monthly
├─ Include: All collections / Selected only
├─ Destination: Email link / Cloud storage (future)
└─ Retention: Keep last 4 backups
```

**Implementation:**
- Cron job generates export
- Emails download link (expires in 7 days)
- Stored in user's account storage temporarily

---

## Open Standards Compliance

### Why .cursive archives are standards-compliant

1. **ZIP format:** Universal archive format, any tool can open
2. **JSON data:** Human-readable, machine-parseable
3. **HTML views:** No special software needed to view
4. **PDF certificates:** Standard verification format
5. **Manifest schema:** Documented, versioned, public

### Third-party tool compatibility

A `.cursive` archive can be:
- Opened in any ZIP tool
- Parsed by any JSON library
- Viewed in any web browser (index.html)
- Verified independently (hash checking)
- Converted to other formats (JSON → Markdown, etc.)

### Re-import guarantee

**Promise:** Any `.cursive` archive exported from version X can be imported into version X or later.

**Backwards compatibility:**
- Manifest includes `cursive_version`
- Import logic handles version differences
- Deprecation policy: 2 years notice before breaking changes

---

## Use Cases: Export in Action

### 1. Student submitting to non-Cursive LMS

**Scenario:** University uses Canvas, not Cursive

**Flow:**
1. Student writes essay in Cursive
2. Clicks "Export this page → PDF"
3. Downloads PDF with verification badge
4. Uploads to Canvas
5. Teacher sees finished work + badge
6. If suspicious, teacher asks student for `.cursive` archive
7. Student exports page + sessions, shares file
8. Teacher uploads to independent verifier tool (open-source)

**Why this works:**
- No lock-in to Cursive platform
- Verification is portable
- Teacher doesn't need Cursive account

---

### 2. Freelancer showcasing process to client

**Scenario:** Designer wants to show "before/after" in portfolio

**Flow:**
1. Designer creates logo in Cursive
2. Records walkthrough with audio
3. Exports page + sessions
4. Uploads to personal website
5. Embeds HTML viewer (from index.html)
6. Client can browse finished work + watch replay

**Why this works:**
- Portfolio is self-hosted
- No dependency on Cursive servers
- Client doesn't need Cursive account

---

### 3. Researcher archiving field notes

**Scenario:** Anthropologist on 3-month expedition, intermittent internet

**Flow:**
1. Takes daily notes in Cursive (offline-first)
2. Includes photos, drawings, GPS data
3. At end of month, exports collection
4. Stores .cursive archive on encrypted USB
5. Later, imports into university's institutional repository
6. Repository system can read JSON, display HTML

**Why this works:**
- Data is portable, not trapped
- Works offline
- Institutional systems can ingest

---

### 4. Teacher grading assignments

**Scenario:** Class of 30 students, teacher wants local copies

**Flow:**
1. Students submit pages (share links)
2. Teacher uses "Batch export" tool (future feature)
3. Downloads one .cursive archive with all 30 submissions
4. Opens index.html, browses all essays offline
5. Checks verification badges
6. For suspicious submission, opens session JSON directly

**Why this works:**
- Teacher has local backup
- Can grade offline (on plane, etc.)
- No risk of students deleting work

---

### 5. User leaving Cursive platform

**Scenario:** User wants to switch to another tool

**Flow:**
1. User requests full account export
2. Downloads `.cursive` archive
3. Installs competitor app that supports Cursive format
4. Imports archive → all pages, sessions, metadata preserved
5. Continues working in new tool

**Why this works:**
- No platform lock-in
- True data sovereignty
- Encourages ecosystem of compatible tools

---

## API for Export (for third-party tools)

```typescript
// REST endpoints
GET /api/export/page/:id
GET /api/export/page/:id/with-sessions
GET /api/export/collection/:id
GET /api/export/user/full

// Response (async for large exports)
{
  "job_id": "export-xyz",
  "status": "processing",
  "estimated_seconds": 45
}

// Poll for completion
GET /api/export/jobs/:job_id
{
  "job_id": "export-xyz",
  "status": "completed",
  "download_url": "https://...",
  "expires_at": "2025-11-06T14:30:00Z"
}

// Import endpoint
POST /api/import
Content-Type: multipart/form-data

Body: .cursive file

Response:
{
  "ok": true,
  "imported": {
    "pages": 243,
    "collections": 5,
    "sessions": 892
  },
  "conflicts": [
    {
      "page_id": "abc-123",
      "resolution": "created_new_id"
    }
  ]
}
```

---

## UI: Export Menu

In app header:

```
User Menu →
├─ Settings
├─ Export →
│  ├─ Export this page
│  ├─ Export this collection
│  ├─ Export my entire account
│  ├─ Scheduled backups...
│  └─ Import from .cursive
└─ Sign out
```

In page view:

```
Page Actions (⋯) →
├─ Share page
├─ Export →
│  ├─ HTML
│  ├─ Markdown
│  ├─ PDF
│  ├─ JSON
│  └─ With verification (.cursive)
└─ Delete
```

---

## Implementation Checklist

### Phase 1: Single page export (Week 1)
- [ ] HTML export (styled, standalone)
- [ ] Markdown export (plain text)
- [ ] PDF export (with badge)
- [ ] JSON export (TipTap structure)

### Phase 2: Verification export (Week 2)
- [ ] .cursive archive format
- [ ] manifest.json schema
- [ ] session JSON inclusion
- [ ] fingerprint JSON
- [ ] certificate PDF generation

### Phase 3: Collection export (Week 3)
- [ ] Collection → .cursive archive
- [ ] index.html browsable view
- [ ] folder structure preservation
- [ ] asset bundling

### Phase 4: Full account export (Week 4)
- [ ] Async job queue for large exports
- [ ] Download link generation
- [ ] Email notification
- [ ] Expiry handling

### Phase 5: Import (Week 5-6)
- [ ] .cursive file parsing
- [ ] Manifest validation
- [ ] Preview UI before import
- [ ] Conflict resolution
- [ ] ID remapping logic

### Phase 6: Advanced (Week 7+)
- [ ] Scheduled automatic backups
- [ ] Batch export (multiple pages)
- [ ] Cloud storage integration (Dropbox, Google Drive)
- [ ] Third-party verifier tool (open-source)

---

## Why This Aligns with Protocol Values

**Sovereignty:**
- Users truly own their data
- Can leave platform anytime
- No vendor lock-in

**Transparency:**
- Open format, documented
- Human-readable HTML views
- Machine-parseable JSON

**Verifiable Craft:**
- Verification travels with content
- Independent verification possible
- Cryptographic proofs included

**Hospitality:**
- Easy for non-technical users
- Works offline
- No special software needed

**Embodied:**
- Preserves full creation timeline
- GPS, photos, audio all included
- Context travels with content

**Open Web:**
- Standard formats (ZIP, JSON, HTML)
- No proprietary codecs
- Works with existing tools
