import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("System")
        self.title("Frames Example")
        self.geometry("600x500")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        frame1 = customtkinter.CTkFrame(self)
        frame2 = customtkinter.CTkFrame(self, fg_color="transparent", border_color="#88B6F2", border_width=5)
        frame3 = customtkinter.CTkFrame(self, fg_color="#3F618C", border_color="#88B6F2", border_width=5)

        frame1.grid(row=0, column=0)
        frame2.grid(row=1, column=0)
        frame3.grid(row=2, column=0)

app = App()
app.mainloop()
