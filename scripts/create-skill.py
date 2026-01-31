#!/usr/bin/env python3
"""
Super Skills 技能生成器
帮助用户快速创建新的技能目录和基础文件
"""

import os
import sys
import json
from pathlib import Path

# 技能分类
CATEGORIES = {
    "product": "🎯 产品类",
    "development": "💻 研发类",
    "content": "✍️ 内容类",
    "devops": "🔧 运维/数据"
}

# 难度级别
DIFFICULTY = {
    "beginner": "初级 - 适合新手",
    "intermediate": "中级 - 需要一定经验",
    "advanced": "高级 - 需要丰富经验"
}

def print_header():
    """打印欢迎信息"""
    print("\n" + "=" * 60)
    print("🚀 Super Skills 技能生成器")
    print("=" * 60)
    print("\n创建新的技能目录和基础文件\n")

def get_skill_info():
    """收集技能信息"""
    info = {}
    
    info["name"] = input("技能名称 (kebab-case, 如: new-skill): ").strip().lower().replace(" ", "-")
    
    info["title"] = input("技能标题 (中文, 如: 新技能): ").strip()
    
    info["description"] = input("简短描述 (一句话说明用途): ").strip()
    
    print("\n选择技能类别:")
    for idx, (key, label) in enumerate(CATEGORIES.items(), 1):
        print(f"  {idx}. {label}")
    
    while True:
        try:
            choice = int(input("\n输入类别编号: ").strip())
            categories_list = list(CATEGORIES.keys())
            if 1 <= choice <= len(categories_list):
                info["category"] = categories_list[choice - 1]
                break
            print("❌ 无效选择，请重试")
        except ValueError:
            print("❌ 请输入有效的数字")
    
    print("\n选择难度级别:")
    for idx, (key, label) in enumerate(DIFFICULTY.items(), 1):
        print(f"  {idx}. {label}")
    
    while True:
        try:
            choice = int(input("\n输入难度编号: ").strip())
            difficulty_list = list(DIFFICULTY.keys())
            if 1 <= choice <= len(difficulty_list):
                info["difficulty"] = difficulty_list[choice - 1]
                break
            print("❌ 无效选择，请重试")
        except ValueError:
            print("❌ 请输入有效的数字")
    
    info["estimated_time"] = input("预计使用时间 (如: 10-15 min): ").strip() or "5-10 min"
    
    info["author"] = input("作者名称 (可选): ").strip() or "Contributor"
    
    return info

def create_skill_directory(skill_info):
    """创建技能目录和文件"""
    skill_path = Path(f"skills/{skill_info['name']}")
    
    if skill_path.exists():
        print(f"\n❌ 错误: 技能目录 {skill_info['name']} 已存在")
        return False
    
    skill_path.mkdir(parents=True)
    print(f"\n✅ 创建目录: {skill_path}")
    
    references_path = skill_path / "references"
    references_path.mkdir()
    print(f"✅ 创建目录: {references_path}")
    
    return True

