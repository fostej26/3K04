from turtle import bgcolor, width
import customtkinter as ctk
import hashlib
import webbrowser
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def callback(url):
    webbrowser.open_new(url)


class Window(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        username = ""
        self.title("3K04 Assignment 1")  # Set the window title
        self.geometry("800x600")  # Set the window size
        self.configure(fg_color="white")  # Set the background color
        self.init_login_page()  # Invoke window set up function

        # Main Frame for the login UI

    def init_login_page(self):

        # Create the window using customtkinter
        self.login_frame = ctk.CTkFrame(self, fg_color="white")
        self.login_frame.pack(padx=20, pady=20)
        self.state("zoomed")

        # Open the logo png from the assests file
        logo_original_image = Image.open("assets/Pacemaker logo.png")
        logo_resized_image = logo_original_image.resize((300, 200))
        self.logo_image = ImageTk.PhotoImage(
            logo_resized_image)  # Store the image in self to prevent garbage collection

        # Create the label with the resized image
        logo_label = ctk.CTkLabel(
            self.login_frame,
            image=self.logo_image,
            text=""
        )
        logo_label.pack(pady=10)

        # Label for Username
        subheading_username = ctk.CTkLabel(self.login_frame, text="Enter Username:", font=("Helvetica", 12))
        subheading_username.pack(pady=5)

        # Entry for Username
        self.username_entry = ctk.CTkEntry(self.login_frame, width=200)
        self.username_entry.pack(pady=5)

        # Label for Password
        subheading_password = ctk.CTkLabel(self.login_frame, text="Enter Password:", font=("Helvetica", 12))
        subheading_password.pack(pady=5)

        # Entry for Password
        self.password_entry = ctk.CTkEntry(self.login_frame, width=200, show='*')  # 'show' hides the password
        self.password_entry.pack(pady=5)

        # Message Label for notifying user the state of their login
        self.message_label = ctk.CTkLabel(self.login_frame, text="", font=("Helvetica", 12), text_color="red")
        self.message_label.pack(pady=10)

        # Create Sign In button
        self.signin_button = ctk.CTkButton(self.login_frame, text="Sign In", cursor="hand2", command=self.handle_signin)
        self.signin_button.pack(pady=10)

        # Create Register button
        self.register_button = ctk.CTkButton(self.login_frame, text="Register", cursor="hand2",
                                             command=self.handle_register)
        self.register_button.pack(pady=10)

    # Hash the passwords in the text file
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    # Function for processing sign in of user (already registered)
    def handle_signin(self):

        # Retrieve the username and passwords from the tk_entries
        username = self.username_entry.get()
        password = self.password_entry.get()
        hashed_password = self.hash_password(password)

        # Open the text file
        with open("users.txt", "r") as f:

            # Separate the user list in the file
            users = f.read().splitlines()
            for user in users:
                user_data = user.split()
                if username == user_data[0]:  # Check if the provided username matches the first entry in the line
                    if hashed_password == user_data[1]:  # Check if the hashed password matches the second entry
                        # in the line
                        self.message_label.configure(text="Sign In successful!", text_color="green")
                        self.init_pacemaker_page()  # Open pacemaker page
                        return
                    else:
                        # Message displayed when password is incorrectly inputted
                        self.message_label.configure(text="Incorrect password. Please try again.", text_color="red")
                        return
        self.message_label.configure(text="Username not found. Please register.")

    #
    def handle_register(self):

        # Retrieve the username and password from the text entries on the page
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            # Open the users text file
            with open("users.txt", "r") as f:
                users = f.read().splitlines()

                # Check if there are already 10 users
                if len(users) >= 10:
                    self.message_label.configure(text="User limit reached. Cannot register more users.",
                                                 text_color="red")
                    return

                # Iterate through the list of users
                for user in users:

                    # If the entered username already exists, notify the user and return
                    if username == user.split()[0]:
                        self.message_label.configure(
                            text="Username already registered. Please sign in or choose a new username.")
                        return

            # If it's a new user, add their name and password
            with open("users.txt", "a") as f:
                f.write(f"{username} {self.hash_password(password)}\n")
            self.message_label.configure(text="Registration successful!", text_color="green")

            # Clear the entry boxes
            self.username_entry.delete(0, 'end')  # Clear username entry
            self.password_entry.delete(0, 'end')  # Clear password entry
        except FileNotFoundError:
            with open("users.txt", "w") as f:
                f.write(f"{username} {self.hash_password(password)}\n")
            self.message_label.configure(text="Registration successful!", text_color="green")
            self.username_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')

    # Create the pacemaker page after logging in
    def init_pacemaker_page(self):
        # Clear the login frame and ensure it's destroyed
        self.login_frame.pack_forget()  # Hide the login frame
        self.login_frame.destroy()  # Remove the login frame entirely

        self.state("zoomed")

        # Create the navbar frame at the top
        self.navbar_frame = ctk.CTkFrame(self, fg_color="white")
        self.navbar_frame.pack(side="top", fill="x")  # This makes it fixed at the top

        # Return to the login screen
        logout_button = ctk.CTkButton(
            self.navbar_frame,
            text="Logout",  # Name of the button
            cursor="hand2",
            command=self.show_login_page,  # The function the button performs
            fg_color="red",  # Background color
            text_color="white",  # Text color (foreground)
            font=("Arial", 12)  # Font style and size
        )
        logout_button.pack(side="right", padx=5)

        # Change password
        change_password_button = ctk.CTkButton(
            self.navbar_frame,
            text="Change Password",  # Name of the button
            cursor="hand2",
            command=self.change_password_page,  # The function the button performs
            fg_color="white",
            border_width=1,  # Background color
            text_color="black",  # Text color (foreground)
            font=("Arial", 12)  # Font style and size
        )
        change_password_button.pack(side="right", padx=5)

        logo_original_image = Image.open("assets/Pacemaker logo.png")
        logo_resized_image = logo_original_image.resize((150, 100))
        self.logo_image = ImageTk.PhotoImage(
            logo_resized_image)  # Store the image in self to prevent garbage collection

        # Create the label with the resized image
        logo_label = ctk.CTkLabel(
            self.navbar_frame,
            image=self.logo_image,
            text=""
        )
        logo_label.pack(side="left", padx=5)

        # Import the GitHub logo and place the resized image in a box
        github_image = Image.open("assets/github.png")
        resized_github_image = github_image.resize((40, 40))
        self.github_image = ImageTk.PhotoImage(resized_github_image)

        # Create the label with the resized image
        link2 = ctk.CTkLabel(self.navbar_frame, image=self.github_image, cursor="hand2", text="")  # Remove text
        link2.pack(side="right", padx=5)
        link2.bind("<Button-1>", lambda e: callback("https://github.com/fostej26/3K04"))

        # Prevent garbage collection
        link2.image = self.github_image

        # Create the content frame
        self.content_frame = ctk.CTkFrame(self, border_width=2, border_color="gray", fg_color="white")
        self.content_frame.pack(fill="both", expand=True)

        # Create the content frame grid
        for i in range(16):
            self.content_frame.grid_rowconfigure(i, weight=1)
            self.content_frame.grid_columnconfigure(i, weight=1)

        # Create the connection status frame for when we connect the Pacemaker
        connection_status_frame = ctk.CTkFrame(self.content_frame, fg_color="white", border_width=2,
                                               border_color="gray")
        connection_status_frame.grid(row=0, column=0, rowspan=2, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Create a connection status label
        connection_status_label = ctk.CTkLabel(connection_status_frame, text="Connection Status",
                                               font=("Helvetica", 12))
        connection_status_label.pack(padx=5, pady=5, side="top")

        # This frame houses the button
        connect_buttons_frame = ctk.CTkFrame(self.content_frame, fg_color="white")
        connect_buttons_frame.grid(row=2, column=0, rowspan=2, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Configure the grid layout for the connect_buttons_frame
        connect_buttons_frame.grid_rowconfigure(0, weight=1)
        connect_buttons_frame.grid_rowconfigure(1, weight=1)
        connect_buttons_frame.grid_columnconfigure(0, weight=1)

        # Add buttons inside the connect_buttons_frame
        connect_pm_button = ctk.CTkButton(
            connect_buttons_frame,
            text="Connect Pacemaker",
            cursor="hand2",
            # command= connect pacemaker function laterrrr
            fg_color="white",
            border_width=2,  # Background color
            text_color="black",  # Text color (foreground)
            border_color="gray",
            font=("Arial", 12)
        )
        connect_pm_button.grid(row=0, column=0, padx=0, pady=5, sticky="nsew")

        disconnect_pm_button = ctk.CTkButton(
            connect_buttons_frame,
            text="Disconnect Pacemaker",
            cursor="hand2",
            # command= connect pacemaker function laterrrr
            fg_color="white",
            border_width=2,  # Background color
            text_color="black",  # Text color (foreground)
            border_color="gray",
            font=("Arial", 12)
        )
        disconnect_pm_button.grid(row=1, column=0, padx=0, pady=5, sticky="nsew")

        pacemaker_modes_frame = ctk.CTkFrame(self.content_frame, fg_color="white", border_width=2, border_color="gray")
        pacemaker_modes_frame.grid(row=4, column=0, rowspan=11, columnspan=2, padx=5, pady=10, sticky="nsew")

        # Configure the grid layout for the pacemaker_modes_frame
        for i in range(5):
            pacemaker_modes_frame.grid_rowconfigure(i, weight=1)

        pacemaker_modes_frame.grid_columnconfigure(0, weight=1)

        'VARIABLE WILL BE USED FOR SETTING PACEMAKER MODES IN FUTURE'

        pacemaker_mode_var = ctk.StringVar(value="")

        # Add a label inside the pacemaker modes frame
        pacemaker_modes_label = ctk.CTkLabel(pacemaker_modes_frame, text="Pacemaker Modes", font=("Helvetica", 16))
        pacemaker_modes_label.grid(row=0, column=0, padx=5, pady=5, sticky="n")

        # Add radio buttons inside the pacemaker modes frame
        AOO_button = ctk.CTkRadioButton(pacemaker_modes_frame, text="AOO", font=("Helvetica", 12),
                                        variable=pacemaker_mode_var, value="AOO")
        AOO_button.grid(row=1, column=0, padx=5, pady=2, sticky="n")

        VOO_button = ctk.CTkRadioButton(pacemaker_modes_frame, text="VOO", font=("Helvetica", 12),
                                        variable=pacemaker_mode_var, value="VOO")
        VOO_button.grid(row=2, column=0, padx=5, pady=2, sticky="n")

        AAI_button = ctk.CTkRadioButton(pacemaker_modes_frame, text="AAI", font=("Helvetica", 12),
                                        variable=pacemaker_mode_var, value="AAI")
        AAI_button.grid(row=3, column=0, padx=5, pady=2, sticky="n")

        VVI_button = ctk.CTkRadioButton(pacemaker_modes_frame, text="VVI", font=("Helvetica", 12),
                                        variable=pacemaker_mode_var, value="VVI")
        VVI_button.grid(row=4, column=0, padx=5, pady=2, sticky="n")

        # add frame for plots
        self.egraphs_frame = ctk.CTkFrame(self.content_frame, fg_color="white")
        self.egraphs_frame.grid(row=0, column=2, rowspan=15, columnspan=15, padx=5, pady=10, sticky="nsew")

        # Configure the grid layout for the egraphs_frame

        for i in range(16):
            self.egraphs_frame.grid_rowconfigure(i, weight=1)
        self.egraphs_frame.grid_columnconfigure(0, weight=1)

        'EGRAPH LABELS CURRENTLY OCCUPY 7 GRIDSPACES, GRAPH WILL OCCUPY 6, LABEL 1'

        # Add a label inside the egraphs_frame
        egraphs_label = ctk.CTkLabel(self.egraphs_frame, text="Electrogram Plots", font=("Helvetica", 16))
        egraphs_label.grid(row=0, column=0, rowspan=1, padx=5, pady=5, sticky="n")
        egraphs_label = ctk.CTkLabel(self.egraphs_frame, text="Electrogram Plots", font=("Helvetica", 24))
        egraphs_label.grid(row=0, column=0, rowspan = 1, padx=5, pady=5, sticky="n")

        ventrical_label = ctk.CTkLabel(self.egraphs_frame, text="Ventrical Electrogram", font=("Helvetica", 16))
        ventrical_label.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        atrial_label = ctk.CTkLabel(self.egraphs_frame, text="Atrial Electrogram", font=("Helvetica", 16))
        atrial_label.grid(row=8, column=0, padx=5, pady=5, sticky="n")

        self.ventricular_electrogram()
        self.atrium_electrogram()


    def change_password_page(self):
        self.content_frame.pack_forget()  # Hide the login frame
        self.content_frame.destroy()
        self.navbar_frame.pack_forget()  # Hide the login frame
        self.navbar_frame.destroy()  # Remove the login frame entirely


        self.change_password_frame = ctk.CTkFrame(self)
        self.change_password_frame.pack(padx=20, pady=20)
        self.state("zoomed")

        logo_original_image = Image.open("assets/Pacemaker logo.png")
        logo_resized_image = logo_original_image.resize((300, 200))
        self.logo_image = ImageTk.PhotoImage(
            logo_resized_image)  # Store the image in self to prevent garbage collection

        # Create the label with the resized image
        logo_label = ctk.CTkLabel(
            self.change_password_frame,
            image=self.logo_image,
            text=""
        )
        logo_label.pack(pady=10)

        username_label = ctk.CTkLabel(self.change_password_frame, text="Enter username:")
        username_label.pack(pady=5)

        username = ctk.CTkEntry(self.change_password_frame, width=200)
        username.pack(pady=5)

        password_label = ctk.CTkLabel(self.change_password_frame, text="Enter new password:")
        password_label.pack(pady=5)

        newpassword = ctk.CTkEntry(self.change_password_frame, width=200)
        newpassword.pack(pady=5)

        info_label = ctk.CTkLabel(self.change_password_frame, text = " ")
        info_label.pack(pady=10)

        enter_info_button = ctk.CTkButton(self.change_password_frame, text="Change",
                                          command=lambda: self.enter_info(username.get(), newpassword.get(),
                                                                          info_label))
        enter_info_button.pack(pady=10)

        back_button = ctk.CTkButton(self.change_password_frame, text="Back", command=self.show_pacemaker_page)
        back_button.pack(pady=10)

    def enter_info(self, username, newpassword, label):
        if username == 0 or newpassword == 0:
            label.configure(text="No empty entries please")
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
            if not found_flag:
                label.configure(text="No existing user")
                return

            with open("users.txt", "w") as f:
                f.write("\n".join(users))

            label.configure(text="Successfully changed password")

        except FileNotFoundError:
            label.configure(text="users.txt does not exist")

    def show_login_page(self):
        # Clear existing frames (like the pacemaker page)
        for widget in self.winfo_children():
            widget.destroy()  # Destroy all child widgets in the main window

        self.init_login_page()

    def show_pacemaker_page(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.init_pacemaker_page()

    def ventricular_electrogram(self):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_title("Ventricle Electrogram")
        ax.set_ylabel("Voltage (V)")
        ax.grid()
        line, = ax.plot([], [], lw=2)
        ax.set_xlim(0, 2 * np.pi)
        ax.set_ylim(-1.5, 1.5)
        def animate(i):
            x = np.linspace(0, 2 * np.pi, 1000)
            y = np.sin(x + i / 10.0)
            line.set_data(x, y)
            return line,
        ani = animation.FuncAnimation(fig, animate, frames=1000, interval=50, blit=True)
        canvas = FigureCanvasTkAgg(fig, master=self.egraphs_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

    def atrium_electrogram(self):
        fig, ax = plt.subplots(figsize=(12, 6))  # Adjust size as needed
        ax.set_title("Atrium Electrogram")
        ax.set_ylabel("Voltage (V)")
        ax.grid()
        line, = ax.plot([], [], lw=3)
        ax.set_xlim(0, 4)
        ax.set_ylim(-2, 2)
        def animate(i):
            x = np.linspace(0, 4, 1000)
            y = np.sin(2 * np.pi * (x-0.01*i))
            line.set_data(x, y)
            return line,
        ani = animation.FuncAnimation(fig, animate, frames=1000, interval=50, blit=True)
        canvas = FigureCanvasTkAgg(fig, master=self.egraphs_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=9, column=0, padx=5, pady=5, sticky="nsew")

class AOO():
    def __init__(self):
        LRL = 0
        URL = 0
        AtrAMP = 0
        AtrPW = 0


class VOO():
    def __init__(self):
        LRL = 0
        URL = 0
        VenAMP = 0
        VenPW = 0

class AAI():
    def __init__(self):
        LRL = 0
        URL = 0
        AtrAMP = 0
        AtrPW = 0
        ARP = 0

class VVI():
    def __init__(self):
        LRL = 0
        URL = 0
        VenAMP = 0
        VenPW = 0
        VRP = 0


# Add entry boxes for pacemaker values - save pacemaker values in users.txt
# Add confirm button for select pacemaker mode
# Consider the ranges for the programmable data


# Start the event loop.
if __name__ == "__main__":
    ctk.set_appearance_mode("light")  # Modes: "light" (standard), "dark", "system" (default)
    ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue")
    window = Window()
    window.mainloop()


    