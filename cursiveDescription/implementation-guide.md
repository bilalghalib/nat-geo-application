# Implementation Guide: Share + Verification + Export

## Build Order (Prioritized)

### Phase 0: Foundation (Already Done)
✅ Pages with content
✅ Background session recording (ADR-003)
✅ Basic presentation sessions table
✅ TipTap editor

---

## Phase 1: Basic Share (Week 1)

**Goal:** Get to "Share page" working with clean URLs

### 1.1 Add public page routes
```typescript
// app/p/[pageId]/page.tsx
export default async function PublicPage({ params }: { params: { pageId: string } }) {
  const page = await getPublicPage(params.pageId);
  
  if (!page || page.visibility !== 'public') {
    return <NotFound />;
  }
  
  return (
    <div className="max-w-3xl mx-auto p-8">
      <PageHeader 
        title={page.title}
        author={page.author}
        date={page.created_at}
      />
      <PageContent content={page.content} />
    </div>
  );
}
```

### 1.2 Add Share Page dialog
```tsx
// components/SharePageDialog.tsx
export function SharePageDialog({ page }: { page: Page }) {
  const [visibility, setVisibility] = useState(page.visibility || 'unlisted');
  const url = `/p/${page.id}`;
  
  const handleSave = async () => {
    await updatePageVisibility(page.id, visibility);
    toast.success('Page sharing settings updated');
  };
  
  return (
    <Dialog>
      <DialogHeader>
        <DialogTitle>Share page</DialogTitle>
      </DialogHeader>
      
      <RadioGroup value={visibility} onValueChange={setVisibility}>
        <RadioGroupItem value="public" label="Public" />
        <RadioGroupItem value="unlisted" label="Unlisted" />
        <RadioGroupItem value="private" label="Private" />
      </RadioGroup>
      
      {visibility !== 'private' && (
        <div className="flex gap-2">
          <Input value={url} readOnly />
          <Button onClick={() => copyToClipboard(url)}>Copy</Button>
        </div>
      )}
      
      <DialogFooter>
        <Button onClick={handleSave}>Save</Button>
      </DialogFooter>
    </Dialog>
  );
}
```

### 1.3 Add Share button to page editor
```tsx
// In your page editor toolbar
<DropdownMenu>
  <DropdownMenuTrigger asChild>
    <Button variant="ghost">
      <Share className="h-4 w-4 mr-2" />
      Share
    </Button>
  </DropdownMenuTrigger>
  <DropdownMenuContent>
    <DropdownMenuItem onClick={() => openSharePageDialog()}>
      <FileText className="mr-2 h-4 w-4" />
      Share page
    </DropdownMenuItem>
    {/* More items in later phases */}
  </DropdownMenuContent>
</DropdownMenu>
```

**Deliverable:** Users can share page links that work

---

## Phase 2: Walkthroughs (Week 2)

**Goal:** Share + view recorded sessions

### 2.1 Walkthrough viewer route
```typescript
// app/w/[sessionId]/page.tsx
export default async function WalkthroughViewer({ params }: { params: { sessionId: string } }) {
  const session = await getSession(params.sessionId);
  
  if (!session || !session.public) {
    return <NotFound />;
  }
  
  return (
    <WalkthroughPlayer 
      session={session}
      events={session.events}
      audioUrl={session.audio_url}
    />
  );
}
```

### 2.2 Walkthrough player component
```tsx
// components/WalkthroughPlayer.tsx
export function WalkthroughPlayer({ session, events }: Props) {
  const [currentTime, setCurrentTime] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  
  // Replay events at correct timestamps
  useEffect(() => {
    if (!isPlaying) return;
    
    const interval = setInterval(() => {
      setCurrentTime(t => t + 100);
      
      // Find events that should fire at this time
      const eventsToFire = events.filter(e => 
        e.timestamp_ms <= currentTime && 
        e.timestamp_ms > currentTime - 100
      );
      
      eventsToFire.forEach(applyEvent);
    }, 100);
    
    return () => clearInterval(interval);
  }, [isPlaying, currentTime]);
  
  return (
    <div className="h-screen flex flex-col">
      <header className="border-b p-4">
        <h1>{session.title || 'Walkthrough'}</h1>
      </header>
      
      <main className="flex-1 overflow-hidden">
        {/* Render page content with events applied */}
        <PageView content={pageContent} />
      </main>
      
      <footer className="border-t p-4">
        <div className="flex items-center gap-4">
          <Button onClick={() => setIsPlaying(!isPlaying)}>
            {isPlaying ? <Pause /> : <Play />}
          </Button>
          
          <Slider 
            value={[currentTime]} 
            max={session.active_duration_ms}
            onValueChange={([time]) => setCurrentTime(time)}
          />
          
          <span className="text-sm">
            {formatDuration(currentTime)} / {formatDuration(session.active_duration_ms)}
          </span>
        </div>
        
        {session.audio_url && (
          <audio src={session.audio_url} ref={audioRef} />
        )}
      </footer>
    </div>
  );
}
```

