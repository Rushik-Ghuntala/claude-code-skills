"""
X/Twitter Algorithm Signal Weights

Based on X's open-source algorithm (2023 release + subsequent updates).
These weights represent the relative importance of different engagement
signals in X's ranking algorithm.

Used by: Tweet Optimizer (Skill 4), Engagement Prediction (Skill 5)
"""

# === Core Engagement Signal Multipliers ===
# These represent how much each action type boosts a tweet's ranking score
ENGAGEMENT_WEIGHTS = {
    "reply": 54.0,       # Replies are the strongest signal
    "bookmark": 40.0,    # Bookmarks = quality signal (private save)
    "like": 30.0,        # Likes are the baseline engagement
    "retweet": 20.0,     # Retweets spread reach
    "quote_tweet": 25.0, # Quote tweets show deeper engagement
    "profile_click": 12.0,  # Indicates curiosity about author
    "link_click": 8.0,   # Clicked through to a link
    "detail_expand": 6.0,   # Expanded to read more
    "dwell_time": 10.0,  # Time spent reading (>2s = positive signal)
}

# === Content Format Bonuses ===
# Multipliers applied based on tweet content format
FORMAT_BONUSES = {
    "has_media": 2.0,        # Images/video get 2x boost
    "has_video": 3.0,        # Video gets extra boost over images
    "has_poll": 1.5,         # Polls drive interaction
    "is_thread": 1.2,        # Threads get slight boost
    "has_code_block": 1.3,   # Code screenshots/blocks (dev audience)
    "has_emoji": 1.05,       # Minimal boost for emoji usage
}

# === Negative Signals (Penalties) ===
# These reduce a tweet's ranking score
PENALTIES = {
    "external_link": -5.0,    # Links to external sites penalized
    "excess_hashtags": -10.0, # Per hashtag beyond 2
    "excess_mentions": -3.0,  # Per mention beyond 3 (looks spammy)
    "all_caps_ratio": -2.0,   # High ratio of caps = shouting
    "url_only": -8.0,         # Tweet is just a URL
    "engagement_bait": -5.0,  # "Like if you agree" type content
    "follow_bait": -5.0,      # "Follow me for more" as main content
}

# === Optimal Tweet Characteristics ===
OPTIMAL_RANGES = {
    "char_length": (200, 250),      # Optimal character count
    "hashtag_count": (0, 2),        # Max 2 hashtags
    "mention_count": (0, 2),        # Max 2 mentions
    "line_breaks": (2, 6),          # Visual whitespace
    "sentences": (2, 5),            # Readable length
    "thread_length": (5, 12),       # Optimal thread size
}

# === Ranking Model Weights ===
# How much each ranking model contributes to final score
RANKING_MODELS = {
    "real_graph": 0.30,      # Interaction likelihood between users
    "sim_clusters": 0.25,    # Niche community relevance
    "twhin": 0.20,           # Topic relationship matching
    "tweepcred": 0.15,       # User authority/credibility score
    "recency": 0.10,         # Time decay factor
}

# === Time Decay ===
# How quickly a tweet loses ranking power
TIME_DECAY = {
    "half_life_hours": 6,        # Score halves every 6 hours
    "viral_extension_hours": 24, # Viral tweets get extended window
    "thread_extension_hours": 12, # Threads decay slower
}

# === Dev-Specific Topic Boost ===
# Topics that tend to perform well in developer Twitter
DEV_TOPIC_BOOST = {
    "ai_ml": 1.8,
    "web_dev": 1.3,
    "devops": 1.2,
    "open_source": 1.5,
    "career_advice": 1.6,
    "hot_takes": 1.4,
    "tutorials": 1.3,
    "build_in_public": 1.4,
    "benchmarks": 1.5,
    "new_releases": 1.6,
}

# === Scoring Thresholds ===
SCORE_THRESHOLDS = {
    "excellent": 80,
    "good": 60,
    "average": 40,
    "below_average": 20,
    "poor": 0,
}

SCORE_LABELS = {
    "excellent": "Excellent - High viral potential",
    "good": "Good - Should perform well",
    "average": "Average - Room for improvement",
    "below_average": "Below Average - Needs significant work",
    "poor": "Poor - Consider rewriting",
}

# === Engagement Bait Phrases ===
ENGAGEMENT_BAIT_PHRASES = [
    "like if you agree", "rt if you", "follow me for", "like and retweet",
    "share if you", "retweet if", "follow for follow", "f4f",
    "like for like", "drop a like",
]

# === Analysis Functions ===

import re
from dataclasses import dataclass, field


