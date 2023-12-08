import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_delete():
    entry.delete(len(entry.get()) - 1)

def button_equal():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=50, cursor='heart', font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

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
    ("()", 4, 2),
    (".", 4, 3),
    ("+", 4, 3)
]

for button_text, row, column in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=10, font=('Arial', 14), command=lambda text=button_text: button_click(text))
    button.grid(row=row, column=column, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear", padx=20, pady=10, font=('Arial', 14), command=button_clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete", padx=20, pady=10, font=('Arial', 14), command=button_delete)
delete_button.grid(row=5, column=2, padx=5, pady=5)

equal_button = tk.Button(root, text="=", padx=20, pady=10, font=('Arial', 14), command=button_equal)
equal_button.grid(row=5, column=3, columnspan=2, padx=5, pady=5)

root.mainloop()
