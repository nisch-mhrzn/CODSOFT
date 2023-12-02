import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_task_index = listbox.curselection()
    
    # DElete task only works when task is selected
    if selected_task_index:
        listbox.delete(selected_task_index)

# MAin window
root = tk.Tk()
root.title("To-Do List")
entry = tk.Entry(root, width=40)
entry.pack(pady=10)
listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)
listbox.pack()

# Create Buttons for adding and deleteing tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# MainLoop
root.mainloop()
