import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import string

def generate_password():
    length = length_var.get()
    if length < 4:
        messagebox.showwarning("Warning", "Password length should be at least 4.")
        return
    chars = ""
    if var_upper.get():
        chars += string.ascii_uppercase
    if var_lower.get():
        chars += string.ascii_lowercase
    if var_digits.get():
        chars += string.digits
    if var_special.get():
        chars += string.punctuation

    if not chars:
        messagebox.showwarning("Warning", "Please select at least one character set!")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    password_var.set(password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Frame for inputs
frame_inputs = tk.Frame(root, pady=10)
frame_inputs.pack()

tk.Label(frame_inputs, text="Password Length:").grid(row=0, column=0, sticky="w")
length_var = tk.IntVar(value=12)
length_spin = tk.Spinbox(frame_inputs, from_=4, to=64, textvariable=length_var, width=5)
length_spin.grid(row=0, column=1, padx=5)

# Character set options
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_special = tk.BooleanVar(value=True)

tk.Checkbutton(frame_inputs, text="Uppercase", variable=var_upper).grid(row=1, column=0, sticky="w")
tk.Checkbutton(frame_inputs, text="Lowercase", variable=var_lower).grid(row=1, column=1, sticky="w")
tk.Checkbutton(frame_inputs, text="Digits", variable=var_digits).grid(row=2, column=0, sticky="w")
tk.Checkbutton(frame_inputs, text="Special Chars", variable=var_special).grid(row=2, column=1, sticky="w")

# Generate/Copy buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)
tk.Button(frame_buttons, text="Generate Password", command=generate_password, width=18, bg="lightblue").pack(side="left", padx=5)
tk.Button(frame_buttons, text="Copy", command=copy_password, width=8, bg="lightgreen").pack(side="right", padx=5)

# Output
password_var = tk.StringVar()
tk.Label(root, text="Generated Password:").pack(pady=10)
output_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 16), justify="center", width=28)
output_entry.pack(pady=5)

root.mainloop()
