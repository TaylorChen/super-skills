#!/usr/bin/env python3
"""
Super Skills 使用数据分析系统
收集和分析技能使用情况
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime, timedelta

class SkillsAnalytics:
    """技能使用数据分析类"""
    
    def __init__(self):
        self.data_dir = Path('data/analytics')
        self.config_path = Path('scripts/analytics-config.json')
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
    def record_usage(self, skill_name, duration=None, success=True, feedback=None):
        """记录技能使用情况"""
        today = datetime.now().strftime('%Y-%m-%d')
        data_file = self.data_dir / f"{today}.json"
        
        # 读取现有数据
        if data_file.exists():
            with open(data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            data = {
                "date": today,
                "usage_records": []
            }
        
        # 添加新记录
        record = {
            "timestamp": datetime.now().isoformat(),
            "skill_name": skill_name,
            "duration": duration,
            "success": success,
            "feedback": feedback
        }
        
        data["usage_records"].append(record)
        
        # 写入数据
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 记录技能使用: {skill_name}")
    
    def analyze_usage(self, days=7):
        """分析最近几天的使用情况"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days-1)
        
        all_records = []
        
        # 收集指定时间范围内的数据
        for i in range(days):
            date = (start_date + timedelta(days=i)).strftime('%Y-%m-%d')
            data_file = self.data_dir / f"{date}.json"
            
            if data_file.exists():
                try:
                    with open(data_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    all_records.extend(data.get("usage_records", []))
                except Exception as e:
                    pass
        
        if not all_records:
            return "❌ 没有找到使用记录"
        
        # 分析数据
        analysis = {
            "total_usage": len(all_records),
            "skills_used": set(),
            "success_count": 0,
            "failure_count": 0,
            "total_duration": 0,
            "usage_by_skill": {},
            "success_rate_by_skill": {},
            "average_duration_by_skill": {}
        }
        
        for record in all_records:
            skill = record["skill_name"]
            analysis["skills_used"].add(skill)
            
            if record["success"]:
                analysis["success_count"] += 1
            else:
                analysis["failure_count"] += 1
            
            if record["duration"]:
                analysis["total_duration"] += record["duration"]
            
            # 按技能统计
            if skill not in analysis["usage_by_skill"]:
                analysis["usage_by_skill"][skill] = 0
                analysis["success_rate_by_skill"][skill] = {"success": 0, "total": 0}
                analysis["average_duration_by_skill"][skill] = {"total": 0, "count": 0}
            
            analysis["usage_by_skill"][skill] += 1
            analysis["success_rate_by_skill"][skill]["total"] += 1
            if record["success"]:
                analysis["success_rate_by_skill"][skill]["success"] += 1
            
            if record["duration"]:
                analysis["average_duration_by_skill"][skill]["total"] += record["duration"]
                analysis["average_duration_by_skill"][skill]["count"] += 1
        
        # 计算成功率和平均时长
        for skill in analysis["success_rate_by_skill"]:
            total = analysis["success_rate_by_skill"][skill]["total"]
            success = analysis["success_rate_by_skill"][skill]["success"]
            analysis["success_rate_by_skill"][skill] = (success / total * 100) if total > 0 else 0
        
        for skill in analysis["average_duration_by_skill"]:
            total = analysis["average_duration_by_skill"][skill]["total"]
            count = analysis["average_duration_by_skill"][skill]["count"]
            analysis["average_duration_by_skill"][skill] = (total / count) if count > 0 else 0
        
        return analysis
    
    def generate_report(self, days=7):
        """生成分析报告"""
        analysis = self.analyze_usage(days)
        
        if isinstance(analysis, str):  # 错误消息
            return analysis
        
        report = f"# 技能使用分析报告\n\n"
        report += f"## 总体统计\n"
        report += f"- **总使用次数**: {analysis['total_usage']}\n"
        report += f"- **使用技能数**: {len(analysis['skills_used'])}\n"
        report += f"- **成功率**: {(analysis['success_count'] / analysis['total_usage'] * 100):.1f}%\n"
        report += f"- **平均使用时长**: {analysis['total_duration'] / analysis['total_usage']:.1f} 秒\n\n"
        
        report += "## 使用频率最高的技能\n"
        sorted_skills = sorted(analysis['usage_by_skill'].items(), key=lambda x: x[1], reverse=True)
        for skill, count in sorted_skills[:5]:
            percentage = (count / analysis['total_usage'] * 100):.1f
            report += f"- **{skill}**: {count} 次 ({percentage}%)\n"
        report += "\n"
        
        report += "## 成功率最高的技能\n"
        sorted_success = sorted(analysis['success_rate_by_skill'].items(), key=lambda x: x[1], reverse=True)
        for skill, rate in sorted_success[:5]:
            report += f"- **{skill}**: {rate:.1f}%\n"
        report += "\n"
        
        report += "## 平均使用时长\n"
        sorted_duration = sorted(analysis['average_duration_by_skill'].items(), key=lambda x: x[1], reverse=True)
        for skill, duration in sorted_duration[:5]:
            report += f"- **{skill}**: {duration:.1f} 秒\n"
        report += "\n"
        
        report += "## 改进建议\n"
        # 识别使用率低的技能
        low_usage_skills = [s for s, c in analysis['usage_by_skill'].items() if c < 3]
        if low_usage_skills:
            report += f"- **使用率低的技能**: {', '.join(low_usage_skills)}\n"
            report += "  建议: 优化技能描述、添加更多示例或提高技能质量\n"
        
        # 识别成功率低的技能
        low_success_skills = [s for s, r in analysis['success_rate_by_skill'].items() if r < 70]
        if low_success_skills:
            report += f"- **成功率低的技能**: {', '.join(low_success_skills)}\n"
            report += "  建议: 改进技能逻辑、增加错误处理或提供更清晰的使用指导\n"
        
        # 识别使用时长长的技能
        long_duration_skills = [s for s, d in analysis['average_duration_by_skill'].items() if d > 30]
        if long_duration_skills:
            report += f"- **使用时长长的技能**: {', '.join(long_duration_skills)}\n"
            report += "  建议: 优化技能执行效率、减少不必要的步骤或提供进度反馈\n"
        
        return report
    
    def export_data(self, days=30, format='json'):
        """导出使用数据"""
        analysis = self.analyze_usage(days)
        
        if isinstance(analysis, str):  # 错误消息
            return analysis
        
        export_file = self.data_dir / f"export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{format}"
        
        if format == 'json':
            with open(export_file, 'w', encoding='utf-8') as f:
                json.dump(analysis, f, ensure_ascii=False, indent=2)
        elif format == 'markdown':
            report = self.generate_report(days)
            with open(export_file, 'w', encoding='utf-8') as f:
                f.write(report)
        
        print(f"✅ 导出数据到: {export_file}")
        return f"数据已导出到: {export_file}"

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='Super Skills 使用数据分析系统')
    parser.add_argument('--record', '-r', help='记录技能使用')
    parser.add_argument('--duration', '-d', type=float, help='使用时长（秒）')
    parser.add_argument('--success', '-s', type=lambda x: x.lower() == 'true', default=True, help='是否成功')
    parser.add_argument('--feedback', '-f', help='用户反馈')
    parser.add_argument('--analyze', '-a', type=int, default=7, help='分析最近几天的数据')
    parser.add_argument('--export', '-e', type=int, help='导出最近几天的数据')
    parser.add_argument('--format', '-t', choices=['json', 'markdown'], default='json', help='导出格式')
    args = parser.parse_args()
    
    analytics = SkillsAnalytics()
    
    if args.record:
        # 记录技能使用
        analytics.record_usage(args.record, args.duration, args.success, args.feedback)
    
    elif args.export:
        # 导出数据
        result = analytics.export_data(args.export, args.format)
        print(result)
    
    else:
        # 分析数据
        report = analytics.generate_report(args.analyze)
        print(report)

if __name__ == "__main__":
    main()