def generate_skill_md(skill_info):
    """生成 SKILL.md 文件"""
    skill_path = Path(f"skills/{skill_info['name']}")
    
    content = f"""# {skill_info['title']}

{skill_info['description']}。

## 快速开始

### 5 步上手

1. **准备输入** - [描述第一步]
2. **触发技能** - 在 AI 工具中输入 `/{skill_info['name']}-full`
3. **描述需求** - [描述第三步]
4. **生成内容** - AI 自动生成[输出内容]
5. **迭代优化** - 根据反馈调整[相关内容]

### 使用示例

```
/{skill_info['name']}-full
[描述你的需求]
```

## 工作流程

```mermaid
graph LR
    A[输入] --> B[处理]
    B --> C[输出]
    
    style A fill:#e1f5ff
    style C fill:#c8e6c9
```

## 加载文件
- [references/guide.md](references/guide.md) - [描述]

## 相关 Skills
- [列出相关技能]

## 示例
- 📄 [示例文件](../../resources/examples/{skill_info['name']}/sample.md)

## 检查清单
- [ ] 检查项 1
- [ ] 检查项 2
- [ ] 检查项 3

## 最佳实践

### [主题 1]
- ✅ [最佳实践 1]
- ✅ [最佳实践 2]

### [主题 2]
- ✅ [最佳实践 3]
- ✅ [最佳实践 4]

## 常见问题

**Q: [常见问题 1]?**
A: [回答 1]

**Q: [常见问题 2]?**
A: [回答 2]

## 触发指令

⚠️ **Prompt-as-Code (v5.0)**: 触发指令已迁移至 `metadata.json`。支持：
- `/{skill_info['name']}-full` - [描述]
- `/{skill_info['name']}-quick` - [描述]

## Token 效率

- 主 Skill 文件: ~300 tokens
- 参考指南总计: ~2k+ tokens
"""
    
    skill_md = skill_path / "SKILL.md"
    with open(skill_md, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ 创建文件: {skill_md}")
    
    return True

def generate_metadata_json(skill_info):
    """生成 metadata.json 文件"""
    skill_path = Path(f"skills/{skill_info['name']}")
    
    # 询问是否添加参数化配置
    add_params = input("是否添加参数化配置? (y/n): ").strip().lower() == 'y'
    
    # 询问是否添加外部服务集成
    add_services = input("是否添加外部服务集成? (y/n): ").strip().lower() == 'y'
    
    prompts = [
        {
            "trigger": f"/{skill_info['name']}-full",
            "description": "完整工作流",
            "template": f"提供完整的{skill_info['title']}工作流，参考相关示例和最佳实践。"
        },
        {
            "trigger": f"/{skill_info['name']}-quick",
            "description": "快速检查",
            "template": f"快速进行{skill_info['title']}，重点关注关键要素。"
        }
    ]
    
    if add_params:
        print("\n为完整工作流添加参数化配置:")
        
        # 添加通用参数
        parameters = {
            "format": {
                "description": "输出格式",
                "options": ["detailed", "concise", "executive"],
                "default": "detailed"
            },
            "lang": {
                "description": "输出语言",
                "options": ["zh", "en"],
                "default": "zh"
            }
        }
        
        # 询问是否添加更多参数
        add_more_params = input("是否添加更多自定义参数? (y/n): ").strip().lower() == 'y'
        
        if add_more_params:
            param_count = int(input("要添加多少个自定义参数? (1-3): ").strip())
            for i in range(param_count):
                print(f"\n添加参数 {i+1}:")
                param_name = input("参数名称: ").strip()
                param_desc = input("参数描述: ").strip()
                param_type = input("参数类型 (options/boolean): ").strip().lower()
                
                if param_type == "options":
                    options = input("选项列表 (逗号分隔): ").strip().split(',')
                    default = input("默认值: ").strip()
                    parameters[param_name] = {
                        "description": param_desc,
                        "options": [opt.strip() for opt in options],
                        "default": default
                    }
                else:
                    default = input("默认值 (true/false): ").strip().lower() == 'true'
                    parameters[param_name] = {
                        "description": param_desc,
                        "type": "boolean",
                        "default": default
                    }
        
        # 添加参数到完整工作流
        prompts[0]["parameters"] = parameters
    
    metadata = {
        "name": skill_info["name"],
        "organization": "super-skills",
        "version": "5.0.0",
        "status": "stable",
        "category": skill_info["category"],
        "difficulty": skill_info["difficulty"],
        "estimated_time": skill_info["estimated_time"],
        "author": skill_info["author"],
        "abstract": skill_info["description"],
        "prompts": prompts
    }
    
    if add_services:
        services = []
        service_types = ["github", "openai", "slack", "jira", "custom"]
        
        print("\n选择需要集成的外部服务:")
        for idx, service in enumerate(service_types, 1):
            print(f"  {idx}. {service}")
        
        selected = input("输入服务编号 (多个用逗号分隔): ").strip().split(',')
        
        for sel in selected:
            try:
                service_idx = int(sel.strip()) - 1
                if 0 <= service_idx < len(service_types):
                    service_name = service_types[service_idx]
                    required = input(f"{service_name} 是否为必需? (y/n): ").strip().lower() == 'y'
                    
                    service_config = {
                        "name": service_name,
                        "required": required
                    }
                    
                    if service_name == "custom":
                        service_config["name"] = input("自定义服务名称: ").strip()
                        service_config["description"] = input("自定义服务描述: ").strip()
                    
                    services.append(service_config)
            except ValueError:
                pass
        
        if services:
            metadata["services"] = services
    
    metadata_file = skill_path / "metadata.json"
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=4)
    print(f"✅ 创建文件: {metadata_file}")
    
    return True

