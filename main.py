from tkinter import Tk, Button, Entry, Label, Frame, PhotoImage
import hashlib
import webbrowser
from PIL import Image, ImageTk


def callback(url):
    webbrowser.open_new(url)

class Window(Tk):
    def __init__(self):
        super().__init__()

        #save user info for uses once already logged in i.e. delete account/change password
        current_username =""
        current_password =""

        self.title("3K04 Assignment 1")

        # Main Frame for the login UI
        self.login_frame = Frame(self)
        self.login_frame.pack(pady=20)

        # Subheading for Username
        subheading_username = Label(self.login_frame, text="Enter Username:", font=("Helvetica", 12))
        subheading_username.pack(pady=5)
        
        # Entry for Username
        self.username_entry = Entry(self.login_frame, width=30)
        self.username_entry.pack(pady=5)

        # Subheading for Password
        subheading_password = Label(self.login_frame, text="Enter Password:", font=("Helvetica", 12))
        subheading_password.pack(pady=5)
        
        # Entry for Password
        self.password_entry = Entry(self.login_frame, width=30, show='*')  # 'show' hides the password
        self.password_entry.pack(pady=5)

        # Message Label
        self.message_label = Label(self.login_frame, text="", font=("Helvetica", 12), fg="red")
        self.message_label.pack(pady=10)

        # Create Sign In button
        self.signin_button = Button(self.login_frame, text="Sign In",cursor="hand2")
        self.signin_button.bind("<Button-1>", self.handle_signin)  # Bind left mouse button click
        self.signin_button.pack(pady=10)

        # Create Sign Up button
        self.register_button = Button(self.login_frame, text="Register", cursor="hand2")
        self.register_button.bind("<Button-1>", self.handle_register)  # Bind left mouse button click
        self.register_button.pack(pady=10)

        #Create Change Password button


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
                        self.init_pacemaker_page()  # Open pacemaker page
                        return 
                    else:
                        self.message_label.config(text="Incorrect password. Please try again.")
                        return
        self.message_label.config(text="Username not found. Please register.")


    def handle_register(self, event):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            with open("users.txt", "r") as f:
                users = f.read().splitlines()

                # Check if there are already 10 users
                if len(users) >= 10:
                    self.message_label.config(text="User limit reached. Cannot register more users.", fg="red")
                    return
                
                for user in users:
                    if username == user.split()[0]:
                        self.message_label.config(text="Username already registered. Please sign in or choose a new username.")
                        return

            with open("users.txt", "a") as f:
                f.write(f"{username} {self.hash_password(password)}\n")
            self.message_label.config(text="Registration successful!", fg="green")
            self.username_entry.delete(0, 'end')  # Clear username entry
            self.password_entry.delete(0, 'end')  # Clear password entry
        except FileNotFoundError:
            with open("users.txt", "w") as f:
                f.write(f"{username} {self.hash_password(password)}\n")
            self.message_label.config(text="Registration successful!", fg="green")
            self.username_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')

    # self.changepass_button = Button(self, text="Change Password")
    # self.changepass_button.bind("<Button-1>", self.handle_changepass)
    # self.changepass_button.pack(pady=10)

    def init_pacemaker_page(self):
        # Clear the login frame and ensure it's destroyed
        self.login_frame.pack_forget()  # Hide the login frame
        self.login_frame.destroy()  # Remove the login frame entirely

        # Create the navbar frame at the top
        self.navbar_frame = Frame(self, bd=2)
        self.navbar_frame.pack(side="top", fill="x")  # This makes it fixed at the top

        #return to the login screen
        logout_button = Button(self.navbar_frame, text="Logout", cursor="hand2",command=self.show_login_page)
        logout_button.pack(side="right", padx=5)

        #change password
        change_password_button = Button(self.navbar_frame, text="Change Password", cursor="hand2", command=self.change_password_page)
        change_password_button.pack(side="right", padx=5)

        groupname = Label(self.navbar_frame, text="The Pulse: Pacemaker", font=("Helvetica", 12))
        groupname.pack(side="left", pady=5)

        github_image = PhotoImage(file="assets/github.png")

        # Open and resize the image
        original_image = Image.open("assets/github.png")
        resized_image = original_image.resize((35, 35))
        github_image = ImageTk.PhotoImage(resized_image)

        # Create the label with the resized image
        link2 = Label(self.navbar_frame, image=github_image, cursor="hand2")
        link2.pack(side="right", padx=5)
        link2.bind("<Button-1>", lambda e: self.callback("https://github.com/fostej26/3K04"))

        # Keep a reference to the image to prevent it from being garbage collected
        link2.image = github_image

        # You can now add more widgets for the pacemaker page below this
        # For example, a Label to simulate content:
        self.content_frame = Frame(self)
        self.content_frame.pack(fill="both", expand=True)  # Fill the rest of the space
        

    def change_password_page(self):
        for widget in self.navbar_frame.winfo_children():
            widget.destroy()

        self.change_password_window = Frame(self)
        self.change_password_window.pack(pady=20)

        username_label = Label(self.change_password_window, text="Enter username:")
        username_label.pack(pady=5)

        username = Entry(self.change_password_window, width=30)
        username.pack(pady=5)

        password_label = Label(self.change_password_window, text="Enter new password:")
        password_label.pack(pady=5)

        newpassword = Entry(self.change_password_window, width=30)
        newpassword.pack(pady=5)

        info_label = Label(self.change_password_window)
        info_label.pack(pady=10)

        enter_info_button = Button(self.change_password_window, text="Change", command=lambda: self.enter_info(username.get(),newpassword.get(), info_label))
        enter_info_button.pack(pady=10)

        back_button = Button(self.change_password_window, text="Back", command=self.init_pacemaker_page)
        back_button.pack(pady=10)

    def enter_info(self, username, newpassword, label):
        if username == 0 or newpassword == 0:
            label.config(text="No empty entries please")
            return

        new_hashed_password = self.hash_password(newpassword)

        try:
            with open("users.txt", "r") as f:
                users = f.read().splitlines()

            found_flag = False
            for i, user in enumerate(users):
                user_data = user.split()
                if username == user_data[0]:
                    users[i] = f"{username} {new_hashed_password}"
                    found_flag = True
                    break
            if found_flag == False:
                label.config(text="No existing user")
                return

            with open("users.txt", "w") as f:
                f.write("\n".join(users))

            label.config(text="Successfully changed password")

        except FileNotFoundError:
            label.config(text="users.txt does not exist")

    def show_login_page(self):
        # Clear the pacemaker page
        for widget in self.login_frame.winfo_children():
            widget.destroy()
        self.destroy()
        # Recreate the login UI
        self.__init__()

    # def handle_changepass(self):
    #     self.message_label.config(text="Please enter Username and new Password", fg="green")
    #     username = self.username_entry.get()

# Start the event loop.
if __name__ == "__main__":
    window = Window()
    window.mainloop()
