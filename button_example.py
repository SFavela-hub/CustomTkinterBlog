import customtkinter
import os
from PIL import Image

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("System")
        self.title("Buttons Example")
        self.geometry("600x200")

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        click_me_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "gear.png")), size=(15, 15))


        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        button1 = customtkinter.CTkButton(self, text="Click Me!")
        button2 = customtkinter.CTkButton(self, text="Click Me!", fg_color="transparent", border_color="#3c78d8", border_width=2)
        button3 = customtkinter.CTkButton(self, text="Click Me!", corner_radius=50)
        button4 = customtkinter.CTkButton(self, text="", corner_radius=50, image=click_me_image)

        button1.grid(row=0, column=0)
        button2.grid(row=1, column=0)
        button3.grid(row=2, column=0)
        button4.grid(row=3, column=0)

app = App()
app.mainloop()
