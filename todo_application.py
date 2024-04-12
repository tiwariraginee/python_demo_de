import json

def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

def add_task(tasks, task):
    tasks.append({'task': task, 'completed': False})

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "Completed" if task['completed'] else "Not Completed"
            print(f"{idx}. {task['task']} - {status}")

def mark_completed(tasks, index):
    tasks[index]['completed'] = True

def remove_task(tasks, index):
    del tasks[index]

def main():
    filename = "todo_list.json"
    tasks = load_tasks(filename)

    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == '3':
            view_tasks(tasks)
            index = int(input("Enter the index of the task to mark as completed: ")) - 1
            mark_completed(tasks, index)
        elif choice == '4':
            view_tasks(tasks)
            index = int(input("Enter the index of the task to remove: ")) - 1
            remove_task(tasks, index)
        elif choice == '5':
            save_tasks(tasks, filename)
            print("To-Do List saved successfully. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
