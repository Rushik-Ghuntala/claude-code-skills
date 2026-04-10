"""
X API MCP Response Processing Helpers

Utility functions for processing responses from the X/Twitter MCP server.
Handles both live mode (MCP available) and offline mode (fallback) gracefully.

Used by: All skills that interact with X API data
"""

from typing import Any


def is_live_mode(mcp_tools: list[str] | None = None) -> bool:
    """Check if MCP tools are available for live X API access."""
    if mcp_tools is None:
        return False
    x_tools = [t for t in mcp_tools if "twitter" in t.lower() or "x-" in t.lower()]
    return len(x_tools) > 0


def parse_tweet(raw_tweet: dict[str, Any]) -> dict[str, Any]:
    """Parse a raw tweet object from MCP into a standardized format."""
    return {
        "id": raw_tweet.get("id", ""),
        "text": raw_tweet.get("text", ""),
        "author": raw_tweet.get("author", {}).get("username", "unknown"),
        "author_followers": raw_tweet.get("author", {}).get("followers_count", 0),
        "likes": raw_tweet.get("public_metrics", {}).get("like_count", 0),
        "retweets": raw_tweet.get("public_metrics", {}).get("retweet_count", 0),
        "replies": raw_tweet.get("public_metrics", {}).get("reply_count", 0),
        "bookmarks": raw_tweet.get("public_metrics", {}).get("bookmark_count", 0),
        "impressions": raw_tweet.get("public_metrics", {}).get("impression_count", 0),
        "created_at": raw_tweet.get("created_at", ""),
        "has_media": bool(raw_tweet.get("attachments", {}).get("media_keys")),
        "has_links": "http" in raw_tweet.get("text", ""),
        "is_thread": raw_tweet.get("conversation_id") != raw_tweet.get("id"),
    }


def calculate_engagement_rate(tweet: dict[str, Any]) -> float:
    """Calculate engagement rate for a parsed tweet."""
    impressions = tweet.get("impressions", 0)
    if impressions == 0:
        return 0.0
    total_engagement = (
        tweet.get("likes", 0)
        + tweet.get("retweets", 0) * 2
        + tweet.get("replies", 0) * 3
        + tweet.get("bookmarks", 0) * 2
    )
    return (total_engagement / impressions) * 100


def parse_trending_topics(raw_trends: list[dict]) -> list[dict[str, Any]]:
    """Parse trending topics from MCP response."""
    parsed = []
    for trend in raw_trends:
        parsed.append({
            "name": trend.get("name", ""),
            "tweet_volume": trend.get("tweet_volume", 0),
            "url": trend.get("url", ""),
            "category": categorize_trend(trend.get("name", "")),
        })
    return sorted(parsed, key=lambda x: x["tweet_volume"] or 0, reverse=True)


def categorize_trend(trend_name: str) -> str:
    """Categorize a trending topic into dev-relevant categories."""
    trend_lower = trend_name.lower()

    dev_keywords = {
        "language": ["python", "javascript", "rust", "go", "java", "typescript", "swift", "kotlin"],
        "framework": ["react", "vue", "next", "svelte", "django", "flask", "spring", "rails"],
        "ai_ml": ["ai", "gpt", "llm", "ml", "claude", "copilot", "openai", "anthropic"],
        "devops": ["docker", "kubernetes", "aws", "azure", "gcp", "ci/cd", "deploy"],
        "career": ["interview", "salary", "layoff", "hiring", "remote", "job"],
        "tools": ["vscode", "vim", "git", "github", "terminal", "cli"],
    }

    for category, keywords in dev_keywords.items():
        if any(kw in trend_lower for kw in keywords):
            return category

    return "general"


def format_number(n: int) -> str:
    """Format large numbers for display (e.g., 1500 -> 1.5K)."""
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    elif n >= 1_000:
        return f"{n / 1_000:.1f}K"
    return str(n)


def estimate_impressions(
    follower_count: int,
    engagement_score: int,
    has_media: bool = False,
    is_thread: bool = False,
) -> tuple[int, int]:
    """
    Estimate impression range based on follower count and engagement score.

    Returns (low_estimate, high_estimate).
    """
    # Base impression rate (% of followers who see the tweet)
    base_rate = 0.10  # ~10% of followers see organic tweets

    # Score multiplier (higher score = more algorithmic boost)
    if engagement_score >= 80:
        score_mult = 5.0
    elif engagement_score >= 60:
        score_mult = 3.0
    elif engagement_score >= 40:
        score_mult = 1.5
    elif engagement_score >= 20:
        score_mult = 0.8
    else:
        score_mult = 0.5

    # Format bonuses
    format_mult = 1.0
    if has_media:
        format_mult *= 2.0
    if is_thread:
        format_mult *= 1.5

    base = follower_count * base_rate * score_mult * format_mult
    low = int(base * 0.6)
    high = int(base * 1.8)

    # Minimum floor
    low = max(low, 50)
    high = max(high, low * 2)

    return (low, high)
