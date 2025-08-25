"""
Unit tests for the ToDo application.

This module contains pytest-based tests for the `Task` and `ToDoList` classes
from `todo.todo`, as well as the `get_index` function from `app`. The tests
cover initialization, validation, task management (add, remove, complete,
modify), persistence (save and load), and user input handling.

Fixtures such as `sample_task`, `completed_task`, `empty_todo_list`, and
`populated_todo_list` are used to provide test data and states.
"""

from datetime import datetime
import pytest
from todo.todo import Task, ToDoList, TaskValidationError
from app import get_index


class TestTask:
    """Tests for the Task class itself."""

    def test_task_initialization_valid(self, sample_task):
        """Tests successful Task initialization with valid data."""
        assert sample_task.task == 'Sport'
        assert sample_task.description == 'Go to gym'
        assert sample_task.deadline.strftime('%Y-%m-%d') == '2025-08-15'
        assert sample_task.priority == 7
        assert sample_task.completed is False
        assert sample_task.completion_date is None

    @pytest.mark.parametrize('invalid_task', ["", " ", 123, None])
    def test_task_initialization_invalid_name(self, invalid_task):
        """Tests Task initialization with invalid task names."""
        with pytest.raises(TaskValidationError, match="Task name must be a non-empty string."):
            Task(invalid_task, "Decription", None, 1)

    @pytest.mark.parametrize('invalid_priority', ["nine", "", 0, 11, None])
    def test_task_initialization_invalid_priority(self, invalid_priority):
        """Tests Task initialization with invalid task priorities."""
        with pytest.raises(TaskValidationError, match="Priority must be an integer between 1 and 10."):
            Task("Task", "Description", None, invalid_priority)

    def test_task_initialization_invalid_deadline_format(self):
        """Tests Task initialization with an invalid deadline format."""
        with pytest.raises(TaskValidationError,
                           match="Deadline must be a string \\(YYYY-MM-DD\\), a datetime object, or None/empty."):
            Task("Task", "Description", "2023/01/12", 2)

    def test_mark_as_completed(self, sample_task):
        """Tests marking a task as completed."""
        sample_task.mark_as_completed()
        assert sample_task.completed is True
        assert isinstance(sample_task.completion_date, datetime)

    def test_mark_already_completed_task(self, completed_task):
        """Tests marking an already completed task (should not change state or date)."""
        org_comp_date = completed_task.completion_date
        completed_task.mark_as_completed()
        assert completed_task.completed is True
        assert completed_task.completion_date == org_comp_date


