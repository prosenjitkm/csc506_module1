# Data Structure Learning Tool

**Course:** CSC506 - Design and Analysis of Algorithms  
**Module:** 1 (Data Structures & Complexity)  
**Date:** November 16, 2025  
**Version:** 1.0 (Unified Guide)

---
## 1. Purpose & Audience
This single document is designed for someone who was **not part of the original development** to quickly:  
- Understand what the project does  
- Set it up locally  
- Explore the UI and features  
- Learn the architecture & code layout  
- Run benchmarks & interpret results  
- Extend or debug if needed

---
## 2. High-Level Overview
The Data Structure Learning Tool is a **web application** that teaches fundamental data structures (Stack, Queue, Linked List) through:  
- Interactive visual operations (insert, delete, search, peek, clear)  
- Real-time complexity info (time & space)  
- Performance benchmarking with actual timed results  
- Educational use case panels (when to use each structure)  

**Tech Stack:** Python (Flask) backend + HTML/CSS/JavaScript (+ Chart.js) frontend.  
No database; everything runs in memory for simplicity.

---
## 3. Core Features Snapshot
| Category | Highlights |
|----------|------------|
| Data Structures | Stack, Queue, Linked List |
| Operations | Insert / Push / Enqueue, Delete / Pop / Dequeue, Peek, Search, Clear |
| Complexity | Time + Space (Big-O + explanations) |
| Use Cases | Real-world examples, advantages, disadvantages |
| Benchmarks | Actual measured timing for insert/delete/search |
| Visualization | Animated updates, highlighting search hits |
| API | 20 REST endpoints for structures, complexity & benchmarking |

---
## 4. Prerequisites
| Requirement | Minimum |
|-------------|---------|
| Python      | 3.8+ |
| pip         | Installed with Python |
| OS          | Windows / macOS / Linux |
| Browser     | Modern (Chrome/Firefox/Edge/Safari) |
| RAM         | 2GB (4GB+ recommended) |

Verify Python:  
```bash
python --version
```
Expected: `Python 3.x.x`

---
## 5. Installation & First Run
Navigate to the project root:  
```bash
cd C:\Users\prose\IdeaProjects\csc506_module1
```
Install dependencies:  
```bash
pip install -r requirements.txt
```
(Installs: Flask 3.0.0, Werkzeug 3.0.1)

Start the application:  
```bash
python app.py
```
Successful launch output includes:  
```
Running on http://127.0.0.1:5000
```
Open the UI in your browser:  
```
http://127.0.0.1:5000
```
Stop server any time with `Ctrl + C` in terminal.

---
## 6. Directory & File Map
```
csc506_module1/
├── app.py                  # Flask app entry
├── requirements.txt        # Dependencies
├── src/
│   ├── models/             # Data structure classes
│   │   └── datastructures.py (Stack, Queue, LinkedList)
│   ├── repositories/       # Repository pattern (state holders)
│   │   └── repository.py
│   ├── services/           # Business logic & benchmarking
│   │   └── service.py
│   ├── controllers/        # API controllers (request -> service)
│   │   └── controller.py
│   └── utils/              # Complexity data & logging
│       ├── complexity.py
│       └── logger.py
├── templates/
│   └── index.html          # UI layout
├── static/
│   ├── css/style.css       # Styling
│   └── js/script.js        # Frontend logic & fetch calls
├── test_operations.py      # Basic operation tests
├── test_benchmarks.py      # Benchmark test script
└── verify_benchmark_data.py# Verifies benchmark is real
```

---
## 7. Architecture (Layered)
```
Browser (HTML/CSS/JS) → Flask Routes (app.py) → Controllers → Services → Repository → Models
                                                   ↓               ↓
                                           Utilities (complexity, logging)
```
**Layers Explained:**  
- **Models**: Pure data structure implementations.  
- **Repository**: Holds instances (acts like in-memory persistence).  
- **Services**: Business logic + timing benchmarks + validation.  
- **Controllers**: Translate HTTP requests to service calls, return JSON.  
- **Utilities**: Static complexity metadata + log decorators.  
- **Frontend**: Fetches endpoints, renders visuals & charts.

