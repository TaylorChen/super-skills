#!/usr/bin/env python3
"""
内容生成工具脚本
用于辅助内容生成相关的操作
"""

import os
import sys
import json
from pathlib import Path

def print_header():
    """打印欢迎信息"""
    print("\n" + "=" * 60)
    print("🚀 内容生成工具")
    print("=" * 60)
    print("\n辅助内容生成相关的操作\n")

def list_content_skills():
    """列出所有内容生成相关的技能"""
    content_skills_path = Path("skills/content-generation")
    
    if not content_skills_path.exists():
        print("❌ 内容生成技能目录不存在")
        return
    
    print("📋 内容生成技能列表:")
    print("-" * 40)
    
    for skill_dir in content_skills_path.iterdir():
        if skill_dir.is_dir():
            # 尝试读取 SKILL.md 文件获取标题
            skill_md_path = skill_dir / "SKILL.md"
            if skill_md_path.exists():
                with open(skill_md_path, 'r', encoding='utf-8') as f:
                    first_line = f.readline().strip()
                    if first_line.startswith('# '):
                        title = first_line[2:]
                    else:
                        title = skill_dir.name
            else:
                title = skill_dir.name
            
            print(f"- {title} ({skill_dir.name})")
    
    print("-" * 40)

def main():
    """主函数"""
    print_header()
    list_content_skills()
    
    print("\n💡 提示:")
    print("  - 使用 /xhs-images-full 生成小红书风格图片")
    print("  - 使用 /image-gen-full 生成自定义图像")
    print("  - 使用 /url-to-markdown-full 将网页转换为 Markdown")
    print("  - 使用 /compress-image-full 压缩图片")

if __name__ == "__main__":
    main()
