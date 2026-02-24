# Design System: Poro Run

**Project:** Poro Run — Sporting & Cultural Festival, Korhogo, Côte d'Ivoire  
**Tech Stack:** Django 6.0.1 · Vanilla CSS · Poppins font

---

## 1. Visual Theme & Atmosphere

**Vibe:** Electrifying, Festive, Nocturnal.

Poro Run lives in the dark. The UI is set against a near-black midnight navy background — not a harsh jet black, but a deep cosmic blue-black that gives depth and warmth. Layered on top of this darkness are **three radiant orbs of color**: a warm molten orange blooms from the top-left, a hot-pink neon explodes from the bottom-right, and a dreamy electric violet glows at the center. Together they create a subtle bioluminescent festival atmosphere reminiscent of neon lights at a night street carnival.

The design is **bold and direct** — large, heavy headings announce the brand, while colorful gradient accents on CTAs and social icons inject vibrancy. The overall density is **open but purposeful**, with generous section spacing and a clear visual hierarchy.

This is a design system made to feel like the night-time energy of an African street festival: joyful, vibrant, memorable.

---

## 2. Color Palette & Roles

| Descriptive Name | Hex | Functional Role |
|---|---|---|
| **Cosmic Midnight Navy** | `#0a0a23` | Primary page background — the "night sky" canvas |
| **Deep Dusk Blue** | `#07102a` | Navbar gradient end, footer background — slightly lighter midnight |
| **Molten Festival Orange** | `#ff7d00` | Primary accent — CTA buttons, nav links hover, brand energy |
| **Hot Carnival Pink** | `#ff4da6` | Secondary accent — gradient buttons, footer links, social icons |
| **Electric Dream Violet** | `#7b4cff` | Tertiary accent — gradient blends, atmospheric glow, social icons |
| **Frosted White** | `#ffffff` / `rgba(255,255,255,0.95)` | Primary text on dark backgrounds |
| **Whisper Gray** | `#6b7280` | Secondary/muted text — subtitles, less prominent copy |
| **Glass Card** | `rgba(255,255,255,0.04)` | Card/container background — barely-there frosted glass feel |

**Gradient patterns:**
- **Primary gradient:** `linear-gradient(90deg, #ff7d00, #ff4da6)` — used for CTA buttons & inscription button
- **Social icon gradient:** `linear-gradient(135deg, #ff4da6, #7b4cff)` — pink-to-violet sweep for social links
- **Atmospheric blobs:** Radial gradients of orange, pink, and violet at low opacity create depth on `body` and `body::before`

---

## 3. Typography Rules

**Font Family:** [Poppins](https://fonts.google.com/specimen/Poppins) (Google Fonts), with Arial and system sans-serif as fallback.

| Role | Weight | Notes |
|---|---|---|
| **Brand logo / Main H1** | Bold 700 | Large, uppercase, wide letter-spacing (1px) |
| **Section headings (H2)** | SemiBold 600 | Clear visual hierarchy markers |
| **Sub-headings (H3)** | SemiBold 600 | Cards and feature titles |
| **Body copy / Paragraphs** | Regular 400 | 15–16px, comfortable reading size |
| **Nav links** | Regular 400 | 16px, transitions to orange on hover |
| **Footer small text** | Regular 400 | ~15px, near-full white opacity |

**Character:** Poppins is geometric and modern with rounded letterforms that feel friendly yet professional — perfectly matching the event's festive-but-legitimate identity.

---

## 4. Component Stylings

### Buttons
- **Primary CTA (`.btn-primary`, `.btn-kit`):** Warm orange-to-pink gradient (`#ff7d00 → #ff4da6`), subtly rounded corners (6px) sharp enough to feel intentional. White text. Smooth 0.5s hover transition.
- **Purchase/Action buttons (`.btn-buy`, `.bouton`):** Solid accent color fill, slightly rounded edges. Used for transactional actions.
- **Inscription button (`.btn-inscription`):** Same orange-to-pink gradient as primary CTA. 10px/20px padding. Rounded 6px corners.

### Cards / Containers
- **Kit product cards (`.box`):** Semi-transparent glass background (`rgba(255,255,255,0.04)`), gently rounded corners (~12px implied by context). Subtle elevation through contrast with background.
- **Sponsor cards (`.sponsor-card`):** Transparent/glass container, contains centered logo and sponsor name.
- **Map container:** Generously rounded corners (12px), heavy shadow `0 10px 30px rgba(3,8,20,0.5)` to feel elevated from the dark background.

### Navigation Bar
- **Default state:** Full-width, dark gradient background (`#0a0a23 → #07102a`), sticky/fixed at top (`z-index: 100`).
- **Scrolled state (`.navbar.transparent`):** Semi-transparent deep blue with backdrop blur — still readable, feels more open.
- **Logo:** Bold 700, 22px, 1px letter-spacing, white.

### Social Icons
- **Pill-shaped circular buttons** (40×40px, `border-radius: 50%`) with pink-to-violet gradient fill. Hover state: lifts 4px with increased shadow.

### Inputs / Forms
- Functional, minimal styling. Input fields for quantity (`zone_text`) are small, centered.

---

## 5. Layout Principles

**Grid Philosophy:** Flexbox-first, responsive by reduction.

- **Navbar:** Space-between flex row, sticky top.
- **Hero section:** Two-column flex row — text left (55%), image carousel right (45%) on desktop. Collapses to full-width stacked column on mobile (≤600px).
- **Activity cards (`.atouts`):** 3-column horizontal flex with `flex-wrap`, gaps of ~16–20px. Stacks to 1 column on mobile.
- **Kit section (`.foot-kit`):** Row with image carousel left and CTA button right. Stacks vertically on mobile.
- **Sponsors grid (`.sponsors-grid`):** Auto-fill grid.
- **Footer:** 3-column flex (`space-between`) — Contact left, Copyright center, Social right. Collapses to centered stack on tablet (≤800px).

**Whitespace Strategy:** Sections separated by generous vertical padding (28–40px) and `margin-top`. The dark background makes white space feel like cosmological depth rather than emptiness.

**Max Widths:** Key containers use `max-width: 1000–1200px` with `margin: auto` to center on wide screens.

---

## 6. Stitch Design System Block (for prompt injection)

> Copy this block into any new Stitch prompt to maintain design consistency:

```
**DESIGN SYSTEM (REQUIRED):**
- Platform: Web, Mobile-first responsive
- Theme: Dark, festive, vibrant — deep night carnival energy
- Background: Cosmic Midnight Navy (#0a0a23) with radial orange/pink/violet atmospheric glows
- Primary Accent: Molten Festival Orange (#ff7d00) for primary buttons and hover states
- Secondary Accent: Hot Carnival Pink (#ff4da6) for gradients, links, icon fills
- Tertiary Accent: Electric Dream Violet (#7b4cff) for gradient blends and icon accents
- Text Primary: Frosted White (#ffffff / rgba 95%) on dark backgrounds
- Text Secondary: Whisper Gray (#6b7280) for subtitles and muted copy
- Card Surfaces: Glass-dark (rgba(255,255,255,0.04)) — barely-there frosted panels
- Typography: Poppins (Bold 700 for headings, SemiBold 600 for subheadings, Regular 400 for body)
- Buttons: Subtly rounded (6px), orange-to-pink gradient for primary CTAs, white text
- Social Icons: Circular (40px), pink-to-violet gradient fill, hover lifts 4px
- Navbar: Sticky, dark gradient, transitions to blur-transparent on scroll
- Layout: Flexbox-first, 2-col desktop hero, stacks to 1-col mobile
```
