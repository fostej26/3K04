from tkinter import Tk, Button, Entry, Label

class Window(Tk):
    def __init__(self):
        super().__init__()

        self.title("3K04 Assignment 1")

        # Subheading for Username
        subheading_username = Label(self, text="Enter Username:", font=("Helvetica", 12))
        subheading_username.pack(pady=5)
        
        # Entry for Username
        self.username_entry = Entry(self, width=30)
        self.username_entry.pack(pady=5)

        # Subheading for Password
        subheading_password = Label(self, text="Enter Password:", font=("Helvetica", 12))
        subheading_password.pack(pady=5)
        
        # Entry for Password
        self.password_entry = Entry(self, width=30, show='*')  # 'show' hides the password
        self.password_entry.pack(pady=5)

        # Create Sign In button
        self.signin_button = Button(self, text="Sign In")
        self.signin_button.bind("<Button-1>", self.handle_signin)  # Bind left mouse button click
        self.signin_button.pack(pady=10)

        # Create Sign Up button
        self.register_button = Button(self, text="Register")
        self.register_button.bind("<Button-1>", self.handle_register)  # Bind left mouse button click
        self.register_button.pack(pady=10)

    def handle_signin(self, event):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.destroy()

    def handle_register(self, event):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.destroy()

# Start the event loop.
if __name__ == "__main__":
    window = Window()
    window.mainloop()
