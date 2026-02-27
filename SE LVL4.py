import tkinter as tk
from tkinter import messagebox

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []
    except Exception:
        print("Error while reading the file.")
        return []

def save_tasks(tasks):
    try:
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception as e:
        print(f"Error while writing to the file: {e}")

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("450x500")
        self.root.config(bg="#f4f4f9")

        self.tasks = load_tasks()

        title_label = tk.Label(root, text="Task Manager", font=("Helvetica", 20, "bold"), bg="#f4f4f9", fg="#333")
        title_label.pack(pady=15)

        list_frame = tk.Frame(root)
        list_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        self.task_listbox = tk.Listbox(list_frame, width=40, height=12, font=("Helvetica", 12), 
                                       selectbackground="#4a90e2", selectforeground="white", 
                                       bg="#ffffff", fg="#333333", relief=tk.FLAT, highlightthickness=1, 
                                       highlightbackground="#cccccc", highlightcolor="#4a90e2")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        self.update_listbox()

        input_frame = tk.Frame(root, bg="#f4f4f9")
        input_frame.pack(pady=10, padx=20, fill=tk.X)

        self.task_entry = tk.Entry(input_frame, font=("Helvetica", 12), relief=tk.FLAT, highlightthickness=1, 
                                   highlightbackground="#cccccc", highlightcolor="#4a90e2")
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), ipady=5)
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        add_button = tk.Button(input_frame, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", 
                               font=("Helvetica", 10, "bold"), relief=tk.FLAT, cursor="hand2", padx=10, pady=5)
        add_button.pack(side=tk.RIGHT)

        delete_button = tk.Button(root, text="Delete Selected Task", command=self.delete_task, bg="#f44336", fg="white", 
                                  font=("Helvetica", 10, "bold"), relief=tk.FLAT, cursor="hand2", padx=10, pady=5)
        delete_button.pack(pady=(0, 20))

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        taskText = self.task_entry.get().strip()
        if taskText:
            self.tasks.append(taskText)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
            save_tasks(self.tasks)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
            self.tasks.pop(selected_task_index)
            save_tasks(self.tasks)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def on_closing(self):
        save_tasks(self.tasks)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
