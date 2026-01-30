#!/usr/bin/env python3
import os
import re
import sys

# Define valid impact levels
VALID_IMPACTS = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]

def lint_rule_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    errors = []
    filename = os.path.basename(file_path)

    # 1. Check Metadata Table
    if "| Metadata | Value |" not in content:
        errors.append("Missing Metadata Table header")
    else:
        # Check Title
        if not re.search(r"\| Title \| .+ \|", content):
            errors.append("Missing 'Title' in Metadata")
        
        # Check Impact
        impact_match = re.search(r"\| Impact \| \*\*(.+)\*\* \|", content)
        if not impact_match:
             # Try without bold
            impact_match = re.search(r"\| Impact \| (.+) \|", content)
            
        if impact_match:
            impact = impact_match.group(1).strip()
            if impact not in VALID_IMPACTS:
                 errors.append(f"Invalid Impact level: '{impact}'. Must be one of {VALID_IMPACTS}")
        else:
            errors.append("Missing 'Impact' in Metadata")

    # 2. Check Rationale
    if "## Rationale" not in content:
        errors.append("Missing '## Rationale' section")

    # 3. Check Patterns Section
    if "## Patterns" not in content:
        errors.append("Missing '## Patterns' section")

    # 4. Check Incorrect/Correct Examples
    # Flexible matching for headers
    if not re.search(r"### .*Incorrect", content, re.IGNORECASE) and not re.search(r"### .*❌", content):
        errors.append("Missing 'Incorrect' or '❌' example section")
    
    if not re.search(r"### .*Correct", content, re.IGNORECASE) and not re.search(r"### .*✅", content):
        errors.append("Missing 'Correct' or '✅' example section")

    return errors

def main():
    skills_dir = "skills"
    total_files = 0
    total_errors = 0
    
    print("🔍 Starting Super Skills 5.0 Rule Linter...\n")

    for skill in sorted(os.listdir(skills_dir)):
        skill_path = os.path.join(skills_dir, skill)
        rules_dir = os.path.join(skill_path, "rules")
        
        if os.path.isdir(rules_dir):
            for rule_file in sorted(os.listdir(rules_dir)):
                if rule_file.endswith(".md") and not rule_file.startswith("_"):
                    total_files += 1
                    full_path = os.path.join(rules_dir, rule_file)
                    errors = lint_rule_file(full_path)
                    
                    if errors:
                        total_errors += 1
                        print(f"❌ {skill}/{rule_file}:")
                        for err in errors:
                            print(f"  - {err}")
                    else:
                        print(f"✅ {skill}/{rule_file}")

    print(f"\nSummary: Scanned {total_files} rules.")
    if total_errors > 0:
        print(f"⚠️  Found issues in {total_errors} files.")
        sys.exit(1)
    else:
        print("🎉 All rules passed strict 5.0 validation!")
        sys.exit(0)

if __name__ == "__main__":
    main()