### 2.3 Share Walkthrough dialog
```tsx
// components/ShareWalkthroughDialog.tsx
export function ShareWalkthroughDialog({ session }: { session: PresentationSession }) {
  const [includeAudio, setIncludeAudio] = useState(!!session.audio_url);
  const url = `/w/${session.id}`;
  
  const handleShare = async () => {
    await updateSession(session.id, { 
      public: true,
      include_audio: includeAudio 
    });
    
    toast.success('Walkthrough shared', {
      action: {
        label: 'Copy link',
        onClick: () => copyToClipboard(url)
      }
    });
  };
  
  return (
    <Dialog>
      <DialogHeader>
        <DialogTitle>Share walkthrough</DialogTitle>
      </DialogHeader>
      
      <div className="space-y-4">
        <div className="border rounded p-3">
          <div className="text-sm font-medium">Duration</div>
          <div className="text-sm text-stone-600">
            {formatDuration(session.active_duration_ms)}
          </div>
        </div>
        
        {session.audio_url && (
          <label className="flex items-center gap-2">
            <Checkbox checked={includeAudio} onCheckedChange={setIncludeAudio} />
            <span className="text-sm">Include audio narration</span>
          </label>
        )}
        
        <div className="flex gap-2">
          <Input value={url} readOnly />
          <Button onClick={() => copyToClipboard(url)}>Copy</Button>
        </div>
      </div>
      
      <DialogFooter>
        <Button onClick={handleShare}>Share</Button>
      </DialogFooter>
    </Dialog>
  );
}
```

**Deliverable:** Users can share + view walkthroughs

---

## Phase 3: Verification Badge (Week 3)

**Goal:** Show "Human-made" badge on pages with fingerprints

### 3.1 Calculate fingerprint from sessions
```python
# server/verification.py
def calculate_fingerprint(page_id: str) -> dict:
    """Generate fingerprint from all sessions for this page"""
    sessions = get_sessions_for_page(page_id)
    
    if not sessions:
        return {'confidence_score': 0}
    
    all_events = []
    for session in sessions:
        all_events.extend(session['events'])
    
    # Calculate metrics
    strokes = [e for e in all_events if e['event_type'] == 'ink_stroke']
    typing = [e for e in all_events if e['event_type'] == 'typing']
    revisions = [e for e in all_events if e['event_type'] in ['backspace', 'undo']]
    
    # Human pattern detection
    stroke_durations = [s.get('duration_ms', 0) for s in strokes]
    stroke_variance = np.std(stroke_durations)
    
    idle_gaps = calculate_idle_gaps(typing)
    correction_rate = len(revisions) / max(len(typing), 1)
    
    # Confidence score
    confidence = 50  # base
    
    if 200 <= stroke_variance <= 800:  # Human range
        confidence += 20
    elif stroke_variance < 50:  # Too perfect
        confidence -= 30
    
    if len([g for g in idle_gaps if g > 5000]) >= 3:  # Thinking pauses
        confidence += 15
    
    if 0.05 <= correction_rate <= 0.20:  # Human error rate
        confidence += 15
    
    confidence = max(0, min(100, confidence))
    
    return {
        'hash': hashlib.sha256(json.dumps(all_events).encode()).hexdigest(),
        'confidence_score': confidence,
        'stroke_count': len(strokes),
        'revision_count': len(revisions),
        'total_active_ms': sum(s['active_duration_ms'] for s in sessions),
        'session_count': len(sessions)
    }
```

