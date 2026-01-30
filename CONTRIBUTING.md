# 贡献指南

感谢你对 Super Skills 项目的关注!我们欢迎各种形式的贡献。

## 🎯 贡献方式

### 1. 新增 Skill

如果你想贡献一个新的 skill:

1. **Fork 本仓库**
2. **创建 skill 目录**
   ```bash
   mkdir skills/your-skill-name
   ```

3. **使用生成器创建基础文件** (推荐)
   ```bash
   python3 scripts/generate-metadata.py
   ```

4. **填写必要文件**:
   - `SKILL.md` - 主文件 (必需)
   - `metadata.json` - 元数据配置 (必需)
   - `references/` - 参考文档目录 (可选)
   - `examples/` - 示例文件 (推荐)

5. **运行验证**
   ```bash
   python3 scripts/lint-rules.py
   python3 scripts/token-optimizer.py
   ```

6. **提交 Pull Request**

### 2. 改进现有 Skill

- 修复错别字或格式问题
- 补充示例文件
- 优化 references 文档
- 改进 prompt 模板

### 3. 完善文档

- 翻译文档到其他语言
- 补充使用示例
- 改进快速上手指南

### 4. 报告问题

发现 bug 或有改进建议?请[创建 Issue](https://github.com/taylorchen/super-skills/issues/new)。

---

## 📋 Skill 质量标准

### 必需项

- ✅ `SKILL.md` 包含完整的 YAML frontmatter
- ✅ `metadata.json` 格式正确
- ✅ 至少 1 个实战示例
- ✅ 通过 `lint-rules.py` 验证

### 推荐项

- ⭐ 主文件 (SKILL.md) < 500 tokens
- ⭐ 至少 1 个 reference 文档
- ⭐ 中英双语支持
- ⭐ 包含 Mermaid 流程图

### SKILL.md 格式

```markdown
---
name: skill-name
description: 清晰的描述,包括使用场景
license: MIT
---

# Skill 标题

简要说明

## 何时使用

**使用此 skill 当:**
- 场景 1
- 场景 2

**使用其他 skill 当:**
- 其他场景 → 使用 `other-skill`

## 快速参考

| 工作内容 | 加载文件 | 关键概念 |
| --- | --- | --- |
| ... | ... | ... |

## 加载文件

- [ ] [references/guide.md](references/guide.md) - 描述

## 相关 Skills

| Skill | 用途 |
| --- | --- |
| **other-skill** | 说明 |

## 检查清单

- [ ] 检查项 1
- [ ] 检查项 2
```

### metadata.json 格式

```json
{
    "name": "skill-name",
    "organization": "super-skills",
    "version": "5.0.0",
    "status": "stable",
    "abstract": "English abstract",
    "prompts": [
        {
            "trigger": "/skill-name-full",
            "description": "完整工作流",
            "template": "详细的 prompt 模板"
        }
    ]
}
```

---

## 🔍 代码审查流程

所有 Pull Request 都会经过以下检查:

1. **自动化验证**
   - ✅ Metadata 格式检查
   - ✅ Token 预算检查
   - ✅ Markdown lint

2. **人工审查**
   - 📝 内容质量
   - 📝 示例完整性
   - 📝 文档清晰度

3. **合并标准**
   - 通过所有自动化检查
   - 至少 1 位维护者批准
   - 无未解决的讨论

---

## 💬 交流渠道

- **GitHub Discussions**: 一般讨论、问题咨询
- **GitHub Issues**: Bug 报告、功能请求
- **Pull Requests**: 代码贡献

---

## 📜 行为准则

### 我们的承诺

为了营造开放和友好的环境,我们承诺:

- 🤝 尊重不同观点和经验
- 💬 使用友好和包容的语言
- 🎯 专注于对社区最有利的事情
- 🙏 对他人的贡献表示感谢

### 不可接受的行为

- ❌ 使用性化的语言或图像
- ❌ 人身攻击或侮辱性评论
- ❌ 骚扰行为
- ❌ 发布他人的私人信息

---

## 🎉 贡献者名单

感谢所有为本项目做出贡献的开发者!

<!-- 贡献者列表将自动生成 -->

---

## 📄 许可证

通过贡献代码,你同意你的贡献将在 [MIT License](LICENSE) 下发布。

---

**再次感谢你的贡献!** 🚀
