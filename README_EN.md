# Super Skills

<div align="center">

**High-quality Agent Skills collection covering Product, Development, Operations, and Data domains**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills Count](https://img.shields.io/badge/skills-20-blue.svg)](#skills-list)

[English](#) | [中文](README.md)

</div>

## Introduction

Super Skills is an open-source [Agent Skills](https://agentskills.io) repository containing 20 carefully designed skills that help AI coding assistants better complete professional tasks in product, development, operations, and other domains.

All skills follow the Agent Skills open standard and can be used in the following AI tools:
- ✅ Claude Code
- ✅ Cursor
- ✅ Codex
- ✅ OpenCode
- ✅ GitHub Copilot
- ✅ Antigravity
- ✅ Roo Code

## Quick Start

### 🎯 5-Minute Guide

**New users**: Check out the [5-Minute Quick Start Guide](docs/quickstart.md) to learn through 4 practical scenarios.

### 🔍 Interactive Selector

Not sure which skill to use? Try the interactive selector:

```bash
python3 scripts/skill-selector.py
```

### Install with skills CLI

```bash
# Install all skills
npx skills add https://github.com/taylorchen/super-skills

# Install specific skill
npx skills add https://github.com/taylorchen/super-skills --skill code-review
```

### Manual Installation

Copy skill folders to your AI tool's skills directory:

```bash
# Claude Code
cp -r skills/code-review ~/.claude/skills/

# Cursor
cp -r skills/code-review ~/.cursor/skills/

# Codex
cp -r skills/code-review ~/.codex/skills/
```

## Skills List

### 🎯 Product (5 skills)

| Skill | Description | Use Cases |
| --- | --- | --- |
| [product-requirements](skills/product-requirements) | Product Requirements Document | PRD writing, requirements analysis, acceptance criteria |
| [competitive-analysis](skills/competitive-analysis) | Competitive Analysis | Competitor research, SWOT analysis, market positioning |
| [user-story](skills/user-story) | User Story Writing | Agile development, Sprint planning, Backlog management |
| [prototype-design](skills/prototype-design) | Prototype Design | Prototyping, interaction design, requirements visualization |
| [product-roadmap](skills/product-roadmap) | Product Roadmap Planning | Product strategy, version planning, milestone setting |

### 💻 Development (7 skills)

| Skill | Description | Use Cases |
| --- | --- | --- |
| [technical-design](skills/technical-design) | Technical Design | Architecture design, tech selection, design review |
| [code-review](skills/code-review) | Code Review | Code review, quality control, best practices |
| [api-design](skills/api-design) | API Design | RESTful/GraphQL/gRPC design |
| [database-schema](skills/database-schema) | Database Design | Data modeling, index optimization, query optimization |
| [refactoring-guide](skills/refactoring-guide) | Refactoring Guide | Code refactoring, technical debt, code quality |
| [testing-strategy](skills/testing-strategy) | Testing Strategy | Unit testing, integration testing, test coverage |
| [tech-research](skills/tech-research) | Technical Research | Tech selection, POC validation, research reports |

### ✍️ Content (4 skills)

| Skill | Description | Use Cases |
| --- | --- | --- |
| [blog-writer](skills/blog-writer) | Technical Blog Writing | Technical writing, knowledge sharing, content creation |
| [seo-optimization](skills/seo-optimization) | SEO Optimization | SEO audit, keyword research, content optimization |
| [geo-optimization](skills/geo-optimization) | GEO Optimization | Local SEO, multilingual optimization, internationalization |
| [documentation](skills/documentation) | Technical Documentation | API docs, user manuals, architecture documentation |

### 🔧 Operations/Data (4 skills)

| Skill | Description | Use Cases |
| --- | --- | --- |
| [deployment-guide](skills/deployment-guide) | Deployment Guide | CI/CD, Docker, Kubernetes deployment |
| [monitoring-setup](skills/monitoring-setup) | Monitoring Setup | Monitoring setup, log collection, alerting configuration |
| [data-analysis](skills/data-analysis) | Data Analysis | Data analysis, visualization, statistical analysis |
| [performance-tuning](skills/performance-tuning) | Performance Tuning | Performance analysis, frontend/backend optimization |

## Usage

### Auto-discovery

AI tools automatically identify relevant scenarios based on the skill's `description` field:

```
# When writing a PRD, the product-requirements skill is automatically activated
"I need to write a requirements document for user registration"
```

### Manual Invocation

Use `/skill-name` to explicitly load a specific skill:

```
/code-review
Please review this code...
```

### Progressive Loading

Each skill uses progressive loading design, loading only needed reference files:

```
skills/code-review/
├── SKILL.md              # Main file (~300 tokens)
└── references/           # Load on demand
    ├── security-checks.md
    ├── performance-checks.md
    └── maintainability.md
```

## Project Structure

```
super-skills/
├── skills/                    # Skills directory
│   ├── product-requirements/  # Product requirements
│   │   ├── SKILL.md
│   │   └── references/
│   ├── code-review/           # Code review
│   │   ├── SKILL.md
│   │   └── references/
│   └── ... (18 other skills)
├── README.md                  # Project documentation
├── README_EN.md              # English documentation
├── LICENSE                    # MIT License
└── package.json              # NPM configuration
```

## Contributing

Contributions of new skills or improvements to existing skills are welcome!

### Contribution Process

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/amazing-skill`)
3. Commit your changes (`git commit -m 'Add amazing skill'`)
4. Push to the branch (`git push origin feature/amazing-skill`)
5. Create a Pull Request

### Skill Development Guidelines

Each skill must include:

1. **SKILL.md** - Main file with YAML frontmatter
   ```yaml
   ---
   name: skill-name
   description: Clear description including use cases
   license: MIT
   ---
   ```

2. **references/** - Detailed guidance documents (optional)
   - Split by topic into multiple files
   - Each file 600-1500 tokens
   - Support progressive loading

3. **Follow Agent Skills Specification**
   - Reference: https://agentskills.io/specification

## License

[MIT License](LICENSE)

## Acknowledgments

- [Agent Skills](https://agentskills.io) - Open Agent Skills specification
- [nuxt-skills](https://github.com/onmax/nuxt-skills) - Project structure reference

## Contact

- Issues: [GitHub Issues](https://github.com/taylorchen/super-skills/issues)
- Discussions: [GitHub Discussions](https://github.com/taylorchen/super-skills/discussions)

---

<div align="center">

**If this project helps you, please give it a ⭐️ Star!**

Made with ❤️ by [Taylor Chen](https://github.com/taylorchen)

</div>
