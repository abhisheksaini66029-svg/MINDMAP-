# MINDMAP 🧠 — AI-Powered Mental Wellness Journal

A private, AI-assisted journaling app built with **Python + Streamlit** and
powered by Google's **Gemini API**. Deployable on Streamlit Community Cloud.

> ⚕️ **MINDMAP is not a medical tool and does not replace professional mental health care.**

---

## 🚀 Live App

**Local:** [http://localhost:8502](http://localhost:8502)

To start the app at any time:

```bash
cd mindmap
streamlit run app.py
```

Streamlit prints the URL in the terminal — open it in your browser:

```
  Local URL:    http://localhost:8502
  Network URL:  http://<your-ip>:8502
  External URL: http://<public-ip>:8502
```

> If port 8502 is busy, Streamlit picks the next available port. Always use the URL printed in your terminal.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📅 Daily Check-in | Mood, stress, sleep, tags, and free-text note — one entry per day, editable |
| 🪞 AI Reflection | Gemini-generated warm reflection + 2 journaling prompts (consent-gated) |
| 📊 Insights Dashboard | Metric cards, line charts, scatter plot, and a calendar heatmap |
| 📋 Weekly AI Summary | 7-day narrative with themes, positives, and observations |
| 🚩 Pattern Flags | Transparent rule-based detection (no diagnoses, thresholds adjustable) |
| 🏥 Therapist Report | Opt-in PDF export with date range, preview, and download |
| ⚙️ Settings & Privacy | AI toggle, model name, thresholds, data export (CSV/JSON), delete all data |
| 🎲 Demo Data | 60 days of realistic sample entries including a low-mood stretch |

---

## 🛠️ Local Setup

### 1. Clone / copy the project

```bash
git clone <your-repo-url>
cd mindmap
```

### 2. Create a virtual environment

```bash
python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your Gemini API key

Copy the example secrets file:

```bash
# macOS / Linux
cp .streamlit/secrets.toml.example .streamlit/secrets.toml

# Windows
copy .streamlit\secrets.toml.example .streamlit\secrets.toml
```

Edit `.streamlit/secrets.toml` and add your key:

```toml
GEMINI_API_KEY = "your-actual-api-key-here"
```

Get a free key at: https://aistudio.google.com/app/apikey

> The app works fully without the key — AI features (Reflection, Weekly Summary)
> will show a friendly warning and be skipped automatically.

### 5. Run the app

```bash
streamlit run app.py
```

Open the URL printed in your terminal — typically **http://localhost:8502**.

---

## ☁️ Streamlit Community Cloud Deployment

1. Push your project to a **public or private GitHub repository**.
   Make sure `.streamlit/secrets.toml` is in your `.gitignore` — **never commit your key**.

2. Go to https://share.streamlit.io and click **New app**.

3. Select your repository, set the **Main file path** to `app.py`.

4. Under **Advanced settings → Secrets**, paste:
   ```toml
   GEMINI_API_KEY = "your-actual-api-key-here"
   ```

5. Click **Deploy**. Done!

> The SQLite database (`mindmap.db`) is created automatically in the app's
> working directory on first run. On Community Cloud, data persists between
> sessions but is wiped on redeploy — export your data regularly.

---

## 📁 Project Structure

```
mindmap/
├── app.py                        # Entry point & page router
├── config.py                     # Central constants & defaults
├── requirements.txt              # Pinned dependencies
├── .streamlit/
│   ├── config.toml               # Streamlit theme (no CSS/JS)
│   └── secrets.toml.example      # Template — commit this, NOT secrets.toml
├── db/
│   └── database.py               # SQLite schema + all CRUD operations
├── services/
│   ├── llm.py                    # Gemini wrapper (retry, consent guard, safety)
│   ├── analytics.py              # Metric aggregation + chart DataFrames
│   ├── flags.py                  # Rule-based pattern detection
│   └── report.py                 # PDF generation via ReportLab
├── views/
│   ├── auth.py                   # Login / register UI
│   ├── checkin.py                # Daily Check-in page
│   ├── reflection.py             # AI Reflection page
│   ├── dashboard.py              # Insights Dashboard page
│   ├── weekly_summary.py         # Weekly AI Summary page
│   ├── pattern_flags.py          # Pattern Flags page
│   ├── therapist_report.py       # Therapist Report page
│   └── settings.py               # Settings & Privacy page
└── tests/
    ├── test_flags.py             # 26 pytest unit tests — flag logic
    └── test_analytics.py         # 29 pytest unit tests — analytics
```

---

## 🧪 Running Tests

```bash
# From the mindmap/ directory
pytest tests/ -v
```

**55 tests, all pure Python** — no DB, no Streamlit, no network required.

```
55 passed in 0.90s
```

---

## 🔒 Privacy

- All data is stored **only in the local SQLite database** (`mindmap.db`).
- **Nothing is shared** with any third party without your explicit consent.
- AI features send journal entry text to the **Google Gemini API** only after
  you grant consent on the in-app consent screen.
- You can withdraw consent at any time in ⚙️ Settings.
- Passwords are stored as **bcrypt hashes** — never plain text.
- Export all your data (CSV / JSON) or delete everything from Settings.
- The Therapist Report PDF contains only your own raw data — no AI content.

---

## 🛡️ AI Safety

- The LLM uses a system prompt that enforces a **supportive, non-clinical tone**.
- The AI **never diagnoses, prescribes, or gives medical advice**.
- If a very low mood score (≤ 3) or concerning language is detected, a
  **crisis resources block** is shown instead of AI content.
- All AI outputs are clearly labelled as non-clinical.
- The AI on/off switch in Settings disables all Gemini calls immediately.

---

## ⚠️ Known Limitations

- **Single-device only by default**: The SQLite database is local. For multi-device
  access, replace `db/database.py` with a cloud database (e.g. Supabase, Neon).
- **Community Cloud data persistence**: Data may be lost on redeploy or hibernation.
  Export your data regularly using the Settings page.
- **Gemini quota**: Free-tier Gemini API keys have rate limits. The app handles
  quota errors gracefully and shows a friendly message.
- **PDF export**: ReportLab renders text-only; charts are not included in the PDF.
- **Single user per browser session**: No multi-user switching within one session.
- **No email / password reset**: This is a local-first app with no email integration.
  If you forget your password, delete `mindmap.db` to reset all accounts.

---

## 🧰 Tech Stack

| Layer | Choice |
|---|---|
| UI | Streamlit (native components only — no HTML/CSS/JS) |
| LLM | Google Gemini 2.5 Flash via `google-genai` SDK |
| Database | SQLite (via Python `sqlite3`) |
| Auth | bcrypt password hashing |
| Charts | Plotly + Altair |
| PDF | ReportLab |
| Retry | tenacity (exponential backoff) |
| Tests | pytest (55 tests) |
