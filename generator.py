import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = int(length_entry.get())
    chars = string.ascii_letters
    if numbers_var.get():
        chars += string.digits
    if symbols_var.get():
        chars += string.punctuation

    if length < 4:
        messagebox.showwarning("Too Short", "Password length should be at least 4.")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    result_var.set(password)

def copy_password():
    pyperclip.copy(result_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack()
length_entry.insert(0, "12")

numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=5)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=30).pack()

tk.Button(root, text="Copy to Clipboard", command=copy_password).pack(pady=5)

root.mainloop()
