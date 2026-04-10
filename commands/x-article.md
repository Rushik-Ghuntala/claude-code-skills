---
name: x-article
description: Create a long-form X article or technical blog post with companion promotional tweet
skill: article-generator
arguments: "[topic + type] - Topic and optional article type (tutorial, deep-dive, opinion, listicle, case-study, career)"
user_invocable: true
---

Invoke the `article-generator` skill with the user's topic and type.

Usage: `/x-article [topic + type]`

Examples:
- `/x-article How to build a CLI tool in Go --type tutorial`
- `/x-article Why microservices are the wrong default --type opinion`
- `/x-article 12 DevOps tools that saved us money --type listicle`
- `/x-article How we scaled to 10M requests/day --type case-study`
- `/x-article How React Server Components actually work --type deep-dive`
- `/x-article 5 years of senior engineering lessons --type career`
