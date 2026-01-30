# API 设计规范

RESTful, GraphQL, gRPC 设计指南。

## 加载文件
- [AGENTS.md](AGENTS.md) (核心规则)
- [references/guide.md](references/guide.md) (设计指南)
- [rules/use-nouns-for-resources.md](rules/use-nouns-for-resources.md)
- [rules/implement-idempotency.md](rules/implement-idempotency.md)

## 相关 Skills
- **database-schema**, **technical-design**, **documentation**

## 示例
- 📄 [restful-api-sample.md](../../resources/examples/api-design/restful-api-sample.md)
- 📄 [api-spec-sample.yaml](../../resources/examples/api-design/api-spec-sample.yaml)

## 检查清单
- [ ] URL 名词复数 (如 `/users`)
- [ ] HTTP 方法正确 (GET/POST/PUT/DELETE)
- [ ] 标准 HTTP 状态码 (201, 204, 422)
- [ ] 响应包含统一的 request_id
- [ ] 接口版本控制 (`/v1/`)

## 触发指令
- `/api-design-full`
- `/api-design-quick`
