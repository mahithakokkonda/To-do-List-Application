import tkinter as tk
from tkinter import messagebox
import json

# Function to load tasks from JSON file
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save tasks to JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to add a new task
def add_task():
    task_text = entry_task.get()
    if task_text:
        tasks.append({'task': task_text, 'completed': False})
        save_tasks(tasks)
        list_tasks.insert(tk.END, task_text)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete a task
def delete_task():
    try:
        index = list_tasks.curselection()[0]
        list_tasks.delete(index)
        del tasks[index]
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to mark a task as complete
def complete_task():
    try:
        index = list_tasks.curselection()[0]
        tasks[index]['completed'] = True
        save_tasks(tasks)
        list_tasks.itemconfig(index, {'bg': 'light green'})
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as complete.")

# Function to display tasks
def display_tasks():
    for task in tasks:
        list_tasks.insert(tk.END, task['task'])
        if task['completed']:
            index = tasks.index(task)
            list_tasks.itemconfig(index, {'bg': 'light green'})

# Main window
root = tk.Tk()
root.title("To-Do List")

# Load tasks
tasks = load_tasks()

# Task Entry
entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)

# Buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack()

button_add = tk.Button(frame_buttons, text="Add Task", command=add_task)
button_add.grid(row=0, column=0, padx=5)

button_delete = tk.Button(frame_buttons, text="Delete Task", command=delete_task)
button_delete.grid(row=0, column=1, padx=5)

button_complete = tk.Button(frame_buttons, text="Mark Complete", command=complete_task)
button_complete.grid(row=0, column=2, padx=5)

# Task List
list_tasks = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
list_tasks.pack()

# Display tasks
display_tasks()

root.mainloop()
