"""
config.py — Central configuration and constants for MINDMAP.

All tuneable defaults live here. Never hard-code model names or
thresholds in multiple places — import from this module instead.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# LLM
# ---------------------------------------------------------------------------
DEFAULT_MODEL_NAME: str = "gemini-2.5-flash"

# ---------------------------------------------------------------------------
# Pattern-flag defaults (users can override in Settings)
# ---------------------------------------------------------------------------
DEFAULT_MOOD_LOW_THRESHOLD: int = 4       # mood ≤ this triggers low-mood flag
DEFAULT_STRESS_HIGH_THRESHOLD: int = 7    # stress ≥ this for stress+sleep flag
DEFAULT_LOW_MOOD_STREAK_DAYS: int = 5     # consecutive days for streak flag
DEFAULT_SLEEP_QUALITY_LOW: int = 2        # sleep_quality ≤ this for stress+sleep flag
DEFAULT_MOOD_DROP_THRESHOLD: int = 2      # week-over-week average drop to flag

# ---------------------------------------------------------------------------
# Mood emoji labels (index 0 = mood 1, index 9 = mood 10)
# ---------------------------------------------------------------------------
MOOD_EMOJIS: list[str] = [
    "😞", "😟", "😕", "😐", "🙂", "😊", "😄", "😁", "🤩", "🥳"
]

STRESS_EMOJIS: list[str] = [
    "😌", "🧘", "😐", "😑", "😤", "😣", "😰", "😨", "😱", "🤯"
]

SLEEP_QUALITY_LABELS: list[str] = [
    "😴 Terrible", "😪 Poor", "😐 Fair", "😊 Good", "🌟 Excellent"
]

# ---------------------------------------------------------------------------
# Entry tags
# ---------------------------------------------------------------------------
ENTRY_TAGS: list[str] = [
    "work", "family", "health", "exercise", "social",
    "travel", "finance", "relationship", "creativity", "rest",
]

# ---------------------------------------------------------------------------
# Crisis helplines by country code
# ---------------------------------------------------------------------------
CRISIS_LINES: dict[str, dict[str, str]] = {
    "US": {
        "name": "988 Suicide & Crisis Lifeline",
        "number": "988",
        "url": "https://988lifeline.org",
    },
    "UK": {
        "name": "Samaritans",
        "number": "116 123",
        "url": "https://www.samaritans.org",
    },
    "CA": {
        "name": "Crisis Services Canada",
        "number": "1-833-456-4566",
        "url": "https://www.crisisservicescanada.ca",
    },
    "AU": {
        "name": "Lifeline Australia",
        "number": "13 11 14",
        "url": "https://www.lifeline.org.au",
    },
    "IN": {
        "name": "iCall",
        "number": "9152987821",
        "url": "https://icallhelpline.org",
    },
    "Other": {
        "name": "International Association for Suicide Prevention",
        "number": "Visit website",
        "url": "https://www.iasp.info/resources/Crisis_Centres/",
    },
}

# ---------------------------------------------------------------------------
# Safety: mood score at or below this triggers crisis resources instead of AI
# ---------------------------------------------------------------------------
CRISIS_MOOD_THRESHOLD: int = 3

# ---------------------------------------------------------------------------
# Concerning language keywords (lowercase) — trigger crisis block
# ---------------------------------------------------------------------------
CRISIS_KEYWORDS: list[str] = [
    "suicide", "suicidal", "end my life", "kill myself", "self-harm",
    "self harm", "hurt myself", "don't want to be here", "don't want to live",
    "no reason to live",
]

# ---------------------------------------------------------------------------
# LLM system prompt template
# ---------------------------------------------------------------------------
SYSTEM_PROMPT: str = """
You are a warm, supportive wellness companion embedded in a personal journaling app.
Your role is to help users reflect on their emotional experiences in a gentle,
non-judgmental way. 

STRICT RULES — follow these without exception:
1. You are NOT a therapist, psychiatrist, or medical professional.
2. NEVER diagnose, prescribe, or suggest medical treatments.
3. NEVER interpret entries as symptoms of any clinical condition.
4. Keep all language supportive, curious, and strengths-based.
5. Ground every observation exclusively in what the user has shared in this session.
6. If the user seems distressed, gently acknowledge their feelings and encourage
   professional support — do not attempt to resolve clinical concerns.
7. Be concise. Warm but not saccharine. Human but not overfamiliar.
"""

# ---------------------------------------------------------------------------
# DB
# ---------------------------------------------------------------------------
DB_PATH: str = "mindmap.db"

# ---------------------------------------------------------------------------
# Demo data
# ---------------------------------------------------------------------------
DEMO_USERNAME: str = "demo_user"
DEMO_DAYS: int = 60
