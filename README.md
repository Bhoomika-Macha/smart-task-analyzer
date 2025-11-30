# 🧠 Smart Task Analyzer  
A lightweight intelligent task-prioritization tool built using **Django (backend)** and **HTML/CSS/JavaScript (frontend)**.  
This assignment demonstrates problem-solving, clean architecture, API design, edge-case handling, and algorithmic thinking.

---

## 🚀 Setup Instructions

### ✔ 1. Create Virtual Environment
    ```bash
    python -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows
### ✔ 2. Install Dependencies
    ```bash
    pip install -r requirements.txt
### ✔3. Run Backend (Django API)
    ```bash
    python manage.py runserver
Backend runs at: http://127.0.0.1:8000/  
### ✔4. Run Frontend
    ```bash
    cd frontend
    python -m http.server 9000 --bind 127.0.0.1
Open in browser: http://127.0.0.1:9000

### 🎯 Design Decisions
***✔ Minimalistic API***
Two endpoints:

/api/tasks/analyze/ → sorts tasks by priority

/api/tasks/suggest/ → returns top 3 tasks

This keeps the system clean and focused on core logic.

***✔ Separated Scoring Logic***
All priority calculations are in a dedicated scoring.py file.
This improves:
Readability
Maintainability
Testability

***✔ Frontend with Vanilla JS***
No frameworks used, per assignment requirement.
Uses fetch() to POST JSON to Django.

***✔ Clean Error Handling***
Invalid JSON → frontend alerts user
Missing attributes → scoring function applies penalties
API accepts POST only (as expected)

### 🧪 Unit Tests
The project includes 3 meaningful tests covering:
Overdue tasks
Quick-win scoring
Dependency penalties

### Run tests:
      ```bash
        python manage.py test

### 🌱 Future Improvements

Add Eisenhower Matrix (Urgent vs Important)

Add dependency visual graph

Add weekend/holiday awareness to urgency

Allow users to save tasks to database

Add ML-based priority learning
    
