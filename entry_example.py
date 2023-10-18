import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("System")
        self.title("Entries Example")
        self.geometry("600x200")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        entry1 = customtkinter.CTkEntry(self)
        entry2 = customtkinter.CTkEntry(self, width=500, placeholder_text="This is placeholder text")
        entry3 = customtkinter.CTkEntry(self, width=500, placeholder_text="This placeholder text will go away upon clicking the widget", placeholder_text_color="#3c78d8", border_color="#3c78d8")
        entry4 = customtkinter.CTkEntry(self, width=500, border_color="#3c78d8")
        entry5 = customtkinter.CTkEntry(self, width=500, text_color="#f9cb9c", border_color="#3c78d8")

        entry1.grid(row=0, column=0)
        entry2.grid(row=1, column=0)
        entry3.grid(row=2, column=0)
        entry4.grid(row=3, column=0)
        entry5.grid(row=4, column=0)

app = App()
app.mainloop()
