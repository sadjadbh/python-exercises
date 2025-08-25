"""
Core logic for the command-line To-Do List application.

This module defines the primary classes for managing tasks:
- TaskValidationError: A custom exception for handling invalid task data.
- Task: Represents a single to-do item with its attributes and validation.
- ToDoList: Manages the collection of tasks, including adding, sorting,
  saving, and loading.
"""

import csv
from datetime import datetime
from typing import Optional, Union


class TaskValidationError(ValueError):
    """Custom exception raised for errors in task validation."""


class Task:
    """
    Represents a task with attributes for task name, description,
    deadline, priority, and completion status.
    """

    def __init__(self, task: str, description: str, deadline: Optional[Union[str, datetime]], priority: Union[int, str], completed=False, completion_date=None) -> None:
        """
        Initializes a new Task object.

        Args:
            task (str): The name of the task. Must be a non-empty string.
            description (str): A description of the task. Must be a string.
            deadline (str | datetime | None): The deadline for the task.
            priority (int | str): The priority of the task (1-10).
            completed (bool, optional): The completion status of the task. Defaults to False.
            completion_date (datetime | str | None, optional): The date the task was completed.
        """

        # --- VALIDATE AND STORE CLEANED VALUES IN TEMPORARY VARIABLES ---
        # A list to aggregate all validation errors.
        errors = []

        # Validate task name: must be a non-empty string
        cleaned_task = None
        if not isinstance(task, str) or not task.strip():
            errors.append("Task name must be a non-empty string.")
        else:
            cleaned_task = task.strip()

        # Validate desciption: must be a string
        cleaned_description = None
        if not isinstance(description, str):
            errors.append("Description must be a string.")
        else:
            cleaned_description = description

        # Validate priority: must be an integer between 1 and 10
        cleaned_priority = None
        try:
            priority = int(priority)
            if not 1 <= priority <= 10:
                errors.append("Priority must be an integer between 1 and 10.")
            else:
                cleaned_priority = priority
        except (ValueError, TypeError):
            errors.append("Priority must be an integer between 1 and 10.")

        # Validate and parse deadline
        cleaned_deadline = None
        # Handle if a datetime object is already provided.
        if isinstance(deadline, datetime):
            cleaned_deadline = deadline
        # Handle if a string is provided for the deadline.
        elif isinstance(deadline, str) and deadline.strip():
            try:
                cleaned_deadline = datetime.strptime(
                    deadline.strip(), '%Y-%m-%d')
            except (ValueError, TypeError):
                errors.append(
                    "Deadline must be a string (YYYY-MM-DD), a datetime object, or None/empty.")

        # Validate completion status and date
        cleaned_completed = bool(completed)
        cleaned_completion_date = None
        # Handle string-based completion dates (e.g., from a CSV).
        if isinstance(completion_date, str) and completion_date.strip():
            try:
                cleaned_completion_date = datetime.strptime(
                    completion_date, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                # Silently ignore invalid date strings from the CSV for now,
                # but don't add to errors list
                # as this is for loading, not user input.
                cleaned_completion_date = None
        # Handle if a datetime object is already provided.
        elif isinstance(completion_date, datetime):
            cleaned_completion_date = completion_date

        # --- ERROR REPORTING ---
        # If any errors were collected, raise a single custom exception with all messages
        if errors:
            raise TaskValidationError("\n".join(errors))

        # --- ASSIGN CLEANED VALUES TO SELF IF ALL VALIDATIONS PASSED ---
        self.task = cleaned_task
        self.description = cleaned_description
        self.priority = cleaned_priority
        self.deadline = cleaned_deadline
        self.completed = cleaned_completed
        self.completion_date = cleaned_completion_date

    def mark_as_completed(self) -> None:
        """Marks the task as completed and sets the completion date to now."""
        if not self.completed:
            self.completed = True
            self.completion_date = datetime.now()
        print(f"✅ Task '{self.task}' marked as completed.")


class ToDoList:
    """
    Manages a list of Task objects.
    Allows adding, removing, displaying, saving, and loading tasks.
    """

    def __init__(self) -> None:
        """
        Initializes an empty ToDoList.
        """
        self.tasks = []

    def _sort_tasks(self) -> None:
        """Sorts tasks by priority (desc) and deadline (asc)."""
        # Sorts by priority (high to low) and then by deadline (sooner to later).
        # Tasks without deadlines are pushed to the end using datetime.max.
        self.tasks.sort(key=lambda x: (-x.priority,
                        x.deadline if x.deadline else datetime.max))

    def display_tasks(self) -> None:
        """
        Displays all tasks in the to-do list, sorted by priority (descending)
        and then by deadline (ascending).
        """
        if not self.tasks:
            print('Your to-do list is empty! 🎉\n')
            return

        print('📌 To Do List:\n')
        for i, task in enumerate(self.tasks, 1):
            status_icon = "[✓]" if task.completed else "[ ]"
            task_deadline = 'No Deadline'
            if task.deadline:
                try:
                    # Format datetime objects for display.
                    task_deadline = task.deadline.strftime('%Y-%m-%d')
                except AttributeError:
                    # Fallback for unexpected data types.
                    task_deadline = str(task.deadline)

            completion_info = ''
            if task.completed and task.completion_date:
                completion_date = task.completion_date.strftime(
                    '%Y-%m-%d %H:%M:%S')
                completion_info = f" (Completed: {completion_date})"

            print(f"{i}. {status_icon} {task.task}{completion_info}")
            print(f"   Priority: {task.priority}")
            print(f"   Deadline: {task_deadline}")
            print(f"   Description: {task.description}\n")

    def add_task(self, task: Task) -> None:
        """
        Receives a new Task object from the provided details and adds it to the list.
        The list is then re-sorted.
        """
        try:
            self.tasks.append(task)
            self._sort_tasks()
            print(f"✅ Task '{task.task}' added successfully.\n")

        # Catch any unexpected issues during the add operation.
        except AttributeError as e:
            print(f"❌ Invalid task object: {e}\n")
        except TypeError as e:
            print(f"❌ Task type error: {e}\n")

    def complete_task(self, task_num: Union[str, int]) -> None:
        """
        Marks a task as completed by its 1-based display number.

        Args:
            task_number_str (str | int): The display number of the task to mark as completed.
        """
        if not self.tasks:
            print('List is empty. Nothing to mark as completed! 🤷\n')
            return

        # Access the task and call its completion method.
        self.tasks[task_num - 1].mark_as_completed()

    def remove_task(self, task_number: Union[str, int]) -> None:
        """
        Removes a task from the list by its 1-based display number.

        Args:
            task_number_str (str | int): The display number of the task to remove.
        """
        if not self.tasks:
            print('List is empty. Nothing to remove. 🤷\n')
            return

        # Use pop to remove the task and get it for the confirmation message.
        removed_task = self.tasks.pop(task_number-1)
        print(
            f"🗑️ Task '{removed_task.task}' removed successfully! \n")

    def modify_task(self, task_number: Union[str, int], mod_task: Task) -> None:
        """
        Modifies a task in the list by its 1-based display number.
        """
        if not self.tasks:
            print('List is empty. Nothing to modify. 🤷\n')
            return

        # Store the original name for the success message.
        original_task_name = self.tasks[task_number-1].task

        # Replace the old task object with the new, modified one.
        self.tasks[task_number-1] = mod_task

        # Re-sort the list in case priority or deadline changed.
        self._sort_tasks()
        print(f"✅ Task '{original_task_name}' modified successfully.\n")

    def save_list(self) -> None:
        """
        Saves the current list of tasks to a CSV file.
        The filename includes a timestamp to prevent overwriting previous saves.
        """

        if not self.tasks:
            print("List is empty. Nothing to save. 💾\n")
            return
        # Generate a unique filename with the current date.
        timestamp = datetime.now().strftime('%Y%m%d')
        filename = f'ToDoList_{timestamp}.csv'

        try:
            with open(filename, 'w', encoding='utf-8', newline='') as output:
                writer = csv.writer(output)
                # Write the header row.
                writer.writerow(
                    ['Task', 'Priority', 'Deadline', 'Description', 'Completed', 'Completion Date'])
                # Write each task's data to a row.
                for task in self.tasks:
                    # Format dates as strings for CSV storage; handle None cases.
                    task_deadline = task.deadline.strftime(
                        '%Y-%m-%d') if task.deadline else ''

                    completion_date_str = task.completion_date.strftime(
                        '%Y-%m-%d %H:%M:%S') if task.completion_date else ''
                    writer.writerow(
                        [task.task, task.priority, task_deadline, task.description,
                         task.completed, completion_date_str]
                    )

            print(f"💾 List saved successfully as '{filename}'!\n")

        # Handle specific, common errors with user-friendly messages.
        except OSError as e_os:
            print(
                f"File System Error: Could not save to '{filename}'. "
                f"Details: ({type(e_os).__name__}: {e_os})\n"
            )

        except AttributeError as e_attr:
            print(
                f"Data Error: A task item is malformed while trying to save. Details: {e_attr}\n")

        except csv.Error as e_csv:
            print(
                f"CSV Formatting Error: Problem writing data to CSV for '{filename}'. "
                f"Details: {e_csv}\n"
            )

    def load_list(self, loc: str) -> None:
        """
        Loads tasks from a specified CSV file into the current list,
        replacing any existing tasks. The loaded tasks are then sorted.

        Args:
            loc (str): The path to the CSV file to load.
        """
        newly_loaded_tasks = []
        try:
            with open(loc, 'r', encoding='utf-8', newline='') as file:
                reader = csv.reader(file)
                try:
                    # Read the header to map column names to indices.
                    header = next(reader)
                    # Define expected headers for validation.
                    expected_header = [
                        ['Task', 'Priority', 'Deadline', 'Description',
                            'Completed', 'Completion Date'],
                        ['Task', 'Priority', 'Deadline', 'Description']
                    ]
                    if header not in expected_header:
                        print(
                            f"⚠️ Warning: CSV header in '{loc}' is '{header}', "
                            f"expected '{expected_header}'. Attempting to load anyway.")

                    # Create a map for flexible column ordering.
                    header_map = {col: idx for idx, col in enumerate(header)}

                except StopIteration:
                    print(
                        f"❌ Error: File '{loc}' is empty or header is missing. No tasks loaded.\n")
                    return

                # Process each row in the CSV file.
                for i, line in enumerate(reader, 2):
                    # Basic row validation.
                    if len(line) < len(header):
                        print(f"⚠️ Warning: Skipping malformed row on line {i} in '{loc}': "
                              "Row has fewer columns than the header.")
                        continue
                    try:
                        # Extract data using the header map for robustness.
                        task_name = line[header_map['Task']]
                        priority_str = line[header_map['Priority']]
                        description = line[header_map['Description']
                                           ] if 'Description' in header_map else ""
                        deadline_csv_str = line[header_map['Deadline']
                                                ] if 'Deadline' in header_map else None
                        completed_str = line[header_map['Completed']
                                             ] if 'Completed' in header_map else 'False'
                        completed = completed_str.strip().lower() == 'true'
                        completion_date_str = line[header_map['Completion Date']
                                                   ] if 'Completion Date' in header_map else None

                        # Create a Task instance from the row data.
                        task_instance = Task(
                            task_name, description, deadline_csv_str, priority_str,
                            completed=completed, completion_date=completion_date_str)
                        newly_loaded_tasks.append(task_instance)

                    # Catch validation errors for individual tasks
                    # without stopping the whole process.
                    except TaskValidationError as e_row:
                        print(
                            f"Warning: Skipping malformed task on line {i} in '{loc}': {e_row}")

            # Replace the old list with the newly loaded tasks.
            self.tasks = newly_loaded_tasks
            self._sort_tasks()

            if newly_loaded_tasks:
                print(
                    f"✅ Successfully loaded {len(newly_loaded_tasks)} task(s) from '{loc}'.\n")
            else:

                print(
                    f"ℹ️ No valid tasks were loaded from '{loc}'. "
                    f"The list might be empty or all rows had issues.\n"
                )

        # Handle specific file and data errors.
        except FileNotFoundError:
            print(f"❌ Error: The file '{loc}' was not found.\n")
        except IsADirectoryError:
            print(f"❌ Error: '{loc}' is a directory, not a file.\n")
        except OSError as e_os:
            print(f"❌ Error reading file '{loc}': {e_os}\n")
        except csv.Error as e_csv:
            print(
                f"❌ Error parsing CSV data in '{loc}': {e_csv}. File may be corrupted.\n")
