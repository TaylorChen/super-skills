# 技术方案设计

系统架构设计、技术选型及评估框架。

## 加载文件
- [AGENTS.md](AGENTS.md) (核心规则)
- [references/guide.md](references/guide.md) (完整指南)
- [rules/zero-spof.md](rules/zero-spof.md)
- [rules/circuit-breaker.md](rules/circuit-breaker.md)

## 相关 Skills
- **database-schema**, **api-design**, **deployment-guide**

## 示例
- 📄 [architecture-sample.md](../../resources/examples/technical-design/architecture-sample.md)

## 检查清单
- [ ] 设计满足吞吐量及响应时延要求
- [ ] 无单点故障，具备容灾能力
- [ ] 具备熔断、降级或限流机制
- [ ] 关键业务逻辑配备监控指标

## 触发指令
- `/technical-design-full`
- `/technical-design-quick`
