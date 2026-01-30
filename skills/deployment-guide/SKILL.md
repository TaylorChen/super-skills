# 部署指南

全面的部署指南,涵盖 CI/CD 流程、容器化和编排。

## 加载文件
- [ ] [references/guide.md](references/guide.md) - 主要指导文档
## 可用指导
**[references/guide.md](references/guide.md)** - 包含部署指南的系统化指导、必备工具清单及关键质量控制点。
## 相关 Skills
| Skill | 用途 |
| --- | --- |
| **monitoring-setup** | 部署后的服务观测及告警 |
| **technical-design** | 部署架构的整体方案设计 |
## 检查清单
- [ ] 是否明确了当前任务的核心目标?
- [ ] 是否遵循了行业标准的实施流程?
- [ ] 产出物是否经过了基本的质量评审?
- [ ] 关键数据或配置是否已进行备份或版本化?
## 触发指令
- **设计 CI/CD 流水线**: `/deployment-guide 为我的[技术栈]项目设计一套 GitHub Actions 自动化部署流程,包含构建、测试及镜像推送。`
- **K8s 部署配置**: `/deployment-guide 请为我的微服务编写标准的 Kubernetes Deployment 和 Service YAML 定义,确保包含健康检查探针。`
## Token 效率