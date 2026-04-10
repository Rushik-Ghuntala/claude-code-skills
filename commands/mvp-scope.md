---
name: mvp-scope
description: Generate a comprehensive zero-to-production scope of work from an MVP idea with database schemas, API specs, tech stack, landing page, SEO, marketing, and launch plan
skill: mvp-scope-generator
arguments: "[file path or description] - Path to an MVP report (.md/.pdf) or a plain text description of your idea"
user_invocable: true
---

Invoke the `mvp-scope-generator` skill to generate a comprehensive zero-to-production scope of work document. Takes an MVP idea (from an mvp-idea-generator report, a file, or a plain description) and produces a hyper-specific, actionable build plan covering database architecture, API specs, tech stack, landing page, SEO, marketing, deployment, testing, timeline, costs, and post-launch growth.

Usage: `/mvp-scope [file path or description]`

Examples:
- `/mvp-scope ~/reports/mvp-2026-04-10.md` — scope from an MVP report file
- `/mvp-scope An API monitoring tool for indie developers at $9/mo` — scope from a description
- `/mvp-scope` — will prompt for input source (MVP report or description)
