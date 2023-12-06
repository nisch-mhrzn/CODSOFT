import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def power_function():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + "**")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=50, cursor='heart')
entry.grid(row=0, column=0, columnspan=5)
#UI interface
buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("^", 4, 2, power_function),
    ("+", 4, 3)
]

for button_text, row, column, command in buttons:
    button = tk.Button(root, text=button_text, padx=24, pady=25, command=lambda text=button_text, cmd=command: cmd() if cmd else button_click(text))
    button.grid(row=row, column=column)

clear_button = tk.Button(root, text="Clear", padx=20, pady=10, command=button_clear)
clear_button.grid(row=5, column=0, columnspan=2)

equal_button = tk.Button(root, text="=", padx=20, pady=10, command=button_equal)
equal_button.grid(row=5, column=2, columnspan=2)

root.mainloop()