class TestToDoList:
    """Tests for the ToDoList class, which manages tasks."""

    def test_add_task(self, populated_todo_list):
        """Tests that tasks are added and sorted correctly by priority and deadline."""
        # The populated_todo_list fixture adds tasks out of order.
        # We check if they are sorted correctly upon retrieval.
        # Priority 7
        assert populated_todo_list.tasks[0].task == "Research"
        # Priority 5, has deadline
        assert populated_todo_list.tasks[1].task == "Read a book"
        # Priority 5, no deadline (comes after)
        assert populated_todo_list.tasks[2].task == "Call mom"
        # Priority 3
        assert populated_todo_list.tasks[3].task == "Go for a run"

    def test_display_tasks_empty(self, empty_todo_list, capsys):
        """Tests the display message for an empty list."""
        empty_todo_list.display_tasks()
        captured = capsys.readouterr()
        assert "Your to-do list is empty! 🎉" in captured.out

    def test_display_tasks_populated(self, populated_todo_list, capsys):
        """Tests that populated list content is displayed correctly."""
        populated_todo_list.display_tasks()
        captured = capsys.readouterr()
        assert "Research" in captured.out
        assert "Priority: 7" in captured.out
        assert "Deadline: 2025-08-20" in captured.out

    def test_complete_task_valid(self, populated_todo_list, capsys):
        """Tests completing a valid task by its 1-based index."""
        task_to_complete = populated_todo_list.tasks[0]
        populated_todo_list.complete_task(1)
        assert task_to_complete.completed is True
        captured = capsys.readouterr()
        assert f"✅ Task '{task_to_complete.task}' marked as completed." in captured.out

    def test_complete_task_from_empty_list(self, empty_todo_list, capsys):
        """Tests trying to complete a task from an empty list."""
        empty_todo_list.complete_task(1)
        captured = capsys.readouterr()
        assert "List is empty. Nothing to mark as completed" in captured.out

    def test_complete_task_invalid_index(self, populated_todo_list, capsys):
        """Tests trying to complete a task with an out-of-bounds index."""
        list_len = len(populated_todo_list.tasks)
        populated_todo_list.complete_task(99)
        captured = capsys.readouterr()
        assert f"Invalid task number! Please enter a number between 1 and {list_len}." in captured.out

    def test_remove_task_valid(self, populated_todo_list, capsys):
        """Tests removing a valid task by its 1-based index."""
        initial_count = len(populated_todo_list.tasks)
        removed_task_name = populated_todo_list.tasks[0].task
        populated_todo_list.remove_task(1)
        assert len(populated_todo_list.tasks) == initial_count - 1
        assert removed_task_name not in [
            t.task for t in populated_todo_list.tasks]
        captured = capsys.readouterr()
        assert f"🗑️ Task '{removed_task_name}' removed successfully!" in captured.out

    def test_remove_task_from_empty_list(self, empty_todo_list, capsys):
        """Tests trying to remove a task from an empty list."""
        empty_todo_list.remove_task(1)
        captured = capsys.readouterr()
        assert "List is empty. Nothing to remove." in captured.out

    def test_remove_task_invalid_index(self, populated_todo_list, capsys):
        """Tests trying to remove a task with an out-of-bounds index."""
        list_len = len(populated_todo_list.tasks)
        populated_todo_list.remove_task(99)
        captured = capsys.readouterr()
        assert f"Invalid task number! Please enter a number between 1 and {list_len}." in captured.out

    def test_modify_task(self, populated_todo_list, capsys):
        """Tests modifying a task by passing a new Task object."""
        original_task_name = populated_todo_list.tasks[0].task
        modified_obj = Task("Updated Task", "New Desc", "2026-01-01", 10)
        populated_todo_list.modify_task(1, modified_obj)
        # The list is re-sorted, so the new task should be at the top
        assert populated_todo_list.tasks[0].task == "Updated Task"
        assert populated_todo_list.tasks[0].priority == 10
        captured = capsys.readouterr()
        assert f"✅ Task '{original_task_name}' modified successfully." in captured.out

    def test_modify_task_invalid_index(self, populated_todo_list, sample_task, capsys):
        """Tests trying to modify a task with an invalid index."""
        list_len = len(populated_todo_list.tasks)
        populated_todo_list.modify_task(99, sample_task)
        captured = capsys.readouterr()
        assert f"Invalid task number! Please enter a number between 1 and {list_len}." in captured.out

    def test_save_list_empty(self, empty_todo_list, capsys):
        """Tests that the correct message is shown when saving an empty list."""
        empty_todo_list.save_list()
        captured = capsys.readouterr()
        assert "List is empty. Nothing to save. 💾" in captured.out

    def test_load_list(self, populated_todo_list, tmp_path):
        """Tests saving a list to a file and loading it back."""
        # Use pytest's built-in temporary directory feature
        file_path = tmp_path / "test_list.csv"
        content = "Task,Priority,Deadline,Description,Completed,Completion Date\n"
        for task in populated_todo_list.tasks:
            deadline = task.deadline.strftime(
                '%Y-%m-%d') if task.deadline else ''
            completed = str(task.completed)
            comp_date = task.completion_date.strftime(
                '%Y-%m-%d %H:%M:%S') if task.completion_date else ''
            content += f"{task.task},{task.priority},{deadline},{task.description},{completed},{comp_date}\n"

        file_path.write_text(content)

        new_list = ToDoList()
        new_list.load_list(str(file_path))

        assert len(new_list.tasks) == len(populated_todo_list.tasks)
        assert new_list.tasks[0].task == populated_todo_list.tasks[0].task
        assert new_list.tasks[0].priority == populated_todo_list.tasks[0].priority

    def test_load_list_malformed_task(self, empty_todo_list, tmp_path, capsys):
        """Tests that loading a file with a bad row skips it and continues."""
        malformed_content = (
            "Task,Priority,Deadline,Description,Completed,Completion Date\n"
            "Valid Task,5,2025-01-01,Desc,False,\n"
            "Malformed,,invalid,,,\n"
        )
        malformed_file = tmp_path / "malformed.csv"
        malformed_file.write_text(malformed_content)

        empty_todo_list.load_list(str(malformed_file))
        captured = capsys.readouterr()
        assert "Warning: Skipping malformed task on line 3" in captured.out
        assert len(empty_todo_list.tasks) == 1
        assert empty_todo_list.tasks[0].task == "Valid Task"


class TestAppFunctions:
    """Tests helper functions from the main app.py file."""

    def test_get_index_valid(self, monkeypatch):
        """Tests get_index with valid user input."""
        monkeypatch.setattr('builtins.input', lambda prompt: '2')
        index = get_index("Enter index", 5)
        assert index == 2

    def test_get_index_invalid_then_valid(self, monkeypatch, capsys):
        """Tests that get_index handles invalid (out of range) input before valid input."""
        inputs = iter(['99', '1'])
        monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
        index = get_index("Enter index", 4)
        assert index == 1
        captured = capsys.readouterr()
        assert "Invalid index. Please enter a number between 1 and 4." in captured.out

    def test_get_index_non_numeric(self, monkeypatch, capsys):
        """Tests that get_index handles non-numeric input before valid input."""
        inputs = iter(['abc', '3'])
        monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
        index = get_index("Enter index", 4)
        assert index == 3
        captured = capsys.readouterr()
        assert "Invalid input. Please enter a whole number." in captured.out
