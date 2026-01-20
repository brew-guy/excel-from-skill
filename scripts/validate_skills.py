"""Simple validator to check `.github/skills` structure."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
skills_dir = root / ".github" / "skills"

errors = []
if not skills_dir.exists():
    errors.append("No .github/skills directory found")
else:
    for child in skills_dir.iterdir():
        if not child.is_dir():
            continue
        skill_md = child / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"Skill {child.name} is missing SKILL.md")
        examples = child / "examples"
        if not examples.exists():
            errors.append(f"Skill {child.name} is missing examples/ directory")

if errors:
    print("Validation failed:")
    for e in errors:
        print(" - ", e)
    raise SystemExit(1)

print("All skills look sane.")
