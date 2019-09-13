from tkinter import ttk
from child import Child


class Update(Child):
    
    def __init__(self, parent, app):
        super(Update, self).__init__(parent, app)
        self.initEdit()
        self.view = app

    def initEdit(self):
        self.title('Редактировать контакт')
        
        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', 
                      lambda event: self.view.update_record(self.entry_name.get(),
                                                            self.combobox.get(),
                                                            self.entry_phone.get()))
        self.btn_OK.destroy()
