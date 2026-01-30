# 代码审查规范

高质量代码 Review 指南，涵盖安全性、性能及可维护性。

## 加载文件
- [AGENTS.md](AGENTS.md) (核心程序化规则)
- [references/guide.md](references/guide.md)
- [rules/avoid-sql-injection.md](rules/avoid-sql-injection.md)
- [rules/handle-errors-explicitly.md](rules/handle-errors-explicitly.md)

## 相关 Skills
- **testing-strategy**, **refactoring-guide**, **api-design**

## 示例
- 📄 [review-sample.md](../../resources/examples/code-review/review-sample.md)

## 检查清单
- [ ] 逻辑正确性及边界条件
- [ ] 安全漏洞 (SQL 注入, 凭证泄露等)
- [ ] 代码风格及可读性 (命名, DRY)
- [ ] 潜在性能瓶颈 (索引, 循环)

## 触发指令
- `/code-review-full`
- `/code-review-quick`
