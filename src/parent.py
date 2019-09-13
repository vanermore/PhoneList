import os
import tkinter as tk
from tkinter import ttk, PhotoImage
from PIL import ImageTk

from child import Child
from upd import Update
from db import DataBase



class App(tk.Frame):

    imageAdd: PhotoImage
    imageDelete: PhotoImage
    imageEdit: PhotoImage
    tree: ttk.Treeview

    def __init__(self, parent):
        super(App, self).__init__(parent)
        self.parent = parent
        self.initUI()
        self.db = DataBase()
        self.view_records()

    def initUI(self):
        self.parent.title("Phone List")
        self.parent.geometry("650x435+300+200")
        self.parent.resizable(False, False)
        toolbar = tk.Frame(bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.imageAdd = tk.PhotoImage(file="img/add.png")

        btn_add = tk.Button(toolbar, text="Новый контакт", command=self.openChild,
                            bd=0, compound=tk.TOP, image=self.imageAdd)
        btn_add.pack(side=tk.LEFT)

        self.imageEdit = tk.PhotoImage(file='img/edit.png')
        btn_edit = tk.Button(toolbar, text='Редактировать', command=self.openEdit,
                             bd=0, image=self.imageEdit, compound=tk.TOP)
        btn_edit.pack(side=tk.LEFT)

        self.imageDelete = ImageTk.PhotoImage(file='img/delete.jpg')
        btn_delete = tk.Button(toolbar, text='Удалить',
                               command=self.delete_records, bd=0, image=self.imageEdit, compound=tk.TOP)
        btn_delete.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ID', 'NAME', 'DESCRIPTION', 'PHONE'),
                                 height=15, show="headings")

        self.tree.column("ID", width=30, anchor=tk.CENTER)
        self.tree.column("NAME", width=265, anchor=tk.CENTER)
        self.tree.column("DESCRIPTION", width=150, anchor=tk.CENTER)
        self.tree.column("PHONE", width=265, anchor=tk.CENTER)

        self.tree.heading("ID", text='ID')
        self.tree.heading("NAME", text='Контакт')
        self.tree.heading("DESCRIPTION", text='Телефон')
        self.tree.heading("PHONE", text='Номер')

        self.tree.pack()

    def view_records(self):
        self.db.c.execute('SELECT * FROM phone_list')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('DELETE FROM phone_list WHERE id=?', (self.tree.set(selection_item, '#1')))
        self.db.conn.commit()
        self.view_records()

    def records(self, name, description, phone):
        self.db.insert_data(name, description, phone)
        self.view_records()

    def update_record(self, name, description, phone):
        self.db.c.execute('UPDATE phone_list SET name=?, description=?, phone=? WHERE id=?',
                          (name, description, phone, self.tree.set(self.tree.selection()[0],
                                                                   '#1')))
        self.db.conn.commit()
        self.view_records()

    def openChild(self):
        Child(self.parent, self)

    def openEdit(self):
        Update(self.parent, self)