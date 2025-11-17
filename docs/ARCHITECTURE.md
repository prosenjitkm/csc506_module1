# Architecture Overview

## Layered Architecture Diagram

```
┌─────────────────────────────────────────────────┐
│                  HTTP REQUEST                    │
│              (from browser/client)               │
└────────────────────┬────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────┐
│                 ROUTES (app.py)                  │
│   /api/stack/push, /api/queue/enqueue, etc.    │
└────────────────────┬────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────┐
│          CONTROLLER LAYER (controller.py)        │
│  - StackController                               │
│  - QueueController                               │
│  - LinkedListController                          │
│  - ComplexityController                          │
│  - BenchmarkController                           │
│                                                   │
│  Responsibilities:                               │
│  • Validate HTTP input                           │
│  • Handle request/response                       │
│  • Return JSON                                   │
└────────────────────┬────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────┐
│           SERVICE LAYER (service.py)             │
│  - StackService                                  │
│  - QueueService                                  │
│  - LinkedListService                             │
│  - ComplexityService                             │
│  - BenchmarkService                              │
│                                                   │
│  Responsibilities:                               │
│  • Business logic                                │
│  • Operation orchestration                       │
│  • Error handling                                │
└────────────────────┬────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────┐
│         REPOSITORY LAYER (repository.py)         │
│  - DataStructureRepository                       │
│                                                   │
│  Responsibilities:                               │
│  • Data access                                   │
│  • Manage data structure instances               │
│  • Reset/clear operations                        │
└────────────────────┬────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────┐
│       DATA STRUCTURES (datastructures.py)        │
│  - Stack (LIFO)                                  │
│  - Queue (FIFO)                                  │
│  - LinkedList (Nodes)                            │
│                                                   │
│  Responsibilities:                               │
│  • Core data structure logic                     │
│  • push, pop, enqueue, dequeue, etc.            │
└─────────────────────────────────────────────────┘
```

## Request Flow Example

### Example: Push to Stack

1. **Client** → `POST /api/stack/push` with `{"value": "5"}`

2. **Route** (`app.py`) → Receives request, calls `stack_controller.push()`

3. **Controller** (`StackController`) → 
   - Validates input (checks if value exists)
   - Calls `stack_service.push(value)`

4. **Service** (`StackService`) → 
   - Gets stack from repository
   - Calls `stack.push(value)`
   - Returns formatted result with state and size

5. **Repository** (`DataStructureRepository`) → 
   - Maintains the stack instance
   - Returns stack when requested

6. **Data Structure** (`Stack`) → 
   - Performs actual push operation
   - Updates internal list

7. **Response** ← Returns through layers:
   - Service formats data
   - Controller converts to JSON
   - Route sends HTTP response
   - Client receives `{"state": [5], "size": 1}`

## Benefits

### 1. **Separation of Concerns**
Each layer has one responsibility:
- Controllers: HTTP handling
- Services: Business logic  
- Repository: Data access
- Models: Data structure implementation

### 2. **Testability**
```python
# Easy to test each layer independently
def test_stack_service():
    repo = DataStructureRepository()
    service = StackService(repo)
    result = service.push(5)
    assert result['state'] == [5]
```

### 3. **Maintainability**
- Change HTTP framework? Only update controllers
- Change business rules? Only update services
- Change data storage? Only update repository
- Add new data structure? Add to each layer

### 4. **Reusability**
- Services can be used by different interfaces (REST API, GraphQL, CLI)
- Repository can be swapped (memory, database, file)

## File Responsibilities

| File | Layer | Purpose |
|------|-------|---------|
| `app.py` | Routes | Maps URLs to controllers |
| `controller.py` | Controller | Handles HTTP requests/responses |
| `service.py` | Service | Business logic and operations |
| `repository.py` | Repository | Data access and storage |
| `datastructures.py` | Model | Core implementations |
| `complexity.py` | Utility | Complexity data |

## Why This Architecture?

### Traditional Monolithic (Before):
```python
# All in one file - hard to maintain
@app.route("/api/stack/push")
def push():
    data = request.get_json()
    value = data.get("value")
    stack.push(value)  # Direct access
    return jsonify({"state": stack.to_list()})
```

### Layered Architecture (After):
```python
# Clean separation
@app.route("/api/stack/push")
def push():
    return stack_controller.push()  # Controller handles it

# Controller validates
class StackController:
    def push(self):
        data = request.get_json()
        value = data.get("value")
        if not value:
            return error
        return self.service.push(value)  # Service handles logic

# Service contains business logic
class StackService:
    def push(self, value):
        stack = self.repository.get_stack()
        stack.push(value)
        return {"state": stack.to_list(), "size": stack.size()}
```

## Best Practices Applied

✅ **Single Responsibility Principle**: Each class has one job
✅ **Dependency Injection**: Services receive dependencies via constructor
✅ **Separation of Concerns**: HTTP, logic, and data are separated
✅ **Testability**: Each layer can be tested independently
✅ **Maintainability**: Changes in one layer don't affect others
✅ **Scalability**: Easy to add new features or replace implementations

