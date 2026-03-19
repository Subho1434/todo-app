# TO-DO CLI v2

A simple Python Command-Line Interface (CLI) To-Do List app.  
You can add, update, delete, and view tasks directly from your terminal. Tasks are saved automatically in a file.

---

## 🛠 Features

- Add new tasks
- Update existing tasks
- Delete tasks
- View all tasks
- Persistent storage in `tasks.txt`
- Colorful terminal output using `colorama` for better UX
- Simple, interactive CLI menu

---

## 💡 Skills Demonstrated

- Python fundamentals: loops, conditionals, functions, lists
- CRUD operations
- File handling (read/write tasks to a file)
- Command-line interface design
- Using external libraries (`colorama`) for terminal styling
- Input validation and error handling

---

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/Subho1434/todo-app.git`

2. Navigate to the `v2` folder:

```bash
cd todo-app/v2
```

3. (Optional) Create and activate a virtual environment:

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

4. Install required dependencies:

```bash
pip install colorama
```

---

## 🏃‍♂️ How to Run

Run the main script:

```bash
python cli-todo-app-v2.py
```

You will see a menu:

```text
1. Add Task
2. Update Task
3. Delete Task
4. View Tasks
5. Exit
```

* Enter the number corresponding to your choice.
* Follow prompts to manage your tasks.
* Tasks are automatically saved to `tasks.txt`.

---

## 📝 Usage Examples

### Add Task

```
Enter task name: Buy groceries
[Success]: Task added successfully.
```

### Update Task

```
Enter task ID to update: 1
Enter new task name: Buy vegetables
[Success]: Task updated successfully.
```

### Delete Task

```
Enter task ID to delete: 1
[Success]: Deleted: Buy vegetables
```

### View Tasks

```
1. Buy groceries
2. Finish assignment
```

---

## 📁 File Structure

* `v2/cli-todo-app-v2.py` — main Python script containing the CLI logic
* `v2/tasks.txt` — automatically created file to store tasks (persistent storage)
* `v2/README.md` — project documentation
* `.venv/` — optional virtual environment
* `.gitignore` — files and folders to ignore in Git

---

## 🎯 Goal

This project demonstrates a complete, beginner-friendly Python CLI application with:

* Persistent storage using files
* Clear and color-coded terminal output
* Modular and maintainable code
* Practical application of CRUD operations and user input handling

