"""
_path_bootstrap.py — Imported first by every module that needs project-root imports.

Adds the directory containing this file (the project root) to sys.path exactly once.
Works on local machines, Streamlit Community Cloud (/mount/src/...), and in pytest.
"""
import sys
from pathlib import Path

# This file lives at the project root, so its parent IS the root.
_ROOT = Path(__file__).resolve().parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
