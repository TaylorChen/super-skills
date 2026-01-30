---
description: 从功能构思到代码实现的全链路工作流
---

# 功能开发全链路工作流

本文档定义了从一个模糊的功能点创意到最终代码实现的标准化协作流程。

## 阶段 1: 需求定义与竞品研究
1. 唤醒 `competitive-analysis` 技能,对该功能的市场同类产品进行 SWOT 分析。
2. 唤醒 `product-requirements` 技能,按照 `prd-template.md` 编写 PRD。
3. 加载 `user-story/AGENTS.md`,确保故事拆分严格遵循 **INVEST 原则 [us-001]** 并编写 **BDD 验收标准 [us-002]**。

## 阶段 2: 方案设计与接口定义
1. 加载 `technical-design/AGENTS.md`,优先执行 **无单点故障检查 [td-001]** 和 **熔断机制设计 [td-002]**。
2. 加载 `database-schema/AGENTS.md`,重点规避 **N+1 查询 [db-001]** 并应用 **最左前缀索引原则 [db-002]**。
3. 加载 `api-design/AGENTS.md`,应用 **资源名词化规范 [api-001]** 及 **幂等性保障 [api-002]**。

## 阶段 3: 开发、测试与部署
1. 唤醒 `testing-strategy` 技能,制定测试金字塔策略。
2. 进行代码实现。
3. 加载 `code-review/AGENTS.md`,自动化扫描 **SQL 注入 [cr-001]** 及 **错误处理 [cr-002]**。
4. 唤醒 `deployment-guide` 技能,实施 CI/CD 自动化流水线。

## 阶段 4: 性能监测与优化
1. 唤醒 `monitoring-setup` 技能,配置关键业务指标和异常告警。
2. 唤醒 `performance-tuning` 技能,对上线后的接口性能进行基准测试和深度优化。
