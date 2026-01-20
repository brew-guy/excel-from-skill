# excel-from-skill

This repository demonstrates how to create Agent Skills for Excel generation and brand-aware exports.

Skills are stored under `.github/skills/` as subdirectories. Available skills in this repo:

- `.github/skills/excel-generation` — converts JSON/CSV to `.xlsx` using `pandas` and `openpyxl`. Supports a `--brand` argument to apply visual styling.
- `.github/skills/brand-guidelines` — brand definitions (colors, fonts, examples) used by other skills.

Quick start

```pwsh
# generate a simple report
python .github/skills/excel-generation/excel_skill.py --input .github/skills/excel-generation/examples/data.json --output reports/report.xlsx

# generate a branded report
python .github/skills/excel-generation/excel_skill.py --input .github/skills/excel-generation/examples/data.json --output reports/report-branded.xlsx --brand .github/skills/brand-guidelines/examples/sample_brand.json
```


## Using with AI Agents

This repository is designed to be consumed by AI agents. The workflow is:

1.  **Discovery**: The agent scans `.github/skills/` to find available capabilities.
2.  **Learning**: The agent reads `SKILL.md` in each subdirectory to understand inputs, outputs, and usage.
3.  **Execution**: The agent combines skills to solve the user request.
    -   *Example Request*: "Make a branded Excel report from this data."
    -   *Agent Action*: The agent uses `excel-generation` to create the file and `brand-guidelines` to apply the correct colors and fonts.
    -   *Command*: `python .github/skills/excel-generation/excel_skill.py ... --brand ...`

## Sample Prompts

To use these skills with an agent, you can use natural language requests. The agent will map your intent to the available skills.

**Basic Generation:**
> "Convert the file `.github/skills/excel-generation/examples/data.json` into an Excel spreadsheet."

**Branded Generation:**
> "Generate an Excel report from `.github/skills/excel-generation/examples/data.json` and apply the Anthropic brand styles."

**Custom Branding:**
> "Create an Excel sheet from `data.csv` using the brand guidelines in `my_brand.json`."


Guidelines

- Skills must live in `.github/skills/<skill-name>/` and include a `SKILL.md` file with YAML frontmatter (see VS Code docs).
- Keep skill resources (scripts, examples) inside the skill directory so they are portable and self-contained.

For developers: run `python scripts/validate_skills.py` to ensure each skill has `SKILL.md` and an `examples` folder.
