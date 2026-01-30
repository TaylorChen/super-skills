# API 设计指导文档

全面的 API 设计指南,涵盖 RESTful、GraphQL 和 gRPC 三种主流 API 设计范式。

## RESTful API 设计

### 核心原则

1. **资源导向**: URL 表示资源,HTTP 方法表示操作
2. **无状态**: 每个请求包含所有必要信息
3. **统一接口**: 使用标准 HTTP 方法
4. **分层系统**: 支持缓存、负载均衡等中间层

### URL 设计规范

**资源命名:**

```
✅ 推荐:
GET    /api/v1/users              # 获取用户列表
GET    /api/v1/users/123          # 获取单个用户
POST   /api/v1/users              # 创建用户
PUT    /api/v1/users/123          # 更新用户
DELETE /api/v1/users/123          # 删除用户
GET    /api/v1/users/123/orders   # 获取用户的订单

❌ 避免:
GET    /api/v1/getUsers           # 不要在 URL 中使用动词
POST   /api/v1/user/create        # 不要使用动词
GET    /api/v1/users/delete/123   # 删除应该用 DELETE 方法
```

**命名规则:**

- 使用复数名词 (`users` 而非 `user`)
- 使用小写字母和连字符 (`user-profiles` 而非 `userProfiles`)
- 避免深层嵌套 (最多 3 层)

### HTTP 方法

| 方法 | 用途 | 幂等性 | 安全性 |
| --- | --- | --- | --- |
| GET | 获取资源 | ✅ | ✅ |
| POST | 创建资源 | ❌ | ❌ |
| PUT | 完整更新资源 | ✅ | ❌ |
| PATCH | 部分更新资源 | ❌ | ❌ |
| DELETE | 删除资源 | ✅ | ❌ |

### 状态码规范

**成功响应:**

| 状态码 | 含义 | 使用场景 |
| --- | --- | --- |
| 200 OK | 成功 | GET、PUT、PATCH 成功 |
| 201 Created | 已创建 | POST 创建成功 |
| 204 No Content | 无内容 | DELETE 成功 |

**客户端错误:**

| 状态码 | 含义 | 使用场景 |
| --- | --- | --- |
| 400 Bad Request | 请求错误 | 参数校验失败 |
| 401 Unauthorized | 未认证 | 缺少或无效的认证信息 |
| 403 Forbidden | 无权限 | 认证成功但无权限 |
| 404 Not Found | 未找到 | 资源不存在 |
| 409 Conflict | 冲突 | 资源状态冲突 |
| 422 Unprocessable Entity | 无法处理 | 业务逻辑错误 |
| 429 Too Many Requests | 请求过多 | 触发限流 |

**服务器错误:**

| 状态码 | 含义 | 使用场景 |
| --- | --- | --- |
| 500 Internal Server Error | 服务器错误 | 未预期的错误 |
| 502 Bad Gateway | 网关错误 | 上游服务错误 |
| 503 Service Unavailable | 服务不可用 | 服务维护或过载 |

### 请求和响应格式

**请求示例:**

```http
POST /api/v1/users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "SecurePass123!"
}
```

**成功响应:**

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "id": "123",
    "username": "john_doe",
    "email": "john@example.com",
    "created_at": "2024-01-29T15:30:00Z"
  },
  "timestamp": "2024-01-29T15:30:00Z",
  "request_id": "req_abc123"
}
```

**错误响应:**

```json
{
  "code": 40001,
  "message": "Validation failed",
  "errors": [
    {
      "field": "email",
      "message": "Email already exists"
    }
  ],
  "timestamp": "2024-01-29T15:30:00Z",
  "request_id": "req_abc123"
}
```

### 分页

**查询参数方式:**

```
GET /api/v1/users?page=2&page_size=20
```

**响应格式:**

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [...],
    "pagination": {
      "page": 2,
      "page_size": 20,
      "total": 100,
      "total_pages": 5
    }
  }
}
```

**游标分页 (推荐用于大数据集):**

```
GET /api/v1/users?cursor=eyJpZCI6MTIzfQ&limit=20
```

### 过滤和排序

**过滤:**

```
GET /api/v1/users?status=active&role=admin
GET /api/v1/users?created_after=2024-01-01
```

**排序:**

```
GET /api/v1/users?sort=created_at:desc
GET /api/v1/users?sort=name:asc,created_at:desc
```

**字段选择:**

```
GET /api/v1/users?fields=id,username,email
```

