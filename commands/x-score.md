---
name: x-score
description: Score a tweet draft on engagement potential (0-100) with improvement suggestions
skill: engagement-prediction
arguments: "[draft tweet] - Your draft tweet text to score"
user_invocable: true
---

Invoke the `engagement-prediction` skill with the user's draft tweet.

Usage: `/x-score [draft tweet]`

Examples:
- `/x-score Just mass-shipped a new feature. Feels good.`
- `/x-score Unpopular opinion: you don't need Kubernetes for most projects`
- `/x-score TIL: JavaScript has structuredClone() now. No more JSON.parse(JSON.stringify(obj)) hacks.`
