import os
from colorama import Fore, Style, init

init(autoreset=True)

tasks = []
FILE_NAME = "tasks.txt"


# ---------- CLI UI ----------
def header(title):
    print(Fore.CYAN + "=" * 35)
    print(Fore.CYAN + f"{title.center(35)}")
    print(Fore.CYAN + "=" * 35)


def divider():
    print(Fore.YELLOW + "-" * 35)


def success(msg):
    print(Fore.GREEN + f"[Success]: {msg}")


def error(msg):
    print(Fore.RED + f"[Error]: {msg}")


def info(msg):
    print(Fore.BLUE + f"[info]: {msg}")


# ---------- Core Logic ----------
def check_tasks():
    if not tasks:
        error("Task list is empty.")
        return False
    return True


def load_file():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f.readlines():
                tasks.append(line.strip())


def save_tasks():
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def add_task():
    header("ADD TASK")
    task_name = input("Enter task name: ")
    if task_name.strip():
        tasks.append(task_name)
        save_tasks()
        success("Task added successfully.")
    else:
        error("Task cannot be empty.")


def update_task():
    header("UPDATE TASK")
    if check_tasks():
        view_tasks(show_header=False)
        try:
            task_id = int(input("\nEnter task ID to update: "))
            if 1 <= task_id <= len(tasks):
                new_name = input("Enter new task name: ")
                tasks[task_id - 1] = new_name
                save_tasks()
                success("Task updated successfully.")
            else:
                error("Invalid ID.")
        except ValueError:
            error("Please enter a valid number.")


def delete_task():
    header("DELETE TASK")
    if check_tasks():
        view_tasks(show_header=False)
        try:
            task_id = int(input("\nEnter task ID to delete: "))
            if 1 <= task_id <= len(tasks):
                removed = tasks.pop(task_id - 1)
                save_tasks()
                success(f"Deleted: {removed}")
            else:
                error("Invalid ID.")
        except ValueError:
            error("Please enter a valid number.")


def view_tasks(show_header=True):
    if show_header:
        header("YOUR TASKS")

    if check_tasks():
        divider()
        for index, task in enumerate(tasks, start=1):
            print(Fore.MAGENTA + f"{index}. " + Style.DIM + task)
    divider()


# ---------- Main App ----------
def main():
    load_file()

    while True:
        header("TO-DO CLI v2")

        divider()

        print(Fore.YELLOW + "1." + Style.RESET_ALL + " Add Task")
        print(Fore.YELLOW + "2." + Style.RESET_ALL + " Update Task")
        print(Fore.YELLOW + "3." + Style.RESET_ALL + " Delete Task")
        print(Fore.YELLOW + "4." + Style.RESET_ALL + " View Tasks")
        print(Fore.YELLOW + "5." + Style.RESET_ALL + " Exit")

        divider()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            error("Invalid input. Enter a number.")
            continue

        if choice == 1:
            add_task()
        elif choice == 2:
            update_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            view_tasks()
        elif choice == 5:
            success("Exiting... Thank you for using To-Do CLI!")
            break
        else:
            error("Invalid choice. Try again.")


if __name__ == '__main__':
    main()