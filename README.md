# Task-Manager
---

# Task Manager CLI (Python)

A simple **Command Line Task Manager** built with Python.
This project lets you manage tasks directly from the terminal with **persistent storage in JSON**.

## Features

*  Add new tasks
*  View all tasks
*  Mark tasks as completed
*  Delete tasks
*  Save tasks in a `task.json` file for persistence

## Project Structure

```bash
task-manager/
│── task.json        # Stores tasks in JSON format
│── task_manager.py  # Main Python script
```

## How to Run

1. Clone the repo

   ```bash
   git clone git@github.com:asingo-paul/Task-Manager.git
   cd Task-Manager
   ```

2. Run the script

   ```bash
   python task_manager.py
   ```

3. Choose from the menu:

   ```
   1. View tasks
   2. Add task
   3. Delete task
   4. Mark task completed
   5. Exit
   ```

## Example

```bash
Enter id: 1
Enter the title: Learn Python
Is the task completed? (y/n): n

Task Added!
[{'id': 1, 'title': 'Learn Python', 'done': False}]
```

## Future Improvements

* Add due dates and priorities
* Export tasks to CSV/Excel
* Build a web dashboard with Flask/Django
* Deploy on AWS as a microservice

---

*This project shows how Python can be used for simple yet powerful automation — a stepping stone toward full-stack cloud-native apps.*

---

