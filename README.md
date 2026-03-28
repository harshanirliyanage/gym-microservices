# 🏋️ Gym Management System - Microservices Architecture

> **IT4020 - Modern Topics in IT | Assignment 2**
> Sri Lanka Institute of Information Technology (SLIIT)
> Year 4 Semester 1 | 2026

---

## 👥 Group Members & Contributions

| Name | Service | Port |
|------|---------|------|
| Raveesha (Leader) | Member Service | 8001 |
| Jaya | Trainer Service | 8002 |
| Pabasara | Workout Service | 8003 |
| Laks | Equipment Service | 8004 |

> **API Gateway runs on Port 8000**

---

## 📋 Project Overview

This project implements a **Microservices Architecture** for a Gym Management System using Python FastAPI. Each service is independently deployable and communicates through a central API Gateway.

### Business Domain: Gym Management
- **Member Service** → Manage gym memberships
- **Trainer Service** → Manage gym trainers
- **Workout Service** → Manage workout plans
- **Equipment Service** → Manage gym equipment

---

## 🏗️ Project Structure

```
gym-microservices/
│
├── gateway/                    # API Gateway (Port 8000)
│   └── main.py                 # Routes all requests to microservices
│
├── member-service/             # Member Microservice (Port 8001) - Raveesha
│   ├── models.py               # Pydantic data models
│   ├── data_service.py         # Mock data layer
│   ├── service.py              # Business logic layer
│   └── main.py                 # FastAPI application & endpoints
│
├── trainer-service/            # Trainer Microservice (Port 8002) - Jaya
│   ├── models.py
│   ├── data_service.py
│   ├── service.py
│   └── main.py
│
├── workout-service/            # Workout Microservice (Port 8003) - Pabasara
│   ├── models.py
│   ├── data_service.py
│   ├── service.py
│   └── main.py
│
├── equipment-service/          # Equipment Microservice (Port 8004) - Laks
│   ├── models.py
│   ├── data_service.py
│   ├── service.py
│   └── main.py
│
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
└── README.md                   # Project documentation
```

---

## 🏛️ Architecture Diagram

```
                        ┌─────────────────────────────┐
                        │         CLIENT               │
                        │  (Browser / Postman)         │
                        └──────────────┬──────────────┘
                                       │
                                       ▼
                        ┌─────────────────────────────┐
                        │       API GATEWAY            │
                        │      Port: 8000              │
                        │  http://localhost:8000/docs  │
                        └──────┬───────┬───────┬──────┘
                               │       │       │       │
               ┌───────────────┘       │       │       └───────────────┐
               │               ┌───────┘       └───────┐               │
               ▼               ▼                       ▼               ▼
    ┌──────────────┐ ┌──────────────┐     ┌──────────────┐ ┌──────────────┐
    │   MEMBER     │ │   TRAINER    │     │   WORKOUT    │ │  EQUIPMENT   │
    │   SERVICE    │ │   SERVICE    │     │   SERVICE    │ │   SERVICE    │
    │  Port: 8001  │ │  Port: 8002  │     │  Port: 8003  │ │  Port: 8004  │
    └──────────────┘ └──────────────┘     └──────────────┘ └──────────────┘
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/gym-microservices.git
cd gym-microservices
```

### Step 2: Create & Activate Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Services

You need to open **5 separate terminals** and run each service:

### Terminal 1 — Member Service
```bash
cd member-service
uvicorn main:app --reload --port 8001
```

### Terminal 2 — Trainer Service
```bash
cd trainer-service
uvicorn main:app --reload --port 8002
```

### Terminal 3 — Workout Service
```bash
cd workout-service
uvicorn main:app --reload --port 8003
```

### Terminal 4 — Equipment Service
```bash
cd equipment-service
uvicorn main:app --reload --port 8004
```

### Terminal 5 — API Gateway (Start this last)
```bash
cd gateway
uvicorn main:app --reload --port 8000
```

---

## 📖 API Documentation (Swagger UI)

Once all services are running, access the interactive docs:

