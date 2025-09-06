import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,
            static_folder='static',
            static_url_path='/static')

# Load tasks from file on startup
def load_tasks():
    try:
        with open("task.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("task.json", "w") as file:
        json.dump(tasks, file, indent=4)

# In-memory store
tasks = load_tasks()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/view')
def view_task():
    return render_template('view.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form.get("title")
        done = request.form.get("done") == "y"

        # Assign next available ID
        new_id = max([t["id"] for t in tasks], default=0) + 1

        task_item = {
            "id": new_id,
            "title": title,
            "done": done
        }
        tasks.append(task_item)
        save_tasks(tasks)

        return redirect(url_for('view_task'))

    return render_template('add.html')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    return render_template('delete.html')

@app.route('/mark/<int:task_id>')
def mark_completed(task_id):
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            break
    save_tasks(tasks)
    return render_template('mark.html')

if __name__ == '__main__':
    app.run(debug=True)
