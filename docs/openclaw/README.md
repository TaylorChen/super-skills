# OpenClaw 支持说明

本目录用于提供 OpenClaw 专用的安装与使用说明，确保技能同时符合 AgentSkills 与 OpenClaw 的最小规范要求。

## 兼容性要求

- 所有 `SKILL.md` 顶部包含 YAML frontmatter，且至少有 `name` 与 `description` 字段
- `metadata.json` 仍保留为仓库内的完整元数据来源

## 安装方式

### 方式一：复制到 OpenClaw skills 目录

1. 将本仓库的 `skills/` 目录复制到 OpenClaw 的 skills 搜索路径之一
2. 重新加载 OpenClaw 或重启以触发技能扫描

### 方式二：保持项目目录并配置额外搜索路径

1. 保持本仓库在本地
2. 在 OpenClaw 的配置中加入该仓库 `skills/` 目录作为额外搜索路径
3. 重新加载 OpenClaw 或重启以触发技能扫描

## 目录结构

- `skills/` 作为主技能入口目录
- 子目录（如 `content-generation/`、`ai-generation/`、`utilities/`）仍保留原有结构

## 常见问题

- 如果技能未被识别，优先确认 `SKILL.md` 是否包含 frontmatter 与必填字段
- 若 OpenClaw 不递归扫描子目录，请将子目录加入额外搜索路径或使用扁平化导出流程
