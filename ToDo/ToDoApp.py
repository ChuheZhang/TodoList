import tkinter as tk
from tkinter import messagebox

def add_todo():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_todo():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

app = tk.Tk()
app.title('Todo List App')

# 创建列表框
listbox = tk.Listbox(app, width=50, height=15)
listbox.pack(pady=10)

# 创建输入框
entry = tk.Entry(app, width=40)
entry.pack(pady=10)

# 创建按钮
add_button = tk.Button(app, text='Add Task', width=20, command=add_todo)
add_button.pack(pady=5)

delete_button = tk.Button(app, text='Delete Selected Task', width=20, command=delete_todo)
delete_button.pack(pady=5)



app.mainloop()
