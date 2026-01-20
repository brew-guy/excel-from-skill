---
name: brand-guidelines
description: Expertise in Roche corporate branding guidelines including colors, typography, and logo usage. Use it when brand colors or style guidelines, visual formatting, or company design standards apply.
---

# Roche Brand Guidelines

## Overview

This skill provides detailed information about Roche's corporate branding, covering colors, typography, and usage principles.

**Keywords**: branding, corporate identity, visual identity, post-processing, styling, brand colors, typography, Roche brand, visual formatting, visual design

## Brand Guidelines

Examples and sample files are in `examples/`. Use `.github/skills/brand-guidelines/examples/sample_brand.json` as a starting point for branding exports.

### 1. Colors

Roche's color palette is designed to be vibrant and emotional, anchored by Roche Blue.

#### Primary Colors

These are the core brand colors.
| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Roche Blue** | `#0B41CD` | `rgb(11, 65, 205)` | Primary brand color, logo, buttons, links, active states. |
| **Dark Blue** | `#022366` | `rgb(2, 35, 102)` | Hover states, deep accents. |
| **Light Blue** | `#1482FA` | `rgb(20, 130, 250)` | Highlights, lighter accents. |

#### Base Colors (Neutrals)

Used for backgrounds and text to provide warmth and space.
| Name | Hex | Usage |
|------|-----|-------|
| **White** | `#FFFFFF` | Main background, text on dark backgrounds. |
| **Light Grey** | `#F8F8F8` | Secondary backgrounds, hover states. |
| **Dark Grey** | `#544F4F` | Image captions, secondary text. |
| **Black** | `#000000` | Main text (often used with opacity/lightness adjustments). |

#### Accent Colors

Used sparingly for functional feedback or emphasis.
| Name | RGB | Usage |
|------|-----|-------|
| **Info** | `rgb(194, 186, 181)` | Informational messages. |
| **Tip/Success** | `rgb(0, 122, 59)` | Success messages, positive indicators. |
| **Warning/Error** | `rgb(214, 0, 7)` | Error messages, alerts. |
| **Note** | `rgb(250, 201, 181)` | Notes, highlights. |

### 2. Typography

The typographic system relies on the **Roche Sans** family for most applications, ensuring a clean and modern look. **Roche Serif** is used selectively for quotes or specific emphasis.

#### Font Families

- **Primary**: `Roche Sans` (Weights: Light 300, Regular 400, Bold 700)
- **Secondary**: `Roche Serif` (Weights: Light 300, Regular 400, Bold 700)
- **Condensed**: `Roche Sans Condensed` (Used for specific tight layouts)

#### Type Hierarchy

| Element       | Font family        | Size | Weight        | Line Height |
| ------------- | ------------------ | ---- | ------------- | ----------- |
| **Heading 1** | Roche Sans         | 48px | 300 (Light)   | 1.3         |
| **Heading 2** | Roche Sans         | 40px | 300 (Light)   | 1.3         |
| **Heading 3** | Roche Sans         | 30px | 300 (Light)   | 1.3         |
| **Heading 4** | Roche Sans         | 24px | 300 (Light)   | 1.3         |
| **Body Text** | Roche Sans         | 18px | 300 (Light)   | 1.4         |
| **Buttons**   | Roche Sans         | 16px | 400 (Regular) | 1.3         |
| **Captions**  | Roche Sans         | 16px | 400 (Regular) | 1.5         |
| **Quotes**    | Roche Serif Italic | 16px | 400 (Regular) | 1.3         |

### 3. Usage Guidelines

#### Buttons

- **Primary Button**: Roche Blue (`#0B41CD`) background with White text. Square corners (0px border-radius).
- **Secondary Button**: White background with Roche Blue border (`#0B41CD`) and text.
- **Hover States**:
  - Primary: Dark Blue (`#022366`).
  - Secondary: Light grey background or Dark Blue text/border depending on context.

#### Logo

- The Roche logo visualizes the vibrant warm blue.
- Always maintain clear space around the logo.
- Do not alter the logo colors.

## Features

### Smart Font Application

- Applies **Roche Sans** font to headings (24pt and larger)
- Applies **Roche Sans** font to body text
- Applies **Roche Serif** to quotes/special emphasis where appropriate
- Automatically falls back to system defaults if custom fonts unavailable

### Text Styling

- Headings (24pt+): Roche Sans
- Body text: Roche Sans
- Smart color selection based on background (Uses Roche Blue/Black/White)
- Preserves text hierarchy and formatting

### Shape and Accent Colors

- Non-text shapes use Roche accent colors
- Cycles through **Roche Blue**, **Light Blue**, and functional accents
- Maintains visual interest while staying on-brand

### Analytics & Conditional Formatting

You can define business rules to automatically highlight critical data points using Roche accent colors.

```json
"analytics": {
  "rules": [
    {
      "column_pattern": "p-value|significance",
      "condition": "lessThan",
      "value": 0.05,
      "style": { "bg_color": "c2bab5", "font_color": "007a3b" } 
    }
  ]
}
```

### Automated Insights (Charts)

The skill automatically analyzes your data to generate branded charts on a new "Insights" sheet.

-   **Styling**: Automatically uses **Roche Blue**, **Dark Blue**, and **Light Blue** from your brand definition.
 
## Validation

You can verify that a brand definition file is valid and ready for use with other skills by running the included validator script.

```pwsh
python .github/skills/brand-guidelines/scripts/validate_brand.py .github/skills/brand-guidelines/examples/sample_brand.json
```

## Technical Details

### Font Management

-   Uses `Roche Sans` and `Roche Serif` fonts when available.
-   Provides automatic fallback to Arial/Helvetica (headings) and Arial (body).
-   **Note**: For best results, ensure Roche fonts are installed in your environment.

### Color Application

-   Uses RGB color values for precise brand matching (e.g., Roche Blue `0B41CD`).
-   Applied via available libraries (python-pptx/openpyxl).
-   Maintains color fidelity across different systems.

### CSS Variables Reference

```css
:root {
  /* Colors */
  --roche-blue: #0b41cd;
  --roche-dark-blue: #022366;
  --roche-light-blue: #1482fa;
  --roche-white: #ffffff;
  --roche-text-main: #000000;
  --roche-text-secondary: #544f4f;

  /* Accents */
  --roche-success: rgb(0, 122, 59);
  --roche-error: rgb(214, 0, 7);

  /* Fonts */
  --font-family-sans: "Roche Sans", sans-serif;
  --font-family-serif: "Roche Serif", serif;
}
```