### 版本控制

**URL 版本 (推荐):**

```
GET /api/v1/users
GET /api/v2/users
```

**Header 版本:**

```
GET /api/users
Accept: application/vnd.example.v1+json
```

### 认证和授权

**Bearer Token (推荐):**

```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**API Key:**

```http
X-API-Key: your_api_key_here
```

### 限流

**响应头:**

```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1640995200
```

**超限响应:**

```json
{
  "code": 42901,
  "message": "Rate limit exceeded",
  "retry_after": 60
}
```

## GraphQL API 设计

### Schema 设计

**类型定义:**

```graphql
type User {
  id: ID!
  username: String!
  email: String!
  profile: Profile
  posts: [Post!]!
  createdAt: DateTime!
}

type Profile {
  bio: String
  avatar: String
  website: String
}

type Post {
  id: ID!
  title: String!
  content: String!
  author: User!
  publishedAt: DateTime
}
```

**查询:**

```graphql
type Query {
  user(id: ID!): User
  users(
    page: Int = 1
    pageSize: Int = 20
    filter: UserFilter
  ): UserConnection!
  
  post(id: ID!): Post
  posts(authorId: ID): [Post!]!
}

input UserFilter {
  status: UserStatus
  role: UserRole
  createdAfter: DateTime
}

type UserConnection {
  edges: [UserEdge!]!
  pageInfo: PageInfo!
  totalCount: Int!
}

type UserEdge {
  node: User!
  cursor: String!
}

type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}
```

**变更:**

```graphql
type Mutation {
  createUser(input: CreateUserInput!): CreateUserPayload!
  updateUser(id: ID!, input: UpdateUserInput!): UpdateUserPayload!
  deleteUser(id: ID!): DeleteUserPayload!
}

input CreateUserInput {
  username: String!
  email: String!
  password: String!
}

type CreateUserPayload {
  user: User
  errors: [Error!]
}

type Error {
  field: String
  message: String!
}
```

### 查询示例

```graphql
query GetUser {
  user(id: "123") {
    id
    username
    email
    profile {
      bio
      avatar
    }
    posts {
      id
      title
      publishedAt
    }
  }
}
```

### 最佳实践

1. **使用 Relay 规范**: Connection、Edge、PageInfo
2. **避免 N+1 查询**: 使用 DataLoader
3. **限制查询深度**: 防止恶意深层嵌套查询
4. **使用枚举**: 而非字符串常量
5. **错误处理**: 返回结构化错误信息

## gRPC API 设计

### Protocol Buffers 定义

```protobuf
syntax = "proto3";

package user.v1;

option go_package = "github.com/example/user/v1;userv1";

// 用户服务
service UserService {
  // 获取用户
  rpc GetUser(GetUserRequest) returns (GetUserResponse);
  
  // 列出用户
  rpc ListUsers(ListUsersRequest) returns (ListUsersResponse);
  
  // 创建用户
  rpc CreateUser(CreateUserRequest) returns (CreateUserResponse);
  
  // 更新用户
  rpc UpdateUser(UpdateUserRequest) returns (UpdateUserResponse);
  
  // 删除用户
  rpc DeleteUser(DeleteUserRequest) returns (DeleteUserResponse);
  
  // 流式接口
  rpc StreamUsers(StreamUsersRequest) returns (stream User);
}

// 用户消息
message User {
  string id = 1;
  string username = 2;
  string email = 3;
  Profile profile = 4;
  int64 created_at = 5;
}

message Profile {
  string bio = 1;
  string avatar = 2;
  string website = 3;
}

// 请求消息
message GetUserRequest {
  string id = 1;
}

message GetUserResponse {
  User user = 1;
}

message ListUsersRequest {
  int32 page = 1;
  int32 page_size = 2;
  UserFilter filter = 3;
}

message ListUsersResponse {
  repeated User users = 1;
  int32 total = 2;
}

message UserFilter {
  optional string status = 1;
  optional string role = 2;
}

message CreateUserRequest {
  string username = 1;
  string email = 2;
  string password = 3;
}

message CreateUserResponse {
  User user = 1;
}
```

### 错误处理

```protobuf
// 使用 google.rpc.Status
import "google/rpc/status.proto";