@dataclass
class TweetAnalysis:
    """Result of analyzing a tweet for engagement potential."""
    total_score: float = 0.0
    hook_score: float = 0.0
    reply_score: float = 0.0
    share_score: float = 0.0
    save_score: float = 0.0
    algorithm_score: float = 0.0
    audience_score: float = 0.0
    char_count: int = 0
    word_count: int = 0
    has_question: bool = False
    has_code: bool = False
    has_link: bool = False
    has_media_indicator: bool = False
    has_list: bool = False
    has_numbers: bool = False
    hashtag_count: int = 0
    emoji_count: int = 0
    mention_count: int = 0
    engagement_bait: bool = False
    improvements: list[str] = field(default_factory=list)


def analyze_tweet(text: str) -> TweetAnalysis:
    """
    Analyze a tweet for engagement potential across 6 dimensions.

    Returns a TweetAnalysis with scores totaling 0-100.
    """
    a = TweetAnalysis()
    a.char_count = len(text)
    a.word_count = len(text.split())
    a.has_question = "?" in text
    a.has_code = bool(re.search(r'[`{}\[\]();]|=>|function |const |let |var |import |def |class ', text))
    a.has_link = bool(re.search(r'https?://', text))
    a.has_media_indicator = bool(re.search(r'\.(png|jpg|gif|mp4|webp)', text, re.I))
    a.has_list = bool(re.search(r'^\s*[\d\-\*]', text, re.M))
    a.has_numbers = bool(re.search(r'\d+[%xXkKmM]|\d{2,}', text))
    a.hashtag_count = len(re.findall(r'#\w+', text))
    a.emoji_count = len(re.findall(r'[\U0001f300-\U0001f9ff]', text))
    a.mention_count = len(re.findall(r'@\w+', text))
    a.engagement_bait = any(phrase in text.lower() for phrase in ENGAGEMENT_BAIT_PHRASES)

    # --- Hook Strength (0-20) ---
    hook = 0.0
    first_line = text.split('\n')[0].strip()
    if len(first_line) > 20:
        hook += 5  # Has substance
    if a.has_numbers:
        hook += 4  # Specificity
    if any(w in first_line.lower() for w in ["stop", "never", "always", "worst", "best", "#1", "unpopular"]):
        hook += 4  # Strong opener words
    if first_line.endswith(":") or first_line.endswith("👇"):
        hook += 3  # Thread/continuation indicator
    if len(first_line) >= 60:
        hook += 2  # Detailed hook
    if re.search(r'\d+', first_line):
        hook += 2  # Numbers in hook
    a.hook_score = min(hook, 20)

    # --- Reply Potential (0-20) ---
    reply = 0.0
    if a.has_question:
        reply += 8  # Questions drive replies
    if any(w in text.lower() for w in ["what do you", "agree or disagree", "what's your", "am i wrong",
                                        "hot take", "unpopular opinion", "fight me", "change my mind"]):
        reply += 6  # Debate drivers
    if any(w in text.lower() for w in ["what would you", "drop your", "tell me", "how do you"]):
        reply += 4  # Direct invitations
    if a.has_numbers:
        reply += 2  # Specific claims invite correction
    a.reply_score = min(reply, 20)

    # --- Share Potential (0-20) ---
    share = 0.0
    if a.has_code:
        share += 5  # Code is shareable among devs
    if a.has_numbers:
        share += 4  # Data-driven = social currency
    if a.has_list:
        share += 3  # Lists are easy to share
    if a.char_count >= 150:
        share += 3  # Substantive content
    if any(w in text.lower() for w in ["tip", "trick", "hack", "til", "today i learned", "pro tip"]):
        share += 3  # Useful content gets shared
    if any(w in text.lower() for w in ["thread", "🧵"]):
        share += 2  # Thread indicator
    a.share_score = min(share, 20)

    # --- Save Potential (0-15) ---
    save = 0.0
    if a.has_code:
        save += 5  # Code examples get bookmarked
    if a.has_list:
        save += 4  # Lists are reference material
    if any(w in text.lower() for w in ["bookmark", "save this", "reference", "cheat sheet", "guide"]):
        save += 3  # Explicit save triggers
    if any(w in text.lower() for w in ["step", "how to", "tutorial", "template"]):
        save += 3  # Actionable content
    a.save_score = min(save, 15)

    # --- Algorithm Fit (0-15) ---
    algo = 8.0  # Base score
    # Length optimization
    if OPTIMAL_RANGES["char_length"][0] <= a.char_count <= OPTIMAL_RANGES["char_length"][1]:
        algo += 3
    elif a.char_count < 80:
        algo -= 2  # Too short
    # Penalties
    if a.has_link:
        algo -= 3  # External link penalty
    if a.hashtag_count > 2:
        algo -= 2 * (a.hashtag_count - 2)
    if a.mention_count > 3:
        algo -= 1 * (a.mention_count - 3)
    if a.engagement_bait:
        algo -= 3
    # Bonuses
    if a.has_media_indicator:
        algo += 2
    if '\n' in text:
        algo += 1  # Line breaks = readability
    a.algorithm_score = max(0, min(algo, 15))

    # --- Audience Match (0-10) ---
    aud = 3.0  # Base
    dev_keywords = ["code", "dev", "engineer", "api", "bug", "deploy", "git", "react", "python",
                    "javascript", "rust", "docker", "kubernetes", "ai", "ml", "database", "sql",
                    "frontend", "backend", "fullstack", "cli", "terminal", "server", "cloud",
                    "typescript", "node", "css", "html", "framework", "library", "open source",
                    "startup", "saas", "mvp", "ship", "build"]
    matches = sum(1 for kw in dev_keywords if kw in text.lower())
    aud += min(matches * 1.5, 7)
    a.audience_score = min(aud, 10)

    # --- Total ---
    a.total_score = a.hook_score + a.reply_score + a.share_score + a.save_score + a.algorithm_score + a.audience_score

    # --- Improvements ---
    if a.hook_score < 10:
        a.improvements.append("Add a specific detail (number, metric, or comparison) to your opening line")
    if a.reply_score < 8:
        a.improvements.append("Include a question or debate angle to drive replies (54x algorithm weight)")
    if a.save_score < 6:
        a.improvements.append("Add actionable value (code example, step-by-step, or tip) to drive bookmarks")
    if a.has_link:
        a.improvements.append("Move the link to a self-reply to avoid the -5x algorithm penalty")
    if a.hashtag_count > 2:
        a.improvements.append(f"Reduce hashtags from {a.hashtag_count} to 2 or fewer")
    if a.char_count < 100:
        a.improvements.append("Expand the tweet — optimal length is 200-250 characters")
    if a.engagement_bait:
        a.improvements.append("Remove engagement bait phrases — the algorithm penalizes these")
    if a.share_score < 8:
        a.improvements.append("Add a quotable one-liner that others would want to retweet")

    return a


