# 产品需求文档撰写

PRD 编写、AC 定义及测试用例。

## 快速开始

### 5 步上手

1. **准备输入** - 明确要开发的功能或产品
2. **触发技能** - 在 AI 工具中输入 `/product-requirements-full`
3. **描述需求** - 简要说明功能背景和目标
4. **生成文档** - AI 自动生成完整 PRD
5. **迭代优化** - 根据反馈调整需求细节

### 使用示例

```
/product-requirements-full
我需要为"用户自助重置密码"功能编写 PRD，包括邮件验证、手机验证两种方式
```

## 工作流程

```mermaid
graph LR
    A[需求输入] --> B[用户研究]
    B --> C[需求分析]
    C --> D[PRD编写]
    D --> E[验收标准定义]
    E --> F[质量检查]
    F --> G[输出文档]
    
    style A fill:#e1f5ff
    style G fill:#c8e6c9
```

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

## 最佳实践

### 需求定义
- ✅ 使用 SMART 原则定义目标
- ✅ 明确用户画像和使用场景
- ✅ 区分功能需求和非功能需求

### 优先级管理
- ✅ P0: 必须实现的核心功能
- ✅ P1: 重要但可延后的功能
- ✅ P2: 锦上添花的增强功能

### 验收标准
- ✅ 使用 Given-When-Then 格式
- ✅ 确保标准可测试、可验证
- ✅ 覆盖正常流程和异常场景

## 常见问题

**Q: 如何确定需求的优先级?**
A: 参考 MoSCoW 方法：Must have (P0)、Should have (P1)、Could have (P2)、Won't have (暂不实现)

**Q: PRD 应该多详细?**
A: 根据团队规模和项目复杂度调整。小团队可简化，大项目需要更详细的技术规范

**Q: 如何处理需求变更?**
A: 建立需求变更流程，评估影响范围，更新版本号，通知相关干系人

**Q: 验收标准怎么写才清晰?**
A: 使用 BDD 格式："Given [前置条件], When [执行操作], Then [预期结果]"

## 触发指令

⚠️ **Prompt-as-Code (v5.0)**: 触发指令已迁移至 `metadata.json`。支持：
- `/product-requirements-full` - 引导编写完整 PRD
- `/product-requirements-quick` - 快速检查需求逻辑

## Token 效率

- 主 Skill 文件: ~300 tokens
- 参考指南总计: ~4k+ tokens
