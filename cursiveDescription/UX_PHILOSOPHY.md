# Canvas UX Philosophy: The Tool Interface

## Core Principle: "Ambient Intelligence"
The interface should feel like having a thoughtful colleague looking over your shoulder - present when needed, invisible when not, always respectful of your flow.

## Visual Language: The Tool System

### 1. Attention Halos (Not Boxes)
Instead of harsh rectangles, use subtle radial gradients that "breathe":

```typescript
interface AttentionHalo {
  center: Point;           // Where user's attention is
  radius: number;          // Size of focus area
  intensity: number;       // 0-1, fades over time
  type: 'thinking' | 'question' | 'insight' | 'connection';
}
```

**Visual Implementation:**
- Soft radial gradients with 5-15% opacity
- Gentle pulsing animation (2-3 second cycle)
- Colors that complement, not compete:
  - Thinking: Soft blue (#E3F2FD at 10%)
  - Question: Warm amber (#FFF3E0 at 12%)
  - Insight: Light green (#F1F8E9 at 10%)
  - Connection: Soft purple (#F3E5F5 at 8%)

### 2. Focus Ripples
When user double-clicks, create expanding ripples that:
- Start from click point
- Fade as they expand
- "Discover" content as they travel
- Stop at content boundaries

```typescript
interface FocusRipple {
  origin: Point;          // Where user clicked
  currentRadius: number;  // Expanding from 0
  discovered: ContentRegion[];  // What we've found
  fadeStartRadius: number;      // When to start fading
}
```

### 3. Semantic Anchors
Small, subtle indicators at content "centers of mass":

```typescript
interface SemanticAnchor {
  position: Point;
  type: 'text' | 'drawing' | 'diagram' | 'thought';
  weight: number;  // Importance/density
  label?: string;  // Optional micro-label
}
```

Visual: Tiny dots (2-3px) that appear on hover/focus, with micro-labels on extended hover.

## Interaction Model: Focus + Context

### The Click Location Matters
When user double-clicks, that point becomes the "focus center":

```typescript
interface FocusContext {
  center: Point;          // Where user clicked
  primary: Region;        // 200px radius - detailed analysis
  secondary: Region;      // 400px radius - context awareness
  peripheral: Region;     // 800px radius - relationship detection
}
```

**Analysis Strategy:**
1. **Primary Zone**: Full Sonnet analysis with OCR
2. **Secondary Zone**: Haiku quick scan for context
3. **Peripheral Zone**: Just detect presence/type

This creates natural "depth of field" - sharp focus where user is looking, softer awareness of surroundings.

## Canvas Model: Infinite with Landmarks

### Why Infinite Canvas Wins:
1. **Spatial Memory**: Humans remember WHERE things are
2. **Organic Growth**: Ideas expand naturally
3. **Relationship Mapping**: Connections aren't confined to pages
4. **Flow State**: No interruption to create new pages

### But With Smart Constraints:

#### 1. Viewport Anchoring
```typescript
interface Viewport {
  center: Point;
  zoom: number;
  anchor?: ContentRegion;  // Optional content to keep in view
}
```

#### 2. Semantic Regions (Not Pages)
Self-organizing regions based on content density:

```typescript
interface SemanticRegion {
  id: string;
  bounds: BoundingBox;
  title?: string;         // Auto-generated or user-defined
  density: number;        // How much content
  lastActive: Date;       // For cleanup/archiving
  bookmark?: boolean;     // User can bookmark regions
}
```

#### 3. Smart Navigation
- **Minimap**: Ultra-subtle, appears on scroll
- **Bookmarks**: Save specific views
- **Trails**: Show path through canvas over time
- **Portals**: Link between distant regions

### Performance Strategy for Infinite Canvas:

```typescript
interface CanvasLOD {  // Level of Detail
  viewport: BoundingBox;
  visible: Node[];           // Full detail
  simplified: Node[];        // Reduced detail (1 tile away)
  markers: SemanticAnchor[]; // Just anchors (2+ tiles away)
}
```

## The Tool Feedback System

### 1. Hover Intelligence
When hovering over content (after 500ms):
- Soft glow (5% opacity)
- Micro-summary appears (if available)
- Related content subtly brightens

### 2. Drawing Feedback
While drawing:
- Faint "wake" trails that fade after 2 seconds
- Pressure visualization through subtle width variation
- No harsh colors - all within a muted palette

### 3. AI Presence
Instead of popup boxes:
- Soft annotation layers that fade in
- Inline text that appears near content
- Gentle connecting lines between related items

## Implementation Approach

### Phase 1: Focus-Aware Analysis
```typescript
async function analyzeWithFocus(
  clickPoint: Point,
  canvas: CanvasData
): Promise<FocusedAnalysis> {
  // Create focus zones
  const zones = createConcentricZones(clickPoint);
  
  // Analyze based on distance from click
  const primaryAnalysis = await analyzePrimary(zones.primary);
  const context = await analyzeContext(zones.secondary);
  const connections = findConnections(zones.peripheral);
  
  return {
    focus: primaryAnalysis,
    context,
    connections,
    suggestion: generateInsight(primaryAnalysis, context)
  };
}
```

### Phase 2: Tool Visuals
```typescript
interface ToolLayer {
  halos: AttentionHalo[];
  anchors: SemanticAnchor[];
  connections: Connection[];
  
  render(): ReactElement {
    return (
      <Layer opacity={0.8} listening={false}>
        {halos.map(h => <RadialGradient {...h} />)}
        {anchors.map(a => <SemanticDot {...a} />)}
        {connections.map(c => <SubtlePath {...c} />)}
      </Layer>
    );
  }
}
```

### Phase 3: Infinite Canvas with LOD
```typescript
class InfiniteCanvas {
  private quadTree: QuadTree<Node>;  // Spatial indexing
  private viewportCache: Map<string, CanvasLOD>;
  
  getVisibleContent(viewport: BoundingBox): CanvasLOD {
    const key = getViewportKey(viewport);
    
    if (this.viewportCache.has(key)) {
      return this.viewportCache.get(key)!;
    }
    
    const lod = {
      visible: this.quadTree.query(viewport),
      simplified: this.quadTree.query(expandBox(viewport, 1.5)),
      markers: this.quadTree.query(expandBox(viewport, 3))
        .map(n => toAnchor(n))
    };
    
    this.viewportCache.set(key, lod);
    return lod;
  }
}
```

## Design Decisions

### ✅ Infinite Canvas (Not Pages)
**Why:** 
- Preserves spatial memory
- Allows organic growth
- Better for relationship mapping
- No context switching

**How we handle concerns:**
- Performance: LOD + viewport caching
- Organization: Semantic regions + bookmarks
- Sharing: Can share viewport links or regions
- Overwhelm: Focus zones + progressive disclosure

### ✅ Click Location Awareness
**Why:**
- Shows user intent
- Enables focused analysis
- Creates natural depth of field
- Reduces cognitive load

**Implementation:**
- Concentric analysis zones
- Weighted by distance from click
- Progressive detail reduction

### ✅ Tool Interface (Not Clutter)
**Why:**
- Maintains flow state
- Reduces visual noise
- Respects user's content
- Feels intelligent, not intrusive

**Key Elements:**
- 5-15% opacity maximum
- Fade/breathe animations
- Complementary colors only
- Appears on demand, fades automatically

## Summary

The interface should feel like **thinking with a subtle companion** - never shouting, always tooling, occasionally offering a gentle insight. The infinite canvas provides **spatial freedom**, while smart focus and LOD ensure **performance**. Every visual element should **earn its pixels** by providing value without breaking concentration.

**The goal:** Make the user feel like they're thinking with superpowers, not fighting with software.