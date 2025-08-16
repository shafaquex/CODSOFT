import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import string

# --- Theme Settings: Cute Pastel Cat ---
BG_COLOR = "#FFF2F7"
BTN_GEN_COLOR = "#FFD6EC"
BTN_COPY_COLOR = "#D5EAFF"
OUTLINE_COLOR = "#FFB7DD"
LABEL_COLOR = "#AA9FE0"
CAT_EMOJI = "🐱"
COPY_EMOJI = "✨"
PAW_EMOJI = "🐾"
WINDOW_ICON_PATH = "kitty.png"  # Place a cute icon file in your working folder

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
root.title(f"{CAT_EMOJI} Password Generator")
root.geometry("420x340")
root.config(bg=BG_COLOR)
root.resizable(False, False)

# --- Window Icon ---
try:
    from PIL import ImageTk, Image
    icon_img = ImageTk.PhotoImage(Image.open(WINDOW_ICON_PATH))
    root.iconphoto(False, icon_img)
except Exception:
    pass

# --- App Title ---
title_label = tk.Label(
    root, text=f"Password Generator {PAW_EMOJI}",
    font=("Comic Sans MS", 20, "bold"),
    bg=BG_COLOR, fg=LABEL_COLOR, pady=10
)
title_label.pack()

# --- Frame for Inputs ---
frame_inputs = tk.Frame(root, bg=BG_COLOR, pady=5)
frame_inputs.pack()

tk.Label(frame_inputs, text="Password Length:",
         font=("Arial", 12), bg=BG_COLOR, fg=LABEL_COLOR).grid(row=0, column=0, sticky="w")
length_var = tk.IntVar(value=12)
length_spin = ttk.Spinbox(frame_inputs, from_=4, to=64, textvariable=length_var,
                          width=5, font=("Arial", 12))
length_spin.grid(row=0, column=1, padx=5)
    
# --- Checkboxes for Character Sets ---
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_special = tk.BooleanVar(value=True)

ttk.Checkbutton(frame_inputs, text="Uppercase", variable=var_upper).grid(row=1, column=0, sticky="w")
ttk.Checkbutton(frame_inputs, text="Lowercase", variable=var_lower).grid(row=1, column=1, sticky="w")
ttk.Checkbutton(frame_inputs, text="Digits", variable=var_digits).grid(row=2, column=0, sticky="w")
ttk.Checkbutton(frame_inputs, text="Special Chars", variable=var_special).grid(row=2, column=1, sticky="w")

# --- Generate / Copy Buttons with Emoji ---
frame_buttons = tk.Frame(root, bg=BG_COLOR)
frame_buttons.pack(pady=10)

btn_gen = tk.Button(
    frame_buttons, text=f"{CAT_EMOJI} Generate", command=generate_password,
    width=16, font=("Arial", 13, "bold"),
    bg=BTN_GEN_COLOR, fg="#925E91", bd=0, relief="solid", activebackground="#FFDDF4"
)
btn_gen.pack(side="left", padx=6)

btn_copy = tk.Button(
    frame_buttons, text=f"{COPY_EMOJI} Copy", command=copy_password,
    width=8, font=("Arial", 13, "bold"),
    bg=BTN_COPY_COLOR, fg="#4987A9", bd=0, relief="solid", activebackground="#E1F2FF"
)
btn_copy.pack(side="right", padx=6)

# --- Output ---
password_var = tk.StringVar()
tk.Label(
    root, text=f"{PAW_EMOJI} Generated Password:", bg=BG_COLOR, fg=LABEL_COLOR,
    font=("Arial", 13)).pack(pady=8)
output_entry = tk.Entry(
    root, textvariable=password_var, font=("Consolas", 18, "bold"),
    justify="center", width=28, bd=2, relief="solid", fg="#925E91", bg="#FFF9F9",
    highlightbackground=OUTLINE_COLOR, highlightthickness=1
)
output_entry.pack(pady=5)

root.mainloop()
