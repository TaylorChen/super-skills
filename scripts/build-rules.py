#!/usr/bin/env python3
import os
import re
import sys

# Token budget for AGENTS.md (approx characters / 1.5)
# Setting strict limit for "Programmatic" rules to ensure fast context loading
TOKEN_BUDGET = 2000 

def estimate_tokens(text):
    # Simple heuristic
    return len(text) // 2

def build_agents_md(skill_path):
    rules_dir = os.path.join(skill_path, "rules")
    if not os.path.exists(rules_dir):
        return True # Skip non-4.0 skills

    skill_name = os.path.basename(skill_path)
    agents_md_path = os.path.join(skill_path, "AGENTS.md")
    
    # Read metadata if exists
    metadata_path = os.path.join(skill_path, "metadata.json")
    version = "unknown"
    if os.path.exists(metadata_path):
        import json
        with open(metadata_path, 'r') as f:
            meta = json.load(f)
            version = meta.get("version", "unknown")

    content = [f"# Agent Rules: {skill_name.replace('-', ' ').title()} (v{version})\n"]
    content.append("This document contains procedural rules for AI agents. Loaded automatically for high-precision task execution.\n")

    # Iterate over all .md files in rules/ (excluding _template.md)
    for rule_file in sorted(os.listdir(rules_dir)):
        if rule_file.endswith(".md") and not rule_file.startswith("_"):
            with open(os.path.join(rules_dir, rule_file), 'r', encoding='utf-8') as f:
                rule_content = f.read()
                # Clean up rule content: remove the metadata table for AGENTS.md density
                rule_content = re.sub(r"\| Metadata \| Value \|.*\n\| --- \| --- \|.*\n(\| .* \| .* \|\n)+", "", rule_content)
                # Remove Rationale header to save tokens, keep content? No, keep Rationale as it helps reasoning.
                # But maybe compress headers.
                content.append(rule_content.strip())
                content.append("\n---\n")

    final_content = "\n".join(content)
    tokens = estimate_tokens(final_content)
    
    print(f"✨ Built: {agents_md_path} ({tokens} tokens)")
    
    if tokens > TOKEN_BUDGET:
        print(f"❌ ERROR: {skill_name} AGENTS.md exceeds token budget! ({tokens}/{TOKEN_BUDGET})")
        return False
        
    with open(agents_md_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    return True

def main():
    skills_dir = "skills"
    failed = False
    
    for skill in os.listdir(skills_dir):
        skill_path = os.path.join(skills_dir, skill)
        if os.path.isdir(skill_path):
            if not build_agents_md(skill_path):
                failed = True

    if failed:
        sys.exit(1)

if __name__ == "__main__":
    main()
