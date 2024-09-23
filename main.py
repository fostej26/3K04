from tkinter import Tk, Button

class Window(Tk):
    def __init__(self):
        super().__init__()

        self.title("3K04 Assignment 1")

        # Create Sign In button
        self.signin_button = Button(self, text="Sign In")
        self.signin_button.bind("<Button-1>", self.handle_signin)  # Bind left mouse button click
        self.signin_button.pack(pady=10)

        # Create Sign Up button
        self.signup_button = Button(self, text="Sign Up")
        self.signup_button.bind("<Button-1>", self.handle_signup)  # Bind left mouse button click
        self.signup_button.pack(pady=10)

    def handle_signin(self, event):
        print("Sign In clicked")
        self.destroy()

    def handle_signup(self, event):
        print("Sign Up clicked")
        self.destroy()

# Start the event loop.
if __name__ == "__main__":
    window = Window()
    window.mainloop()
