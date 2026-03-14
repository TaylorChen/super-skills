#!/usr/bin/env python3
"""
更新所有技能文件，添加深度总结内容
"""

import os
import re
from pathlib import Path

def load_deep_summary():
    """加载深度总结内容"""
    summary_file = Path('DEEP_SUMMARY.md')
    if not summary_file.exists():
        print("❌ 错误: DEEP_SUMMARY.md 文件不存在")
        return None
    
    with open(summary_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return content

def update_skill_file(skill_file, deep_summary):
    """更新单个技能文件"""
    with open(skill_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已经包含深度总结
    if "## 深度总结：AI 技能优化与维护指南" in content:
        print(f"✅ {skill_file.name} 已包含深度总结")
        return False
    
    # 找到文件末尾，添加深度总结
    new_content = content + '\n\n' + deep_summary
    
    with open(skill_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ 更新 {skill_file.name}")
    return True

def main():
    """主函数"""
    # 加载深度总结
    deep_summary = load_deep_summary()
    if not deep_summary:
        return
    
    skills_dir = Path('skills')
    if not skills_dir.exists():
        print("❌ 错误: skills 目录不存在")
        return
    
    print("🚀 开始更新所有技能文件...\n")
    
    updated_count = 0
    total_count = 0
    
    # 遍历所有技能目录
    for skill_path in skills_dir.iterdir():
        if not skill_path.is_dir():
            continue
        
        # 检查是否有 SKILL.md 文件
        skill_file = skill_path / "SKILL.md"
        if not skill_file.exists():
            continue
        
        total_count += 1
        if update_skill_file(skill_file, deep_summary):
            updated_count += 1
    
    # 检查子目录中的技能
    subdirs = ['content-generation', 'ai-generation', 'utilities']
    for subdir in subdirs:
        subdir_path = skills_dir / subdir
        if not subdir_path.is_dir():
            continue
        
        for skill_path in subdir_path.iterdir():
            if not skill_path.is_dir():
                continue
            
            skill_file = skill_path / "SKILL.md"
            if not skill_file.exists():
                continue
            
            total_count += 1
            if update_skill_file(skill_file, deep_summary):
                updated_count += 1
    
    print(f"\n📊 更新完成:")
    print(f"  总计检查: {total_count} 个技能")
    print(f"  成功更新: {updated_count} 个技能")
    print(f"  未需更新: {total_count - updated_count} 个技能")

if __name__ == "__main__":
    main()
