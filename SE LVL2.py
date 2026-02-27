class Task:
    def __init__(self, task_id, title, description, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

tasks = []

def create_task():
    task_id = input("Enter Task ID: ")
    title = input("Enter Task Title: ")
    description = input("Enter Task Description: ")
    status = input("Enter Task Status: ")
    task = Task(task_id, title, description, status)
    tasks.append(task)
    print("Task created successfully.\n")

def read_tasks():
    if len(tasks) == 0:
        print("No tasks available.\n")
    else:
        for task in tasks:
            print("ID:", task.task_id)
            print("Title:", task.title)
            print("Description:", task.description)
            print("Status:", task.status)
 
 
def update_task():
    task_id = input("Enter Task ID to update: ")
    for task in tasks:
        if task.task_id == task_id:
            task.title = input("Enter new Title: ")
            task.description = input("Enter new Description: ")
            task.status = input("Enter new Status: ")
            print("Task updated successfully.\n")
            return
    print("Task not found.\n")

def delete_task():
    task_id = input("Enter Task ID to delete: ")
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            print("Task deleted successfully.\n")
            return
    print("Task not found.\n")

while True:
    print("1. Create Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        create_task()
    elif choice == "2":
        read_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.\n")
class Task:
    def __init__(self, task_id, title, description, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status


tasks = []


def create_task():
    task_id = input("Enter Task ID: ")
    title = input("Enter Task Title: ")
    description = input("Enter Task Description: ")
    status = input("Enter Task Status: ")
    task = Task(task_id, title, description, status)
    tasks.append(task)
    print("Task created successfully.\n")


def read_tasks():
    if len(tasks) == 0:
        print("No tasks available.\n")
    else:
        for task in tasks:
            print("ID:", task.task_id)
            print("Title:", task.title)
            print("Description:", task.description)
            print("Status:", task.status)
            print("------------------------")


def update_task():
    task_id = input("Enter Task ID to update: ")
    for task in tasks:
        if task.task_id == task_id:
            task.title = input("Enter new Title: ")
            task.description = input("Enter new Description: ")
            task.status = input("Enter new Status: ")
            print("Task updated successfully.\n")
            return
    print("Task not found.\n")


def delete_task():
    task_id = input("Enter Task ID to delete: ")
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            print("Task deleted successfully.\n")
            return
    print("Task not found.\n")


while True:
    print("1. Create Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        create_task()
    elif choice == "2":
        read_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.\n")
