"""
app.py — Entry point for MINDMAP.

Handles:
- Page configuration and theme
- DB initialisation
- Login gate (auth.py)
- Sidebar navigation
- Page routing to views/
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import streamlit as st

# Ensure the project root (folder containing app.py) is on sys.path.
# Works identically locally, on Streamlit Community Cloud, and in pytest.
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from db.database import init_db, get_settings
from views.auth import render_auth


# ---------------------------------------------------------------------------
# Page config (must be first Streamlit call)
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="MINDMAP 🧠",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------------------------------
# DB bootstrap
# ---------------------------------------------------------------------------

init_db()


# ---------------------------------------------------------------------------
# Auth gate
# ---------------------------------------------------------------------------

if "user_id" not in st.session_state:
    render_auth()
    st.stop()


# ---------------------------------------------------------------------------
# Sync session state with DB settings on every run
# ---------------------------------------------------------------------------

user_id: int = st.session_state["user_id"]
settings = get_settings(user_id)
if "crisis_country" not in st.session_state:
    st.session_state["crisis_country"] = settings.get("crisis_country", "US")


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

with st.sidebar:
    st.markdown("# 🧠 MINDMAP")
    st.caption("*Your private AI wellness journal*")
    st.divider()

    username: str = st.session_state.get("username", "User")
    st.markdown(f"👤 **{username}**")

    if st.button("🚪 Log out", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

    st.divider()

    PAGES = {
        "📅 Daily Check-in": "checkin",
        "🪞 AI Reflection": "reflection",
        "📊 Insights Dashboard": "dashboard",
        "📋 Weekly Summary": "weekly_summary",
        "🚩 Pattern Flags": "pattern_flags",
        "🏥 Therapist Report": "therapist_report",
        "⚙️ Settings": "settings",
    }

    selected_label = st.radio(
        "Navigate",
        options=list(PAGES.keys()),
        label_visibility="collapsed",
    )
    page_key = PAGES[selected_label]

    st.divider()
    st.caption(
        "⚕️ **Not a medical tool.**  \n"
        "Not a replacement for professional care.  \n"
        "If you are in crisis, please contact a helpline."
    )


# ---------------------------------------------------------------------------
# Page router
# ---------------------------------------------------------------------------

if page_key == "checkin":
    from views.checkin import render_checkin
    render_checkin()

elif page_key == "reflection":
    from views.reflection import render_reflection
    render_reflection()

elif page_key == "dashboard":
    from views.dashboard import render_dashboard
    render_dashboard()

elif page_key == "weekly_summary":
    from views.weekly_summary import render_weekly_summary
    render_weekly_summary()

elif page_key == "pattern_flags":
    from views.pattern_flags import render_pattern_flags
    render_pattern_flags()

elif page_key == "therapist_report":
    from views.therapist_report import render_therapist_report
    render_therapist_report()

elif page_key == "settings":
    from views.settings import render_settings
    render_settings()
