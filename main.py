from tkinter import Tk, Button, Entry, Label
import hashlib

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

        # Message Label
        self.message_label = Label(self, text="", font=("Helvetica", 12), fg="red")
        self.message_label.pack(pady=10)

        # Create Sign In button
        self.signin_button = Button(self, text="Sign In")
        self.signin_button.bind("<Button-1>", self.handle_signin)  # Bind left mouse button click
        self.signin_button.pack(pady=10)

        # Create Sign Up button
        self.register_button = Button(self, text="Register")
        self.register_button.bind("<Button-1>", self.handle_register)  # Bind left mouse button click
        self.register_button.pack(pady=10)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def handle_signin(self, event):
        username = self.username_entry.get()
        password = self.password_entry.get()
        hashed_password = self.hash_password(password)

        with open("users.txt", "r") as f:
            users = f.read().splitlines()
            for user in users:
                user_data = user.split()
                if username == user_data[0]:
                    if hashed_password == user_data[1]:
                        self.message_label.config(text="Sign In successful!", fg="green")
                        self.destroy()
                        return
                    else:
                        self.message_label.config(text="Incorrect password. Please try again.")
                        return
        self.message_label.config(text="Username not found. Please register.")

    def handle_register(self, event):
        username = self.username_entry.get()
        password = self.password_entry.get()

        with open("users.txt", "r") as f:
            users = f.read().splitlines()
            if len(users) != 0:
                for user in users:
                    if username == user.split()[0]:
                        self.message_label.config(text="Username already registered. Please sign in or choose a new username.")
                        return

        with open("users.txt", "a") as f:
            f.write(f"{username} {self.hash_password(password)}\n")
        self.message_label.config(text="Registration successful!", fg="green")
        self.username_entry.delete(0, 'end')  # Clear username entry
        self.password_entry.delete(0, 'end')  # Clear password entry

# Start the event loop.
if __name__ == "__main__":
    window = Window()
    window.mainloop()