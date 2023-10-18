import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("System")
        self.title("Labels Example")
        self.geometry("600x200")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)

        label1 = customtkinter.CTkLabel(self)
        label2 = customtkinter.CTkLabel(self, text="My text!")
        label3 = customtkinter.CTkLabel(self, text="My text, but blue!", text_color="#3c78d8")
        label4 = customtkinter.CTkLabel(self, text="My text, but in Arial and size 30 font!", font=("Arial", 30))
        label5 = customtkinter.CTkLabel(self, text="My text, but changed foreground color.", fg_color="#3c78d8")
        label6 = customtkinter.CTkLabel(self, text="My text, but changed foreground color and using sticky.", fg_color="#3c78d8")

        label1.grid(row=0, column=0)
        label2.grid(row=1, column=0)
        label3.grid(row=2, column=0)
        label4.grid(row=3, column=0)
        label5.grid(row=4, column=0)
        label6.grid(row=5, column=0, sticky="nsew")

app = App()
app.mainloop()
