# 5 分钟快速上手指南

欢迎使用 Super Skills!本指南将帮助你在 5 分钟内开始使用 skills。

## 🎯 场景 1: 我想写一个 PRD

### 步骤 1: 安装 skill

```bash
# 方式 1: 使用 skills CLI (推荐)
npx skills add https://github.com/taylorchen/super-skills --skill product-requirements

# 方式 2: 手动复制
cp -r skills/product-requirements ~/.cursor/skills/
```

### 步骤 2: 在 AI 工具中触发

在你的 AI 编码助手中输入:

```
/product-requirements-full
我需要为"用户自助重置密码"功能编写 PRD
```

### 步骤 3: AI 自动生成

AI 将自动:
- ✅ 加载 PRD 模板
- ✅ 应用 SMART 原则
- ✅ 生成完整的需求文档
- ✅ 包含验收标准

**预期输出**: 一份包含背景、目标、功能需求、非功能需求和验收标准的完整 PRD 文档。

---

## 💻 场景 2: 我想进行代码审查

### 步骤 1: 快速安装

```bash
npx skills add https://github.com/taylorchen/super-skills --skill code-review
```

### 步骤 2: 触发审查

```
/code-review-security
请检查以下代码是否存在安全漏洞:

[粘贴你的代码]
```

### 步骤 3: 获取审查报告

AI 将检查:
- 🔒 SQL 注入风险
- 🔒 XSS 跨站脚本
- 🔒 敏感数据泄露
- 🔒 权限控制问题

**预期输出**: 详细的安全审查报告,包含问题描述、风险等级和修复建议。

---

## 🎨 场景 3: 我想设计 API 接口

### 步骤 1: 安装 API 设计 skill

```bash
npx skills add https://github.com/taylorchen/super-skills --skill api-design
```

### 步骤 2: 描述需求

```
/api-design-full
我需要设计一个用户管理的 RESTful API,包括注册、登录、个人信息管理等功能
```

### 步骤 3: 获取 API 规范

AI 将生成:
- 📋 完整的 API 端点列表
- 📋 请求/响应格式
- 📋 错误码定义
- 📋 认证方案

**预期输出**: 符合 RESTful 规范的 API 设计文档,可直接用于开发。

---

## 🔍 场景 4: 我不确定用哪个 skill

### 使用交互式选择器

```bash
cd /path/to/super-skills
python3 scripts/skill-selector.py
```

**交互式界面**:
```
🚀 Super Skills 交互式选择器
============================================================

选择一个类别查看相关 skills:

  1. 🎯 产品类
  2. 💻 研发类
  3. ✍️ 内容类
  4. 🔧 运维/数据
  0. 退出

请选择类别 (输入数字): 2

💻 研发类 包含以下 skills:

  1. 架构设计 - 技术方案
  2. API 设计 - RESTful/GraphQL/gRPC
  3. 数据库设计 - 建模与优化
  4. 代码审查 - 质量把控
  ...
```

---

## 📚 进阶使用

### 查看示例

每个 skill 都有实战示例,位于 `resources/examples/` 目录:

```bash
# 查看 PRD 示例
cat resources/examples/product-requirements/prd-sample.md

# 查看代码审查示例
cat resources/examples/code-review/review-sample.md
```

### 自定义 Prompt

你可以根据需要调整触发指令:

```
# 完整工作流
/skill-name-full

# 快速检查
/skill-name-quick

# 或直接描述需求
请帮我 [具体任务],参考 skill-name skill
```

### 组合使用多个 Skills

对于复杂任务,可以组合使用:

```
1. 使用 competitive-analysis 进行竞品分析
2. 使用 product-requirements 编写 PRD
3. 使用 technical-design 设计技术方案
4. 使用 api-design 定义接口
5. 使用 code-review 审查代码
```

---

## 🎬 视频教程

> 📹 **即将推出**: 30 秒快速演示视频

---

## ❓ 常见问题

### Q1: Skills 在哪些 AI 工具中可用?

A: 支持以下工具:
- ✅ Claude Code
- ✅ Cursor
- ✅ Antigravity
- ✅ GitHub Copilot
- ✅ Codex
- ✅ Roo Code

### Q2: 如何更新 skills?

A: 使用 git pull 更新本地仓库,或重新运行 `npx skills add` 命令。

### Q3: 可以自定义 skills 吗?

A: 可以!复制 skill 目录到你的项目,然后修改 SKILL.md 和 references 文件。

### Q4: Skills 会消耗多少 tokens?

A: 主 SKILL.md 文件通常 < 500 tokens,references 文件按需加载,通常 1-6k tokens。

---

## 🆘 需要帮助?

- 📖 查看完整文档: [README.md](../README.md)
- 💬 提问讨论: [GitHub Discussions](https://github.com/taylorchen/super-skills/discussions)
- 🐛 报告问题: [GitHub Issues](https://github.com/taylorchen/super-skills/issues)

---

**🎉 现在你已经准备好使用 Super Skills 了!选择一个场景开始吧!**
