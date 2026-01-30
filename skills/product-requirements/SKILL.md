# 产品需求文档撰写

PRD 编写、AC 定义及测试用例。

## 加载文件
- [references/prd-template.md](references/prd-template.md)
- [references/user-research.md](references/user-research.md)
- [references/requirements-analysis.md](references/requirements-analysis.md)
- [references/acceptance-criteria.md](references/acceptance-criteria.md)

## 相关 Skills
- **user-story**, **competitive-analysis**, **technical-design**

## 示例
- 📄 [prd-sample.md](../../resources/examples/product-requirements/prd-sample.md)

## 检查清单
- [ ] 背景、目标、KPI 是否清晰
- [ ] 优先级 (P0-P2) 及 AC (Given-When-Then)
- [ ] 覆盖异常流程及 Corner Cases

## 触发指令
- `/product-requirements-full`
- `/product-requirements-quick`

## 检查清单

### 内容完整性
- [ ] 明确“为什么做”(背景)及“做成什么样”(目标)
- [ ] 定义核心 KPI
- [ ] 功能描述清晰无歧义

### 质量控制
- [ ] 优先级 (P0/P1/P2) 已确认
- [ ] 配备可测量的验收标准 (BDD)
- [ ] 覆盖极端场景 (Corner Cases)

## 触发指令

⚠️ **Prompt-as-Code (v5.0)**: 触发指令已迁移至 `metadata.json`。支持：
- `/product-requirements-full` - 引导编写完整 PRD
- `/product-requirements-quick` - 快速检查需求逻辑

## Token 效率

- 主 Skill 文件: ~300 tokens
- 参考指南总计: ~4k+ tokens