### 3.2 Add badge to page view
```tsx
// components/PageHeader.tsx
export function PageHeader({ page }: { page: Page }) {
  const { data: verification } = useQuery({
    queryKey: ['verification', page.id],
    queryFn: () => fetchVerification(page.id)
  });
  
  const showBadge = verification && verification.confidence_score >= 70;
  
  return (
    <header className="flex justify-between items-center mb-8">
      <div>
        <h1 className="text-3xl font-light">{page.title}</h1>
        <p className="text-sm text-stone-600">
          by {page.author.name} • {formatDate(page.created_at)}
        </p>
      </div>
      
      {showBadge && (
        <VerificationBadge 
          verification={verification}
          onClick={() => openVerificationModal(verification)}
        />
      )}
    </header>
  );
}

// components/VerificationBadge.tsx
export function VerificationBadge({ verification, onClick }: Props) {
  return (
    <button
      onClick={onClick}
      className="flex items-center gap-1.5 px-3 py-1.5 rounded-md border border-emerald-200 bg-emerald-50 hover:bg-emerald-100 transition-colors"
    >
      <Check className="h-3 w-3 text-emerald-600" />
      <span className="text-xs font-medium text-emerald-700">Human-made</span>
    </button>
  );
}
```

### 3.3 Verification details modal
```tsx
// components/VerificationDetailsModal.tsx
export function VerificationDetailsModal({ verification, pageId }: Props) {
  const { data: sessions } = useQuery({
    queryKey: ['sessions', pageId],
    queryFn: () => fetchSessionsForPage(pageId)
  });
  
  return (
    <Dialog>
      <DialogHeader>
        <DialogTitle>
          <Shield className="inline h-5 w-5 mr-2" />
          Verification Details
        </DialogTitle>
      </DialogHeader>
      
      <div className="space-y-6">
        <Alert>
          <AlertDescription>
            This page was created through authentic human activity across {verification.session_count} work sessions.
          </AlertDescription>
        </Alert>
        
        <div className="grid grid-cols-2 gap-4">
          <MetricCard 
            label="Active time" 
            value={formatDuration(verification.total_active_ms)}
            icon={<Clock />}
          />
          <MetricCard 
            label="Pen strokes" 
            value={verification.stroke_count}
            icon={<Pen />}
          />
          <MetricCard 
            label="Revisions" 
            value={verification.revision_count}
            icon={<Edit />}
          />
          <MetricCard 
            label="Confidence" 
            value={`${verification.confidence_score}%`}
            icon={<Shield />}
          />
        </div>
        
        <div>
          <h4 className="text-sm font-medium mb-2">Work sessions</h4>
          {sessions?.map(session => (
            <div key={session.id} className="flex items-center justify-between p-2 border rounded mb-2">
              <div className="text-sm">
                <div>{formatDate(session.started_at)}</div>
                <div className="text-xs text-stone-500">
                  {formatDuration(session.active_duration_ms)} active
                </div>
              </div>
              {session.session_type === 'recorded' && (
                <Button size="sm" variant="ghost" onClick={() => navigate(`/w/${session.id}`)}>
                  <Play className="h-3 w-3 mr-1" />
                  Watch
                </Button>
              )}
            </div>
          ))}
        </div>
        
        <details>
          <summary className="text-sm cursor-pointer">Show verification hash</summary>
          <code className="text-xs break-all bg-stone-50 p-2 rounded block mt-2">
            {verification.hash}
          </code>
        </details>
      </div>
    </Dialog>
  );
}
```

**Deliverable:** Pages with strong fingerprints show badges

---

## Phase 4: Basic Export (Week 4)

**Goal:** Export single pages in multiple formats

### 4.1 Export API endpoint
```typescript
// app/api/export/page/[pageId]/route.ts
export async function POST(
  request: Request,
  { params }: { params: { pageId: string } }
) {
  const { format, includeSessions } = await request.json();
  const page = await getPage(params.pageId);
  
  switch (format) {
    case 'html':
      return exportAsHTML(page);
    case 'markdown':
      return exportAsMarkdown(page);
    case 'pdf':
      return exportAsPDF(page);
    case 'json':
      return exportAsJSON(page, includeSessions);
    case 'cursive':
      return exportAsCursiveArchive(page, includeSessions);
  }
}

async function exportAsHTML(page: Page) {
  const html = `
