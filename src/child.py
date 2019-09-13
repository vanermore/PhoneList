import tkinter as tk
from tkinter import ttk
import string


class Child(tk.Toplevel):

    entry_name: ttk.Entry
    entry_phone: ttk.Entry
    combobox: ttk.Combobox
    btn_OK: ttk.Button

    def __init__(self, parent, app):
        super(Child, self).__init__(parent)
        self.initUI()
        self.view = app

    def initUI(self):
        self.title("Добавить контакт")
        self.geometry("400x200+400+300")
        self.resizable(False, False)

        label_name = tk.Label(self, text='Контакт')
        label_name.place(x=50, y=50)

        label_description = tk.Label(self, text='Тип телефона')
        label_description.place(x=50, y=80)

        label_phone = tk.Label(self, text='Номер')
        label_phone.place(x=50, y=110)

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=50)

        self.combobox = ttk.Combobox(self, values=["Мобильный", "Домашний"])
        self.combobox.current(0)
        self.combobox.place(x=200, y=80)

        self.entry_phone = ttk.Entry(self)
        self.entry_phone.place(x=200, y=110)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_OK = ttk.Button(self, text='ОК')
        self.btn_OK.place(x=220, y=170)
        self.btn_OK.bind('<Button-1>', lambda event: self.view.records(self.entry_name.get(),
                                                                  self.combobox.get(),
                                                                  self.entry_phone.get()))

        self.grab_set()
        self.focus_set()
