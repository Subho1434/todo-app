# cli-todo-app (Version 1: in-memory)

tasks = []


def line():
    print("_" * 25)


def add_task():
    task_name = input("Enter the task you want to add: ").strip()
    tasks.append(task_name)
    print("Task successfully added.")


def update_task():
    if not tasks:
        print("No tasks found!")
        return
    try:
        show_task()

        task_id = int(input("Enter the task id to update: "))

        if 1 <= task_id <= len(tasks):
            task_name = input("Enter the new task name: ").strip()
            print(f"Updated: {tasks[task_id - 1]} to {task_name}")
            tasks[task_id - 1] = task_name

        else:
            print("Task id not found!")

    except ValueError:
        print("Invalid Input: Enter a number!")


def delete_task():
    if not tasks:
        print("No tasks found!")
        return

    try:
        show_task()
        task_id = int(input("Enter the task id to delete: "))

        if 1 <= task_id <= len(tasks):
            print(f"Deleted: {tasks[task_id - 1]}")
            tasks.pop(task_id - 1)

        else:
            print("Invalid task id!")

    except ValueError:
        print("Invalid Input: Enter a number!")


def show_task():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTasks are:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}: {task}")


def main():
    while True:
        print("\n=====> CLI-Todo <=====")
        print("1. Add a new task")
        print("2. Update a task")
        print("3. Delete a task")
        print("4. show all tasks")
        print("5. Exit")

        try:
            choice = int(input("Please select an option: "))
        except ValueError:
            print("Invalid input: Enter a number.")
            continue

        line()
        if choice == 1:
            add_task()
        elif choice == 2:
            update_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            show_task()
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

        line()


if __name__ == "__main__":
    main()