<!DOCTYPE html>
<html>
<head>
  <title>${page.title}</title>
  <style>${cursiveStyles}</style>
</head>
<body>
  <article>
    <header>
      <h1>${page.title}</h1>
      <p>by ${page.author.name} • ${formatDate(page.created_at)}</p>
    </header>
    <main>
      ${tiptapToHTML(page.content)}
    </main>
  </article>
</body>
</html>
  `;
  
  return new Response(html, {
    headers: {
      'Content-Type': 'text/html',
      'Content-Disposition': `attachment; filename="${slugify(page.title)}.html"`
    }
  });
}

async function exportAsCursiveArchive(page: Page, includeSessions: boolean) {
  const archive = new JSZip();
  
  // Add manifest
  archive.file('manifest.json', JSON.stringify({
    cursive_version: '1.0',
    export_type: 'page_with_sessions',
    exported_at: new Date().toISOString(),
    contents: {
      page: 'page.json',
      sessions: includeSessions ? ['sessions/'] : []
    }
  }));
  
  // Add page
  archive.file('page.json', JSON.stringify(page, null, 2));
  archive.file('page.html', await exportAsHTML(page));
  
  // Add sessions if requested
  if (includeSessions) {
    const sessions = await getSessionsForPage(page.id);
    const sessionsFolder = archive.folder('sessions');
    
    sessions.forEach(session => {
      sessionsFolder.file(
        `${session.id}.json`,
        JSON.stringify(session, null, 2)
      );
    });
    
    // Add fingerprint
    const fingerprint = await calculateFingerprint(page.id);
    archive.file('fingerprint.json', JSON.stringify(fingerprint, null, 2));
  }
  
  const blob = await archive.generateAsync({ type: 'blob' });
  return new Response(blob, {
    headers: {
      'Content-Type': 'application/zip',
      'Content-Disposition': `attachment; filename="${slugify(page.title)}.cursive"`
    }
  });
}
```

### 4.2 Export dialog
```tsx
// components/ExportDialog.tsx
export function ExportDialog({ page }: { page: Page }) {
  const [format, setFormat] = useState<'html' | 'markdown' | 'pdf' | 'json' | 'cursive'>('html');
  const [includeSessions, setIncludeSessions] = useState(false);
  
  const handleExport = async () => {
    const response = await fetch(`/api/export/page/${page.id}`, {
      method: 'POST',
      body: JSON.stringify({ format, includeSessions })
    });
    
    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = response.headers.get('Content-Disposition')?.split('filename=')[1] || 'export';
    a.click();
    
    toast.success('Exported successfully');
  };
  
  return (
    <Dialog>
      <DialogHeader>
        <DialogTitle>Export page</DialogTitle>
      </DialogHeader>
      
      <div className="space-y-4">
        <RadioGroup value={format} onValueChange={setFormat}>
          <RadioGroupItem value="html" label="HTML" description="For web publishing" />
          <RadioGroupItem value="markdown" label="Markdown" description="For plain text" />
          <RadioGroupItem value="pdf" label="PDF" description="For printing" />
          <RadioGroupItem value="json" label="JSON" description="For re-import" />
          <RadioGroupItem value="cursive" label=".cursive archive" description="With sessions" />
        </RadioGroup>
        
        {format === 'cursive' && (
          <label className="flex items-center gap-2">
            <Checkbox checked={includeSessions} onCheckedChange={setIncludeSessions} />
            <span className="text-sm">Include session recordings (for verification)</span>
          </label>
        )}
      </div>
      
      <DialogFooter>
        <Button onClick={handleExport}>
          <Download className="mr-2 h-4 w-4" />
          Export
        </Button>
      </DialogFooter>
    </Dialog>
  );
}
```

**Deliverable:** Users can download their pages in multiple formats

---

## Phase 5: Access Requests (Week 5)

**Goal:** Teachers can request walkthrough access, students approve

