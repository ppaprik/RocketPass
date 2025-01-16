import customtkinter as ctk


class CheckboxFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.title = "Custom Label Title"

        self.label = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6, font=ctk.CTkFont(size=13, weight="bold"))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.checkbox_1 = ctk.CTkCheckBox(self, text="Checkbox 1")
        self.checkbox_1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.checkbox_2 = ctk.CTkCheckBox(self, text="Checkbox 2")
        self.checkbox_2.grid(row=2, column=0, padx=10, pady=10, sticky="w")


    def get(self):
        print(self.checkbox_1.cget("text"), self.checkbox_2.cget("text"))



class ScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        self.title = "Custom Label Title"
        self.checkboxes = []

        self.label = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6, font=ctk.CTkFont(size=13, weight="bold"))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        for i in range(10):
            checkbox = ctk.CTkCheckBox(self, text=f"Checkbox {i+1}")
            checkbox.grid(row=i+1, column=0, padx=10, pady=10, sticky="w")
            self.checkboxes.append(checkbox)

    
    def get(self):
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                print(checkbox.cget("text"))



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("JSON maker")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        ctk.set_appearance_mode("light")

        # self.check_box_frame = CheckboxFrame(self)
        # self.check_box_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsw")

        self.scrollable_frame = ScrollableFrame(self)
        self.scrollable_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsw")

        self.button = ctk.CTkButton(self, text="Button", command=self.scrollable_frame.get)
        self.button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")


    def buttonPressed(self):
        print("Button pressed")



app = App()
app.mainloop()