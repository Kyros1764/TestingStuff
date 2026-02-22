import customtkinter as ctk
import Files.CreateScrollableFrame as CSF

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Fprtnite Events Downloader")
        self.geometry("500x600")

        self.label = ctk.CTkLabel(self, text="Fortnite Events Downloader by Kyros", font=ctk.CTkFont(size=20, weight="bold"))
        self.label.pack(pady=20)

        # Make a selection list
        

    def on_button_click(self):
        self.label.configure(text="Button Clicked!")
        
if __name__ == "__main__":
    app = App()
    app.mainloop()