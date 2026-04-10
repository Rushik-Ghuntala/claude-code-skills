# Creating Your Own Claude Code Skill

This guide walks you through building a Claude Code skill from scratch.

## What is a Skill?

A skill is a set of structured instructions that tells Claude Code how to perform a specific task. When a user invokes a skill (via a slash command), Claude reads the `SKILL.md` file and follows the instructions to produce output.

Skills can include:
- **Reference data** — facts, templates, scoring rubrics
- **Examples** — sample outputs showing expected quality
- **Scripts** — Python helpers for computation
- **Assets** — templates, images, or other static files

## Step-by-Step: Build a "Code Review" Skill

### 1. Create the directory

```bash
mkdir -p skills/code-reviewer/{references,examples}
```

### 2. Write SKILL.md

```markdown
---
name: code-reviewer
description: Reviews code for bugs, security issues, and best practices
allowed-tools: Read Grep Glob
---

# Code Reviewer

You are an expert code reviewer. Analyze the provided code for:
1. Bugs and logic errors
2. Security vulnerabilities (OWASP Top 10)
3. Performance issues
4. Code style and readability

## Input

The user provides a file path or code snippet via `$ARGUMENTS`.

## Process

1. Read the file using the Read tool
2. Analyze against the checklist in `references/review-checklist.md`
3. Score each category 1-10
4. Provide specific, actionable feedback

## Output Format

# Code Review: [filename]

## Summary
[1-2 sentence overview]

## Scores
| Category | Score | Notes |
|----------|-------|-------|
| Bugs | X/10 | ... |
| Security | X/10 | ... |
| Performance | X/10 | ... |
| Readability | X/10 | ... |

## Issues Found
### Critical
- [issue + fix]

### Warnings
- [issue + suggestion]

## What's Good
- [positive observations]
```

### 3. Add references

Create `references/review-checklist.md` with your review criteria:

```markdown
# Review Checklist

## Security
- [ ] No SQL injection vectors
- [ ] Input validation on all user data
- [ ] No hardcoded secrets
...
```

### 4. Add examples

Create `examples/sample-review.md` showing a complete example output. This helps Claude understand the expected quality and format.

### 5. Create the command

Create `commands/review.md`:

```markdown
---
name: review
description: Review code for bugs, security, and best practices
skill: code-reviewer
arguments: "[file path or code] - The code to review"
user_invocable: true
---

Review code for bugs, security issues, performance problems, and readability.

Usage: `/review [file path]`

Examples:
- `/review src/auth.ts` — review authentication code
- `/review src/api/` — review all files in a directory
```

### 6. Install and test

```bash
cp -r skills/code-reviewer ~/.claude/skills/
cp commands/review.md ~/.claude/commands/
```

Then in Claude Code, run `/review src/app.ts` to test.

## Key Concepts

### `$ARGUMENTS`

The `$ARGUMENTS` variable contains everything the user typed after the command name. For `/review src/auth.ts`, `$ARGUMENTS` = `"src/auth.ts"`.

Parse it however makes sense for your skill — as a file path, as a topic string, as structured input with flags.

### `allowed-tools`

Specify which tools your skill needs:
- `Read` — read files from disk
- `Grep` — search file contents
- `Glob` — find files by pattern
- `WebSearch` — search the internet
- `WebFetch` — fetch web page content
- `Bash` — run shell commands

Only request tools your skill actually needs.

### Cross-Skill References

You can reference other skills' data files using relative paths:

```markdown
Read the hook patterns from `../viral-hook-generator/references/hook-patterns.md`
```

This works because all skills are siblings in `~/.claude/skills/`.

### Reference Files vs. Inline Instructions

Put data in reference files when:
- The data is large (tables, lists, templates)
- The data might change independently
- Multiple skills share the same data

Keep instructions inline in SKILL.md when:
- They're short and specific to this skill
- They define the process flow
- They describe output format

## Tips

1. **Be specific** — Claude follows SKILL.md literally. Vague instructions produce vague output.
2. **Include examples** — A good example is worth 1000 words of instruction.
3. **Scope narrowly** — A skill that does one thing well beats one that does five things poorly.
4. **Test iteratively** — Run your skill, see what's off, adjust the instructions, repeat.
5. **Add scoring** — Quantitative scoring (0-100) makes output more actionable and comparable.
