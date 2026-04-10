# Contributing to Claude Code Skills

Thanks for your interest in contributing! Whether you're adding a new skill, improving an existing one, or fixing a typo — every contribution helps.

## Ways to Contribute

1. **Submit a new skill** — Build a skill and open a PR
2. **Improve existing skills** — Better prompts, more reference data, new examples
3. **Report bugs** — If a skill produces bad output, open an issue
4. **Request a skill** — Have an idea? Open a skill request issue
5. **Documentation** — Fix typos, add examples, improve guides

## Creating a New Skill

### 1. Directory Structure

Create a new directory under `skills/`:

```
skills/my-skill/
├── SKILL.md              # Required — the skill instructions
├── references/           # Optional — reference data files
│   └── my-reference.md
├── examples/             # Optional — example outputs
│   └── sample-output.md
├── scripts/              # Optional — helper scripts
│   └── helper.py
└── README.md             # Required — human-readable description
```

### 2. SKILL.md Format

```markdown
---
name: my-skill-name
description: One sentence describing what this skill does
allowed-tools: WebSearch WebFetch Read
---

# Skill Title

Instructions for Claude go here. Be specific and structured.

## Input

User input is available via `$ARGUMENTS`.

## Process

1. Step one...
2. Step two...

## Output Format

Describe the expected output format.
```

**Frontmatter fields:**
- `name` (required): kebab-case identifier
- `description` (required): Shown in the skill list
- `allowed-tools` (optional): Tools the skill can use (e.g., `WebSearch WebFetch Read`)
- `auto_invoke` (optional): Set to `true` if the skill should trigger automatically

### 3. Create a Command File

Create a matching command file in `commands/`:

```markdown
---
name: my-command
description: Short description for the command list
skill: my-skill-name
arguments: "[args] - Description of expected arguments"
user_invocable: true
---

Usage documentation and examples here.
```

### 4. Add a README.md

Each skill needs a human-readable `README.md` for GitHub browsing:

```markdown
# Skill Name
> One-liner description

## Usage
`/my-command [args]`

## What It Does
2-3 sentences explaining the skill.

## Example Output
Show a sample output in a code block.

## Dependencies
List any other skills this depends on.
```

## Naming Conventions

- **Skill directories**: `kebab-case` (e.g., `viral-hook-generator`)
- **Command files**: `kebab-case.md` (e.g., `x-hook.md`)
- **Reference files**: `kebab-case.md`
- **Python scripts**: `snake_case.py`

## PR Checklist

Before submitting your PR, verify:

- [ ] Skill directory has `SKILL.md` with valid frontmatter
- [ ] Skill directory has `README.md` for GitHub browsing
- [ ] Command file exists in `commands/` with correct `skill:` field
- [ ] Skill has been tested locally (install and run the command)
- [ ] No hardcoded paths or personal information in files
- [ ] Description is clear and concise
- [ ] If your skill depends on other skills, document it in your README.md

## Code Style

- Markdown files: Use ATX-style headers (`#`, `##`, `###`)
- SKILL.md: Be specific and structured — Claude follows these instructions literally
- Reference files: Use tables and lists for scannable data
- Python scripts: Follow PEP 8

## Questions?

Open an issue or start a discussion. We're happy to help!