---
## 8. Data Structures & Operations
### Stack (LIFO)
| Operation | Method | Complexity (Time / Space) | Notes |
|-----------|--------|---------------------------|-------|
| Push      | `push` | O(1) / O(1) | Append to list end |
| Pop       | `pop`  | O(1) / O(1) | Remove last element |
| Peek      | `peek` | O(1) / O(1) | Read last element |
| Search    | `search` | O(n) / O(1) | Linear scan |
| Clear     | reset repo | O(1) / O(1) | Reinit structure |

### Queue (FIFO)
| Operation | Method | Complexity | Notes |
|-----------|--------|------------|-------|
| Enqueue   | `enqueue` | O(1) / O(1) | Append to list |
| Dequeue   | `dequeue` | O(n) / O(1) | `pop(0)` shifts elements |
| Peek      | `peek`    | O(1) / O(1) | First element |
| Search    | `search`  | O(n) / O(1) | Linear scan |
| Clear     | reset repo | O(1) / O(1) | Reinit |

### Linked List (Singly)
| Operation | Method | Complexity | Notes |
|-----------|--------|------------|-------|
| Insert (Head) | `insert_at_head` | O(1) / O(1) | Update head pointer |
| Delete    | `delete` | O(n) / O(1) | Traverse to find value |
| Search    | `search` | O(n) / O(1) | Node-by-node |
| Clear     | reset repo | O(1) / O(1) | Reinit |

---
## 9. Complexity Metadata
Stored in `src/utils/complexity.py` for each structure & operation:  
- `time` (e.g., `O(1)`)  
- `space` (e.g., `O(1)`)  
- `explanation` (short)  
- `details` (longer rationale)  
Also includes **USE_CASES** with: best_for, examples, advantages, disadvantages, when_to_use.

Use cases toggle via the "ℹ️ When to Use" buttons in UI.

---
## 10. Benchmarking (Performance Tests)
**Where:** Benchmark section at bottom of UI.  
**What it does:** Measures real elapsed time for performing N operations across insert, delete, search for each data structure.

Input sizes tested: `100, 500, 1000, 2000`  
Timing function: `time.perf_counter()` (high precision).

**Operation Procedure:**  
- Insert: Perform N insertions.  
- Delete: Pre-fill with N, then delete N.  
- Search: Pre-fill with N, then perform N searches.  

**Interpreting the Chart:**  
- Flat line ≈ O(1) (Stack push/pop, Queue enqueue, LL head insert)  
- Linear growth ≈ O(n) (Queue dequeue, searches, LL delete)  

Run headless test:  
```bash
python test_benchmarks.py
python verify_benchmark_data.py  # Proof data is real
```

---
## 11. API Endpoints (Summary)
Base URL: `http://127.0.0.1:5000`

### Stack
- `POST /api/stack/push` {"value": "X"}
- `POST /api/stack/pop`
- `GET  /api/stack/peek`
- `POST /api/stack/search` {"value": "X"}
- `GET  /api/stack/state`
- `POST /api/stack/clear`

### Queue
- `POST /api/queue/enqueue` {"value": "X"}
- `POST /api/queue/dequeue`
- `GET  /api/queue/peek`
- `POST /api/queue/search` {"value": "X"}
- `GET  /api/queue/state`
- `POST /api/queue/clear`

### Linked List
- `POST /api/linkedlist/insert` {"value": "X"}
- `POST /api/linkedlist/delete` {"value": "X"}
- `POST /api/linkedlist/search` {"value": "X"}
- `GET  /api/linkedlist/state`
- `POST /api/linkedlist/clear`

