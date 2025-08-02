from tkinter import *
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task.strip() != "":
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
    # Create main window
    window = Tk()
    window.title("To-Do List")
    window.geometry("400x500")
    window.config(bg="#223441")
    window.resizable(False, False)

    # Title label
    lbl_title = Label(window, text="To-Do List", bg="#223441", fg="white", font=("Arial", 24, "bold"))
    lbl_title.pack(pady=20)

    # Frame for the listbox and scrollbar
    frame_tasks = Frame(window)
    frame_tasks.pack(pady=10)

    # Listbox
    global listbox_tasks
    listbox_tasks = Listbox(frame_tasks, width=25, height=10,
                            font=("Arial", 16), bg="#ececec", fg="#223441",
                            selectbackground="#a6a6a6", activestyle="none")
    listbox_tasks.pack(side=LEFT, fill=BOTH)

    # Scrollbar
    scrollbar_tasks = Scrollbar(frame_tasks)
    scrollbar_tasks.pack(side=RIGHT, fill=BOTH)
    listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
    scrollbar_tasks.config(command=listbox_tasks.yview)

    # Entry box for new tasks
    global entry_task
    entry_task = Entry(window, font=("Arial", 16), width=24)
    entry_task.pack(pady=10)

    # Buttons frame
    frame_buttons = Frame(window)
    frame_buttons.pack(pady=20)

    btn_add = Button(frame_buttons, text="Add Task", font=("Arial", 14), bg="#c5f776",
                     padx=20, pady=10, command=add_task)
    btn_add.pack(fill=BOTH, expand=True, side=LEFT)

    btn_delete = Button(frame_buttons, text="Delete Task", font=("Arial", 14), bg="#ff8b61",
                        padx=20, pady=10, command=delete_task)
    btn_delete.pack(fill=BOTH, expand=True, side=LEFT)

    # Run the main loop
    window.mainloop()

if __name__ == "__main__":
    main()
