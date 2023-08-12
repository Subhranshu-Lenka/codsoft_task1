from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry('650x400')
root.title("To-Do List")


head = Label(root, text="ToDo List", background="#54B435",
             font=("Comic Sans MS", 25, "bold"), anchor=W, padx=15)
head.pack(fill='both', ipady=15)

add_item = ttk.Label(root, text="Add Items", font=20)
add_item.pack(ipady=10, anchor=W, padx=15)


def addItem():
    global row_num

    task = t1.get()
    newTask = ttk.Label(frame2, text=task, justify='left', width=50)
    newTask.grid(row=row_num, column=1, columnspan=3,
                 ipadx=15, padx=5, pady=5)
    t1.delete(0, END)

    def edited_task():
        new_text = t1.get()
        newTask.config(text=new_text)
        t1.delete(0, END)
        b1.config(text="Submit", command=add_item)

    def edit():
        t1.insert(0, task)
        t1.focus_set()
        b1.config(text="EDIT", command=edited_task)

    def delete():
        newTask.destroy()
        editBtn.destroy()
        deleteBtn.destroy()

    editBtn = Button(frame2, text="Edit", fg="white",
                     bg="green", command=edit)
    editBtn.grid(row=row_num, column=4, padx=5, pady=5)

    deleteBtn = Button(frame2, text="Delete", fg="white",
                       bg="red", command=delete)
    deleteBtn.grid(row=row_num, column=5, padx=5, pady=5)

    row_num += 1


frame1 = Frame(root, padx=0)
frame1.pack()

t1 = ttk.Entry(frame1, width=90)
t1.grid(row=0, column=0, padx=15)

b1 = Button(frame1, text="Submit", command=addItem,
            fg="white", bg="#1E5128")
b1.grid(row=0, column=1)

task_bar = ttk.Label(root, text="Tasks", font=19)
task_bar.pack(anchor=W, padx=15, pady=10)


frame2 = Frame(root)
frame2.pack()

row_num = 0

root.mainloop()
