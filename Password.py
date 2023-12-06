import tkinter as tk
import random
import string
import os
def generate_password():
    password_length = int(length_entry.get())
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(password_length))
    password_label.config(text=password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")  # Set the size of the window

length_label = tk.Label(root, text="Password Length:", font=("Arial", 12))  # Set the font size
length_label.pack()

length_entry = tk.Entry(root, font=("Arial", 12))  # Set the font size
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12))  # Set the font size
generate_button.pack()

password_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")  # Set the font size, style, and color
password_label.pack()

root.mainloop()
