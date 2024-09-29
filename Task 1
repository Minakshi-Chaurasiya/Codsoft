import json
import os

# Define the file where tasks will be stored
TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(task, tasks):
    """Add a new task to the list."""
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task}")

def view_tasks(tasks):
    """View all tasks in the list."""
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def remove_task(task_index, tasks):
    """Remove a task by its index."""
    try:
        removed_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"Task removed: {removed_task}")
    except IndexError:
        print("Invalid task index.")

def main():
    """Main function to run the to-do list application."""
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. remove Task")
        print("4. Exit")

        choice = input("Select an option (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task description: ")
            add_task(task, tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            try:
                task_index = int(input("Enter the task number to remove: "))
                remove_task(task_index, tasks)
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif choice == '4':
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
