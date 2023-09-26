from tkinter import Button, Entry, Label, Tk, Listbox, ANCHOR, messagebox
import tkinter as tk

import sql

window = Tk()
main_label = Label(window, text='Daily Tasks'); main_label.pack()  # Main label on starting window
mainentry = Entry(window, width=73); mainentry.pack()  # Entry for adding and editing records
textarea = Listbox(window, width=73, height=7); textarea.pack()  # Main list of tasks (ListBox tkinter)


#  Function displayed all saved records in sqlite3 database
def view_db_tasks():
    textarea.delete(0, tk.END)  # clear listbox before view all records
    for task in sql.get_tasks():
        textarea.insert(tk.END, task[0])


# function for adding records in listbox and db
def adding():
    data = mainentry.get()  # data from entry tkinter
    if data:
        sql.add_task(data)  # calling adding function from sql module (argument entry data)
        view_db_tasks()
    else:
        messagebox.showinfo('Добавление', 'Напишите название новой задачи')  # Exception and messagebox in tkinter


# function for deleting records from listbox and db
def deleting():
    if textarea.curselection():
        task_name = textarea.get(ANCHOR)  # ANCHOR it's current selection in listbox
        sql.del_task(task_name)  # calling deleting function from sql module (task name)
        view_db_tasks()
    else:
        messagebox.showinfo('Удаление', 'Выделите задачу которую хотите удалить')  # Exception and messagebox in tkinter


# function for editing records in listbox and db
def editing():
    new_name = mainentry.get()
    task_name = textarea.get(ANCHOR)
    if ANCHOR and new_name and (task_name != new_name):
        sql.edit_task(task_name, new_name)  # calling editing function from sql module (task name)
        view_db_tasks()
    else:
        messagebox.showinfo('Редактирование', 'Нет нового названия, не выделили старую задачу,\n'
                                              'Новое название и старое совпадают')
        # Exception and messagebox in tkinter


add_button = Button(text='ADD', command=adding); add_button.pack()  # All main buttons of application
del_button = Button(text='DELETE', command=deleting); del_button.pack()
edit_button = Button(text='Edit', command=editing); edit_button.pack()

if __name__ == '__main__':
    view_db_tasks()  # calling view function from first start application
    window.mainloop()
