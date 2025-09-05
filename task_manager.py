import os 
import sys
import json



task = []

def main():
    while True:
        print("\nTask Manager Menu")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_task()
        elif choice == "2":
            add_task()
            save_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_completed()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1–5")

            



def add_task():
    id = int(input("Enter id: "))
    title = input("Enter the title: ")
    done = input("Is the task completed? (y/n): ")

    # Convert user input into True/False
    if done == "y":
        done_status = True
    elif done == "n":
        done_status = False
    else:
        print("Invalid input, marking as incomplete by default.")
        done_status = False

    # Create the task dictionary
    task_item = {
        "id": id,
        "title": title,
        "done": done_status
    }
    
    task.append(task_item)
    print("Task Added!")
    print(task)



def save_task():

    with open("task.json", "w") as file:
        json.dump(task, file, indent=4)

def load_task():
    global task
    try:
        with open("task.json", "r") as file:
            task = json.load(file)
    except FileNotFoundError:
        task = []

def view_task():

    if task == []:
        print("No tasks found!")
    for i in task:
        status = "complete" if i['done'] else "incomplete"
        print(f"ID: {i['id']} | Title: {i['title']} | Status: {status}")


def delete_task():
    delete = int(input("enter the what task ID you want to delete: "))

    found = False

    for i in task:
        if delete == i["id"]:
            task.remove(i)
            with open("task.json", "w") as file:
                json.dump(task, file, indent=4)
            print("task is deleted successfully!")
            found = True
            
            break
    if not found:
        print("ID not found! Try another one please!")
            
       

def mark_completed():
    mark = int(input("Enter a task ID: "))
    found = False

    for i in task:
        if mark == i["id"]:
            i["done"] = True
            found = True
            with open("task.json", "w") as file:
                json.dump(task, file, indent=4)
            print("Task marked as completed!")
            break

    if not found:
        print("Task not found!")



           




main()
load_task()
add_task()
save_task()
view_task()
delete_task()
mark_completed()




