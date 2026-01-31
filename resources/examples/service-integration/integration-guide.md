# 外部服务集成指南

## 概述

本指南详细说明如何在 super-skills 项目中集成外部服务，包括 API 调用、认证管理、速率限制处理等。

## 配置结构

### 服务配置文件

服务集成配置文件使用 JSON 格式，包含以下主要部分：

1. **services** - 定义所有可用的外部服务
2. **service_groups** - 按功能对服务进行分组

### 服务配置示例

```json
{
  "services": [
    {
      "name": "github",
      "description": "GitHub API integration",
      "type": "api",
      "auth": {
        "type": "oauth2",
        "token_env": "GITHUB_TOKEN"
      },
      "endpoints": {
        "repos": "https://api.github.com/repos",
        "issues": "https://api.github.com/issues"
      },
      "rate_limits": {
        "requests_per_minute": 5000
      }
    }
  ],
  "service_groups": [
    {
      "name": "development",
      "services": ["github"],
      "description": "Development tools and APIs"
    }
  ]
}
```

## 服务类型

### 1. API 服务

用于与 RESTful API 交互的服务类型。

**配置字段：**
- `type`: "api"
- `auth`: 认证配置
- `endpoints`: API 端点映射
- `rate_limits`: 速率限制设置

### 2. Webhook 服务

用于接收或发送 webhook 的服务类型。

**配置字段：**
- `type`: "webhook"
- `auth`: 认证配置（通常是 webhook URL）
- `rate_limits`: 速率限制设置

### 3. 第三方 SDK 服务

用于集成第三方 SDK 的服务类型。

**配置字段：**
- `type`: "sdk"
- `auth`: SDK 初始化配置
- `rate_limits`: 速率限制设置

## 认证方式

### 1. API Key

```json
"auth": {
  "type": "api_key",
  "key_env": "API_KEY_ENV_VAR",
  "header_name": "Authorization"
}
```

### 2. OAuth2

```json
"auth": {
  "type": "oauth2",
  "token_env": "TOKEN_ENV_VAR",
  "token_type": "Bearer"
}
```

### 3. Webhook URL

```json
"auth": {
  "type": "webhook_url",
  "url_env": "WEBHOOK_URL_ENV_VAR"
}
```

### 4. 基本认证

```json
"auth": {
  "type": "basic",
  "username_env": "USERNAME_ENV_VAR",
  "password_env": "PASSWORD_ENV_VAR"
}
```

## 速率限制管理

每个服务配置都应包含速率限制设置，以避免过度请求导致的服务封禁：

```json
"rate_limits": {
  "requests_per_minute": 60,
  "requests_per_hour": 3600,
  "backoff_strategy": "exponential"
}
```

## 集成实现

### 1. 创建服务客户端

对于每个外部服务，创建一个专用的客户端类来处理 API 调用、认证和错误处理。

### 2. 服务注册

在技能的 metadata.json 中注册需要使用的服务：

```json
"services": [
  {
    "name": "github",
    "required": true,
    "scopes": ["repo", "issues"]
  }
]
```

### 3. 服务调用示例

```python
# 服务调用示例
from services.github.client import GitHubClient

def get_repository_info(owner, repo):
    client = GitHubClient()
    try:
        repo_info = client.get_repository(owner, repo)
        return repo_info
    except Exception as e:
        return {"error": str(e)}
```

## 错误处理

实现统一的错误处理机制，包括：

1. **网络错误** - 处理连接超时、DNS 解析失败等
2. **认证错误** - 处理令牌过期、无效凭证等
3. **速率限制错误** - 处理 API 速率限制触发
4. **业务错误** - 处理 API 返回的业务逻辑错误

## 安全最佳实践

1. **环境变量存储** - 敏感信息应存储在环境变量中，而非硬编码
2. **最小权限原则** - 只请求必要的 API 权限
3. **令牌轮换** - 实现令牌自动轮换机制
4. **请求验证** - 验证所有 API 请求参数
5. **响应验证** - 验证 API 响应格式和内容

## 监控与日志

为外部服务集成添加监控和日志记录：

1. **请求日志** - 记录所有 API 请求和响应
2. **错误监控** - 跟踪和警报服务错误
3. **性能监控** - 监控 API 响应时间和成功率
4. **使用统计** - 收集服务使用情况统计数据

## 示例技能

### GitHub 仓库分析技能

**功能**：分析 GitHub 仓库的结构、贡献者和活动。

**服务依赖**：
- GitHub API

**实现步骤**：
1. 配置 GitHub 服务
2. 创建仓库分析逻辑
3. 定义技能触发器和参数
4. 实现结果格式化

## 测试策略

### 单元测试
- 测试服务客户端的各个方法
- 测试认证和错误处理

### 集成测试
- 测试完整的服务调用流程
- 测试速率限制和重试机制

### 模拟测试
- 使用模拟服务进行测试，避免实际 API 调用
- 模拟各种错误场景

## 部署注意事项

1. **环境配置** - 确保所有必要的环境变量已正确设置
2. **网络访问** - 确保服务可以访问外部 API
3. **防火墙设置** - 配置必要的防火墙规则
4. **依赖管理** - 管理外部服务 SDK 依赖

## 维护与更新

1. **服务版本管理** - 跟踪外部服务的 API 版本
2. **变更监控** - 监控外部服务的 API 变更
3. **文档更新** - 及时更新服务集成文档
4. **性能优化** - 定期优化服务调用性能

## 常见问题

### Q: 如何处理服务认证失败？
A: 实现自动重试机制，并在多次失败后提供明确的错误信息。

### Q: 如何处理速率限制？
A: 实现指数退避策略，并在请求前检查剩余速率限制。

### Q: 如何确保服务集成的安全性？
A: 使用环境变量存储敏感信息，实现最小权限原则，定期轮换凭证。

### Q: 如何测试服务集成？
A: 使用模拟服务进行测试，避免实际 API 调用和潜在的速率限制问题。