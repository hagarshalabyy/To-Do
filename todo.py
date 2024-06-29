tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def list_tasks():
    if not tasks:
        print("No tasks to show.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    while True:
        print("\nTo-Do List")
        print("1. Add task")
        print("2. List tasks")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
