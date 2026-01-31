# {{skill_title}}

{{skill_description}}

## 快速开始

### 5 步上手

1. **准备输入** - {{step1_description}}
2. **触发技能** - 在 AI 工具中输入 `{{skill_trigger}}`
3. **描述需求** - {{step3_description}}
4. **生成内容** - AI 自动生成{{output_description}}
5. **查看结果** - {{step5_description}}

### 使用示例

```
{{skill_trigger}}
{{example_prompt}}
```

## 工作流程

```mermaid
graph TD
    A[{{step1_title}}] --> B[{{step2_title}}]
    B --> C[{{step3_title}}]
    C --> D[{{step4_title}}]
    D --> E[{{step5_title}}]
    
    style A fill:#e1f5ff
    style E fill:#c8e6c9
```

## 加载文件
{{#each references}}
- [{{file}}]({{file}}) - {{description}}
{{/each}}

## 相关 Skills
{{#each related_skills}}
- **{{name}}** - {{description}}
{{/each}}

## 功能特性

{{#each features}}
- ✅ **{{title}}** - {{description}}
{{/each}}

## 检查清单
{{#each checklist}}
- [ ] {{item}}
{{/each}}

## 最佳实践

{{#each best_practices}}
### {{title}}
{{#each items}}
- ✅ {{item}}
{{/each}}
{{/each}}

## 常见问题

{{#each faq}}
**Q: {{question}}**
A: {{answer}}
{{/each}}

## 触发指令

{{#each triggers}}
- **{{trigger}}** - {{description}}
{{/each}}

## 输出示例

```
{{output_example}}
```

## Token 效率

- 主 Skill 文件: ~{{main_tokens}} tokens
- 参考指南总计: ~{{ref_tokens}} tokens
