#!/usr/bin/env python3
"""
Super Skills 测试框架
用于测试技能的结构和功能
"""

import os
import sys
import json
import argparse
from pathlib import Path

class SkillTester:
    """技能测试类"""
    
    def __init__(self, skill_dir):
        self.skill_dir = Path(skill_dir)
        self.results = []
        self.errors = []
        self.warnings = []
    
    def test_structure(self):
        """测试技能目录结构"""
        print(f"\n🧪 测试技能结构: {self.skill_dir.name}")
        
        # 检查必需文件
        required_files = [
            "SKILL.md",
            "metadata.json",
            "references/guide.md"
        ]
        
        for file_path in required_files:
            full_path = self.skill_dir / file_path
            if full_path.exists():
                self.results.append(f"✅ 存在: {file_path}")
            else:
                self.errors.append(f"❌ 缺失: {file_path}")
        
        # 检查目录结构
        if (self.skill_dir / "references").exists():
            self.results.append("✅ 存在: references 目录")
        else:
            self.errors.append("❌ 缺失: references 目录")
    
    def test_metadata(self):
        """测试 metadata.json 文件"""
        metadata_path = self.skill_dir / "metadata.json"
        
        if not metadata_path.exists():
            return
        
        print("\n🧪 测试 metadata.json")
        
        try:
            with open(metadata_path, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
            
            # 检查必需字段
            required_fields = [
                "name", "organization", "version", "status",
                "category", "difficulty", "estimated_time",
                "abstract", "prompts"
            ]
            
            for field in required_fields:
                if field in metadata:
                    self.results.append(f"✅ 存在字段: {field}")
                else:
                    self.errors.append(f"❌ 缺失字段: {field}")
            
            # 检查 prompts 格式
            if "prompts" in metadata:
                if isinstance(metadata["prompts"], list):
                    self.results.append(f"✅ prompts 格式正确: {len(metadata['prompts'])} 个触发器")
                    
                    for i, prompt in enumerate(metadata["prompts"]):
                        if "trigger" in prompt and "description" in prompt and "template" in prompt:
                            self.results.append(f"✅ 触发器 {i+1} 格式正确")
                        else:
                            self.errors.append(f"❌ 触发器 {i+1} 格式错误")
                else:
                    self.errors.append("❌ prompts 必须是数组")
            
            # 检查服务配置
            if "services" in metadata:
                if isinstance(metadata["services"], list):
                    self.results.append(f"✅ services 格式正确: {len(metadata['services'])} 个服务")
                else:
                    self.errors.append("❌ services 必须是数组")
                    
        except json.JSONDecodeError as e:
            self.errors.append(f"❌ JSON 解析错误: {e}")
        except Exception as e:
            self.errors.append(f"❌ 测试 metadata.json 时出错: {e}")
    
    def test_skill_md(self):
        """测试 SKILL.md 文件"""
        skill_md_path = self.skill_dir / "SKILL.md"
        
        if not skill_md_path.exists():
            return
        
        print("\n🧪 测试 SKILL.md")
        
        try:
            with open(skill_md_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查文件大小
            if len(content) < 100:
                self.warnings.append("⚠️ SKILL.md 文件过短")
            elif len(content) > 5000:
                self.warnings.append("⚠️ SKILL.md 文件过长")
            else:
                self.results.append(f"✅ SKILL.md 文件大小适中: {len(content)} 字符")
            
            # 检查必要章节
            required_sections = [
                "快速开始", "工作流程", "使用示例",
                "触发指令", "Token 效率"
            ]
            
            for section in required_sections:
                if section in content:
                    self.results.append(f"✅ 存在章节: {section}")
                else:
                    self.warnings.append(f"⚠️ 缺失章节: {section}")
            
            # 检查 Mermaid 图表
            if "```mermaid" in content:
                self.results.append("✅ 包含 Mermaid 图表")
            else:
                self.warnings.append("⚠️ 建议添加 Mermaid 图表")
                
        except Exception as e:
            self.errors.append(f"❌ 测试 SKILL.md 时出错: {e}")
    
    def test_references(self):
        """测试 references 目录"""
        references_path = self.skill_dir / "references"
        
        if not references_path.exists():
            return
        
        print("\n🧪 测试 references 目录")
        
        # 检查指南文件
        guide_path = references_path / "guide.md"
        if guide_path.exists():
            self.results.append("✅ 存在: references/guide.md")
            
            # 检查指南内容
            try:
                with open(guide_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if len(content) < 100:
                    self.warnings.append("⚠️ guide.md 文件过短")
                else:
                    self.results.append(f"✅ guide.md 文件大小适中: {len(content)} 字符")
                    
            except Exception as e:
                self.errors.append(f"❌ 测试 guide.md 时出错: {e}")
        else:
            self.errors.append("❌ 缺失: references/guide.md")
    
    def run_all_tests(self):
        """运行所有测试"""
        print("=" * 60)
        print(f"🚀 开始测试技能: {self.skill_dir.name}")
        print("=" * 60)
        
        self.test_structure()
        self.test_metadata()
        self.test_skill_md()
        self.test_references()
        
        self.print_results()
    
    def print_results(self):
        """打印测试结果"""
        print("\n" + "=" * 60)
        print("📋 测试结果汇总")
        print("=" * 60)
        
        if self.results:
            print("\n✅ 通过测试:")
            for result in self.results:
                print(f"  {result}")
        
        if self.warnings:
            print("\n⚠️ 警告:")
            for warning in self.warnings:
                print(f"  {warning}")
        
        if self.errors:
            print("\n❌ 错误:")
            for error in self.errors:
                print(f"  {error}")
        
        total_tests = len(self.results) + len(self.warnings) + len(self.errors)
        pass_rate = len(self.results) / total_tests * 100 if total_tests > 0 else 0
        
        print(f"\n📊 统计信息:")
        print(f"  总测试数: {total_tests}")
        print(f"  通过: {len(self.results)}")
        print(f"  警告: {len(self.warnings)}")
        print(f"  错误: {len(self.errors)}")
        print(f"  通过率: {pass_rate:.1f}%")
        
        if len(self.errors) == 0:
            print("\n🎉 所有测试通过!")
        else:
            print(f"\n❌ 测试失败: {len(self.errors)} 个错误")
        
        print("=" * 60 + "\n")
        
        return len(self.errors) == 0

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='Super Skills 测试框架')
    parser.add_argument('skill', nargs='?', default='all', help='技能名称或 "all" 测试所有技能')
    args = parser.parse_args()
    
    skills_dir = Path('skills')
    
    if not skills_dir.exists():
        print("❌ 错误: skills 目录不存在")
        sys.exit(1)
    
    if args.skill == 'all':
        # 测试所有技能
        skill_dirs = [d for d in skills_dir.iterdir() if d.is_dir()]
        print(f"\n📋 测试所有技能: {len(skill_dirs)} 个技能")
        
        all_passed = True
        for skill_dir in skill_dirs:
            tester = SkillTester(skill_dir)
            passed = tester.run_all_tests()
            if not passed:
                all_passed = False
        
        print("=" * 60)
        print("🏁 测试完成")
        print("=" * 60)
        
        if all_passed:
            print("🎉 所有技能测试通过!")
            sys.exit(0)
        else:
            print("❌ 部分技能测试失败")
            sys.exit(1)
    else:
        # 测试单个技能
        skill_dir = skills_dir / args.skill
        
        if not skill_dir.exists():
            print(f"❌ 错误: 技能目录不存在: {args.skill}")
            sys.exit(1)
        
        tester = SkillTester(skill_dir)
        passed = tester.run_all_tests()
        
        if passed:
            sys.exit(0)
        else:
            sys.exit(1)

if __name__ == "__main__":
    main()