message CreateUserResponse {
  oneof result {
    User user = 1;
    google.rpc.Status error = 2;
  }
}
```

### 最佳实践

1. **使用语义化版本**: `user.v1`, `user.v2`
2. **字段编号规划**: 预留字段编号空间
3. **使用 optional**: 明确可选字段
4. **避免嵌套过深**: 保持消息结构扁平
5. **使用流式 RPC**: 处理大量数据

## API 文档

### OpenAPI (Swagger) 示例

```yaml
openapi: 3.0.0
info:
  title: User API
  version: 1.0.0
  description: 用户管理 API

servers:
  - url: https://api.example.com/v1
    description: 生产环境
  - url: https://api-staging.example.com/v1
    description: 测试环境

paths:
  /users:
    get:
      summary: 获取用户列表
      parameters:
        - name: page
          in: query
          schema:
            type: integer
            default: 1
        - name: page_size
          in: query
          schema:
            type: integer
            default: 20
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserListResponse'
    
    post:
      summary: 创建用户
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
      responses:
        '201':
          description: 创建成功
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserResponse'

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: string
        username:
          type: string
        email:
          type: string
          format: email
        created_at:
          type: string
          format: date-time
    
    CreateUserRequest:
      type: object
      required:
        - username
        - email
        - password
      properties:
        username:
          type: string
          minLength: 3
          maxLength: 20
        email:
          type: string
          format: email
        password:
          type: string
          minLength: 8
  
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

security:
  - bearerAuth: []
```

## API 安全

### 认证

1. **JWT Token**: 无状态认证
2. **OAuth 2.0**: 第三方授权
3. **API Key**: 简单场景

### 授权

1. **RBAC**: 基于角色的访问控制
2. **ABAC**: 基于属性的访问控制
3. **资源级权限**: 细粒度控制

### 安全最佳实践

- ✅ 使用 HTTPS
- ✅ 验证所有输入
- ✅ 防止 SQL 注入
- ✅ 防止 XSS 攻击
- ✅ 实施限流
- ✅ 记录审计日志
- ✅ 敏感数据加密

## 性能优化

### 缓存策略

**HTTP 缓存头:**

```http
Cache-Control: public, max-age=3600
ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
Last-Modified: Wed, 21 Oct 2024 07:28:00 GMT
```

**条件请求:**

```http
If-None-Match: "33a64df551425fcc55e4d42a148795d9f25f89d4"
If-Modified-Since: Wed, 21 Oct 2024 07:28:00 GMT
```

### 批量操作

```http
POST /api/v1/users/batch
Content-Type: application/json

{
  "operations": [
    {"method": "create", "data": {...}},
    {"method": "update", "id": "123", "data": {...}},
    {"method": "delete", "id": "456"}
  ]
}
```

### 异步处理

```http
POST /api/v1/users/import
Content-Type: application/json

{
  "file_url": "https://example.com/users.csv"
}

# 响应
HTTP/1.1 202 Accepted
Location: /api/v1/jobs/abc123

{
  "job_id": "abc123",
  "status": "pending"
}
```

## 测试

### 单元测试

测试 API 处理逻辑:
- 参数验证
- 业务逻辑
- 错误处理

### 集成测试

测试 API 端到端流程:
- 请求/响应格式
- 状态码
- 数据库交互

### 契约测试

使用 Pact 等工具确保 API 契约一致性。

## 监控

### 关键指标

- **可用性**: 99.9% SLA
- **响应时间**: P95 < 200ms
- **错误率**: < 0.1%
- **吞吐量**: QPS

### 日志

```json
{
  "timestamp": "2024-01-29T15:30:00Z",
  "request_id": "req_abc123",
  "method": "POST",
  "path": "/api/v1/users",
  "status": 201,
  "duration_ms": 45,
  "user_id": "user_123",
  "ip": "192.168.1.1"
}
```



## 7. 典型认证授权流程图

```mermaid
sequenceDiagram
    participant User as 用户/客户端
    participant App as 应用服务器
    participant Auth as 认证中心 (OIDC/OAuth)
    participant DB as 数据库

    User->>App: 1. 访问受保护资源
    App-->>User: 2. 401 Unauthorized (跳转认证)
    User->>Auth: 3. 提交凭据 (用户名/密码)
    Auth->>Auth: 4. 验证凭据
    Auth-->>User: 5. 返回 Access Token / ID Token
    User->>App: 6. 携带 Token 请求
    App->>App: 7. 验证 Token 有效性/权限
    App->>DB: 8. 执行业务逻辑
    DB-->>App: 9. 返回数据
    App-->>User: 10. 200 OK (交付资源)
```