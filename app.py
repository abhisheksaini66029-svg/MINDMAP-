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

# ── Step 1: fix sys.path before ANY local import ──────────────────────────
# _path_bootstrap.py lives at the project root and adds that root to
# sys.path.  Importing it here (and only here) means every subsequent
# import — including those inside db/ and views/ — always resolves,
# whether running locally, in pytest, or on Streamlit Community Cloud
# (/mount/src/<repo>/).
import _path_bootstrap  # noqa: F401  (side-effect import — do not remove)

import streamlit as st

# ── Step 2: local imports AFTER path is guaranteed ───────────────────────
from db.database import init_db, get_settings   # init_db() called below
from views.auth import render_auth               # render_auth() called below


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
# DB bootstrap — creates all SQLite tables on first run, no-ops thereafter
# ---------------------------------------------------------------------------

init_db()


# ---------------------------------------------------------------------------
# Auth gate — shows login/register screen; halts execution if not signed in
# ---------------------------------------------------------------------------

if "user_id" not in st.session_state:
    render_auth()
    st.stop()          # nothing below runs until the user is logged in


# ---------------------------------------------------------------------------
# Sync user settings into session state on every page load
# ---------------------------------------------------------------------------

user_id: int = st.session_state["user_id"]
settings = get_settings(user_id)          # reads from DB, never None
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
