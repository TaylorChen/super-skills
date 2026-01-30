#!/usr/bin/env python3
"""
Super Skills 交互式选择器
帮助用户快速找到并使用合适的 skill
"""

import os
import sys
from pathlib import Path

# Skills 分类
CATEGORIES = {
    "🎯 产品类": [
        ("product-requirements", "PRD 撰写 - 产品需求文档"),
        ("competitive-analysis", "竞品分析 - SWOT 分析"),
        ("user-story", "用户故事 - 敏捷开发"),
        ("prototype-design", "原型设计 - 交互流程"),
        ("product-roadmap", "路线图规划 - 版本规划")
    ],
    "💻 研发类": [
        ("technical-design", "架构设计 - 技术方案"),
        ("api-design", "API 设计 - RESTful/GraphQL/gRPC"),
        ("database-schema", "数据库设计 - 建模与优化"),
        ("code-review", "代码审查 - 质量把控"),
        ("refactoring-guide", "重构指南 - 代码优化"),
        ("testing-strategy", "测试策略 - 测试金字塔"),
        ("tech-research", "技术调研 - POC 验证")
    ],
    "✍️ 内容类": [
        ("blog-writer", "技术博客 - 内容创作"),
        ("seo-optimization", "SEO 优化 - 搜索优化"),
        ("geo-optimization", "GEO 优化 - 本地化"),
        ("documentation", "技术文档 - API 文档")
    ],
    "🔧 运维/数据": [
        ("deployment-guide", "部署指南 - CI/CD"),
        ("monitoring-setup", "监控配置 - 告警设置"),
        ("data-analysis", "数据分析 - 可视化"),
        ("performance-tuning", "性能调优 - 优化方案")
    ]
}

def print_header():
    """打印欢迎信息"""
    print("\n" + "=" * 60)
    print("🚀 Super Skills 交互式选择器")
    print("=" * 60)
    print("\n选择一个类别查看相关 skills:\n")

def print_categories():
    """打印类别列表"""
    for idx, category in enumerate(CATEGORIES.keys(), 1):
        print(f"  {idx}. {category}")
    print(f"  0. 退出\n")

def print_skills(category_name):
    """打印指定类别的 skills"""
    print(f"\n{category_name} 包含以下 skills:\n")
    skills = CATEGORIES[category_name]
    for idx, (skill_id, skill_desc) in enumerate(skills, 1):
        print(f"  {idx}. {skill_desc}")
    print(f"  0. 返回上级\n")
    return skills

def show_skill_info(skill_id):
    """显示 skill 详细信息"""
    skill_path = Path(f"skills/{skill_id}")
    skill_md = skill_path / "SKILL.md"
    
    if not skill_md.exists():
        print(f"\n❌ 错误: 找不到 {skill_id} 的 SKILL.md 文件\n")
        return
    
    print("\n" + "=" * 60)
    print(f"📄 Skill: {skill_id}")
    print("=" * 60)
    
    # 读取并显示基本信息
    with open(skill_md, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        in_frontmatter = False
        description = ""
        
        for line in lines:
            if line.strip() == "---":
                in_frontmatter = not in_frontmatter
                continue
            if in_frontmatter and line.startswith("description:"):
                description = line.replace("description:", "").strip()
                break
    
    print(f"\n📝 描述: {description}\n")
    
    # 显示触发指令
    print("⚡ 触发指令:")
    print(f"  /{skill_id}-full   - 完整工作流")
    print(f"  /{skill_id}-quick  - 快速检查\n")
    
    # 显示示例文件
    example_dir = Path(f"resources/examples/{skill_id}")
    if example_dir.exists():
        examples = list(example_dir.glob("*.md"))
        if examples:
            print("📚 示例文件:")
            for example in examples:
                print(f"  - {example.name}")
            print()
    
    # 显示参考文件
    ref_dir = skill_path / "references"
    if ref_dir.exists():
        refs = list(ref_dir.glob("*.md"))
        if refs:
            print("📖 参考文档:")
            for ref in refs:
                print(f"  - {ref.name}")
            print()
    
    print("💡 使用方法:")
    print(f"  1. 在 AI 工具中输入: /{skill_id}-full")
    print(f"  2. 或手动加载: skills/{skill_id}/SKILL.md")
    print("\n" + "=" * 60 + "\n")
    
    input("按 Enter 键继续...")

def main():
    """主函数"""
    # 检查是否在项目根目录
    if not Path("skills").exists():
        print("\n❌ 错误: 找不到 skills 目录")
        print("💡 提示: 请在项目根目录运行此脚本\n")
        sys.exit(1)
    
    while True:
        print_header()
        print_categories()
        
        try:
            choice = input("请选择类别 (输入数字): ").strip()
            
            if choice == "0":
                print("\n👋 再见!\n")
                break
            
            category_idx = int(choice) - 1
            category_names = list(CATEGORIES.keys())
            
            if 0 <= category_idx < len(category_names):
                category_name = category_names[category_idx]
                
                while True:
                    skills = print_skills(category_name)
                    skill_choice = input("请选择 skill (输入数字): ").strip()
                    
                    if skill_choice == "0":
                        break
                    
                    skill_idx = int(skill_choice) - 1
                    if 0 <= skill_idx < len(skills):
                        skill_id, _ = skills[skill_idx]
                        show_skill_info(skill_id)
                    else:
                        print("\n❌ 无效选择,请重试\n")
            else:
                print("\n❌ 无效选择,请重试\n")
        
        except ValueError:
            print("\n❌ 请输入有效的数字\n")
        except KeyboardInterrupt:
            print("\n\n👋 再见!\n")
            break

if __name__ == "__main__":
    main()
