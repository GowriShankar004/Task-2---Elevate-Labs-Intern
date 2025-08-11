# todo.py
# Simple Persistent CLI To-Do List Application

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file into a list."""
    try:
        with open(TASKS_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save the task list to a file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\n✅ No tasks found!\n")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

def add_task(tasks):
    """Add a new task."""
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added!\n")
    else:
        print("⚠️ Task cannot be empty.\n")

def remove_task(tasks):
    """Remove a task by its number."""
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                save_tasks(tasks)
                print(f"🗑️ Removed: {removed}\n")
            else:
                print("⚠️ Invalid task number.\n")
        except ValueError:
            print("⚠️ Please enter a valid number.\n")

def main():
    tasks = load_tasks()
    while True:
        print("==== TO-DO LIST MENU ====")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
