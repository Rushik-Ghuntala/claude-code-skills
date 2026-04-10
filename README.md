# Claude Code Skills

**11 production-ready Claude Code skills for X/Twitter content creation, engagement optimization, and MVP market research.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Skills](https://img.shields.io/badge/Skills-11-green)
![Commands](https://img.shields.io/badge/Commands-10-orange)
![Agents](https://img.shields.io/badge/Agents-3-purple)

> Turn Claude Code into a content creation powerhouse and market research engine. Generate viral tweets, compose optimized threads, score engagement potential, plan content calendars, write long-form articles, and research MVP opportunities — all from your terminal.

## Quick Install

```bash
curl -fsSL https://raw.githubusercontent.com/Rushik-Ghuntala/claude-code-skills/main/install.sh | bash
```

Or clone and install locally:

```bash
git clone https://github.com/Rushik-Ghuntala/claude-code-skills.git
cd claude-code-skills
./install.sh
```

## What's Inside

### Content Creation Skills (X/Twitter)

| Command | Skill | What It Does |
|---------|-------|-------------|
| `/x-post [topic]` | post-creator | Create 3 ready-to-publish tweet variants with engagement scores |
| `/x-thread [topic]` | thread-composer | Compose optimized multi-tweet threads (5 architectures) |
| `/x-hook [topic]` | viral-hook-generator | Generate 5-7 scroll-stopping openers from 15 proven archetypes |
| `/x-optimize [draft]` | tweet-optimizer | Rewrite tweets using X's open-source algorithm signals |
| `/x-score [draft]` | engagement-prediction | Score any tweet 0-100 with per-dimension breakdown |
| `/x-schedule [type]` | posting-schedule | Get optimal posting times for developer audiences |
| `/x-calendar [niche]` | content-calendar | Generate a 7-day content plan adapted to your growth stage |
| `/x-article [topic]` | article-generator | Write long-form X articles and technical blog posts |
| `/x-trends [niche]` | trend-discovery | Discover trending developer topics with content angles |

### Research Skills

| Command | Skill | What It Does |
|---------|-------|-------------|
| `/mvp-ideas [count] [niche]` | mvp-idea-generator | Research 9+ platforms to find scored MVP opportunities with $10K MRR paths |

### Agents

| Agent | What It Does |
|-------|-------------|
| content-strategist | Full strategy orchestration — combines all 9 content skills into a complete weekly plan |
| engagement-analyzer | Compare multiple tweet/thread drafts with detailed scoring analysis |
| trend-researcher | Deep multi-query trend analysis across developer niches |

## Demo

### `/x-post "React Server Components"`

```
Creating 3 tweet variants...

1. [Score: 82/100] Value Bomb
   "React Server Components aren't about speed.
   They're about moving $0 to the client.
   Fewer bundles. Fewer waterfalls. Fewer loading spinners.
   The real win? Your users stop noticing your framework."

2. [Score: 78/100] Hot Take
   "Hot take: If you're not using React Server Components yet,
   you're shipping 40% more JavaScript than you need to.
   I benchmarked 12 production apps. The results were brutal."

3. [Score: 75/100] Question Hook
   "What if I told you React Server Components
   could cut your bundle size in half?
   Here's the 3-line change that did it for us:"
```

### `/mvp-ideas 3 developer tools`

```
MVP Opportunity Research Report

Top 3 Ideas:
1. API Endpoint Monitor for Indie Devs (Score: 78/100)
   — Lightweight monitoring at 1/10th the price of Datadog
2. PR Review Queue Manager (Score: 73/100)
   — Smart PR prioritization for teams of 5-20
3. Dependency Vulnerability Dashboard (Score: 68/100)
   — Aggregated alerts across repos with fix suggestions

Each idea includes: pain points with sources, target persona,
MVP features, pricing, competitors, growth strategy,
and month-by-month path to $10K MRR.
```

### `/x-thread "Why TypeScript won"`

```
Thread: Why TypeScript Won (8 tweets)

1/ TypeScript didn't win because it's a better language.

It won because it solved the ONE problem every team hits
at 10,000 lines of JavaScript.

Here's the real story: 🧵

2/ In 2012, JavaScript had no types, no intellisense,
and refactoring meant "find and replace + pray."

Google had Closure Compiler. Facebook had Flow.
Microsoft had... an idea.

[... 6 more tweets with scores and char counts]
```

## How Skills Work Together

The skills are designed as a composable system:

```
                    ┌─────────────────────┐
                    │  content-strategist  │ (orchestrates everything)
                    └──────────┬──────────┘
                               │
        ┌──────────┬───────────┼───────────┬──────────┐
        ▼          ▼           ▼           ▼          ▼
   ┌─────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
   │ trends  │ │calendar│ │  post  │ │ thread │ │article │
   └────┬────┘ └───┬────┘ └───┬────┘ └───┬────┘ └───┬────┘
        │          │          │          │          │
        └──────────┴──────┬───┴──────────┘          │
                          ▼                         │
                   ┌─────────────┐                  │
                   │ viral-hook  │◄─────────────────┘
                   │  generator  │ (foundational — hooks for all content)
                   └─────────────┘
                          │
              ┌───────────┼───────────┐
              ▼           ▼           ▼
        ┌──────────┐ ┌────────┐ ┌──────────┐
        │ optimizer│ │ scorer │ │ schedule │
        └──────────┘ └────────┘ └──────────┘
```

**viral-hook-generator** is the foundation — its 15 hook archetypes are used by post-creator, thread-composer, article-generator, and more. The **content-strategist** agent orchestrates all skills to create complete weekly content strategies.

## Installation Options

### Full Install (Recommended)

```bash
./install.sh
```

Installs all 11 skills and 10 commands. Skills are symlinked to `~/.claude/skills/`, commands are copied to `~/.claude/commands/`.

### Individual Skill

```bash
./install.sh --skill viral-hook-generator
```

Installs a single skill and its matching command.

### Plugin Mode

```bash
./install.sh --plugin
```

Installs as a Claude Code plugin at `~/.claude/plugins/claude-code-skills/`.

### Manual Install

Copy any skill folder to `~/.claude/skills/` and its command file to `~/.claude/commands/`:

```bash
cp -r skills/viral-hook-generator ~/.claude/skills/
cp commands/x-hook.md ~/.claude/commands/
```

### Uninstall

```bash
./uninstall.sh
```

Cleanly removes all installed skills, commands, and symlinks.

## Creating Your Own Skill

Every skill is just a directory with a `SKILL.md` file. Here's the minimal structure:

```
my-skill/
├── SKILL.md              # Skill instructions (Claude reads this)
├── references/           # Reference data files
│   └── my-data.md
└── examples/             # Example outputs
    └── sample.md
```

The `SKILL.md` has this format:

```markdown
---
name: my-skill
description: What it does (shown in skill list)
allowed-tools: WebSearch WebFetch Read
---

# My Skill

Instructions for Claude go here...
Use `$ARGUMENTS` to access user input.
```

See [docs/creating-a-skill.md](docs/creating-a-skill.md) for the full tutorial.

## Algorithm Intelligence

The X/Twitter skills are built on **X's open-source algorithm signals**:

| Signal | Weight | What It Means |
|--------|--------|--------------|
| Reply | +54x | Replies are the strongest positive signal |
| Bookmark | +40x | Saves indicate high-value content |
| Like | +30x | Standard engagement signal |
| Retweet | +20x | Amplification signal |
| Quote Tweet | +20x | Adds commentary value |
| Profile Click | +24x | Interest in the author |
| Media | +2x bonus | Images/video boost reach |
| External Link | -5x penalty | Links reduce distribution |
| Excess Hashtags | -10x each | More than 2 hashtags hurts |

All content skills optimize for these signals by default.

## Dual-Mode Operation

**Offline mode** (default): Uses Claude's knowledge of developer Twitter patterns, algorithm signals, and content strategies. No API keys needed. Works immediately after install.

**Live mode** (optional): Enhances trend-discovery with real-time data via X API. Set these environment variables:

```bash
export X_API_KEY="your-api-key"
export X_API_SECRET="your-api-secret"
export X_ACCESS_TOKEN="your-access-token"
export X_ACCESS_SECRET="your-access-secret"
```

## Project Structure

```
claude-code-skills/
├── skills/              # 11 skill directories (each with SKILL.md + references)
├── commands/            # 10 slash command definitions
├── agents/              # 3 agent definitions
├── lib/                 # Shared Python utilities
├── docs/                # Extended documentation
├── install.sh           # One-command installer
├── uninstall.sh         # Clean removal
└── plugin.json          # Plugin manifest
```

## Contributing

We welcome contributions! Whether it's a new skill, improvements to existing ones, or documentation fixes.

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Ideas for new skills:**
- LinkedIn post optimizer
- GitHub README generator
- Newsletter content creator
- YouTube title/description optimizer
- Product launch playbook generator

## License

MIT - see [LICENSE](LICENSE)

---

Built by [Rushik Ghuntala](https://github.com/Rushik-Ghuntala)
