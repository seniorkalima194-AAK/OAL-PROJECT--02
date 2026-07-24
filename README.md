<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=D4AF37&height=220&section=header&text=Offline-adaptive%20learning%20website&fontSize=55&fontColor=2C1A00&fontAlignY=38&desc=A%20website%20for%20upgrading%20performance%20of%20students&descAlignY=58&descSize=18" width="100%"/>
</div>

### *Empowering Personalized Education Without Internet Connectivity*

<p align="center">

<img src="https://img.shields.io/badge/Status-Under%20Development-0A66C2?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Version-1.0-blueviolet?style=for-the-badge"/>
<img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge"/>
<img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react&logoColor=black"/>
<img src="https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql&logoColor=white"/>

</p>

# 🎓 Adaptive Learning System

> ALS — An offline-first intelligent learning platform that personalises lesson sequences and quiz difficulty based on individual student performance — no internet connection required at runtime.

[📖 Documentation](#-documentation) · [🚀 Quick Start](#-quick-start) · [📡 API Reference](#-api-reference) · [🤝 Contributing](#-contributing)

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Environment Variables](#-environment-variables)
- [API Reference](#-api-reference)
- [Adaptive Engine](#-adaptive-engine)
- [Role System](#-role-system)
- [Database Schema](#-database-schema)
- [Testing](#-testing)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

## 📌 About the Project

The **Adaptive Learning System (ALS)** is a full-stack offline-capable application built for educational environments with unreliable or no internet access. It delivers a personalised curriculum to each student by continuously evaluating quiz performance and automatically adjusting lesson difficulty — no instructor intervention required.

The backend is a versioned REST API built with **FastAPI**, persisting to a local **SQLite** database via **SQLAlchemy 2.x**. The frontend is a **React SPA** with role-gated views for students and administrators. At the centre of the system is an adaptive engine that scores quizzes, tracks progress, and recommends the next lesson based on configurable performance thresholds.

All architectural decisions — schema design, API contracts, service layer boundaries, middleware stack — are documented as living artefacts in `/docs` and must remain in sync with the codebase they describe.

---

## ✨ Key Features

- 🔌 **Offline-first** — SQLite database, zero external service dependencies at runtime
- 🧠 **Adaptive engine** — promotes, demotes, or holds lesson difficulty based on real student performance
- 🔐 **JWT authentication** — stateless token-based auth with configurable expiry and refresh
- 🛡️ **Role-based access control** — student and admin roles enforced at the middleware layer
- 📡 **Versioned REST API** — all endpoints under `/api/v1/` with consistent `{data, error, meta}` envelopes
- 📋 **Auto-generated OpenAPI docs** — Swagger UI and ReDoc available in development mode
- 🪵 **Structured request logging** — every request logged with method, path, status, duration, and trace ID
- 🏗️ **Clean architecture** — strict layer separation: routes → services → repositories → models
- 🧪 **Isolated test suite** — in-memory SQLite, fresh session per test, 80%+ coverage enforced

---

## 🏗️ System Architecture

```
┌──────────────────────────────────────────────────────┐
│                     React SPA                        │
│              React Router v6  ·  Axios               │
│         Student Views      Admin Dashboard           │
└─────────────────────┬────────────────────────────────┘
                      │  HTTP REST  /api/v1/
┌─────────────────────▼────────────────────────────────┐
│                  FastAPI Backend                      │
│                                                      │
│   ┌─────────────────────────────────────────────┐    │
│   │               Middleware Stack              │    │
│   │  request_logger → auth.py → permissions.py │    │
│   └──────────────────────┬──────────────────────┘    │
│                          │                           │
│   ┌──────────────────────▼──────────────────────┐    │
│   │            Routes  /api/v1/                 │    │
│   │  auth  · lessons  · quizzes  · progress     │    │
│   │  adaptive                                   │    │
│   └──────────────────────┬──────────────────────┘    │
│                          │                           │
│   ┌──────────────────────▼──────────────────────┐    │
│   │                  Services                   │    │
│   │  auth · lesson · quiz · progress            │    │
│   │  recommendation · adaptive_engine           │    │
│   └──────────────────────┬──────────────────────┘    │
│                          │                           │
│   ┌──────────────────────▼──────────────────────┐    │
│   │               Repositories                  │    │
│   │  student · lesson · question · result       │    │
│   └──────────────────────┬──────────────────────┘    │
│                          │                           │
│   ┌──────────────────────▼──────────────────────┐    │
│   │            SQLite  learning_system.db        │    │
│   │   Student · Lesson · Question · QuizResult  │    │
│   │   Progress · Recommendation · Subject       │    │
│   └─────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

### Backend

| Concern | Technology |
|---|---|
| Framework | FastAPI |
| ORM | SQLAlchemy 2.x |
| Migrations | Alembic |
| Validation | Pydantic v2 |
| Authentication | JWT — python-jose |
| Password hashing | passlib\[bcrypt\] |
| Database | SQLite (dev) · PostgreSQL-ready |
| Logging | structlog |
| Testing | pytest · pytest-asyncio · httpx |
| Config | pydantic-settings BaseSettings |

### Frontend

| Concern | Technology |
|---|---|
| Framework | React 18 |
| Routing | React Router v6 |
| HTTP client | Axios |
| State management | Custom hooks |

---

## 📁 Project Structure

```
adaptive-learning-system/
│
├── backend/
│   ├── api/
│   │   ├── routes/                  # Thin endpoint handlers — no business logic
│   │   │   ├── auth_routes.py
│   │   │   ├── lesson_routes.py
│   │   │   ├── quiz_routes.py
│   │   │   ├── progress_routes.py
│   │   │   └── adaptive_routes.py
│   │   └── dependencies/            # FastAPI Depends providers
│   │
│   ├── core/                        # Cross-cutting foundation
│   │   ├── config.py                # Pydantic BaseSettings — single env var source
│   │   ├── security.py              # JWT encode/decode, password hashing
│   │   ├── middleware.py            # Middleware registration and ordering
│   │   ├── logging.py               # Structured JSON logger
│   │   └── constants.py            # Typed literals — roles, limits, thresholds
│   │
│   ├── database/
│   │   ├── connection.py            # Engine, sessionmaker, get_db()
│   │   ├── migrations/              # Alembic revision scripts
│   │   └── seeders/                 # Development and test seed data
│   │
│   ├── middleware/                  # HTTP-layer gates
│   │   ├── auth.py                  # JWT verification → request.state principal
│   │   ├── permissions.py           # Role enforcement (student vs admin)
│   │   └── request_logger.py        # Request/response logging with trace ID
│   │
│   ├── models/                      # SQLAlchemy declarative models (schema source of truth)
│   │   ├── student.py
│   │   ├── subject.py
│   │   ├── lesson.py
│   │   ├── question.py
│   │   ├── quiz_result.py
│   │   ├── progress.py
│   │   └── recommendation.py
│   │
│   ├── repositories/                # All database query logic
│   │   ├── student_repository.py
│   │   ├── lesson_repository.py
│   │   ├── question_repository.py
│   │   └── result_repository.py
│   │
│   ├── schemas/                     # Pydantic request/response contracts
│   │   ├── student_schema.py
│   │   ├── auth_schema.py
│   │   ├── lesson_schema.py
│   │   ├── question_schema.py
│   │   ├── quiz_schema.py
│   │   └── progress_schema.py
│   │
│   ├── services/                    # Business logic and orchestration
│   │   ├── auth_service.py
│   │   ├── lesson_service.py
│   │   ├── quiz_service.py
│   │   ├── progress_service.py
│   │   ├── recommendation_service.py
│   │   └── adaptive_engine.py       # Core adaptive algorithm
│   │
│   ├── storage/                     # Physical asset directories
│   │   ├── images/
│   │   ├── documents/
│   │   │   ├── lessons/
│   │   │   ├── notes/
│   │   │   └── pdfs/
│   │   └── videos/
│   │
│   ├── tests/                       # Isolated pytest test suite
│   │   ├── conftest.py              # Fixtures: DB session, test client, factories
│   │   ├── test_auth.py
│   │   ├── test_quiz.py
│   │   ├── test_progress.py
│   │   └── test_adaptive_engine.py
│   │
│   ├── utils/                       # Pure stateless utility functions
│   │   ├── helpers.py
│   │   ├── validators.py
│   │   ├── score_calculator.py
│   │   └── level_generator.py
│   │
│   ├── main.py                      # FastAPI app entry point
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── services/
│   │   └── routes/
│   └── public/
│
├── docs/                            # Living project documentation
│   ├── ProjectProposal.docx
│   ├── SRS.docx
│   ├── DatabaseDesign.docx
│   ├── API_Documentation.docx
│   ├── UserManual.docx
│   └── FinalReport.docx
│
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/your-username/adaptive-learning-system.git
cd adaptive-learning-system
```

### 2. Backend setup

```bash
cd backend
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Frontend setup

```bash
cd ../frontend
npm install
```

### 4. Configure environment

```bash
cp backend/.env.example backend/.env
# Open .env and fill in all required values — see Environment Variables below
```

### 5. Apply database migrations

```bash
cd backend
alembic upgrade head
```

> ⚠️ Never use `Base.metadata.create_all()` in production. Alembic is the only sanctioned schema management path.

### 6. (Optional) Seed development data

```bash
python -m database.seeders.seed_dev
```

### 7. Run the application

```bash
# Backend — from /backend
uvicorn main:app --reload --port 8000

# Frontend — from /frontend
npm run dev
```

| Service | URL |
|---|---|
| Frontend | `http://localhost:5173` |
| API | `http://localhost:8000/api/v1/` |
| Swagger UI | `http://localhost:8000/docs` |
| ReDoc | `http://localhost:8000/redoc` |

---

## 📋 Documentation

All project documentation lives in `/docs` as `.docx` files and must remain in sync with the codebase:

| Document | Purpose |
|---|---|
| `ProjectProposal.docx` | System rationale, goals, and stakeholders |
| `SRS.docx` | Functional and non-functional requirements with acceptance criteria |
| `DatabaseDesign.docx` | ERD, table definitions, and constraint rationale |
| `API_Documentation.docx` | Human-readable rendering of the OpenAPI schema |
| `UserManual.docx` | Student and admin usage guide with screenshots |
| `FinalReport.docx` | Architecture decisions, retrospective, and deployment summary |

> Stale documentation is a defect. Any schema, API contract, or architecture change requires a corresponding doc update in the same PR.

---

## 🔐 Environment Variables

| Variable | Description | Required |
|---|---|---|
| `DATABASE_URL` | SQLite path or PostgreSQL DSN | ✅ |
| `SECRET_KEY` | JWT signing secret (min 32 chars) | ✅ |
| `ALGORITHM` | JWT algorithm — `HS256` | ✅ |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token TTL in minutes | ✅ |
| `STUDENT_SCORE_THRESHOLD_LOW` | Score below which difficulty decreases | ✅ |
| `STUDENT_SCORE_THRESHOLD_HIGH` | Score above which difficulty increases | ✅ |
| `MAX_UPLOAD_SIZE_MB` | Maximum allowed file upload size | ✅ |
| `SCORE_VERSION` | Active scoring formula version | ✅ |
| `ENVIRONMENT` | `development` or `production` | ✅ |

> There are no silent defaults for secrets. The app fails fast with a clear error if any required variable is missing at startup.

---

## 📡 API Reference

All endpoints are versioned under `/api/v1/`. Every response follows a consistent envelope:

```json
{
  "data": {},
  "error": null,
  "meta": {
    "trace_id": "550e8400-e29b-41d4-a716",
    "timestamp": "2026-06-27T10:00:00Z"
  }
}
```

### Authentication

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| `POST` | `/api/v1/auth/register` | ❌ | Register a new student account |
| `POST` | `/api/v1/auth/login` | ❌ | Obtain JWT access token |
| `POST` | `/api/v1/auth/refresh` | ✅ | Refresh an access token |

### Lessons

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| `GET` | `/api/v1/lessons` | ✅ | List all available lessons |
| `GET` | `/api/v1/lessons/{id}` | ✅ | Get a single lesson by ID |
| `POST` | `/api/v1/lessons` | ✅ Admin | Create a new lesson |
| `PATCH` | `/api/v1/lessons/{id}` | ✅ Admin | Update an existing lesson |
| `DELETE` | `/api/v1/lessons/{id}` | ✅ Admin | Remove a lesson |

### Quizzes

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| `GET` | `/api/v1/quizzes/{lesson_id}` | ✅ | Get quiz questions for a lesson |
| `POST` | `/api/v1/quizzes/{lesson_id}/submit` | ✅ | Submit answers and receive scored result |

### Progress

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| `GET` | `/api/v1/progress` | ✅ | Get authenticated student's progress |
| `GET` | `/api/v1/progress/report` | ✅ Admin | Get all students' aggregated progress |

### Adaptive Engine

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| `GET` | `/api/v1/adaptive/next-lesson` | ✅ | Get the recommended next lesson for the current student |

> **HTTP 401** — missing or expired JWT · **HTTP 403** — insufficient role · **HTTP 405** — unsupported method · **HTTP 422** — validation failure with field-level detail

---

## 🧠 Adaptive Engine

The adaptive engine lives in `services/adaptive_engine.py` and exposes a single callable interface:

```python
recommend_next_lesson(student_id: int, recent_results: list[QuizResult]) -> Lesson
```

### Decision Logic

```
avg(recent scores) < STUDENT_SCORE_THRESHOLD_LOW   →  difficulty - 1  (easier lesson)
avg(recent scores) > STUDENT_SCORE_THRESHOLD_HIGH  →  difficulty + 1  (harder lesson)
otherwise                                          →  difficulty ± 0  (same level)
```

- All thresholds are sourced from `core/constants.py` — never hardcoded in the engine
- The engine is **stateless** and HTTP-context-free — fully unit-testable without mocking FastAPI
- Formula version tracked via `SCORE_VERSION` constant to support re-scoring historical results

---

## 👥 Role System

| Role | Capabilities |
|---|---|
| `student` | Register · Login · View lessons · Submit quizzes · View own progress · Get adaptive recommendations |
| `admin` | All student capabilities + Create/edit/delete lessons · View all students' progress reports |

Roles are enforced exclusively at `middleware/permissions.py`. Role checks are never duplicated inside individual endpoint handlers.

---

## 🗄️ Database Schema

Core tables and their relationships:

```
Student ──────────┬──── QuizResult ────── Question ──── Lesson ──── Subject
    │             │                                         │
    └──── Progress └──── Recommendation ──────────────────►┘
```

| Table | Primary Key | Key Columns |
|---|---|---|
| `students` | `id` | `email`, `password_hash`, `role`, `created_at` |
| `subjects` | `id` | `name`, `description` |
| `lessons` | `id` | `subject_id`, `title`, `difficulty`, `content_path` |
| `questions` | `id` | `lesson_id`, `body`, `correct_answer`, `weight` |
| `quiz_results` | `id` | `student_id`, `lesson_id`, `score`, `submitted_at` |
| `progress` | `id` | `student_id`, `lesson_id`, `status`, `updated_at` |
| `recommendations` | `id` | `student_id`, `lesson_id`, `reason`, `created_at` |

> The `DatabaseDesign.docx` in `/docs` contains the full ERD and constraint rationale. It must match `/models` with zero discrepancies at all times.

---

## 🧪 Testing

```bash
cd backend

# Run full test suite
pytest

# Run with coverage report
pytest --cov=. --cov-report=term-missing

# Run a specific test module
pytest tests/test_adaptive_engine.py -v

# Run async tests only
pytest -m asyncio -v
```

### Coverage Targets

| Layer | Target |
|---|---|
| `services/` | 90% |
| `repositories/` | 85% |
| `utils/` | 100% |
| Overall minimum | 80% |

### Test Design Rules

- All tests use an **in-memory SQLite database** — no dependency on the production `.db` file
- Each test function receives a **fresh session via pytest fixture** — no shared state between tests
- External dependencies are mocked with `unittest.mock.patch`
- `conftest.py` provides: DB session fixture · test FastAPI client fixture · Student, Lesson, and Question factory helpers
- `test_adaptive_engine.py` must cover three branches: below threshold, at threshold, above threshold

---

## 🗺️ Roadmap

- [x] Core authentication — register, login, JWT refresh
- [x] Lesson CRUD with admin role gate
- [x] Quiz submission and scoring
- [x] Adaptive engine v1 — threshold-based difficulty adjustment
- [x] Progress tracking and aggregation
- [x] Structured request logging with trace IDs
- [ ] Adaptive engine v2 — weighted rolling average over last N results
- [ ] Offline PWA shell for the frontend
- [ ] Admin analytics dashboard with progress heatmaps
- [ ] Export progress reports to PDF
- [ ] PostgreSQL migration guide for production deployment

---

## 🤝 Contributing

1. Browse the open **GitHub Issues** — every backend folder has a dedicated issue with objectives and acceptance criteria
2. **Assign yourself** to the issue before starting work to avoid duplication
3. Create a branch following the convention below
4. Implement the changes and write tests — PRs without tests for new logic will **not** be merged
5. Open a PR that references the issue (`Closes #N`)
6. Any schema, API contract, or architecture change requires a corresponding `/docs` update **in the same PR**

### 🌿 Branch Naming Convention

```
{scope}-{short-description}

Examples:
  models-orm-schema-definitions
  services-adaptive-engine
  api-routes-http-surface
  middleware-jwt-auth
  database-connection-and-migrations
  frontend-progress-dashboard
  tests-backend-quality-gate
```

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Built with precision · Documented with intent · Tested before merged
</p>