| Service | Direct URL | Via Gateway |
|---------|-----------|-------------|
| API Gateway | http://localhost:8000/docs | - |
| Member Service | http://localhost:8001/docs | http://localhost:8000/gateway/members |
| Trainer Service | http://localhost:8002/docs | http://localhost:8000/gateway/trainers |
| Workout Service | http://localhost:8003/docs | http://localhost:8000/gateway/workouts |
| Equipment Service | http://localhost:8004/docs | http://localhost:8000/gateway/equipment |

---

## 🔌 API Endpoints

### Member Service (Raveesha)
| Method | Direct Endpoint | Gateway Endpoint | Description |
|--------|----------------|-----------------|-------------|
| GET | `/api/members` | `/gateway/members` | Get all members |
| GET | `/api/members/{id}` | `/gateway/members/{id}` | Get member by ID |
| POST | `/api/members` | `/gateway/members` | Create new member |
| PUT | `/api/members/{id}` | `/gateway/members/{id}` | Update member |
| DELETE | `/api/members/{id}` | `/gateway/members/{id}` | Delete member |

### Trainer Service (Jaya)
| Method | Direct Endpoint | Gateway Endpoint | Description |
|--------|----------------|-----------------|-------------|
| GET | `/api/trainers` | `/gateway/trainers` | Get all trainers |
| GET | `/api/trainers/{id}` | `/gateway/trainers/{id}` | Get trainer by ID |
| POST | `/api/trainers` | `/gateway/trainers` | Create new trainer |
| PUT | `/api/trainers/{id}` | `/gateway/trainers/{id}` | Update trainer |
| DELETE | `/api/trainers/{id}` | `/gateway/trainers/{id}` | Delete trainer |

### Workout Service (Pabasara)
| Method | Direct Endpoint | Gateway Endpoint | Description |
|--------|----------------|-----------------|-------------|
| GET | `/api/workouts` | `/gateway/workouts` | Get all workouts |
| GET | `/api/workouts/{id}` | `/gateway/workouts/{id}` | Get workout by ID |
| POST | `/api/workouts` | `/gateway/workouts` | Create new workout |
| PUT | `/api/workouts/{id}` | `/gateway/workouts/{id}` | Update workout |
| DELETE | `/api/workouts/{id}` | `/gateway/workouts/{id}` | Delete workout |

### Equipment Service (Laks)
| Method | Direct Endpoint | Gateway Endpoint | Description |
|--------|----------------|-----------------|-------------|
| GET | `/api/equipment` | `/gateway/equipment` | Get all equipment |
| GET | `/api/equipment/{id}` | `/gateway/equipment/{id}` | Get equipment by ID |
| POST | `/api/equipment` | `/gateway/equipment` | Add new equipment |
| PUT | `/api/equipment/{id}` | `/gateway/equipment/{id}` | Update equipment |
| DELETE | `/api/equipment/{id}` | `/gateway/equipment/{id}` | Delete equipment |

---

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| Python 3.8+ | Programming Language |
| FastAPI | Web Framework for building APIs |
| Uvicorn | ASGI Server to run FastAPI |
| HTTPx | HTTP client for gateway routing |
| Pydantic | Data validation and modeling |
| Swagger UI | Auto-generated API documentation |

---

## 💡 Why API Gateway?

Without a gateway, clients need to know and call **multiple ports**:
```
❌ Without Gateway:
   Member   → http://localhost:8001
   Trainer  → http://localhost:8002
   Workout  → http://localhost:8003
   Equipment→ http://localhost:8004
```

With the API Gateway, everything goes through **one single port**:
```
✅ With Gateway:
   Everything → http://localhost:8000
```

**Benefits of API Gateway:**
- Single entry point for all requests
- Hides internal service ports from clients
- Can handle authentication, logging, and rate limiting
- Simplifies client-side code

---

## 📦 Dependencies

```
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
httpx==0.25.1
python-multipart==0.0.6
```

---

## 👨‍💻 Team Workflow (Git)

### Pull latest changes before coding
```bash
git pull origin main
```

### Push your changes
```bash
git add .
git commit -m "Your descriptive message here"
git push origin main
```

### Each member only works in their own folder!
- Raveesha → `member-service/`
- Jaya → `trainer-service/`
- Pabasara → `workout-service/`
- Laks → `equipment-service/`

---

*IT4020 Modern Topics in IT | SLIIT | 2026*
