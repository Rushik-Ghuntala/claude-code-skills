# Architecture

How skills, commands, and agents relate in the Claude Code Skills system.

## Core Concepts

### Skills

A skill is a directory containing structured instructions (`SKILL.md`) and supporting files. Claude reads the SKILL.md when the skill is invoked and follows the instructions.

**Location**: `~/.claude/skills/<skill-name>/`

### Commands

A command is a thin `.md` file that maps a `/slash-command` to a skill. It provides the user-facing interface.

**Location**: `~/.claude/commands/<command-name>.md`

### Agents

An agent is an autonomous Claude instance that can chain multiple skills together. Agents have their own model configuration and tool access.

**Location**: Defined in agent `.md` files, referenced by Claude Code.

## Dependency Graph

```
viral-hook-generator (FOUNDATIONAL)
├── Used by: post-creator
├── Used by: thread-composer
├── Used by: article-generator
├── Referenced by: content-calendar
└── Referenced by: trend-discovery

engagement-prediction (FOUNDATIONAL)
└── Used by: post-creator

posting-schedule (FOUNDATIONAL)
├── Referenced by: post-creator
├── Referenced by: article-generator
└── Referenced by: content-calendar

tweet-optimizer (STANDALONE)
trend-discovery (STANDALONE)
mvp-idea-generator (STANDALONE)
```

## Agent Orchestration

### content-strategist

The content-strategist agent is the master orchestrator. It:

1. Runs **trend-discovery** to find current opportunities
2. Uses **content-calendar** to plan the week
3. Creates content with **post-creator**, **thread-composer**, and **article-generator**
4. Optimizes everything through **tweet-optimizer**
5. Scores all content via **engagement-prediction**
6. Assigns posting times via **posting-schedule**

### engagement-analyzer

Compares multiple draft variants by running each through the scoring pipeline.

### trend-researcher

Runs deep multi-query trend analysis with follow-up searches for deeper context.

## Data Flow

```
User Input (/x-post "topic")
     │
     ▼
Command File (commands/x-post.md)
     │ skill: post-creator
     ▼
Skill (skills/post-creator/SKILL.md)
     │ reads references, uses hook patterns
     ▼
Claude Generates Output
     │ 3 tweet variants with scores
     ▼
User sees formatted output
```

## Installation Paths

| Component | Installed To |
|-----------|-------------|
| Skills | `~/.claude/skills/<name>/` (symlink) |
| Commands | `~/.claude/commands/<name>.md` (copy) |
| Agents | Referenced from skill/agent definitions |
| Lib | Stays in repo, accessed via symlinks |
