# ---------- Imports ----------
import os
from datetime import datetime

from colorama import Fore, Style, init

init(autoreset=True)

# ---------- Globals ----------
APP_NAME = "CLI-TODO VERSION-3"
FILE_NAME = "tasks.txt"
tasks = []


# ---------- UI ----------
def border():
    print(Fore.CYAN + "+" + "-" * 68 + "+")


def header(main_header, heading):
    if main_header:
        print()
        border()
        print(Fore.LIGHTYELLOW_EX + f"| {heading:^67}|")
    else:
        print()
        border()
        print(Fore.LIGHTGREEN_EX + f"| {heading:^67}|")


# ---------- Messages ----------
def success(msg):
    print("\n" + Fore.GREEN + Style.BRIGHT + f"✔ {msg}\n")

def error(msg):
    print("\n" + Fore.RED + Style.BRIGHT + f"✖ {msg}\n")

def warning(msg):
    print("\n" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + f"⚠ {msg}\n")

# ---------- File Handling ----------
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return

    with open(FILE_NAME) as file:
        for line in file:
            parts = line.strip().split("||")

            if len(parts) != 4:
                continue

            title, priority, status, timestamp = parts

            tasks.append({
                "title": title,
                "priority": priority,
                "status": status,
                "timestamp": timestamp
            })

def save_tasks():
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            title = task['title']
            priority = task['priority']
            status = str(task['status'])
            timestamp = task['timestamp']
            file.write(f"{title}||{priority}||{status}||{timestamp}\n")

# ---------- Features ----------
def show_tasks(show_header=True):
    if not tasks:
        error("No tasks found.")
        return

    if show_header:
        header(False, "SHOW TASKS")
    border()
    print(Fore.MAGENTA + Style.BRIGHT +
          f"|{'ID':>3} | {'TITLE':<20} | {'PRIORITY':<8} | {'STATUS':<8} | {'TIMESTAMP':<16} |")
    border()

    # Table Rows
    for index, task in enumerate(tasks, start=1):
        title = task['title'][:20]  # truncate long titles
        priority = task['priority']
        status = task['status']
        timestamp = task['timestamp']

        status_color = Fore.GREEN + Style.BRIGHT + f"✔" \
            if status == "True" else Fore.RED + Style.BRIGHT + f"✖"

        print(
            Fore.BLUE + f"|{index:>3}" + Style.RESET_ALL + " | " +
            Fore.WHITE + f"{title:<20}" + Style.RESET_ALL + " | " +
            Fore.YELLOW + f"{priority:<8}" + Style.RESET_ALL + " | " +
            status_color + f"{'':<7}" + Style.RESET_ALL + " | " +
            Fore.CYAN + f"{timestamp} |"
        )

    border()

def add_task():
    title = input("Enter Task title: ")
    priority = input("Enter Task priority: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    tasks.append({
        "title": title,
        "priority": priority.capitalize(),
        "status": "False",
        "timestamp": timestamp
    })

    save_tasks()
    success("Task added successfully.")

# ---------- Update Tasks ----------
def update_task_title(task_id):

    title = input("Enter Task title: ")

    if not title.strip():
        error("Task title cannot be empty.\n")
        return

    if title != '':
        warning("Ary you sure you want to update this task title (y/n)")
        check = input(Fore.YELLOW + ">>> " + Style.RESET_ALL)

        if check.lower() == "y":
            tasks[task_id]["title"] = title.capitalize()

        elif check.lower() == "n":
            return

        else:
            error("Invalid Input: Please enter (y/n)")
            return update_task_title(task_id)


def update_task_priority(task_id):

    update = input("Enter task priority (h: High/m: Medium/l: Low): ")
    if update.lower() == "h" or update.lower() == "high":
        priority = "High"
    elif update.lower() == "m" or update.lower() == "medium":
        priority = "Medium"
    elif update.lower() == "l" or update.lower() == "low":
        priority = "Low"
    else:
        error("Invalid Input: Enter (h/l/m)")
        return

    if priority != '':
        warning("Ary you sure you want to update this task priority (y/n)")
        check = input(Fore.YELLOW + ">>> " + Style.RESET_ALL)

        if check.lower() == "y":
            tasks[task_id]["priority"] = priority

        elif check.lower() == "n":
            return

        else:
            error("Invalid Input: Please enter (y/n)")
            return update_task_priority(task_id)


