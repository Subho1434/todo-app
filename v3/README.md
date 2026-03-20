# 📝 CLI-TODO-APP-V3

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![MIT License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-3.0-yellow)
![Add Task](https://img.shields.io/badge/Feature-Add%20Task-brightgreen)
![Update Task](https://img.shields.io/badge/Feature-Update%20Task-blue)
![Delete Task](https://img.shields.io/badge/Feature-Delete%20Task-red)
![Show Task](https://img.shields.io/badge/Feature-Show%20Task-orange)

A sleek and colorful **Command-Line To-Do List application** built with Python.  
Manage tasks directly from your terminal with **priority levels, completion status, and timestamps**.

---

## 🛠 Features

- ⚡ **Add Tasks** – Input task title and priority (High / Medium / Low)  
- ✏️ **Update Tasks** – Edit title, priority, or status (Done / Not Done)  
- ❌ **Delete Tasks** – Remove completed or unwanted tasks  
- 📋 **Show Tasks** – Display all tasks in a readable, color-coded table  
- 💾 **Persistent Storage** – Tasks are automatically saved in `tasks.txt`  
- 🛡️ **Input Validation** – Prevents invalid entries  
- 🎨 **Colorful CLI UI** – Powered by `colorama` for better visibility  

---

## 💡 Skills Demonstrated

- Python fundamentals (variables, loops, conditionals, functions)  
- File handling with `tasks.txt`  
- CRUD operations using lists and dictionaries  
- Input/output handling in the terminal  
- Using `colorama` for colored terminal output  
- Managing timestamps with `datetime`  

---

## 🚀 How to Run

1️⃣ **Clone the repository**  

```
git clone https://github.com/Subankar-Dey/todo-app.git
cd cli-todo-app-v3
```
2️⃣ Install dependencies
```
pip install colorama
```
3️⃣ Run the application
```
python cli-todo-app-v3.py
```
## 📝 Usage

Upon running the app, you’ll see:

1 → Add Task <br>
2 → Update Task <br>
3 → Delete Task <br>
4 → Show Tasks <br>
5 → Exit

> **🟢 Add Task:** Enter title and priority  
> **🟡 Update Task:** Choose task by ID, then update title, priority, or status  
> **🔴 Delete Task:** Remove task by ID  
> **🔵 Show Tasks:** See all tasks in a color-coded table  
> **⚪ Exit:** Safely close the app

Task storage format (tasks.txt):
```
title||priority||status||timestamp
```
## 🎨 Example Color-Coded Task Table
ID	Title	Priority	Status	Timestamp
1	Finish project	🔴 High	✅ Done	2026-03-20 10:00
2	Buy groceries	🟡 Medium	❌ Not Done	2026-03-20 11:00
3	Read book	🟢 Low	❌ Not Done	2026-03-20 12:00

Legend:
```
🔴 High | 🟡 Medium | 🟢 Low

✅ Done | ❌ Not Done
```
Colors are applied in terminal using colorama.

## 🖼 Screenshot

+--------------------------------------------------------------------+
|                         CLI-TODO VERSION-3                         |
+--------------------------------------------------------------------+
|             OPTION             |             ACTION                |
+--------------------------------------------------------------------+
|               1                |          Add Task                 |
|               2                |          Update Task              |
|               3                |          Delete Task              |
|               4                |          Show Tasks               |
|               5                |          Exit                     |
+--------------------------------------------------------------------+
|                     Enter your choice (1-5):                       |
+--------------------------------------------------------------------+


+--------------------------------------------------------------------+
|                             SHOW TASKS                             |
+--------------------------------------------------------------------+
| ID | TITLE                | PRIORITY | STATUS   | TIMESTAMP        |
+--------------------------------------------------------------------+
|  1 | Fix CLI todo bugs    | High     | ✔        | 2026-03-19 18:45 |
|  2 | Workout for 30 minut | Low      | ✖        | 2026-03-20 07:00 |
|  3 | Push code to GitHub  | Medium   | ✔        | 2026-03-20 09:15 |
|  4 | Learn Kali           | High     | ✖        | 2026-03-20 16:57 |
|  5 | Python pyqt          | Medium   | ✔        | 2026-03-20 17:20 |
|  6 | Github repo          | Low      | ✖        | 2026-03-20 20:47 |
+--------------------------------------------------------------------+

## 🎯 Goal

This version demonstrates:

Advanced task management features

Persistent storage

Modular and professional Python programming

User-friendly terminal experience

## ⚙️ Built With

Python 3.x

colorama (terminal color output)

Standard Python libraries: os, datetime

## 🤝 Contributing

Contributions are welcome!

Fork the repository

Create a branch:
```
git checkout -b feature/AmazingFeature
```
Update code
Add Changes
```
git add .
```
Commit changes:
```
git commit -m "Add AmazingFeature"
```
push changes
```
git pull origin feature/AmazingFeature
```
Push to branch:
```
git push origin feature/AmazingFeature
```
Open a Pull Request
