# Design System Documentation: Editorial Utility & Precision

## 1. Overview & Creative North Star
The Creative North Star for this design system is **"The Guided Canvas."** 

We are moving away from the "template" feel of standard Material Design and towards a high-end, editorial experience. This system focuses on the journey of the "Solution Challenge"—a path from problem to impact. Instead of rigid grids, we utilize **Intentional Asymmetry** and **Tonal Depth** to guide the user’s eye. The interface should feel like a premium workspace: authoritative, breathable, and surgically precise. We achieve this by prioritizing white space as a structural element and using the primary Google Blue not just as a color, but as a "signal" for progress and action.

## 2. Colors & Surface Architecture
Our palette is rooted in a sophisticated interpretation of the Google Blue (#1a73e8), expanded into a tonal range that allows for deep layering.

### The "No-Line" Rule
**Explicit Instruction:** Designers are prohibited from using 1px solid borders for sectioning. Structural boundaries must be defined solely through background color shifts.
- A card should never have an outline to separate it from the background. 
- Use `surface-container-lowest` (#ffffff) for active content cards sitting on a `surface` (#f9f9ff) or `surface-container-low` (#f2f3fd) background.

### Surface Hierarchy & Nesting
Treat the UI as a series of physical layers. Hierarchy is established by "stacking" the surface-container tiers:
1.  **Base Layer:** `surface` (#f9f9ff) - The global canvas.
2.  **Section Layer:** `surface-container-low` (#f2f3fd) - Used for grouping related content areas.
3.  **Active Component Layer:** `surface-container-lowest` (#ffffff) - Reserved for high-priority cards, inputs, and focal points.

### The "Glass & Gradient" Rule
To elevate the "standard" feel, use **Glassmorphism** for floating elements like the top navigation or modals.
- **Top Navbar:** Use `surface` at 80% opacity with a 20px `backdrop-blur`.
- **Signature Textures:** Apply a subtle linear gradient (45deg) from `primary` (#005bbf) to `primary_container` (#1a73e8) for main CTAs. This adds a "jewel" effect that flat colors lack.

## 3. Typography
We utilize **Inter** for its neutral, modernist clarity, but we apply editorial scales to create hierarchy.

- **Display Scale:** Use `display-lg` (3.5rem) sparingly for high-impact metrics (e.g., "75% Complete"). Reduce letter-spacing to -0.02em for a "tight" editorial look.
- **Headline Scale:** `headline-sm` (1.5rem) should be used for section titles, paired with generous top-margin (48px+) to allow the content to breathe.
- **Body Scale:** `body-lg` (1rem) is the workhorse. Ensure a line-height of at least 1.6 to maintain readability during long documentation entries.
- **Labels:** `label-md` (0.75rem) must be in All Caps with +0.05em tracking when used for metadata or categories to distinguish them from body text.

## 4. Elevation & Depth
Depth is achieved through **Tonal Layering** rather than traditional structural lines.

- **The Layering Principle:** Place a `surface-container-lowest` card on a `surface-container-low` background. This creates a "soft lift" that feels natural and premium.
- **Ambient Shadows:** When a component must float (e.g., a "New Participation" FAB), use an extra-diffused shadow: `box-shadow: 0 12px 32px rgba(25, 28, 35, 0.06);`. The shadow color is a tinted version of `on-surface`, never pure black.
- **The "Ghost Border" Fallback:** If a border is required for accessibility, use the `outline-variant` token at **15% opacity**. This provides a hint of a container without breaking the editorial flow.

## 5. Components

### Navigation
- **Top Navbar:** Minimalist. No heavy backgrounds. Use a simple `title-md` for the logo and `label-md` for nav items. Active states are indicated by a 4px primary-colored dot below the text, rather than a background pill.

### Buttons
- **Primary:** Gradient fill (Primary to Primary Container), `DEFAULT` (8px) corners. High-contrast `on-primary` text.
- **Secondary:** `surface-container-high` background with `primary` text. No border.
- **Tertiary:** Text-only, but with an increased font-weight (`title-sm`) to ensure importance.

### Participation Cards
- **Construction:** No dividers. Use `body-sm` in `on-surface-variant` for metadata. 
- **Interaction:** On hover, transition the background from `surface-container-lowest` to a subtle gradient or increase the ambient shadow blur.

### Input Fields
- **Style:** Use "Filled" style with `surface-container-highest` backgrounds. 
- **Focus State:** Transition the background to `surface-container-lowest` and add a 2px `primary` bottom-border. Do not use a 4-sided stroke.

### Progress Trackers (Context Specific)
- Use a thick (8px) track in `surface-container-highest` with a rounded `primary` fill. Pair with `display-sm` for the percentage to emphasize achievement.

## 6. Do's and Don'ts

### Do
- **Do** use whitespace as a separator. If you feel the need for a line, try adding 16px of extra padding instead.
- **Do** use "Optical Centering." Sometimes a button looks better slightly off-grid if it balances a heavy headline.
- **Do** use `tertiary` (#9e4300) for "Attention" items like deadlines—it provides a sophisticated warmth compared to standard error reds.

### Don't
- **Don't** use 100% opaque borders. They create "visual noise" that cheapens the experience.
- **Don't** use standard Material shadows (dp1, dp2). Stick to the Ambient Shadow spec defined in Section 4.
- **Don't** crowd the corners. With an 8px (`DEFAULT`) radius, ensure your internal padding is at least 16px or 24px to prevent "content-cramping."