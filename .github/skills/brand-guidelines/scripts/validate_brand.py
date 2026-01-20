"""Brand Validation Utility.
Checks if a brand JSON file adheres to the required schema.
Supports both Legacy (flat) and v2 (nested) schemas.
"""
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

# Legacy (v1) Fields
REQUIRED_FIELDS_V1 = ["name", "font", "header_bg", "header_font_color"]

# New (v2) Fields
REQUIRED_FIELDS_V2 = ["name", "fonts", "colors"]

def validate_hex(color: str) -> bool:
    """Check if string is a valid hex color code (e.g. #ffffff or ffffff)."""
    # Remove hash if present
    c = color.lstrip("#")
    # Check length (3 or 6) and characters
    return len(c) in (3, 6) and re.fullmatch(r"[0-9a-fA-F]+", c) is not None

def validate_brand(file_path: Path) -> bool:
    try:
        data: dict[str, Any] = json.loads(file_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Error: Could not parse JSON from {file_path}: {e}")
        return False

    valid = True
    
    # Detect Schema Version
    is_v2 = "fonts" in data and "colors" in data
    
    if is_v2:
        print(f"Info: Detected v2 (Advanced) schema for '{file_path.name}'")
        
        # Check v2 Requirements
        if "heading" not in data.get("fonts", {}):
            print("Error: Missing 'fonts.heading'")
            valid = False
        if "body" not in data.get("fonts", {}):
            print("Error: Missing 'fonts.body'")
            valid = False
            
        colors = data.get("colors", {})
        required_colors = ["primary", "background", "text"]
        for c in required_colors:
            if c not in colors:
                print(f"Error: Missing 'colors.{c}'")
                valid = False
        
        # Validate all hex values found in colors dict
        for k, v in colors.items():
            if isinstance(v, str) and not validate_hex(v):
                print(f"Error: Invalid hex color for 'colors.{k}': {v}")
                print(f"Error: Invalid hex color for 'colors.{k}': {v}")
                valid = False
        
        # Check Analytics (Optional)
        if "analytics" in data:
            rules = data.get("analytics", {}).get("rules", [])
            for idx, rule in enumerate(rules):
                if "column_pattern" not in rule:
                    print(f"Error: Missing 'column_pattern' in analytics rule index {idx}")
                    valid = False
                if "condition" not in rule:
                     print(f"Error: Missing 'condition' in analytics rule index {idx}")
                     valid = False
            if not rules:
                print("Info: 'analytics' section present but contains no rules.")
                
    else:
        print(f"Info: Detected Legacy (v1) schema for '{file_path.name}'")
        # Check v1 Requirements
        for field in REQUIRED_FIELDS_V1:
            if field not in data:
                print(f"Error: Missing required field '{field}'")
                valid = False
        
        # Validate colors if present
        for color_field in ["header_bg", "header_font_color"]:
            if color_field in data:
                val = data[color_field]
                if not isinstance(val, str) or not validate_hex(val):
                    print(f"Error: Invalid hex color for '{color_field}': {val}")
                    valid = False

    if valid:
        print(f"Success: '{file_path.name}' is a valid brand file.")
    else:
        print(f"Failure: '{file_path.name}' has errors.")
        
    return valid

def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a brand definition JSON file.")
    parser.add_argument("file", help="Path to the brand JSON file")
    args = parser.parse_args()

    p = Path(args.file)
    if not p.exists():
        print(f"Error: File not found: {p}")
        return 1

    success = validate_brand(p)
    return 0 if success else 1

if __name__ == "__main__":
    raise SystemExit(main())
