---
name: excel-generation
description: Generate .xlsx reports from JSON/CSV inputs using a local Python utility. Use this skill to convert structured data into Excel workbooks, add formatting, and produce multi-sheet reports.
---

# Excel generation skill

This skill provides instructions and a local script to generate Excel `.xlsx` files from JSON or CSV inputs.

When to use

- Converting API responses (JSON) to spreadsheets for analysis
- Generating templated reports from CSV or tabular data
- Producing multi-sheet exports for sharing

Usage

Run the included script locally in the workspace. Examples:

```pwsh
# from a JSON file
python ./excel_skill.py --input examples/data.json --output reports/report.xlsx

# from CSV
python ./excel_skill.py --input examples/data.csv --output reports/report.xlsx

# read JSON from stdin
cat examples/data.json | python ./excel_skill.py --input - --output reports/report.xlsx
```

**Re-branding an existing Excel file:**

If you provide an `.xlsx` file as input, the skill will switch to "Overhaul Mode". This applies the brand styles to *all sheets* in the workbook while preserving the data.

```pwsh
python ./excel_skill.py --input old_report.xlsx --output new_branded_report.xlsx --brand ../brand-guidelines/examples/sample_brand.json
```


Tip: You can run the script from the workspace root or directly from the skill directory. The `--brand` option accepts a path to a brand file (JSON/YAML) to apply brand styles when supported by the configured engine (prefer `openpyxl`).

Files in this skill

- `excel_skill.py` — Python utility that converts JSON/CSV to `.xlsx` using `pandas`.
- `examples/data.json` — small sample dataset to test the script.

Branding

- This skill integrates with the `brand-guidelines` skill to apply visual styling.
- Example brand files are stored in `.github/skills/brand-guidelines/examples/sample_brand.json`.
- Use the `--brand` / `-b` option to pass a brand file when running the script:

```pwsh
python ./excel_skill.py --input examples/data.json --output reports/report-branded.xlsx --brand ../brand-guidelines/examples/sample_brand.json
```

Note: the brand-guidelines skill contains recommended colors, fonts, and logos. Ensure images referenced by a brand file are committed to the repository or available at the stated path.

Security and privacy

This script runs locally and reads files from the workspace. Do not paste secrets or private data into prompts that may be sent to external services. Use the terminal auto-approval controls in VS Code to manage script execution.

Notes for integrators

- You can call the script from tasks or custom commands. Keep execution local to avoid exfiltration.
- For very large datasets, prefer streaming or chunked writes and an engine like `openpyxl` in write-only mode.
