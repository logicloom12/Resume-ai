# � AI Hiring Integrity Platform

An enterprise-grade **Trust Infrastructure for Hiring** built on Flask. The system evaluates candidates across two independent intelligence layers — **Resume Intelligence** and **Interview Integrity** — and produces a composite trust score visible only to recruiters.

> **Employees never see internal scoring metrics.** This is by design.

---

## 🏗 Architecture

| Component | Technology |
|---|---|
| Core | Flask (Single Application) |
| Database | SQLite |
| Authentication | Bcrypt + OTP (Two-Factor) |
| Hashing | SHA-256 (Resume + Interview) |
| Scoring | Deterministic Engine + Hybrid AI Enhancement |
| Access Control | Role-Based (Employee / Recruiter) |
| Audit Trail | Full logging + hash verification |

---

## 📁 Project Structure

```
final_resume/
├── README.md
├── register_cli.py
└── hiring_platform/
    ├── app.py                        # Flask app factory & routes
    ├── config.py                     # Configuration (SMTP, API, secrets)
    ├── database.py                   # SQLite schema & migrations
    │
    ├── auth/                         # Authentication (Phase 1)
    │   ├── __init__.py
    │   └── routes.py                 # Login, register, OTP, logout
    │
    ├── resume_engine/                # Resume Intelligence (Phase 2)
    │   ├── __init__.py
    │   ├── routes.py                 # Upload, confirm, analysis
    │   ├── section_parser.py         # Layout-aware block parsing
    │   ├── hybrid_extractor.py       # NER + rule-based extraction
    │   ├── extractor.py              # Orchestrator
    │   └── scoring.py                # Deterministic resume scoring
    │
    ├── interview_engine/             # Interview Integrity (Phase 3)
    │   ├── __init__.py
    │   ├── routes.py                 # Start, submit, results, stream
    │   ├── integrity_monitor.py      # Deterministic integrity index
    │   ├── transcript_processor.py   # Text analysis metrics
    │   ├── deterministic_scorer.py   # Baseline answer scoring
    │   ├── ai_evaluator.py           # Controlled AI evaluation (30%)
    │   ├── hashing.py                # SHA-256 tamper detection
    │   └── video_manager.py          # Secure video upload/streaming
    │
    ├── static/
    │   ├── style.css
    │   ├── confirm.css
    │   └── interview.css
    │
    └── templates/
        ├── base.html
        ├── register.html / login.html
        ├── employee_dashboard.html
        ├── recruiter_dashboard.html
        ├── upload_resume.html
        ├── confirm_resume.html
        ├── resume_analysis.html
        ├── interview.html
        └── interview_results.html
```

---

## 🔐 Phase 1 — Authentication & Security

- Bcrypt password hashing
- OTP-based two-factor email verification
- Role-based access control (employee / recruiter)
- Session management with rate limiting
- CLI registration tool for admin use

---

## 📄 Phase 2 — Resume Intelligence Engine

- Layout-aware PDF parsing with section segmentation
- Hybrid extraction (NER + rule-based) with confidence metrics
- Deterministic scoring: skills (50%) + identity (20%) + GitHub (30%) − fraud penalty
- GitHub profile validation
- Human verification layer with editable confirmation page
- Resume versioning with SHA-256 hash chain

---

## 🎬 Phase 3 — Live Interview Integrity Engine

### Two Independent Layers

**Layer 1 — Integrity (Behavioral Trust)**
- Deterministic penalties — AI never touches this score
- Client-side monitoring via browser APIs:

| Monitor | Method | Frequency |
|---|---|---|
| Face detection | face-api.js | Every 3s |
| Silence detection | Web Audio API | Every 1s |
| Tab switch | `visibilitychange` | Instant |
| Window blur | `window.onblur` | Instant |
| Copy block | `copy` event + preventDefault | Instant |
| Fullscreen exit | `fullscreenchange` | Instant |
| DevTools | dimension heuristic | Every 3s |

**Layer 2 — Answer Intelligence (Communication Quality)**
- 70% deterministic baseline (word count, filler ratio, relevance, vocabulary)
- 30% AI enhancement (clarity, depth, accuracy, communication)
- AI influence deliberately limited and fallback-protected

### Interview Flow
1. Employee clicks **Start Live Interview** on dashboard
2. Opens isolated fullscreen interview page (new browser tab)
3. Records webcam + monitors integrity + live speech-to-text
4. Submit → backend processes: integrity index → transcript metrics → baseline score → AI evaluation → hash → store
5. Interview status updated to `COMPLETED`
6. Employee sees "Interview Completed — Under Review"

---

## � Score Visibility Policy

| Data | Employee | Recruiter |
|---|:---:|:---:|
| Resume submitted status | ✅ | ✅ |
| Resume version | ✅ | ✅ |
| Skills detected | ✅ | ✅ |
| Interview status | ✅ | ✅ |
| Resume Intelligence Score | ❌ | ✅ |
| Fraud Probability | ❌ | ✅ |
| Integrity Index | ❌ | ✅ |
| Baseline / AI / Final Score | ❌ | ✅ |
| Anomaly Breakdown | ❌ | ✅ |
| Composite Ranking | ❌ | ✅ |

> **Why?** Showing scores to employees causes anxiety, manipulation attempts, and demotivation. Scores remain backend-only.

---

## 📊 Final Composite Score Formula (Internal Only)

```
final_composite = 40% × resume_intelligence_score
                + 35% × integrity_index
                + 25% × answer_quality_score
```

Stored internally. Visible only on recruiter dashboard.

---

## � Getting Started

### Prerequisites
- Python 3.8+
- Gmail account with [App Passwords](https://myaccount.google.com/apppasswords) enabled

### Setup

```bash
git clone <your-repo-url>
cd final_resume/hiring_platform
pip install flask bcrypt python-dotenv requests
python database.py
python app.py
```

App runs at **http://127.0.0.1:5000**

### Configure Email

Edit `hiring_platform/config.py` or set environment variables:
```
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_16_char_app_password
```

---

## 🛣️ API Routes

| Method | Route | Access | Description |
|---|---|---|---|
| GET/POST | `/auth/register` | Public | User registration |
| GET/POST | `/auth/login` | Public | Login with OTP |
| GET | `/employee_dashboard` | Employee | Dashboard (no scores) |
| GET | `/recruiter_dashboard` | Recruiter | Full analytics |
| POST | `/resume/upload` | Employee | Resume upload |
| GET/POST | `/resume/confirm` | Employee | Verify & lock |
| GET | `/resume/analysis` | Employee | Profile view (no scores) |
| GET | `/interview/start` | Employee | Live interview |
| POST | `/interview/submit` | Employee | Submit recording |
| GET | `/interview/<id>/results` | Both | Role-based results |
| GET | `/interview/list` | Both | Interview listing |

---

## 🔒 Security

- No frontend scoring trust — all scores computed server-side
- No plaintext passwords (bcrypt)
- No public video URLs (authenticated streaming)
- SHA-256 hash chains for resume + interview tamper detection
- Full audit trail with verification functions
- OTP rate limiting (3 attempts max)

---

## 📄 License

This project is for educational and demonstration purposes.
