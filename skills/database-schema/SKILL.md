# 数据库设计

系统化的数据库设计方法,涵盖建模、范式化、索引优化和查询性能调优。

## 加载文件
- [ ] [references/guide.md](references/guide.md) - 包含建模、范式、索引方案及高级调优的完整指南
- [ ] [references/guide_EN.md](references/guide_EN.md) - English version of the guide
## 可用指导
**[references/guide.md](references/guide.md)** - 深入讲解如何平衡范式与反范式、索引设计的黄金法则、如何通过 EXPLAIN 执行计划识别系统瓶颈,以及应对海量数据的分库分表实战建议。
## 相关 Skills
| Skill | 用途 |
| --- | --- |
| **api-design** | 定义与数据库交互的数据接口 |
| **performance-tuning** | 系统整体性能瓶颈排查 |
| **technical-design** | 基础设施及中间件选型 |
## 检查清单
- [ ] 表名和字段名是否遵循统一的命名规范 (如小写加下划线)?
- [ ] 每个表是否都包含 `id`, `created_at`, `updated_at` 基础字段?
- [ ] 是否为高频查询字段建立了合适的索引?
- [ ] 索引是否避免了冗余及过度设计?
- [ ] 对于大表分页,是否采用了游标分页 (Seek Method) 而非深偏移?
## 触发指令
## Token 效率