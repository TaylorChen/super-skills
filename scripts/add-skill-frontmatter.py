#!/usr/bin/env python3
"""
Add minimal YAML frontmatter (name, description) to all SKILL.md files.
Uses metadata.json (name + abstract) for values.
"""

from __future__ import annotations

import json
from pathlib import Path


def yaml_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def load_metadata(skill_dir: Path) -> tuple[str, str] | None:
    metadata_path = skill_dir / "metadata.json"
    if not metadata_path.exists():
        return None
    try:
        data = json.loads(metadata_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None

    name = str(data.get("name", "")).strip()
    description = str(data.get("abstract", "")).strip()
    if not name or not description:
        return None
    return name, description


def ensure_frontmatter(content: str, name: str, description: str) -> tuple[str, bool]:
    lines = content.splitlines()
    changed = False

    fm_name = f'name: "{yaml_escape(name)}"'
    fm_desc = f'description: "{yaml_escape(description)}"'

    if lines and lines[0].strip() == "---":
        # Find end of frontmatter
        end_idx = None
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                end_idx = i
                break
        if end_idx is None:
            # Malformed frontmatter; prepend a new block
            new_lines = ["---", fm_name, fm_desc, "---", ""] + lines
            return "\n".join(new_lines) + ("\n" if content.endswith("\n") else ""), True

        fm_lines = lines[1:end_idx]
        has_name = any(l.strip().startswith("name:") for l in fm_lines)
        has_desc = any(l.strip().startswith("description:") for l in fm_lines)

        insert_lines = []
        if not has_name:
            insert_lines.append(fm_name)
        if not has_desc:
            insert_lines.append(fm_desc)

        if insert_lines:
            new_fm = ["---"] + insert_lines + fm_lines + ["---"]
            new_lines = new_fm + lines[end_idx + 1 :]
            return "\n".join(new_lines) + ("\n" if content.endswith("\n") else ""), True

        return content, False

    # No frontmatter
    new_lines = ["---", fm_name, fm_desc, "---", ""] + lines
    return "\n".join(new_lines) + ("\n" if content.endswith("\n") else ""), True


def main() -> None:
    skills_dir = Path("skills")
    if not skills_dir.exists():
        print("❌ 错误: skills 目录不存在")
        return

    updated = 0
    total = 0

    for skill_file in skills_dir.rglob("SKILL.md"):
        skill_dir = skill_file.parent
        meta = load_metadata(skill_dir)
        if not meta:
            print(f"⚠️  跳过: {skill_file} (metadata.json 缺失或不完整)")
            continue

        total += 1
        name, description = meta
        content = skill_file.read_text(encoding="utf-8")
        new_content, changed = ensure_frontmatter(content, name, description)
        if changed:
            skill_file.write_text(new_content, encoding="utf-8")
            updated += 1
            print(f"✅ 更新: {skill_file}")

    print(f"\n📊 完成: 扫描 {total} 个技能, 更新 {updated} 个")


if __name__ == "__main__":
    main()
