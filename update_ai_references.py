#!/usr/bin/env python3
"""
更新所有技能文件，添加 AI 工具参考链接
"""

import os
import re
from pathlib import Path

def update_skill_file(skill_file):
    """更新单个技能文件"""
    with open(skill_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已经包含 AI 工具参考
    if "## AI 工具参考" in content:
        print(f"✅ {skill_file.name} 已包含 AI 工具参考")
        return False
    
    # 找到文件末尾，添加 AI 工具参考
    new_content = content + '\n\n## AI 工具参考\n\n- [Claude 使用指南](../../../CLAUDE.md)\n- [Cursor 使用指南](../../../CURSOR.md)\n- [Trae 使用指南](../../../TRAE.md)\n- [Antigravity 使用指南](../../../ANTIGRAVITY.md)\n- [Codex 使用指南](../../../CODEX.md)\n'
    
    with open(skill_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ 更新 {skill_file.name}")
    return True

def main():
    """主函数"""
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
        if update_skill_file(skill_file):
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
            if update_skill_file(skill_file):
                updated_count += 1
    
    print(f"\n📊 更新完成:")
    print(f"  总计检查: {total_count} 个技能")
    print(f"  成功更新: {updated_count} 个技能")
    print(f"  未需更新: {total_count - updated_count} 个技能")

if __name__ == "__main__":
    main()
