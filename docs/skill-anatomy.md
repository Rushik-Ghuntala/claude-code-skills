# Skill Anatomy

Reference guide for the structure of a Claude Code skill.

## Directory Structure

```
my-skill/
├── SKILL.md              # Required — machine-readable instructions for Claude
├── README.md             # Required — human-readable description for GitHub
├── references/           # Optional — reference data files
│   ├── data.md
│   └── templates.md
├── examples/             # Optional — example outputs
│   └── sample-output.md
├── scripts/              # Optional — Python helper scripts
│   └── helper.py
└── assets/               # Optional — templates, images, static files
    └── template.md
```

## SKILL.md Frontmatter

```yaml
---
name: skill-name           # Required. kebab-case identifier.
description: What it does   # Required. Shown in skill list. Keep under 200 chars.
allowed-tools: Tool1 Tool2  # Optional. Space-separated tool names.
auto_invoke: true           # Optional. If true, skill triggers automatically when relevant.
---
```

### Field Reference

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `name` | Yes | string | Unique identifier in kebab-case |
| `description` | Yes | string | One-line description shown in skill list |
| `allowed-tools` | No | string | Space-separated list of tools the skill can use |
| `auto_invoke` | No | boolean | Whether skill triggers automatically |

### Available Tools

| Tool | Purpose |
|------|---------|
| `Read` | Read files from the local filesystem |
| `Grep` | Search file contents with regex |
| `Glob` | Find files by name patterns |
| `WebSearch` | Search the internet |
| `WebFetch` | Fetch and process web page content |
| `Bash` | Execute shell commands |

## SKILL.md Body

The body contains structured instructions that Claude follows. Best practices:

1. **Start with a role statement**: "You are an expert X who does Y"
2. **Define the input**: Explain how `$ARGUMENTS` should be parsed
3. **Define the process**: Numbered steps Claude follows
4. **Define the output**: Exact format of the expected output
5. **Include error handling**: What to do when things go wrong

## Command File Format

```yaml
---
name: command-name          # The /slash-command name
description: What it does   # Shown in command list
skill: skill-name           # Must match the skill's name field
arguments: "[args]"         # Description of expected arguments
user_invocable: true        # Must be true for slash commands
---
```

## Naming Conventions

| Item | Convention | Example |
|------|-----------|---------|
| Skill directory | kebab-case | `viral-hook-generator` |
| Command file | kebab-case.md | `x-hook.md` |
| SKILL.md name field | kebab-case | `viral-hook-generator` |
| Reference files | kebab-case.md | `hook-patterns.md` |
| Python scripts | snake_case.py | `score_tweet.py` |
| Example files | kebab-case.md | `sample-output.md` |