### 5.1 Request access flow
```tsx
// In VerificationDetailsModal, add button:
<Button variant="outline" onClick={handleRequestAccess}>
  <Eye className="mr-2 h-4 w-4" />
  Request walkthrough access
</Button>

// components/RequestAccessDialog.tsx
export function RequestAccessDialog({ pageId, ownerId }: Props) {
  const [message, setMessage] = useState('');
  
  const handleSend = async () => {
    await createAccessRequest({
      page_id: pageId,
      owner_id: ownerId,
      message
    });
    
    toast.success('Access requested. The owner will be notified.');
  };
  
  return (
    <Dialog>
      <DialogHeader>
        <DialogTitle>Request Access to Creation Timeline</DialogTitle>
      </DialogHeader>
      
      <div className="space-y-4">
        <p className="text-sm text-stone-600">
          You're asking to view the full creation timeline for this page.
          The owner will receive a notification and can approve or decline.
        </p>
        
        <div>
          <Label>Message (optional)</Label>
          <Textarea 
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Why are you requesting access?"
          />
        </div>
      </div>
      
      <DialogFooter>
        <Button variant="ghost">Cancel</Button>
        <Button onClick={handleSend}>Send request</Button>
      </DialogFooter>
    </Dialog>
  );
}
```

### 5.2 Student receives notification + approves
```tsx
// components/AccessRequestNotification.tsx
export function AccessRequestNotification({ request }: Props) {
  const handleRespond = async (status: 'approved' | 'declined') => {
    await respondToAccessRequest(request.id, status);
    toast.success(status === 'approved' ? 'Access granted' : 'Request declined');
  };
  
  return (
    <Card>
      <CardHeader>
        <CardTitle className="text-sm">Walkthrough Access Request</CardTitle>
      </CardHeader>
      <CardContent>
        <p className="text-sm mb-2">
          <strong>{request.requester_name}</strong> requested access to view your 
          walkthrough for <em>{request.page_title}</em>
        </p>
        
        {request.message && (
          <blockquote className="text-sm text-stone-600 border-l-2 pl-2 mb-3">
            {request.message}
          </blockquote>
        )}
        
        <Alert>
          <AlertDescription className="text-xs">
            This would show them: typing events, drawings, timestamps, and audio (if recorded).
          </AlertDescription>
        </Alert>
        
        <div className="flex gap-2 mt-4">
          <Button variant="outline" onClick={() => handleRespond('declined')}>
            Decline
          </Button>
          <Button onClick={() => handleRespond('approved')}>
            Approve
          </Button>
        </div>
      </CardContent>
    </Card>
  );
}
```

**Deliverable:** Teacher-student access request flow works

---

## Phase 6: Go Live (Week 6)

**Goal:** Real-time presentation with viewers

### 6.1 Go Live dialog
```tsx
// components/GoLiveDialog.tsx
export function GoLiveDialog({ pageId }: { pageId: string }) {
  const [title, setTitle] = useState('');
  const [isStarting, setIsStarting] = useState(false);
  
  const handleGoLive = async () => {
    setIsStarting(true);
    
    const session = await createLiveSession({
      page_id: pageId,
      title,
      session_type: 'live'
    });
    
    // Start broadcasting
    await startRealtimeBroadcast(session.id);
    
    const joinUrl = `/w/live/${session.id}`;
    
    toast.success('You're live!', {
      action: {
        label: 'Copy join link',
        onClick: () => copyToClipboard(joinUrl)
      }
    });
    
    // Update UI to show live indicator
    setIsLive(true);
  };
  
  return (
    <Dialog>
      <DialogHeader>
        <DialogTitle>Go live</DialogTitle>
      </DialogHeader>
      
      <div className="space-y-4">
        <div>
          <Label>Session title (optional)</Label>
          <Input 
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="e.g., Office Hours: Calculus Help"
          />
        </div>
        
        <Alert>
          <Mic className="h-4 w-4" />
          <AlertDescription>
            Live sessions include audio. Make sure your microphone is ready.
          </AlertDescription>
        </Alert>
      </div>
      
      <DialogFooter>
        <Button onClick={handleGoLive} disabled={isStarting}>
          {isStarting ? 'Starting...' : 'Go live'}
        </Button>
      </DialogFooter>
    </Dialog>
  );
}
```

