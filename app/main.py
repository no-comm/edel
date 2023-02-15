import customtkinter
import sender
from ex import *
class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x150")
        self.title("Информация")
        self.label = customtkinter.CTkLabel(self, text="Успешно отправлено")
        self.label.pack(padx=20, pady=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x300")
        self.title("Edelwies App")
        self.minsize(600, 300)

        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.textbox = customtkinter.CTkTextbox(master=self)
        self.textbox.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 0), sticky="nsew")
        
        self.combobox = customtkinter.CTkOptionMenu(master=self,
                                       values=["1. Стоимость вашей работы", "2. Оплата поступила"])
        self.combobox.grid(row=1, column=0, padx=20, pady=(20, 0), sticky="ew")
        # self.textbox2 = customtkinter.CTkTextbox(master=self, width=10, height=10)
        # self.textbox2.grid(row=1, column=0, columnspan=1, padx=20, pady=(10, 10), sticky="nsew")
        # self.textbox2.insert("0.0", "Стоимость (Услуга)")
        # self.textbox2.configure(state="disabled")
        
        self.toplevel_window = None


        # self.textbox3 = customtkinter.CTkTextbox(master=self, width=10, height=10)
        # self.textbox3.grid(row=2, column=0, columnspan=1, padx=20, pady=(10, 10), sticky="nsew")


        # self.combobox = customtkinter.CTkComboBox(master=self, values=["Оформление:  Дипломная работа", " Оформление:  Доклад", " Оформление: Контрольные работы", " Оформление: Курсовая работа", " Оформление: Отчет по практике", " Оформление: Презентация", " Оформление: Рефераты", " Оформление: Шпаргалки"])
        # self.combobox.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.textbox4 = customtkinter.CTkTextbox(master=self, width=10, height=10)
        self.textbox4.grid(row=1, column=1, columnspan=1, padx=20, pady=(10, 10), sticky="nsew")
        self.textbox4.insert("0.0", "Email для отправки")
        self.textbox4.configure(state="disabled")

        self.textbox5 = customtkinter.CTkTextbox(master=self, width=10, height=10)
        self.textbox5.grid(row=2, column=1, columnspan=1, padx=20, pady=(10, 10), sticky="nsew")

        self.button = customtkinter.CTkButton(master=self, command=self.button_callback, text="Сгенерировать")
        self.button.grid(row=1, column=2, padx=20, pady=20, sticky="ew")

        self.button2 = customtkinter.CTkButton(master=self, command=self.button_callback2, text="Отправить")
        self.button2.grid(row=2, column=2, padx=20, pady=20, sticky="ew")

    def button_callback(self):
        pr = self.combobox.get()

        self.textbox.delete("0.0", "end")
        self.textbox.insert("insert", answers[int(pr.split(".")[0])-1])
    def button_callback2(self):

        s = sender.send(self.textbox.get("0.0", "end"), self.textbox5.get("0.0", "end"))
        if s:
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()  # if window exists focus it
        else:
            dialog = customtkinter.CTkInputDialog(text="Произошла Ошибка "+s, title="Информация")


if __name__ == "__main__":
    app = App()
    app.mainloop()