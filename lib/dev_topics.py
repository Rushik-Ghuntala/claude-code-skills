"""
Developer Topic Taxonomy

Categorized list of 50+ developer topics for trend discovery,
content planning, and audience targeting.

Used by: Trend Discovery (Skill 1), Content Calendar (Skill 9)
"""

# === Topic Categories ===
# Each topic has: name, category (evergreen/cyclical/event-driven),
# subtopics, and typical audience size indicator

TOPIC_TAXONOMY = {
    # --- Languages & Runtimes ---
    "javascript": {
        "category": "evergreen",
        "subtopics": ["ES2024+", "Node.js", "Deno", "Bun", "TypeScript", "runtime wars"],
        "audience": "massive",
    },
    "python": {
        "category": "evergreen",
        "subtopics": ["Python 3.13+", "typing", "async", "packaging", "uv", "Ruff"],
        "audience": "massive",
    },
    "rust": {
        "category": "evergreen",
        "subtopics": ["memory safety", "async Rust", "embedded", "WASM", "Rust vs Go"],
        "audience": "large",
    },
    "go": {
        "category": "evergreen",
        "subtopics": ["generics", "concurrency", "CLI tools", "microservices"],
        "audience": "large",
    },
    "java": {
        "category": "evergreen",
        "subtopics": ["virtual threads", "Spring Boot", "GraalVM", "records"],
        "audience": "large",
    },
    "swift": {
        "category": "evergreen",
        "subtopics": ["SwiftUI", "Swift 6", "concurrency", "server-side Swift"],
        "audience": "medium",
    },
    "kotlin": {
        "category": "evergreen",
        "subtopics": ["KMP", "Compose", "coroutines", "Ktor"],
        "audience": "medium",
    },
    "zig": {
        "category": "evergreen",
        "subtopics": ["systems programming", "Zig vs Rust", "comptime"],
        "audience": "growing",
    },

    # --- Web Development ---
    "react": {
        "category": "evergreen",
        "subtopics": ["Server Components", "React 19", "hooks", "performance", "state management"],
        "audience": "massive",
    },
    "nextjs": {
        "category": "evergreen",
        "subtopics": ["App Router", "Server Actions", "caching", "middleware", "deployment"],
        "audience": "large",
    },
    "vue": {
        "category": "evergreen",
        "subtopics": ["Vue 3", "Nuxt", "Composition API", "Pinia"],
        "audience": "large",
    },
    "svelte": {
        "category": "evergreen",
        "subtopics": ["Svelte 5", "SvelteKit", "runes", "signals"],
        "audience": "medium",
    },
    "htmx": {
        "category": "evergreen",
        "subtopics": ["hypermedia", "HATEOAS", "simplicity vs SPAs"],
        "audience": "growing",
    },
    "css": {
        "category": "evergreen",
        "subtopics": ["container queries", "has()", "layers", "Tailwind", "CSS-in-JS death"],
        "audience": "large",
    },
    "web_platform": {
        "category": "evergreen",
        "subtopics": ["Web Components", "Service Workers", "WebGPU", "WASM", "PWA"],
        "audience": "large",
    },

    # --- AI & Machine Learning ---
    "ai_coding": {
        "category": "cyclical",
        "subtopics": ["Copilot", "Cursor", "Claude Code", "AI pair programming", "vibe coding"],
        "audience": "massive",
    },
    "llm": {
        "category": "cyclical",
        "subtopics": ["prompt engineering", "RAG", "fine-tuning", "agents", "benchmarks"],
        "audience": "massive",
    },
    "ml_ops": {
        "category": "evergreen",
        "subtopics": ["model deployment", "monitoring", "feature stores", "pipelines"],
        "audience": "medium",
    },
    "computer_vision": {
        "category": "evergreen",
        "subtopics": ["object detection", "image generation", "video AI"],
        "audience": "medium",
    },
    "ai_ethics": {
        "category": "cyclical",
        "subtopics": ["bias", "safety", "regulation", "job displacement"],
        "audience": "large",
    },

    # --- DevOps & Infrastructure ---
    "docker": {
        "category": "evergreen",
        "subtopics": ["containers", "Docker Compose", "multi-stage builds", "alternatives"],
        "audience": "large",
    },
    "kubernetes": {
        "category": "evergreen",
        "subtopics": ["operators", "service mesh", "K8s alternatives", "simplification"],
        "audience": "large",
    },
    "ci_cd": {
        "category": "evergreen",
        "subtopics": ["GitHub Actions", "GitLab CI", "deployment strategies", "testing"],
        "audience": "large",
    },
    "cloud": {
        "category": "evergreen",
        "subtopics": ["AWS", "GCP", "Azure", "multi-cloud", "cost optimization", "serverless"],
        "audience": "massive",
    },
    "platform_engineering": {
        "category": "cyclical",
        "subtopics": ["internal developer platforms", "golden paths", "developer experience"],
        "audience": "growing",
    },
    "observability": {
        "category": "evergreen",
        "subtopics": ["OpenTelemetry", "tracing", "logging", "metrics", "SRE"],
        "audience": "medium",
    },

    # --- Databases & Storage ---
    "databases": {
        "category": "evergreen",
        "subtopics": ["PostgreSQL", "SQLite", "NewSQL", "vector DBs", "time-series"],
        "audience": "large",
    },
    "orm": {
        "category": "cyclical",
        "subtopics": ["Prisma", "Drizzle", "SQLAlchemy", "ORM vs raw SQL debate"],
        "audience": "medium",
    },

    # --- Security ---
    "security": {
        "category": "evergreen",
        "subtopics": ["auth", "OAuth", "supply chain", "OWASP", "zero trust"],
        "audience": "large",
    },
    "cybersecurity": {
        "category": "event-driven",
        "subtopics": ["breaches", "vulnerabilities", "CVEs", "incident response"],
        "audience": "large",
    },

    # --- Career & Culture ---
    "career": {
        "category": "evergreen",
        "subtopics": ["interviews", "salary", "promotion", "burnout", "switching roles"],
        "audience": "massive",
    },
    "remote_work": {
        "category": "cyclical",
        "subtopics": ["RTO mandates", "productivity", "async communication", "tooling"],
        "audience": "large",
    },
    "tech_layoffs": {
        "category": "event-driven",
        "subtopics": ["market conditions", "survival strategies", "pivoting"],
        "audience": "large",
    },
    "indie_hacking": {
        "category": "evergreen",
        "subtopics": ["SaaS", "bootstrapping", "MRR", "solo founder", "build in public"],
        "audience": "large",
    },
    "open_source": {
        "category": "evergreen",
        "subtopics": ["maintainership", "licensing", "funding", "contribution"],
        "audience": "large",
    },
    "developer_experience": {
        "category": "cyclical",
        "subtopics": ["DX", "tooling", "documentation", "SDKs", "developer relations"],
        "audience": "medium",
    },

    # --- Mobile ---
    "ios": {
        "category": "evergreen",
        "subtopics": ["SwiftUI", "UIKit", "App Store", "visionOS"],
        "audience": "large",
    },
    "android": {
        "category": "evergreen",
        "subtopics": ["Jetpack Compose", "Kotlin Multiplatform", "Material You"],
        "audience": "large",
    },
    "react_native": {
        "category": "evergreen",
        "subtopics": ["Expo", "New Architecture", "Fabric", "cross-platform"],
        "audience": "medium",
    },
    "flutter": {
        "category": "evergreen",
        "subtopics": ["Dart", "widgets", "desktop", "web support"],
        "audience": "medium",
    },

    # --- Architecture & Patterns ---
    "system_design": {
        "category": "evergreen",
        "subtopics": ["scalability", "microservices vs monolith", "event-driven", "CQRS"],
        "audience": "large",
    },
    "api_design": {
        "category": "evergreen",
        "subtopics": ["REST", "GraphQL", "gRPC", "tRPC", "API versioning"],
        "audience": "large",
    },
    "testing": {
        "category": "evergreen",
        "subtopics": ["TDD", "integration tests", "E2E", "mocking", "Playwright", "Vitest"],
        "audience": "large",
    },
    "performance": {
        "category": "evergreen",
        "subtopics": ["Core Web Vitals", "profiling", "caching", "CDN", "edge computing"],
        "audience": "medium",
    },

    # --- Emerging Tech ---
    "web3": {
        "category": "cyclical",
        "subtopics": ["smart contracts", "DeFi", "L2s", "Solana", "real utility"],
        "audience": "medium",
    },
    "spatial_computing": {
        "category": "event-driven",
        "subtopics": ["AR/VR", "Apple Vision Pro", "Meta Quest", "WebXR"],
        "audience": "growing",
    },
    "edge_computing": {
        "category": "cyclical",
        "subtopics": ["Cloudflare Workers", "Deno Deploy", "Vercel Edge", "edge databases"],
        "audience": "growing",
    },
    "wasm": {
        "category": "evergreen",
        "subtopics": ["WASI", "component model", "server-side WASM", "browser WASM"],
        "audience": "growing",
    },

    # --- Tools & Productivity ---
    "terminal": {
        "category": "evergreen",
        "subtopics": ["CLI tools", "shell scripts", "dotfiles", "terminal emulators"],
        "audience": "large",
    },
    "editors": {
        "category": "cyclical",
        "subtopics": ["VS Code", "Neovim", "Zed", "Cursor", "editor wars"],
        "audience": "large",
    },
    "git": {
        "category": "evergreen",
        "subtopics": ["workflows", "tips", "branching strategies", "monorepo"],
        "audience": "massive",
    },
}

# === Seasonal/Event-Driven Topics ===
SEASONAL_EVENTS = {
    "january": ["new year tech predictions", "learning goals", "tech resolutions"],
    "march": ["GDC", "tech conferences season starts"],
    "april": ["GitHub Universe prep", "spring cleaning codebases"],
    "may": ["Google I/O", "Microsoft Build"],
    "june": ["WWDC", "mid-year reviews", "summer projects"],
    "july": ["summer side projects", "learning new languages"],
    "september": ["back to coding", "conference season"],
    "october": ["Hacktoberfest", "Halloween coding challenges"],
    "november": ["AWS re:Invent", "Black Friday for dev tools"],
    "december": ["year in review", "top tools of the year", "predictions"],
}

# === Topic Audience Size Estimates ===
AUDIENCE_SIZES = {
    "massive": "1M+ potential impressions",
    "large": "500K-1M potential impressions",
    "medium": "100K-500K potential impressions",
    "growing": "50K-100K potential impressions (high growth rate)",
}