### 6.2 Live indicator in header
```tsx
// When live, show badge in header
{isLive && (
  <div className="flex items-center gap-2 px-3 py-1.5 rounded-md bg-red-50 border border-red-200">
    <div className="h-2 w-2 rounded-full bg-red-500 animate-pulse" />
    <span className="text-xs font-medium text-red-700">Live</span>
    <span className="text-xs text-stone-600">{viewerCount} watching</span>
    
    <Button size="sm" variant="ghost" onClick={copyJoinLink}>
      Copy link
    </Button>
    
    <Button size="sm" variant="destructive" onClick={endLive}>
      End live
    </Button>
  </div>
)}
```

### 6.3 Realtime broadcast (Supabase)
```typescript
// hooks/useLiveBroadcast.ts
export function useLiveBroadcast(sessionId: string) {
  const supabase = useSupabase();
  
  useEffect(() => {
    const channel = supabase.channel(`live:${sessionId}`);
    
    channel
      .on('broadcast', { event: 'page-event' }, ({ payload }) => {
        // Apply event to viewer's page
        applyEvent(payload);
      })
      .subscribe();
    
    return () => {
      channel.unsubscribe();
    };
  }, [sessionId]);
  
  const broadcast = (event: PresentationEvent) => {
    supabase.channel(`live:${sessionId}`)
      .send({
        type: 'broadcast',
        event: 'page-event',
        payload: event
      });
  };
  
  return { broadcast };
}
```

**Deliverable:** Live sessions work with real-time viewing

---

## Quick Wins (Optional Enhancements)

### QW1: Preview before sharing
```tsx
// In SharePageDialog, add:
<Button variant="outline" onClick={openPreview}>
  <Eye className="mr-2 h-4 w-4" />
  Preview public view
</Button>
```

### QW2: Copy link toast
```tsx
// Better UX for copy actions
const copyToClipboard = (url: string) => {
  navigator.clipboard.writeText(url);
  toast.success('Link copied to clipboard', {
    description: url
  });
};
```

### QW3: Share analytics
```sql
-- Track views
CREATE TABLE share_views (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  resource_type TEXT NOT NULL,
  resource_id UUID NOT NULL,
  viewer_id UUID REFERENCES users(id),
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Show in Share dialog:
<div className="text-sm text-stone-600">
  👁️ {viewCount} views
</div>
```

### QW4: QR codes for sharing
```tsx
// In Share dialogs, add:
<Button variant="outline" onClick={generateQR}>
  <QrCode className="mr-2 h-4 w-4" />
  Show QR code
</Button>

// Generate QR code for easy mobile sharing
```

---

## Testing Checklist

### Phase 1
- [ ] Public page loads at `/p/[id]`
- [ ] Private pages return 404
- [ ] Share dialog updates visibility
- [ ] Copy link button works

### Phase 3
- [ ] Fingerprint calculates correctly
- [ ] Badge shows when confidence > 70
- [ ] Clicking badge opens modal
- [ ] Modal shows correct metrics

### Phase 4
- [ ] HTML export is valid
- [ ] .cursive archive is valid ZIP
- [ ] Sessions included when requested
- [ ] Can re-import exported files

### Phase 5
- [ ] Teacher can request access
- [ ] Student receives notification
- [ ] Approval grants access
- [ ] Decline doesn't grant access

### Phase 6
- [ ] Live session starts
- [ ] Events broadcast in real-time
- [ ] Viewers see updates <1s delay
- [ ] End live converts to replay

---

## Summary: What You're Building

1. ✅ **Share Page**: Clean URLs, visibility controls
2. ✅ **Share Walkthrough**: Replay with audio, live streaming
3. ✅ **Verification Badge**: Auto-shown, inspectable
4. ✅ **Export**: Multiple formats, full sovereignty
5. ✅ **Access Requests**: Privacy-preserving verification

**This architecture is simpler than presets because:**
- Fewer concepts (2 share types vs 4 presets)
- Clearer URLs (`/p/` and `/w/` vs `/share?token=`)
- Embedded verification (metadata vs separate view)
- Progressive disclosure (badge → modal → request)

**Start with Phase 1, ship weekly, iterate based on feedback.**
