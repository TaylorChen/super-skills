# API 设计示例 - 用户管理 RESTful API

> **场景描述**: 为 SaaS 平台设计用户管理相关的 RESTful API,包括注册、登录、个人信息管理等功能

## 背景

某 SaaS 平台需要设计一套完整的用户管理 API,要求:
- 支持邮箱/手机号注册
- JWT 认证机制
- 用户信息 CRUD 操作
- 符合 RESTful 规范
- 良好的错误处理

## 输入信息

**功能需求**:
1. 用户注册 (邮箱/手机号)
2. 用户登录/登出
3. 获取用户信息
4. 更新用户信息
5. 修改密码
6. 重置密码

**非功能需求**:
- 响应时间 < 200ms
- 支持并发 1000+ QPS
- 数据安全性高

## API 设计方案

### 1. 资源命名

遵循 RESTful 资源命名规范:

```
/api/v1/users          # 用户集合
/api/v1/users/{id}     # 单个用户
/api/v1/auth/login     # 认证相关
/api/v1/auth/logout
```

### 2. 端点设计

#### 2.1 用户注册

```http
POST /api/v1/users
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "username": "johndoe",
  "phone": "+86-13800138000"
}
```

**响应 (201 Created)**:
```json
{
  "code": 0,
  "message": "注册成功",
  "data": {
    "id": "usr_1a2b3c4d",
    "email": "user@example.com",
    "username": "johndoe",
    "created_at": "2026-01-30T12:15:58Z"
  }
}
```

#### 2.2 用户登录

```http
POST /api/v1/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```

**响应 (200 OK)**:
```json
{
  "code": 0,
  "message": "登录成功",
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIs...",
    "expires_in": 3600,
    "token_type": "Bearer"
  }
}
```

#### 2.3 获取用户信息

```http
GET /api/v1/users/{id}
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

**响应 (200 OK)**:
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "id": "usr_1a2b3c4d",
    "email": "user@example.com",
    "username": "johndoe",
    "phone": "+86-138****8000",
    "avatar": "https://cdn.example.com/avatars/usr_1a2b3c4d.jpg",
    "created_at": "2026-01-30T12:15:58Z",
    "updated_at": "2026-01-30T12:15:58Z"
  }
}
```

#### 2.4 更新用户信息

```http
PATCH /api/v1/users/{id}
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
Content-Type: application/json

{
  "username": "john_doe_new",
  "avatar": "https://cdn.example.com/avatars/new.jpg"
}
```

**响应 (200 OK)**:
```json
{
  "code": 0,
  "message": "更新成功",
  "data": {
    "id": "usr_1a2b3c4d",
    "username": "john_doe_new",
    "avatar": "https://cdn.example.com/avatars/new.jpg",
    "updated_at": "2026-01-30T13:20:00Z"
  }
}
```

#### 2.5 修改密码

```http
PUT /api/v1/users/{id}/password
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
Content-Type: application/json

{
  "old_password": "SecurePass123!",
  "new_password": "NewSecurePass456!"
}
```

**响应 (200 OK)**:
```json
{
  "code": 0,
  "message": "密码修改成功"
}
```

### 3. 错误处理

#### 3.1 错误码定义

| 错误码 | HTTP 状态 | 说明 |
|--------|-----------|------|
| 0 | 200 | 成功 |
| 1001 | 400 | 参数错误 |
| 1002 | 401 | 未认证 |
| 1003 | 403 | 无权限 |
| 1004 | 404 | 资源不存在 |
| 1005 | 409 | 资源冲突 (如邮箱已存在) |
| 1006 | 429 | 请求过于频繁 |
| 5000 | 500 | 服务器内部错误 |

#### 3.2 错误响应格式

```json
{
  "code": 1005,
  "message": "邮箱已被注册",
  "errors": [
    {
      "field": "email",
      "message": "该邮箱已被其他用户使用"
    }
  ],
  "request_id": "req_abc123",
  "timestamp": "2026-01-30T12:15:58Z"
}
```

### 4. 认证机制

#### JWT Token 结构

```json
{
  "header": {
    "alg": "HS256",
    "typ": "JWT"
  },
  "payload": {
    "sub": "usr_1a2b3c4d",
    "email": "user@example.com",
    "role": "user",
    "iat": 1706601358,
    "exp": 1706604958
  }
}
```

#### 认证流程

1. 用户登录成功后获得 access_token 和 refresh_token
2. 后续请求在 Header 中携带: `Authorization: Bearer {access_token}`
3. access_token 过期后使用 refresh_token 刷新
4. refresh_token 过期需重新登录

### 5. 分页与过滤

#### 获取用户列表

```http
GET /api/v1/users?page=1&page_size=20&sort=created_at&order=desc&status=active
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

**响应**:
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [...],
    "pagination": {
      "page": 1,
      "page_size": 20,
      "total": 150,
      "total_pages": 8
    }
  }
}
```

## 关键要点

- ✅ **资源命名**: 使用名词复数,避免动词
- ✅ **HTTP 方法**: GET (查询), POST (创建), PUT/PATCH (更新), DELETE (删除)
- ✅ **状态码**: 正确使用 HTTP 状态码 (200, 201, 400, 401, 404, 500)
- ✅ **版本控制**: URL 中包含版本号 `/api/v1/`
- ✅ **认证**: 使用 JWT Bearer Token
- ✅ **错误处理**: 统一的错误响应格式
- ✅ **幂等性**: PUT/DELETE 操作保证幂等性
- ✅ **安全性**: 密码加密、HTTPS、防 SQL 注入

## 常见问题

### Q1: PUT 和 PATCH 的区别?
A: PUT 用于完整替换资源,PATCH 用于部分更新。例如更新用户信息时,如果只改用户名,用 PATCH 更合适。

### Q2: 如何处理批量操作?
A: 可以设计批量端点,如 `POST /api/v1/users/batch`,请求体包含操作数组。

### Q3: 如何实现软删除?
A: 使用 PATCH 更新状态字段,如 `PATCH /api/v1/users/{id}` 设置 `status: "deleted"`。

## 参考资源

- [RESTful API 设计最佳实践](https://restfulapi.net/)
- [HTTP 状态码参考](https://httpstatuses.com/)
- [JWT 官方文档](https://jwt.io/)

---

> **注意**: 本示例基于 RESTful 规范,实际项目中需根据业务需求调整。
