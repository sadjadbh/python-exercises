# Python To-Do List Manager ✅

A **command-line To-Do List application** written in Python.  
It helps you organize tasks with deadlines, priorities, completion tracking, and persistent storage.  

The project is designed with clean OOP, input validation, sorting, and full test coverage using `pytest`.  

---

## 🚀 Features

- **Task Management**  
  - Add, display, complete, delete, and modify tasks  
  - Store task attributes: `name`, `description`, `deadline`, `priority`, `completion status`  
- **Validation** with custom exceptions (`TaskValidationError`)  
- **Sorting** by priority (high → low), then deadline (soonest → latest)  
- **Persistence** with timestamped CSV files (save & load tasks)  
- **CLI Interface** with input validation & interactive menus  
- **Testing** with `pytest` (unit tests, fixtures, and test configuration)  

---

## 📂 Project Structure

```
13-final-project/
└── todo-list/
    ├── app.py              # CLI entry point
    ├── todo/               # Core logic package
    │   ├── __init__.py
    │   └── todo.py         # Task, ToDoList, TaskValidationError
    ├── tests/              # Tests package
    │   ├── conftest.py     # Pytest fixtures
    │   ├── pytest.ini      # Pytest configuration
    │   └── unit/
    │       ├── __init__.py
    │       └── test_todo.py # Unit tests
    ├── pyproject.toml      # Project metadata & dependencies
    ├── Pipfile             # Pipenv environment definition
    ├── Pipfile.lock        # Locked dependencies
    ├── LICENSE             # License
    └── README.md           # Documentation
```

---

## ⚙️ Installation

Navigate into the project folder:
```bash
cd todo-list
```

**Install dependencies (choose your method):**

Using pipenv:
```bash
pipenv install
pipenv shell
```

Using pip:
```bash
pip install -r requirements.txt   # if exported
```

---

## ▶️ Running the Application

```bash
python app.py
```

**Example menu:**
```
To-Do List
______________________________
Choose an option:
1. Load a to-do list
2. Add a task
3. Display tasks
4. Check a task as completed
5. Delete a task
6. Modify a task
7. Save to-do list
8. Exit
```

---

## 🧪 Running Tests

Run all tests with:
```bash
pytest -v
```

Run a specific test:
```bash
pytest tests/unit/test_todo.py::test_add_task
```

Configuration is handled via pytest.ini and conftest.py.

---

## 📜 Example Output

After adding tasks:
```
📌 To Do List:

1. [ ] Sport
   Priority: 7
   Deadline: 2025-08-15
   Description: Go to gym

2. [✓] Shopping (Completed: 2025-08-16 09:45:12)
   Priority: 5
   Deadline: No Deadline
   Description: Buy groceries
```

---

## 🌱 Future Improvements

- Export/import to JSON, YAML, or database  
- Support recurring tasks  
- GUI or web interface (Flask/Django/FastAPI)  
- Task filtering (e.g., by deadline, priority, completed)  

---

## 📄 License

This project is licensed under the terms of the [LICENSE](./LICENSE).