### Complexity & Info
- `GET /api/complexity?ds=stack&op=insert`
- `GET /api/complexity/detailed?ds=queue&op=delete`
- `GET /api/use-cases?ds=linked_list`
- `GET /api/info?ds=stack`

### Benchmark
- `GET /api/benchmark?ds=stack&op=search`

---
## 12. Common Workflows
### A. Try Stack Interactively
1. Enter a value in Stack input.  
2. Click **Push**.  
3. Observe visual stack update (new box at top).  
4. Click **Peek** → Modal alert with top value & highlight effect.  
5. Click **Search** after entering existing/non-existing value → success or not found highlight.

### B. Run a Benchmark
1. Select `Queue` + `Delete Operation`.  
2. Click **Run Benchmark**.  
3. Observe rising time curve (O(n) due to shifting).  
4. Compare with `Queue` + `Insert Operation` (flat curve).

### C. Explore Use Cases
1. Click "ℹ️ When to Use" on Linked List.  
2. Read scenarios & advantages/disadvantages.  
3. Collapse section to hide content.

---
## 13. Troubleshooting Quick Reference
| Issue | Cause | Fix |
|-------|-------|-----|
| Cannot start app | Missing dependency | `pip install -r requirements.txt` |
| 404 on API | Wrong endpoint or ds/op param | Double-check URL & query params |
| UI not loading | Server not running | Re-run `python app.py` |
| Benchmark slow | Normal for O(n) ops | Reduce input sizes or confirm complexity |
| Search always -1 | Value not inserted yet | Insert first, then search |

If stuck: check console (F12 in browser) & terminal logs.

---
## 14. Glossary (Newcomer Friendly)
| Term | Meaning |
|------|---------|
| LIFO | Last In, First Out (Stack behavior) |
| FIFO | First In, First Out (Queue behavior) |
| Node | Element in a linked list with data + next pointer |
| Big-O | Notation describing operation growth vs input size |
| Benchmark | Timing repeated operations to measure performance |
| Amortized | Average performance over many operations (e.g., list append) |

---
## 15. Learning Path Suggestion
1. Interact with **Stack** (push/pop/peek).  
2. Use **Queue** and notice slow deletes.  
3. Insert/search/delete in **Linked List**.  
4. Open use case panels for all three.  
5. Run benchmarks for each operation.  
6. Compare predicted vs actual time behavior.  
7. Read complexity explanations in `complexity.py`.  
8. Open `datastructures.py` to relate code to UI actions.

---
## 16. Extension Ideas (For Future)
| Idea | Description |
|------|-------------|
| Add Hash Table | Demonstrate O(1) average search |
| Add BST | Show O(log n) vs degenerate O(n) |
| Use `deque` for Queue | Optimize dequeue to O(1) |
| Visualization Steps | Animate per-node traversal for search |
| Export Benchmarks | Download CSV/PDF of timing results |
| Quizzes | Interactive challenges for learners |

---
## 17. Quick Command Cheat Sheet
```bash
# Setup
pip install -r requirements.txt

# Run server
python app.py

# Test data structure operations
python test_operations.py

# Test all benchmark operations
python test_benchmarks.py

# Verify benchmark uses real timing
python verify_benchmark_data.py

# Stop server
Ctrl + C
```

---
## 18. What To Read First (If Brand New)
1. Skim sections 2–4 (Overview & Features).  
2. Follow section 5 (Install & Run).  
3. Play in UI (sections 12).  
4. Read section 8 (Operations & Complexity).  
5. Benchmark (section 10).  
6. Explore architecture (section 7 & code tree).  
7. Extend or refactor using section 16.

---
## 19. Attribution & Context
Originally built for academic learning in **CSC506** to reinforce practical understanding of data structures + time/space complexity by correlating theoretical Big-O with empirical benchmark curves.

---
## 20. Final Notes
This guide is intentionally self-contained—no prior project knowledge required. If you share with a friend/classmate they can get up and running in under 10 minutes.

**Enjoy exploring and learning! 🎓**
