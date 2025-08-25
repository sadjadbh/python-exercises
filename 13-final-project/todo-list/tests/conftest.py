from datetime import datetime
import pytest
from todo.todo import Task, ToDoList


@pytest.fixture
def sample_task():
    """Returns a basic Task object."""
    return Task(task="Sport", description="Go to gym", deadline="2025-08-15", priority=7)


@pytest.fixture
def completed_task():
    """Returns a Task object that is already marked as completed."""
    task = Task(task="Lunch", description="Go to restaurant",
                deadline="2025-08-15", priority=9)
    task.completed = True
    # Use a fixed date for consistency
    task.completion_date = datetime(2025, 8, 14, 12, 30, 0)
    return task


@pytest.fixture
def empty_todo_list():
    """Returns an empty ToDoList object."""
    return ToDoList()


@pytest.fixture
def populated_todo_list():
    """Returns a ToDoList with several tasks, which will be automatically sorted."""
    todo_list = ToDoList()
    # Add tasks out of order to test the automatic sorting
    todo_list.add_task(
        Task("Research", "University research", "2025-08-20", 7))
    todo_list.add_task(Task("Read a book", "Fiction novel", "2025-08-25", 5))
    todo_list.add_task(Task("Go for a run", "Morning Exercise", None, 3))
    todo_list.add_task(Task("Call mom", "", None, 5))
    return todo_list