def format_scorecard(analysis: TweetAnalysis, follower_count: int = 1000) -> str:
    """Format a TweetAnalysis as a human-readable scorecard."""
    score = analysis.total_score
    if score >= SCORE_THRESHOLDS["excellent"]:
        label = SCORE_LABELS["excellent"]
    elif score >= SCORE_THRESHOLDS["good"]:
        label = SCORE_LABELS["good"]
    elif score >= SCORE_THRESHOLDS["average"]:
        label = SCORE_LABELS["average"]
    elif score >= SCORE_THRESHOLDS["below_average"]:
        label = SCORE_LABELS["below_average"]
    else:
        label = SCORE_LABELS["poor"]

    # Impression estimate
    base_rate = 0.10
    if score >= 80:
        mult = 5.0
    elif score >= 60:
        mult = 3.0
    elif score >= 40:
        mult = 1.5
    else:
        mult = 0.8
    base_imp = follower_count * base_rate * mult
    low_imp = int(base_imp * 0.6)
    high_imp = int(base_imp * 1.8)

    def bar(val: float, max_val: float) -> str:
        filled = int((val / max_val) * 10)
        return "█" * filled + "░" * (10 - filled)

    lines = [
        f"Engagement Score: {score:.0f}/100  — {label}",
        "",
        f"  Hook Strength:   {bar(analysis.hook_score, 20)} {analysis.hook_score:.0f}/20",
        f"  Reply Potential:  {bar(analysis.reply_score, 20)} {analysis.reply_score:.0f}/20",
        f"  Share Potential:  {bar(analysis.share_score, 20)} {analysis.share_score:.0f}/20",
        f"  Save Potential:   {bar(analysis.save_score, 15)} {analysis.save_score:.0f}/15",
        f"  Algorithm Fit:    {bar(analysis.algorithm_score, 15)} {analysis.algorithm_score:.0f}/15",
        f"  Audience Match:   {bar(analysis.audience_score, 10)} {analysis.audience_score:.0f}/10",
        "",
    ]

    if analysis.improvements:
        lines.append("Top Improvements:")
        for i, imp in enumerate(analysis.improvements[:3], 1):
            lines.append(f"  {i}. {imp}")
        lines.append("")

    lines.append(f"Estimated impressions ({follower_count:,} followers): {low_imp:,}-{high_imp:,}")

    return "\n".join(lines)