def generate_guide_md(skill_info):
    """生成 references/guide.md 文件"""
    skill_path = Path(f"skills/{skill_info['name']}")
    references_path = skill_path / "references"
    
    content = f"""# {skill_info['title']} 指南

## 概述

本指南提供 {skill_info['title']} 的详细说明和最佳实践。

## 核心概念

### 概念 1

[描述概念 1]

### 概念 2

[描述概念 2]

## 工作流程

```mermaid
graph TD
    A[开始] --> B[步骤 1]
    B --> C[步骤 2]
    C --> D[步骤 3]
    D --> E[结束]
```

## 最佳实践

1. [最佳实践 1]
2. [最佳实践 2]
3. [最佳实践 3]

## 常见问题

### 问题 1

**问题**: [描述问题]

**解决方案**: [描述解决方案]

### 问题 2

**问题**: [描述问题]

**解决方案**: [描述解决方案]

## 参考资料

- [参考 1](链接)
- [参考 2](链接)
"""
    
    guide_md = references_path / "guide.md"
    with open(guide_md, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ 创建文件: {guide_md}")
    
    return True

def generate_example_md(skill_info):
    """生成示例文件"""
    example_path = Path(f"resources/examples/{skill_info['name']}")
    
    if example_path.exists():
        print(f"⚠️  示例目录已存在: {example_path}")
        return True
    
    example_path.mkdir(parents=True)
    
    content = f"""# {skill_info['title']} 示例

## 示例 1

[描述示例 1 的场景]

### 输入

```
[示例输入]
```

### 输出

```
[示例输出]
```

## 示例 2

[描述示例 2 的场景]

### 输入

```
[示例输入]
```

### 输出

```
[示例输出]
```
"""
    
    sample_md = example_path / "sample.md"
    with open(sample_md, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ 创建文件: {sample_md}")
    
    return True

def print_next_steps(skill_info):
    """打印后续步骤"""
    print("\n" + "=" * 60)
    print("🎉 技能创建成功!")
    print("=" * 60)
    print(f"\n技能名称: {skill_info['name']}")
    print(f"技能标题: {skill_info['title']}")
    print(f"技能描述: {skill_info['description']}")
    print(f"类别: {CATEGORIES[skill_info['category']]}")
    print(f"难度: {DIFFICULTY[skill_info['difficulty']]}")
    
    print("\n📝 后续步骤:")
    print(f"  1. 编辑 skills/{skill_info['name']}/SKILL.md")
    print(f"  2. 完善 skills/{skill_info['name']}/references/guide.md")
    print(f"  3. 添加示例文件到 resources/examples/{skill_info['name']}/")
    print(f"  4. 运行验证: python3 scripts/lint-rules.py")
    print(f"  5. 提交 Pull Request")
    
    print("\n💡 提示:")
    print("  - 确保主文件 (SKILL.md) < 500 tokens")
    print("  - 添加 Mermaid 流程图增强可视化")
    print("  - 提供中英双语支持（可选）")
    print("  - 包含实战示例")

def main():
    """主函数"""
    print_header()
    
    skill_info = get_skill_info()
    
    print("\n" + "-" * 60)
    print("技能信息:")
    print(f"  名称: {skill_info['name']}")
    print(f"  标题: {skill_info['title']}")
    print(f"  描述: {skill_info['description']}")
    print(f"  类别: {CATEGORIES[skill_info['category']]}")
    print(f"  难度: {DIFFICULTY[skill_info['difficulty']]}")
    print(f"  预计时间: {skill_info['estimated_time']}")
    print(f"  作者: {skill_info['author']}")
    print("-" * 60)
    
    confirm = input("\n确认创建? (y/n): ").strip().lower()
    
    if confirm != 'y':
        print("\n❌ 已取消")
        sys.exit(0)
    
    if not create_skill_directory(skill_info):
        sys.exit(1)
    
    generate_skill_md(skill_info)
    generate_metadata_json(skill_info)
    generate_guide_md(skill_info)
    generate_example_md(skill_info)
    
    print_next_steps(skill_info)
    print("\n" + "=" * 60 + "\n")

if __name__ == "__main__":
    if not Path("skills").exists():
        print("\n❌ 错误: skills 目录不存在")
        print("💡 提示: 请在项目根目录运行此脚本\n")
        sys.exit(1)
    
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 已取消\n")
        sys.exit(0)
