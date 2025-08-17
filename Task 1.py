from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image 

# --- Theme Colors & Emoji Icons ---
BG_COLOR = "#FAF4E5"
TITLE_COLOR = "#FFC09F"
LISTBOX_BG = "#FFF7F1"
LISTBOX_FG = "#8D7C7B"
BUTTON_ADD_BG = "#B7EDE8"
BUTTON_DELETE_BG = "#F6A6B2"

ADD_ICON = "🐰" 
DELETE_ICON = "🐻" 

def add_task():
    task = entry_task.get()
    if task.strip():
        listbox_tasks.insert(END, task)
        entry_task.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def main():
    window = Tk()
    window.title("🐼 To-Do List") 
    window.geometry("400x500")
    window.config(bg=BG_COLOR)
    window.resizable(False, False)

    # --- App Icon (Window Icon) ---
    try:
        icon_img = ImageTk.PhotoImage(Image.open("panda_icon.png"))
        window.iconphoto(False, icon_img)
    except Exception:
        pass

    lbl_title = Label(window, text="To-Do List 🐱", bg=TITLE_COLOR, fg="white",
                      font=("Arial rounded MT Bold", 24, "bold"))
    lbl_title.pack(pady=20, fill=X)

    frame_tasks = Frame(window, bg=BG_COLOR)
    frame_tasks.pack(pady=10)

    global listbox_tasks
    listbox_tasks = Listbox(frame_tasks, width=25, height=10,
                            font=("Arial", 16), bg=LISTBOX_BG, fg=LISTBOX_FG,
                            selectbackground="#FFD5CD", activestyle="none",
                            bd=0, highlightthickness=2, relief="ridge")
    listbox_tasks.pack(side=LEFT, fill=BOTH, padx=2)

    scrollbar_tasks = Scrollbar(frame_tasks)
    scrollbar_tasks.pack(side=RIGHT, fill=BOTH)
    listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
    scrollbar_tasks.config(command=listbox_tasks.yview)

    global entry_task
    entry_task = Entry(window, font=("Arial", 16), width=24, bd=2,
                       bg="#FFF7F1", fg="#8D7C7B")
    entry_task.pack(pady=10)

    frame_buttons = Frame(window, bg=BG_COLOR)
    frame_buttons.pack(pady=20)

    btn_add = Button(frame_buttons, text=f"{ADD_ICON}  Add", font=("Arial", 14, "bold"),
                     bg=BUTTON_ADD_BG, bd=0, padx=20, pady=10,
                     command=add_task, activebackground="#CEF1E1", activeforeground="#8D7C7B")
    btn_add.pack(fill=BOTH, expand=True, side=LEFT, padx=5)

    btn_delete = Button(frame_buttons, text=f"{DELETE_ICON}  Delete", font=("Arial", 14, "bold"),
                        bg=BUTTON_DELETE_BG, bd=0, padx=20, pady=10,
                        command=delete_task, activebackground="#FFD5CD", activeforeground="#8D7C7B")
    btn_delete.pack(fill=BOTH, expand=True, side=LEFT, padx=5)

    window.mainloop()

if __name__ == "__main__":
    main()

