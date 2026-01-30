#!/usr/bin/env python3
"""
Token Optimizer for Super Skills
使用 tiktoken 精确计算每个 skill 的 token 消耗
"""

import os
import glob
from pathlib import Path

try:
    import tiktoken
    HAS_TIKTOKEN = True
except ImportError:
    HAS_TIKTOKEN = False
    print("⚠️  警告: 未安装 tiktoken,使用简化估算")
    print("💡 提示: 运行 'pip install tiktoken' 获取精确计算\n")

def count_tokens_accurate(text, model="gpt-4"):
    """使用 tiktoken 精确计算 tokens"""
    if HAS_TIKTOKEN:
        try:
            encoding = tiktoken.encoding_for_model(model)
            return len(encoding.encode(text))
        except Exception:
            # Fallback to simple estimation
            return len(text) // 2
    else:
        # Simple estimation: chars / 2
        return len(text) // 2

def check_budget(skill_name, main_tokens, ref_tokens):
    """检查 token 预算并给出警告"""
    total = main_tokens + ref_tokens
    warnings = []
    
    if main_tokens > 500:
        warnings.append(f"⚠️  主文件超出建议值 ({main_tokens} > 500 tokens)")
    
    if total > 10000:
        warnings.append(f"🔴 总计超出 10k tokens ({total})")
    elif total > 5000:
        warnings.append(f"🟡 总计较高 ({total} tokens)")
    
    return warnings

def scan_skills():
    """扫描所有 skills 并统计 token 消耗"""
    print(f"{'Skill Name':<30} | {'Main':<8} | {'Refs':<8} | {'Total':<8} | {'Status'}")
    print("-" * 85)

    skills_dir = Path("skills")
    all_total = 0
    warnings_count = 0

    for skill in sorted(skills_dir.iterdir()):
        if not skill.is_dir():
            continue
        
        skill_name = skill.name

        # Main skill file
        main_file = skill / "SKILL.md"
        main_tokens = 0
        if main_file.exists():
            with open(main_file, 'r', encoding='utf-8') as f:
                main_tokens = count_tokens_accurate(f.read())

        # Reference files
        ref_dir = skill / "references"
        ref_tokens = 0
        if ref_dir.exists():
            for ref_file in ref_dir.glob("*.md"):
                with open(ref_file, 'r', encoding='utf-8') as f:
                    ref_tokens += count_tokens_accurate(f.read())

        total = main_tokens + ref_tokens
        all_total += total
        
        # Check budget and get warnings
        warnings = check_budget(skill_name, main_tokens, ref_tokens)
        status = "✅" if not warnings else "⚠️ "
        
        print(f"{skill_name:<30} | {main_tokens:<8} | {ref_tokens:<8} | {total:<8} | {status}")
        
        if warnings:
            for warning in warnings:
                print(f"  → {warning}")
            warnings_count += 1

    print("-" * 85)
    print(f"\n📊 统计:")
    print(f"  总 Skills: {len(list(skills_dir.iterdir()))}")
    print(f"  总 Tokens: {all_total:,}")
    print(f"  平均 Tokens: {all_total // len(list(skills_dir.iterdir())):,}")
    print(f"  需要优化: {warnings_count} 个")
    
    print("\n💡 建议:")
    print("  - 主文件 (SKILL.md) 应保持在 500 tokens 以内")
    print("  - 单个 reference 文件建议 600-1500 tokens")
    print("  - 总计超过 10k tokens 的 skill 应考虑拆分")
    
    if HAS_TIKTOKEN:
        print("\n✅ 使用 tiktoken 精确计算")
    else:
        print("\n⚠️  使用简化估算 (安装 tiktoken 获取精确结果)")

if __name__ == "__main__":
    if not Path("skills").exists():
        print("❌ 错误: skills 目录不存在")
        print("💡 提示: 请在项目根目录运行此脚本")
    else:
        scan_skills()
