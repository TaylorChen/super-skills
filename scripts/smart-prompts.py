#!/usr/bin/env python3
"""
Super Skills 智能提示系统
根据用户输入和上下文提供相关技能推荐和使用提示
"""

import os
import sys
import json
import argparse
from pathlib import Path
from fuzzywuzzy import fuzz

class SmartPrompts:
    """智能提示系统类"""
    
    def __init__(self):
        self.skills_dir = Path('skills')
        self.prompts_config = Path('scripts/prompts-config.json')
        self.skills_data = []
        self.load_skills_data()
    
    def load_skills_data(self):
        """加载技能数据"""
        if not self.skills_dir.exists():
            return
        
        for skill_dir in self.skills_dir.iterdir():
            if skill_dir.is_dir():
                metadata_path = skill_dir / "metadata.json"
                if metadata_path.exists():
                    try:
                        with open(metadata_path, 'r', encoding='utf-8') as f:
                            metadata = json.load(f)
                        
                        skill_data = {
                            "name": metadata.get("name", skill_dir.name),
                            "title": metadata.get("title", skill_dir.name),
                            "description": metadata.get("abstract", ""),
                            "category": metadata.get("category", ""),
                            "difficulty": metadata.get("difficulty", ""),
                            "triggers": [p.get("trigger") for p in metadata.get("prompts", [])]
                        }
                        
                        self.skills_data.append(skill_data)
                    except Exception as e:
                        pass
    
    def find_relevant_skills(self, query, threshold=70):
        """根据查询找到相关技能"""
        relevant_skills = []
        
        for skill in self.skills_data:
            # 计算相关性分数
            score = max(
                fuzz.partial_ratio(query.lower(), skill["name"].lower()),
                fuzz.partial_ratio(query.lower(), skill["title"].lower()),
                fuzz.partial_ratio(query.lower(), skill["description"].lower())
            )
            
            if score >= threshold:
                skill["relevance_score"] = score
                relevant_skills.append(skill)
        
        # 按相关性分数排序
        relevant_skills.sort(key=lambda x: x["relevance_score"], reverse=True)
        
        return relevant_skills[:5]  # 最多返回5个相关技能
    
    def generate_prompt(self, skill_name):
        """为特定技能生成使用提示"""
        skill = next((s for s in self.skills_data if s["name"] == skill_name), None)
        if not skill:
            return f"❌ 未找到技能: {skill_name}"
        
        prompt = f"# {skill['title']} 使用提示\n\n"
        prompt += f"## 技能描述\n{skill['description']}\n\n"
        
        if skill['triggers']:
            prompt += "## 可用触发器\n"
            for trigger in skill['triggers']:
                prompt += f"- `{trigger}`\n"
            prompt += "\n"
        
        prompt += "## 使用建议\n"
        prompt += "1. **明确需求** - 清晰描述你的具体需求\n"
        prompt += "2. **提供上下文** - 相关的背景信息和约束条件\n"
        prompt += "3. **指定格式** - 期望的输出格式和详细程度\n"
        prompt += "4. **迭代优化** - 根据初始结果提供反馈和调整建议\n\n"
        
        prompt += "## 示例输入\n"
        prompt += f"```\n{skill['triggers'][0] if skill['triggers'] else f'/{skill_name}-full'}\n"
        prompt += f"[描述你的{skill['title']}需求]\n```\n"
        
        return prompt
    
    def get_category_recommendations(self, category):
        """获取特定类别的技能推荐"""
        category_skills = [s for s in self.skills_data if s["category"] == category]
        
        if not category_skills:
            return f"❌ 未找到类别: {category}"
        
        recommendations = f"# {category} 类别技能推荐\n\n"
        recommendations += "## 相关技能\n"
        
        for skill in category_skills:
            recommendations += f"### {skill['title']}\n"
            recommendations += f"- **描述**: {skill['description']}\n"
            if skill['triggers']:
                recommendations += f"- **触发器**: {', '.join(skill['triggers'])}\n"
            recommendations += f"- **难度**: {skill['difficulty']}\n\n"
        
        return recommendations
    
    def generate_contextual_prompt(self, user_input):
        """根据用户输入生成上下文相关提示"""
        relevant_skills = self.find_relevant_skills(user_input)
        
        if not relevant_skills:
            return "❌ 未找到相关技能\n\n请尝试更具体的描述或查看所有可用技能。"
        
        prompt = "# 智能推荐\n\n"
        prompt += "根据你的输入，推荐以下技能:\n\n"
        
        for i, skill in enumerate(relevant_skills, 1):
            prompt += f"## {i}. {skill['title']}\n"
            prompt += f"- **相关性**: {skill['relevance_score']}%\n"
            prompt += f"- **描述**: {skill['description']}\n"
            if skill['triggers']:
                prompt += f"- **使用**: `{skill['triggers'][0]}`\n"
            prompt += f"- **难度**: {skill['difficulty']}\n\n"
        
        prompt += "## 如何使用\n"
        prompt += "1. 复制上面的触发器命令\n"
        prompt += "2. 在AI工具中粘贴并按Enter\n"
        prompt += "3. 详细描述你的需求\n"
        prompt += "4. 等待AI生成结果\n"
        
        return prompt

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='Super Skills 智能提示系统')
    parser.add_argument('--query', '-q', help='用户查询内容')
    parser.add_argument('--skill', '-s', help='技能名称')
    parser.add_argument('--category', '-c', help='技能类别')
    parser.add_argument('--list', '-l', action='store_true', help='列出所有技能')
    args = parser.parse_args()
    
    prompt_system = SmartPrompts()
    
    if args.list:
        # 列出所有技能
        print("# 所有可用技能\n")
        for skill in prompt_system.skills_data:
            print(f"## {skill['title']}\n")
            print(f"- **名称**: {skill['name']}\n")
            print(f"- **描述**: {skill['description']}\n")
            if skill['triggers']:
                print(f"- **触发器**: {', '.join(skill['triggers'])}\n")
            print(f"- **类别**: {skill['category']}\n")
            print(f"- **难度**: {skill['difficulty']}\n")
            print("---\n")
    
    elif args.query:
        # 生成上下文相关提示
        prompt = prompt_system.generate_contextual_prompt(args.query)
        print(prompt)
    
    elif args.skill:
        # 为特定技能生成使用提示
        prompt = prompt_system.generate_prompt(args.skill)
        print(prompt)
    
    elif args.category:
        # 获取类别推荐
        prompt = prompt_system.get_category_recommendations(args.category)
        print(prompt)
    
    else:
        # 显示帮助信息
        parser.print_help()

if __name__ == "__main__":
    main()