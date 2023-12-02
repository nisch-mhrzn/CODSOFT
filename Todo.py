import tkinter as tk

def add_task():
    # Get the task from the entry widget
    task = entry.get()
    
    # Add the task to the listbox if it's not empty
    if task:
        listbox.insert(tk.END, task)
        
        # Clear the entry widget for the next task
        entry.delete(0, tk.END)

def delete_task():
    # Get the index of the selected task
    selected_task_index = listbox.curselection()
    
    # Delete the selected task from the listbox if any is selected
    if selected_task_index:
        listbox.delete(selected_task_index)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Entry widget for adding tasks
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Listbox widget to display tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)
listbox.pack()

# Buttons to add and delete tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Run the Tkinter main loop
root.mainloop()
