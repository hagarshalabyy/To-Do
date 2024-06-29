import json
import datetime

tasks = []

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

def add_task(task, deadline=None):
    tasks.append({"task": task, "deadline": deadline, "completed": False})
    print(f"Task '{task}' added.")

def list_tasks():
    if not tasks:
        print("No tasks to show.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "Done" if task['completed'] else "Pending"
            deadline = task['deadline'] if task['deadline'] else "No deadline"
            print(f"{i}. {task['task']} (Deadline: {deadline}, Status: {status})")

def mark_task_completed(index):
    try:
        tasks[index]['completed'] = True
        print(f"Task {index + 1} marked as completed.")
    except IndexError:
        print("Invalid task number.")

def main():
    global tasks
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as completed")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task: ")
            deadline_input = input("Enter the deadline (YYYY-MM-DD) or leave blank: ")
            deadline = None
            if deadline_input:
                try:
                    deadline = datetime.datetime.strptime(deadline_input, "%Y-%m-%d").date()
                except ValueError:
                    print("Invalid date format. Task will have no deadline.")
            add_task(task, deadline)
            save_tasks()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            index = int(input("Enter the task number to mark as completed: ")) - 1
            mark_task_completed(index)
            save_tasks()
        elif choice == '4':
            print("Exiting...")
            save_tasks()
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
