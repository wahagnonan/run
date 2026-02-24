---
page: events
---
La page Événements de Poro Run — programme complet du festival avec un calendrier détaillé des activités sportives et culturelles.

**DESIGN SYSTEM (REQUIRED):**
- Platform: Web, Mobile-first responsive
- Theme: Dark, festive, vibrant — deep night carnival energy
- Background: Cosmic Midnight Navy (#0a0a23) with radial orange/pink/violet atmospheric glows
- Primary Accent: Molten Festival Orange (#ff7d00) for timeline nodes and headings
- Secondary Accent: Hot Carnival Pink (#ff4da6) for time labels and gradient accents
- Tertiary Accent: Electric Dream Violet (#7b4cff) for section dividers and icon accents
- Text Primary: Frosted White (#ffffff) on all dark surfaces
- Text Secondary: Whisper Gray (#6b7280) for activity descriptions
- Card Surfaces: Glass-dark (rgba(255,255,255,0.04)) for schedule cards
- Typography: Poppins (Bold 700 headings, SemiBold 600 time labels, Regular 400 descriptions)
- Buttons: 6px rounded, orange-pink gradient for CTA
- Layout: Vertical timeline on desktop, full-width stacked on mobile

**Page Structure:**
1. **Page Header:** Bold heading "Programme du Festival" + sub-label with event date (12 Décembre 2025) and hours (08:00 — 22:00)
2. **Hero Event Banner:** Full-width festive banner with the Poro Run logo, date badge (orange pill), and location badge
3. **Vertical Timeline / Schedule:** Chronological list of activities from 08:00 to 22:00 — each item is a glass card showing: time (pink, bold), activity emoji/icon, activity name (white, bold), short description (gray)
4. **Activity Highlights Grid:** 3 featured activities in card format — Ambiance & Danse · Course Sportive · Rencontres & Fun — each with icon, title, and short description
5. **CTA Section:** Centered "Participez !" heading + "Acheter un kit" orange gradient button
6. **Location Reminder:** Compact map embed or Google Maps link button with address
7. **Footer:** Standard global footer

---
💡 **Tip:** Update this prompt with real schedule data from the `Activite` Django model once the edition is set.
