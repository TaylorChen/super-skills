#!/usr/bin/env python3
import sys
import re
import os

def check_prd(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"--- [Super Skills 4.0] PRD Checker Result for: {os.path.basename(file_path)} ---")
    
    # 基础结构检查
    structure_checks = {
        "1. Background & Goals": r"#+.*(背景|目标|Background|Goals)",
        "2. User Analysis/Persona": r"#+.*(用户|人群|User|Persona)",
        "3. Functional Requirements": r"#+.*(功能|需求|Functional|Requirements)",
        "4. Acceptance Criteria (AC)": r"#+.*(验收|AC|Acceptance Criteria)",
        "5. Priority (P0/P1)": r"(P0|P1|P2|优先级|Priority)",
    }

    # 4.0 深度规则检查 (Procedural Rules)
    rule_checks = {
        "[us-001] User Story Format": r"(AS A|作为|I WANT TO|我想要|SO THAT|以便于)",
        "[us-002] BDD Specification": r"(Given|When|Then|前提|操作|结果)",
    }

    passed_struct = 0
    for label, pattern in structure_checks.items():
        if re.search(pattern, content, re.IGNORECASE):
            print(f"✅ {label}")
            passed_struct += 1
        else:
            print(f"❌ {label} (Missing)")

    print("\n--- Deep Rule Validation (v4.0) ---")
    passed_rules = 0
    for label, pattern in rule_checks.items():
        if re.search(pattern, content, re.IGNORECASE | re.MULTILINE):
            print(f"✅ {label}")
            passed_rules += 1
        else:
            print(f"❌ {label} (Non-compliant)")

    print(f"\n--- Total Score: {passed_struct + passed_rules}/{len(structure_checks) + len(rule_checks)} ---")
    
    if (passed_struct + passed_rules) == (len(structure_checks) + len(rule_checks)):
        print("🎉 High Quality! This PRD meets the 4.0 Procedural Standards.")
    else:
        print("💡 Suggestion: Align with INVEST principles and BDD format for better AI synergy.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 prd-checker.py <path_to_prd.md>")
    else:
        check_prd(sys.argv[1])
