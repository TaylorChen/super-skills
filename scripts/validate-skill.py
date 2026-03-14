#!/usr/bin/env python3
"""
技能验证工具
检查技能文件是否符合标准化结构和格式规范
"""

import os
import json
import re
from pathlib import Path

def check_skill_structure(skill_path):
    """检查技能文件结构"""
    print(f"\n🔍 检查技能: {skill_path.name}")
    print("-" * 60)
    
    errors = []
    warnings = []
    
    # 检查必需文件
    required_files = [
        "SKILL.md",
        "metadata.json"
    ]
    
    for file_name in required_files:
        file_path = skill_path / file_name
        if not file_path.exists():
            errors.append(f"❌ 缺少必需文件: {file_name}")
        else:
            print(f"✅ 找到: {file_name}")
    
    # 检查可选目录
    optional_dirs = ["references", "examples", "scripts", "assets"]
    for dir_name in optional_dirs:
        dir_path = skill_path / dir_name
        if dir_path.exists():
            print(f"ℹ️  找到: {dir_name}/")
    
    # 检查 SKILL.md 内容
    skill_md_path = skill_path / "SKILL.md"
    if skill_md_path.exists():
        with open(skill_md_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查 frontmatter 必需字段
        lines = content.splitlines()
        has_frontmatter = bool(lines and lines[0].strip() == "---")
        if not has_frontmatter:
            errors.append("❌ SKILL.md 缺少 YAML frontmatter (name/description 必填)")
        else:
            end_idx = None
            for i in range(1, len(lines)):
                if lines[i].strip() == "---":
                    end_idx = i
                    break
            if end_idx is None:
                errors.append("❌ SKILL.md frontmatter 未闭合")
            else:
                fm_lines = lines[1:end_idx]
                has_name = any(l.strip().startswith("name:") for l in fm_lines)
                has_desc = any(l.strip().startswith("description:") for l in fm_lines)
                if not has_name:
                    errors.append("❌ SKILL.md frontmatter 缺少 name 字段")
                if not has_desc:
                    errors.append("❌ SKILL.md frontmatter 缺少 description 字段")
        
        # 检查必要章节
        required_sections = [
            "快速开始",
            "工作流程",
            "加载文件",
            "相关 Skills",
            "检查清单",
            "最佳实践",
            "常见问题",
            "触发指令"
        ]
        
        for section in required_sections:
            if section not in content:
                warnings.append(f"⚠️  缺少建议章节: {section}")
        
        # 检查 Mermaid 流程图
        if "mermaid" not in content:
            warnings.append("⚠️  缺少 Mermaid 流程图")
        
        # 检查 Token 效率
        if "Token 效率" not in content:
            warnings.append("⚠️  缺少 Token 效率部分")
    
    # 检查 metadata.json 内容
    metadata_path = skill_path / "metadata.json"
    if metadata_path.exists():
        try:
            with open(metadata_path, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
            
            # 检查必要字段
            required_fields = ["name", "organization", "version", "status", "abstract", "prompts"]
            for field in required_fields:
                if field not in metadata:
                    errors.append(f"❌ metadata.json 缺少字段: {field}")
            
            # 检查 prompts 格式
            if "prompts" in metadata:
                for i, prompt in enumerate(metadata["prompts"]):
                    if "trigger" not in prompt:
                        errors.append(f"❌ prompts[{i}] 缺少 trigger 字段")
                    if "description" not in prompt:
                        errors.append(f"❌ prompts[{i}] 缺少 description 字段")
                    if "template" not in prompt:
                        errors.append(f"❌ prompts[{i}] 缺少 template 字段")
            
            # 检查分类字段
            if "category" not in metadata:
                warnings.append("⚠️  metadata.json 建议添加 category 字段")
            
            # 检查难度字段
            if "difficulty" not in metadata:
                warnings.append("⚠️  metadata.json 建议添加 difficulty 字段")
            
            # 检查时间字段
            if "estimated_time" not in metadata:
                warnings.append("⚠️  metadata.json 建议添加 estimated_time 字段")
                
        except json.JSONDecodeError as e:
            errors.append(f"❌ metadata.json 格式错误: {e}")
    
    # 检查 references 目录
    references_path = skill_path / "references"
    if references_path.exists():
        ref_files = list(references_path.glob("*.md"))
        if not ref_files:
            warnings.append("⚠️  references/ 目录为空")
        else:
            print(f"ℹ️  references/ 包含 {len(ref_files)} 个文件")
    
    return errors, warnings

def validate_all_skills():
    """验证所有技能"""
    skills_dir = Path("skills")
    if not skills_dir.exists():
        print("❌ 错误: skills 目录不存在")
        return
    
    print("🚀 开始验证所有技能...\n")
    
    total_errors = 0
    total_warnings = 0
    
    for skill in sorted(skills_dir.iterdir()):
        if not skill.is_dir():
            continue
        
        errors, warnings = check_skill_structure(skill)
        
        for error in errors:
            print(f"  {error}")
        for warning in warnings:
            print(f"  {warning}")
        
        total_errors += len(errors)
        total_warnings += len(warnings)
        
        if not errors and not warnings:
            print("  ✅ 所有检查通过!")
        print()
    
    print("=" * 60)
    print(f"📊 验证结果:")
    print(f"  技能总数: {len(list(skills_dir.iterdir()))}")
    print(f"  错误数: {total_errors}")
    print(f"  警告数: {total_warnings}")
    
    if total_errors == 0:
        print("\n🎉 所有技能验证通过!")
    else:
        print("\n⚠️  存在错误需要修复")

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="技能验证工具")
    parser.add_argument("skill_path", nargs="?", default=None, help="技能目录路径")
    parser.add_argument("--all", action="store_true", help="验证所有技能")
    
    args = parser.parse_args()
    
    if args.all:
        validate_all_skills()
    elif args.skill_path:
        skill_path = Path(args.skill_path)
        if not skill_path.exists():
            print(f"❌ 错误: 路径不存在: {args.skill_path}")
            return
        if not skill_path.is_dir():
            print(f"❌ 错误: 不是目录: {args.skill_path}")
            return
        
        errors, warnings = check_skill_structure(skill_path)
        
        for error in errors:
            print(f"  {error}")
        for warning in warnings:
            print(f"  {warning}")
        
        if not errors and not warnings:
            print("  ✅ 所有检查通过!")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
