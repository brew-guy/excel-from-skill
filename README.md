# Excel Generation Assistant

Welcome! This repository contains tools that allow you to create professional Excel reports from your data files. It is designed to be used with an AI Assistant, allowing you to create and style spreadsheets using simple, natural language.

## How to use

You don't need to write code. Just ask the AI to help you with your data.

**To create a basic spreadsheet:**
> "Convert the file `.github/skills/excel-generation/examples/data.json` into an Excel spreadsheet."

**To apply your brand colors and styles:**
> "Generate an Excel report from `.github/skills/excel-generation/examples/data.json` and apply the Anthropic brand styles."

**To use a specific brand file:**
> "Create an Excel sheet from `data.csv` using the brand guidelines in `my_brand.json`."

---

## Technical Documentation & Developer Guide

The following section is intended for developers or users who want to understand the inner workings or run the tools manually.

### Overview

This repository demonstrates how to create Agent Skills for Excel generation and brand-aware exports.
Skills are stored under `.github/skills/` as subdirectories.

**Available skills:**
- `.github/skills/excel-generation` — converts JSON/CSV to `.xlsx` using `pandas` and `openpyxl`. Supports a `--brand` argument to apply visual styling.
- `.github/skills/brand-guidelines` — brand definitions (colors, fonts, examples) used by other skills.

### Using with AI Agents (Workflow)

1.  **Discovery**: The agent scans `.github/skills/` to find available capabilities.
2.  **Learning**: The agent reads `SKILL.md` in each subdirectory to understand inputs, outputs, and usage.
3.  **Execution**: The agent combines skills to solve the user request.
    -   *Example Request*: "Make a branded Excel report from this data."
    -   *Agent Action*: The agent uses `excel-generation` to create the file and `brand-guidelines` to apply the correct colors and fonts.
    -   *Command*: `python .github/skills/excel-generation/excel_skill.py ... --brand ...`

### Manual Quick Start

```pwsh
# generate a simple report
python .github/skills/excel-generation/excel_skill.py --input .github/skills/excel-generation/examples/data.json --output reports/report.xlsx

# generate a branded report
python .github/skills/excel-generation/excel_skill.py --input .github/skills/excel-generation/examples/data.json --output reports/report-branded.xlsx --brand .github/skills/brand-guidelines/examples/sample_brand.json
```

### Developer Guidelines

- Skills must live in `.github/skills/<skill-name>/` and include a `SKILL.md` file with YAML frontmatter (see VS Code docs).
- Keep skill resources (scripts, examples) inside the skill directory so they are portable and self-contained.
- For developers: run `python scripts/validate_skills.py` to ensure each skill has `SKILL.md` and an `examples` folder.
