# 监控配置

系统化的监控系统配置指南,涵盖指标收集、日志聚合和告警配置。

## 加载文件
- [ ] [references/guide.md](references/guide.md) - 主要指导文档
## 可用指导
**[references/guide.md](references/guide.md)** - 包含监控配置的系统化指导、必备工具清单及关键质量控制点。
## 相关 Skills
| Skill | 用途 |
| --- | --- |
| **deployment-guide** | 监控配置的自动化部署方案 |
| **performance-tuning** | 根据监控数据进行性能调优 |
## 检查清单
- [ ] 是否明确了当前任务的核心目标?
- [ ] 是否遵循了行业标准的实施流程?
- [ ] 产出物是否经过了基本的质量评审?
- [ ] 关键数据或配置是否已进行备份或版本化?
## 监控触发指令
- **设计指标监控**: `/monitoring-setup 针对[高并发业务],请列出必须采集的 5 个关键指标,并提供 Prometheus 的配置建议。`
- **告警规则编写**: `/monitoring-setup 请为我设计一套分级告警策略,确保核心链路(P0)报错能在 1 分钟内通知到对应负责人。`
## Token 效率