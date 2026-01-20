---
name: brand-guidelines
description: Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply.
---

# Anthropic Brand Styling

## Overview

To access Anthropic's official brand identity and style resources, use this skill.

**Keywords**: branding, corporate identity, visual identity, post-processing, styling, brand colors, typography, Anthropic brand, visual formatting, visual design

## Brand Guidelines

Examples and sample files are in `examples/`. Use `.github/skills/brand-guidelines/examples/sample_brand.json` as a starting point for branding exports.

### Colors

**Main Colors:**

- Dark: `#141413` - Primary text and dark backgrounds
- Light: `#faf9f5` - Light backgrounds and text on dark
- Mid Gray: `#b0aea5` - Secondary elements
- Light Gray: `#e8e6dc` - Subtle backgrounds

**Accent Colors:**

- Orange: `#d97757` - Primary accent
- Blue: `#6a9bcc` - Secondary accent
- Green: `#788c5d` - Tertiary accent

### Typography

- **Headings**: Poppins (with Arial fallback)
- **Body Text**: Lora (with Georgia fallback)
- **Note**: Fonts should be pre-installed in your environment for best results

## Features

### Smart Font Application

- Applies Poppins font to headings (24pt and larger)
- Applies Lora font to body text
- Automatically falls back to Arial/Georgia if custom fonts unavailable
- Preserves readability across all systems

### Text Styling

- Headings (24pt+): Poppins font
- Body text: Lora font
- Smart color selection based on background
- Preserves text hierarchy and formatting

### Shape and Accent Colors

- Non-text shapes use accent colors
- Cycles through orange, blue, and green accents
- Maintains visual interest while staying on-brand

### Analytics & Conditional Formatting

You can define business rules to automatically highlight critical data points.

```json
"analytics": {
  "rules": [
    {
      "column_pattern": "p-value|significance",
      "condition": "lessThan",
      "value": 0.05,
      "style": { "bg_color": "c6efce", "font_color": "006100" }
    }
  ]
}
```

-   **column_pattern**: Regex to match column headers.
-   **condition**: `lessThan`, `greaterThan`, `equal`.
-   **value**: Numerical threshold.
-   **style**: `bg_color`, `font_color` (Hex without #).

### Automated Insights (Charts)

The skill automatically analyzes your data to generate branded charts on a new "Insights" sheet.

-   **X-Axis Detection**: Finds the first column with "Date", "Time", "ID", or "Batch" in the name.
-   **Chart Type**:
    -   **Line Chart**: If X-Axis is a Date/Time.
    -   **Bar Chart**: If X-Axis is a Category/ID.
-   **Styling**: Automatically uses the Primary/Secondary/Tertiary colors from your brand definition.
 
## Validation

You can verify that a brand definition file is valid and ready for use with other skills by running the included validator script.

```pwsh
python .github/skills/brand-guidelines/scripts/validate_brand.py .github/skills/brand-guidelines/examples/sample_brand.json
```

It checks for:
-   Valid JSON syntax
-   Required fields (`name`, `font`, `header_bg`, `header_font_color`)
-   Valid Hex color codes

## Technical Details

### Font Management

- Uses system-installed Poppins and Lora fonts when available
- Provides automatic fallback to Arial (headings) and Georgia (body)
- No font installation required - works with existing system fonts
- For best results, pre-install Poppins and Lora fonts in your environment

### Color Application

- Uses RGB color values for precise brand matching
- Applied via python-pptx's RGBColor class
- Maintains color fidelity across different systems