def update_task_status(task_id):

    completed = input(f"Task '{tasks[task_id]['title']}'' is completed (y/n)")
    if completed.lower() == "y":
        status = "True"
    elif completed.lower() == "n":
        status = "False"
    else:
        error("Invalid Input")
        return update_task_status(task_id)

    if status:
        warning("Ary you sure you want to update this task status (y/n)")
        check = input(Fore.YELLOW + ">>> " + Style.RESET_ALL)

        if check.lower() == "y":
            tasks[task_id]["status"] = status

        elif check.lower() == "n":
            return

        else:
            error("Invalid Input: Please enter (y/n)")
            return update_task_status(task_id)



def get_choice():
    print()
    border()
    print(Fore.BLUE + f"| {'1':^30} | {'Update Title':^27}{'':<6} |" + Style.RESET_ALL)
    print(Fore.BLUE + f"| {'2':^30} | {'Update Priority':^30}{'':<3} |" + Style.RESET_ALL)
    print(Fore.BLUE + f"| {'3':^30} | {'Update Status':^28}{'':<5} |" + Style.RESET_ALL)
    print(Fore.BLUE + f"| {'4':^30} | {'Back':^18}{'':<15} |" + Style.RESET_ALL)
    border()
    input_border("Enter your choice (1-4):")
    try:
        choice = int(input(Fore.LIGHTBLUE_EX + ">>> "))
        return choice
    except ValueError:
        return 0

def update_task():
    header(False,"UPDATE TASK")

    signal = 0
    show_tasks(False)

    if not tasks:
        error("No task available!")
        return

    try:
        task_id = int(input("Enter ID to Update Task: "))

        if 1 <= task_id <= len(tasks):
            while True:
                name = ""

                choice = get_choice()
                if choice == 0:
                    error("Invalid Input: Enter Number!")
                    continue

                if choice == 1:
                    update_task_title(task_id - 1)
                    name = "title"
                elif choice == 2:
                    update_task_priority(task_id - 1)
                    name = "priority"
                elif choice == 3:
                    update_task_status(task_id - 1)
                    name = "status"
                elif choice == 4:
                    warning("Back to home...!")
                    break
                else:
                    error("Enter a valid choice(1-4)!")

                if name:
                    save_tasks()
                    success(f"Task {name} updated successfully.")
                    show_tasks(False)
        else:
            error("Task ID is invalid.")

    except ValueError:
        error("Invalid Input: Enter Number!")

def delete_task():
    header(False, "DELETE TASK")
    show_tasks(False)

    if not tasks:
        error("No task available!")
        return

    try:
        task_id = int(input("Enter ID to Delete Task: "))

        if 1 <= task_id <= len(tasks):
            warning("Ary you sure you want to delete the task (y/n)")
            check = input(Fore.YELLOW + ">>> " + Style.RESET_ALL)

            if check.lower() == "y":
                removed_task = tasks.pop(task_id - 1)
                save_tasks()
                success(f"Task '{removed_task['title']}' deleted successfully.")

            elif check.lower() == "n":
                return

            else:
                error("Invalid Input:")
                return delete_task()

        else:
            error("Task ID is invalid.")

    except ValueError:
        error("Invalid Input: Enter Number!")



def input_border(msg):
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT +
          f"| {msg:^65}{'':<1} |")
    border()

# ---------- Main ----------
def main():
    load_tasks()

    while True:
        print()

        header(True,APP_NAME)
        border()
        print(Fore.MAGENTA + Style.BRIGHT +
              f"| {'OPTION':^30} | {'ACTION':^30}{'':<3} |")

        border()
        print(Fore.BLUE + f"| {'1':^30} | {'Add Task':^27}{'':<6} |" + Style.RESET_ALL)
        print(Fore.BLUE + f"| {'2':^30} | {'Update Task':^30}{'':<3} |" + Style.RESET_ALL)
        print(Fore.BLUE + f"| {'3':^30} | {'Delete Task':^30}{'':<3} |" + Style.RESET_ALL)
        print(Fore.BLUE + f"| {'4':^30} | {'Show Tasks':^29}{'':<4} |" + Style.RESET_ALL)
        print(Fore.BLUE + f"| {'5':^30} | {'Exit':^23}{'':<10} |" + Style.RESET_ALL)
        border()

        input_border("Enter your choice (1-5):")
        try:
            choice = int(input(Fore.LIGHTBLUE_EX + ">>> "))

        except ValueError:
            error("Invalid Input! Please enter a number 1-5.")
            continue

        if choice == 1:
            add_task()
        elif choice == 2:
            update_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            show_tasks()
        elif choice == 5:
            warning("Exiting... Goodbye!")
            break
        else:
            error("Please enter a valid choice (1-5)")

# ---------- Entry ----------
if __name__ == "__main__":
    main()