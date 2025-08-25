"""
Main entry point for the To-Do List command-line application.

This script provides the user interface for interacting with the to-do list.
It handles menu display, user input, and calls the appropriate methods
from the ToDoList class to manage tasks.
"""

from typing import Optional
from todo.todo import Task, ToDoList, TaskValidationError

my_list = ToDoList()


def get_index(prompt: str, max_index: int) -> Optional[int]:
    """Safely gets a valid task index from the user."""
    # Prevent trying to get input if the list is empty.
    if max_index == 0:
        print("The to-do list is empty. No tasks to select. 🤷\n")
        return None
    # Loop until a valid integer within the correct range is entered.
    while True:
        try:
            index_str = input(f"{prompt} (1-{max_index}): ")
            index = int(index_str)
            if 1 <= index <= max_index:
                return index
            else:
                print(
                    f"❌ Invalid index. Please enter a number between 1 and {max_index}.")
        except ValueError:
            print("❌ Invalid input. Please enter a whole number.")


def main() -> None:
    """The main application loop."""
    while True:
        # Display the main menu.
        print("\nTo-Do List")
        print('_' * 30)
        print('Choose an option:')
        print('1. Load a to-do list')
        print('2. Add a task')
        print('3. Display tasks')
        print('4. Check a task as completed')
        print('5. Delete a task')
        print('6. Modify a task')
        print('7. Save to-do list')
        print('8. Exit')
        choice = input("Enter your choice (1-8): ")

        # --- Handle Loading a List ---
        if choice == '1':
            file_loc = input("Enter the location of the task list file: ")
            my_list.load_list(file_loc)
            input('Press Enter to continue...')

        # --- Handle Adding a New Task ---
        elif choice == '2':
            try:
                # Gather task details from user input.
                task_name = input("Enter the task name: ")
                description = input(
                    "Enter the task description (leave blank for no description): ")
                deadline = input(
                    "Enter the deadline (leave blank for no deadline): ")
                priority = input("Enter the priority (1-10): ")
                # Create a Task instance, which will validate the input.
                task = Task(task_name, description, deadline, priority)
                my_list.add_task(task)
                input('Press Enter to continue...')
            # Catch validation errors from the Task constructor.
            except TaskValidationError as e:
                print(f"\n❌ Please fix the following errors:\n{e}\n")

        # --- Handle Displaying Tasks ---
        elif choice == '3':
            my_list.display_tasks()
            input('Press Enter to continue...')

        # --- Handle Completing a Task ---
        elif choice == '4':
            my_list.display_tasks()
            # Use the helper function to get a valid index.
            task_index = get_index("Enter the index of the task to check as completed",
                                   len(my_list.tasks))
            if task_index:
                my_list.complete_task(task_index)
            input('Press Enter to continue...')

        # --- Handle Deleting a Task ---
        elif choice == '5':
            my_list.display_tasks()
            task_index = get_index("Enter the index of the task to delete",
                                   len(my_list.tasks))
            if task_index:
                my_list.remove_task(task_index)
            input('Press Enter to continue...')

        # --- Handle Modifying a Task ---
        elif choice == '6':
            my_list.display_tasks()
            task_i = get_index(
                'Enter the index of the task to modify', len(my_list.tasks))

            if task_i:
                # Get the existing task to show current values.
                current_task = my_list.tasks[task_i-1]
                print("\nEnter new details. Press Enter to keep the current value.")
                # Get new values, showing the current ones as a prompt.
                new_name = input(
                    f"Task Name (current: {current_task.task}): ")
                new_description = input(
                    f"Task Description (current: {current_task.description}): ")
                curr_dead = current_task.deadline.strftime(
                    '%Y-%m-%d') if current_task.deadline else None
                new_deadline = input(
                    f"Deadline (current: {curr_dead}): ")
                new_priority = input(
                    f"Priority (current: {current_task.priority}): ")

                # Store only the fields that the user actually changed.
                updated_values = {}
                if new_name.strip():
                    updated_values['task'] = new_name.strip()
                if new_description.strip():
                    updated_values['description'] = new_description.strip()
                if new_deadline.strip():
                    updated_values['deadline'] = new_deadline.strip()
                if new_priority.strip():
                    updated_values['priority'] = new_priority.strip()

            try:
                # Create a new Task object. Use the updated value if it exists,
                # otherwise use the original value.
                # This ensures all attributes are correctly validated again.
                new_task = Task(
                    task=updated_values.get('task', current_task.task),
                    description=updated_values.get(
                        'description', current_task.description),
                    deadline=updated_values.get(
                        'deadline', current_task.deadline),
                    priority=updated_values.get(
                        'priority', current_task.priority),
                    # Preserve the original completion status.
                    completed=current_task.completed,
                    completion_date=current_task.completion_date
                )

                my_list.modify_task(task_i, new_task)

            except TaskValidationError as e:
                print(f"\n❌ Please fix the following errors:\n{e}\n")

            input('Press Enter to continue...')

        # --- Handle Saving the List ---
        elif choice == '7':
            my_list.save_list()
            input('Press Enter to continue...')

        # --- Handle Exiting the Application ---
        elif choice == '8':
            print('Saving your tasks...')
            my_list.save_list()
            print('Goodbye!')
            break

        # --- Handle Invalid Menu Choice ---
        else:
            print("Invalid choice. Please try again.\n")


# Standard Python entry point to run the main function.
if __name__ == "__main__":
    main()
