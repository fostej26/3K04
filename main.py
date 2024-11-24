from re import L, S
from turtle import bgcolor, color, width
import customtkinter as ctk
import hashlib
import webbrowser
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import json
import serial 
import struct

from yarl import URL

def checkparams(LRL, URL, AtrAMP, AtrPW, VenAMP, VenPW, AtrSens, ARP, PVARP, VenSens, VRP, ReactionTime, RecoveryTime, ResponseFactor, ActivityThreshold):
    pass

def is_float(s):
    return s.replace('.', '', 1).isdigit() and s.count('.') <= 1

def callback(url):
    webbrowser.open_new(url)

def get_params_json(param):
    data = json.loads('{"url":444, "lrl":555}')
    return data[param]

class Mode:
    def __init__(self):
        self.name = ""
        self.LRL = 0
        self.URL = 0
        self.AtrAMP = 0
        self.AtrPW = 0
        self.VenAMP = 0
        self.VenPW = 0
        self.AtrSens = 0
        self.ARP = 0
        self.PVARP = 0
        self.VenSens = 0
        self.VRP = 0
        self.ReactionTime = 0
        self.RecoveryTime = 0
        self.ResponseFactor = 0
        self.ActivityThreshold = 0

    def set_name(self, name):
        self.name = name

    def set_params(self, LRL, URL, AtrAMP, AtrPW, VenAMP, VenPW, AtrSens, ARP, PVARP, VenSens, VRP, ReactionTime, RecoveryTime, ResponseFactor, ActivityThreshold):
        self.LRL = LRL
        self.URL = URL
        self.AtrAMP = AtrAMP
        self.AtrPW = AtrPW
        self.VenAMP = VenAMP
        self.VenPW = VenPW
        self.AtrSens = AtrSens
        self.ARP = ARP
        self.PVARP = PVARP
        self.VenSens = VenSens
        self.VRP = VRP
        self.ReactionTime = ReactionTime
        self.RecoveryTime = RecoveryTime
        self.ResponseFactor = ResponseFactor
        self.ActivityThreshold = ActivityThreshold


    def get_params(self):
        return self.LRL, self.URL, self.AtrAMP, self.AtrPW, self.VenAMP, self.VenPW, self.AtrSens, self.ARP, self.PVARP, self.VenSens, self.VRP, self.ReactionTime, self.RecoveryTime, self.ResponseFactor, self.ActivityThreshold
        
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password

class Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Initialize the user as an empty object
        self.newserial = None
        self.user = User("", "")  # Correctly initialize User
        self.title("3K04 Assignment 1")
        self.geometry("800x600")
        self.configure(fg_color="white")
        self.pacemaker_mode_var = ctk.StringVar(value="")
        self.message_label = ctk.CTkLabel(self, text="")  # Create a message label for status messages
        self.message_label.pack()  # Place the label in the window
        self.init_login_page() 

        self.x = []
        self.y = []

        port = serial.Serial()
        port.baudrate = 115200
        port.port = 'COM6'
        port.timeout = 10

        

    def handle_register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        

        try:
            with open("users.txt", "r") as f:
                users = f.read().splitlines()

            if len(users) >= 10:
                self.message_label.configure(text="User limit reached. Cannot register more users.", text_color="red")
                return

            for user in users:
                if username == user.split()[0]:
                    self.message_label.configure(
                        text="Username already registered. Please sign in or choose a new username.")
                    return

            with open("users.txt", "a") as f:
                f.write(f"{username} {self.hash_password(password)}\n")
                self.user = User(username, password)
            self.message_label.configure(text="Registration successful!", text_color="green")

            self.username_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')

        except FileNotFoundError:
            with open("users.txt", "w") as f:
                f.write(f"{username} {self.hash_password(password)}\n")
            self.message_label.configure(text="Registration successful!", text_color="green")
            self.username_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')


    #CURRENTLY DOES NOT WORK, ONLY RELEVANT FOR A2
    def save_parameters(self):
        username = self.user.get_username()
        self.mode = Mode()
        mode_name = self.pacemaker_mode_var.get()
        self.mode.set_name(mode_name)
        def safe_get(entry, default=""):
            try:
                output = entry.get()
                return output
            except:
                return ""

        self.mode.set_params(
            LRL=safe_get(self.LRL_entry),
            URL=safe_get(self.URL_entry),
            AtrAMP=safe_get(getattr(self, 'AtrAMP_entry', None)),
            AtrPW=safe_get(getattr(self, 'AtrPW_entry', None)),
            VenAMP=safe_get(getattr(self, 'VenAMP_entry', None)),
            VenPW=safe_get(getattr(self, 'VenPW_entry', None)),
            AtrSens=safe_get(getattr(self, 'AtrSens_entry', None)),
            ARP=safe_get(getattr(self, 'ARP_entry', None)),
            PVARP=safe_get(getattr(self, 'PVARP_entry', None)),
            VenSens=safe_get(getattr(self, 'VenSens_entry', None)),
            VRP=safe_get(getattr(self, 'VRP_entry', None)),
            ReactionTime=safe_get(getattr(self, 'ReactionTime_entry', None)),
            RecoveryTime=safe_get(getattr(self, 'RecoveryTime_entry', None)),
            ResponseFactor=safe_get(getattr(self, 'ResponseFactor_entry', None)),
            ActivityThreshold=safe_get(getattr(self, 'ActivityThreshold_entry', None))
        )

        
        if all(param == "" or is_float(param) for param in [self.mode.LRL, self.mode.URL, self.mode.AtrAMP, self.mode.AtrPW, self.mode.VenAMP, self.mode.VenPW]):
            self.valid_input_label.grid(row=6, column=0, padx=5, pady=5, sticky="n")
        else:
            self.valid_input_label.grid_remove()
            self.invalid_input_label.grid(row=6, column=0, padx=5, pady=5, sticky="n")
            return
        mode_data = {
            "name": self.mode.name,
            "LRL": self.mode.LRL,
            "URL": self.mode.URL,
            "AtrAMP": self.mode.AtrAMP,
            "AtrPW": self.mode.AtrPW,
            "VenAMP": self.mode.VenAMP,
            "VenPW": self.mode.VenPW,
            "AtrSens": self.mode.AtrSens,
            "ARP": self.mode.ARP,
            "PVARP": self.mode.PVARP,
            "VenSens": self.mode.VenSens,
            "VRP": self.mode.VRP,
            "ReactionTime": self.mode.ReactionTime,
            "RecoveryTime": self.mode.RecoveryTime,
            "ResponseFactor": self.mode.ResponseFactor,
            "ActivityThreshold": self.mode.ActivityThreshold
        }
        try:
            with open("parameters.json", "r") as f:
                users = json.load(f)
        except FileNotFoundError:
            users = []

        for user in users:
            if user["username"] == username:
                if "modes" not in user:
                    user["modes"] = []
                user["modes"].append(mode_data)
                break
        else:
            users.append({"username": username, "modes": [mode_data]})

        with open("parameters.json", "w") as f:
            json.dump(users, f, indent=4)


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
                        self.user = User(username, password)
                        return
                    else:
                        # Message displayed when password is incorrectly inputted
                        self.message_label.configure(text="Incorrect password. Please try again.", text_color="red")
                        return
        self.message_label.configure(text="Username not found. Please register.")


    def enter_info(self, username, newpassword, label):

        # Check if the entries are empty
        if username == 0 or newpassword == 0:
            label.configure(text="No empty entries please")
            return

        # Hash the newly entered password
        new_hashed_password = self.hash_password(newpassword)

        try:
            # Open the text file with user data
            with open("users.txt", "r") as f:
                users = f.read().splitlines()

            # Initialize a flag for if the username is found in the file
            found_flag = False

            # Use the enumerate function to iterate through the indexed user file
            for i, user in enumerate(users):
                user_data = user.split()

                # If the entered username matches the username at the index, add the newly hashed password
                if username == user_data[0]:
                    users[i] = f"{username} {new_hashed_password}"

                    # Set the flag and break out of the loop
                    found_flag = True
                    break

            # If the flag hasn't been set, the entered user doesn't exist
            if not found_flag:
                label.configure(text="No existing user")
                return

            # Write to the user data file
            with open("users.txt", "w") as f:
                f.write("\n".join(users))

            # Set the label status as successful
            label.configure(text="Successfully changed password")

        # File not found error
        except FileNotFoundError:
            label.configure(text="users.txt does not exist")


    def init_AOO(self):
        for widget in self.parameters_frame.winfo_children():
            widget.destroy()
        for i in range(7):
            self.parameters_frame.grid_rowconfigure(i, weight=1)
        self.parameters_frame.grid_columnconfigure(0, weight=1)

        # Pacemaker parameters label
        parameters_label = ctk.CTkLabel(self.parameters_frame, text="Pacemaker Parameters", font=("Helvetica", 12))
        parameters_label.grid(row=0, column=0, padx=5, pady=5, sticky="n")

        # Entry boxes for parameters ##FIX FOR ALL MODES
        self.LRL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="LRL")
        self.LRL_entry.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        self.URL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="URL")
        self.URL_entry.grid(row=2, column=0, padx=5, pady=5, sticky="n")

        self.AtrAMP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrAMP")
        self.AtrAMP_entry.grid(row=3, column=0, padx=5, pady=5, sticky="n")

        self.AtrPW_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrPW")
        self.AtrPW_entry.grid(row=4, column=0, padx=5, pady=5, sticky="n")

        # Initially disabled save button
        self.save_button = ctk.CTkButton(self.parameters_frame, text="Save Parameters", command=self.save_parameters, state="enabled")
        self.save_button.grid(row=5, column=0, padx=5, pady=10, sticky="n")

        self.invalid_input_label = ctk.CTkLabel(self.parameters_frame, text="Invalid Input. Please enter numeric values.", font=("Helvetica", 12), text_color="red")
        self.valid_input_label = ctk.CTkLabel(self.parameters_frame, text="Parameters Saved!", font=("Helvetica", 12), text_color="green")

    def init_VOO(self):
        for widget in self.parameters_frame.winfo_children():
            widget.destroy()
        for i in range(7):
            self.parameters_frame.grid_rowconfigure(i, weight=1)
        self.parameters_frame.grid_columnconfigure(0, weight=1)

        # Pacemaker parameters label
        parameters_label = ctk.CTkLabel(self.parameters_frame, text="Pacemaker Parameters", font=("Helvetica", 12))
        parameters_label.grid(row=0, column=0, padx=5, pady=5, sticky="n")

        # Entry boxes for parameters ##FIX FOR ALL MODES
        self.LRL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="LRL")
        self.LRL_entry.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        self.URL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="URL")
        self.URL_entry.grid(row=2, column=0, padx=5, pady=5, sticky="n")

        self.VenAMP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VenAMP")
        self.VenAMP_entry.grid(row=3, column=0, padx=5, pady=5, sticky="n")

        self.VenPW_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VenPW")
        self.VenPW_entry.grid(row=4, column=0, padx=5, pady=5, sticky="n")

        # Initially disabled save button
        self.save_button = ctk.CTkButton(self.parameters_frame, text="Save Parameters", command=self.save_parameters, state="enabled")
        self.save_button.grid(row=5, column=0, padx=5, pady=10, sticky="n")

        self.invalid_input_label = ctk.CTkLabel(self.parameters_frame, text="Invalid Input. Please enter numeric values.", font=("Helvetica", 12), text_color="red")
        self.valid_input_label = ctk.CTkLabel(self.parameters_frame, text="Parameters Saved!", font=("Helvetica", 12), text_color="green")

    def init_AAI(self):
        for widget in self.parameters_frame.winfo_children():
            widget.destroy()
        for i in range(10):
            self.parameters_frame.grid_rowconfigure(i, weight=1)
        self.parameters_frame.grid_columnconfigure(0, weight=1)

        # Pacemaker parameters label
        parameters_label = ctk.CTkLabel(self.parameters_frame, text="Pacemaker Parameters", font=("Helvetica", 12))
        parameters_label.grid(row=0, column=0, padx=5, pady=5, sticky="n")

        # Entry boxes for parameters ##FIX FOR ALL MODES
        self.LRL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="LRL")
        self.LRL_entry.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        self.URL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="URL")
        self.URL_entry.grid(row=2, column=0, padx=5, pady=5, sticky="n")

        self.AtrAMP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrAMP")
        self.AtrAMP_entry.grid(row=3, column=0, padx=5, pady=5, sticky="n")

        self.AtrPW_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrPW")
        self.AtrPW_entry.grid(row=4, column=0, padx=5, pady=5, sticky="n")

        self.AtrSens_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrSens")
        self.AtrSens_entry.grid(row=5, column=0, padx=5, pady=5, sticky="n")

        self.ARP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="ARP")
        self.ARP_entry.grid(row=6, column=0, padx=5, pady=5, sticky="n")

        self.PVARP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="PVARP")
        self.PVARP_entry.grid(row=7, column=0, padx=5, pady=5, sticky="n")

        # Initially disabled save button
        self.save_button = ctk.CTkButton(self.parameters_frame, text="Save Parameters", command=self.save_parameters, state="enabled")
        self.save_button.grid(row=8, column=0, padx=5, pady=10, sticky="n")

        self.invalid_input_label = ctk.CTkLabel(self.parameters_frame, text="Invalid Input. Please enter numeric values.", font=("Helvetica", 12), text_color="red")
        self.valid_input_label = ctk.CTkLabel(self.parameters_frame, text="Parameters Saved!", font=("Helvetica", 12), text_color="green")
    
    def init_VVI(self):
        for widget in self.parameters_frame.winfo_children():
            widget.destroy()
        for i in range(10):
            self.parameters_frame.grid_rowconfigure(i, weight=1)
        self.parameters_frame.grid_columnconfigure(0, weight=1)

        # Pacemaker parameters label
        parameters_label = ctk.CTkLabel(self.parameters_frame, text="Pacemaker Parameters", font=("Helvetica", 12))
        parameters_label.grid(row=0, column=0, padx=5, pady=5, sticky="n")

        # Entry boxes for parameters ##FIX FOR ALL MODES
        self.LRL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="LRL")
        self.LRL_entry.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        self.URL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="URL")
        self.URL_entry.grid(row=2, column=0, padx=5, pady=5, sticky="n")

        self.VenAMP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VenAMP")
        self.VenAMP_entry.grid(row=3, column=0, padx=5, pady=5, sticky="n")

        self.VenPW_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VenPW")
        self.VenPW_entry.grid(row=4, column=0, padx=5, pady=5, sticky="n")

        self.VenSens_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VenSens")
        self.VenSens_entry.grid(row=5, column=0, padx=5, pady=5, sticky="n")

        self.VRP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VRP")
        self.VRP_entry.grid(row=6, column=0, padx=5, pady=5, sticky="n")

        # Initially disabled save button
        self.save_button = ctk.CTkButton(self.parameters_frame, text="Save Parameters", command=self.save_parameters, state="enabled")
        self.save_button.grid(row=7, column=0, padx=5, pady=10, sticky="n")

        self.invalid_input_label = ctk.CTkLabel(self.parameters_frame, text="Invalid Input. Please enter numeric values.", font=("Helvetica", 12), text_color="red")
        self.valid_input_label = ctk.CTkLabel(self.parameters_frame, text="Parameters Saved!", font=("Helvetica", 12), text_color="green")

    def init_AOOR(self):
        for widget in self.parameters_frame.winfo_children():
            widget.destroy()
        for i in range(6):
            self.parameters_frame.grid_rowconfigure(i, weight=1)
        for j in range(2):
            self.parameters_frame.grid_columnconfigure(j, weight=1)

        # Pacemaker parameters label
        parameters_label = ctk.CTkLabel(self.parameters_frame, text="Pacemaker Parameters", font=("Helvetica", 12))
        parameters_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Entry boxes for parameters
        self.LRL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="LRL")
        self.LRL_entry.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        self.URL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="URL")
        self.URL_entry.grid(row=1, column=1, padx=5, pady=5, sticky="n")

        self.AtrAMP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrAMP")
        self.AtrAMP_entry.grid(row=2, column=0, padx=5, pady=5, sticky="n")

        self.AtrPW_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrPW")
        self.AtrPW_entry.grid(row=2, column=1, padx=5, pady=5, sticky="n")

        self.ReactionTime_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Reaction Time")
        self.ReactionTime_entry.grid(row=3, column=0, padx=5, pady=5, sticky="n")

        self.RecoveryTime_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Recovery Time")
        self.RecoveryTime_entry.grid(row=3, column=1, padx=5, pady=5, sticky="n")

        self.ResponseFactor_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Response Factor")
        self.ResponseFactor_entry.grid(row=4, column=0, padx=5, pady=5, sticky="n")

        self.ActivityThreshold_var = ctk.StringVar(value="Activity Threshold")  # Default value
        self.ActivityThreshold_entry = ctk.CTkOptionMenu(self.parameters_frame, variable=self.ActivityThreshold_var, values=["VL", "L", "ML", "M", "MH", "H", "VH"], fg_color="white", text_color="gray")
        self.ActivityThreshold_entry.grid(row=4, column=1, padx=5, pady=5, sticky="n")

        # Initially enabled save button
        self.save_button = ctk.CTkButton(self.parameters_frame, text="Save Parameters", command=self.save_parameters, state="enabled")
        self.save_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10, sticky="n")

        self.invalid_input_label = ctk.CTkLabel(self.parameters_frame, text="Invalid Input. Please enter numeric values.", font=("Helvetica", 12), text_color="red")
        self.valid_input_label = ctk.CTkLabel(self.parameters_frame, text="Parameters Saved!", font=("Helvetica", 12), text_color="green")

    def init_VOOR(self):
        for widget in self.parameters_frame.winfo_children():
            widget.destroy()
        for i in range(6):
            self.parameters_frame.grid_rowconfigure(i, weight=1)
        for j in range(2):
            self.parameters_frame.grid_columnconfigure(j, weight=1)

        # Pacemaker parameters label
        parameters_label = ctk.CTkLabel(self.parameters_frame, text="Pacemaker Parameters", font=("Helvetica", 12))
        parameters_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Entry boxes for parameters
        self.LRL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="LRL")
        self.LRL_entry.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        self.URL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="URL")
        self.URL_entry.grid(row=1, column=1, padx=5, pady=5, sticky="n")

        self.VenAMP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VenAMP")
        self.VenAMP_entry.grid(row=2, column=0, padx=5, pady=5, sticky="n")

        self.VenPW_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VenPW")
        self.VenPW_entry.grid(row=2, column=1, padx=5, pady=5, sticky="n")

        self.ReactionTime_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Reaction Time")
        self.ReactionTime_entry.grid(row=3, column=0, padx=5, pady=5, sticky="n")

        self.RecoveryTime_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Recovery Time")
        self.RecoveryTime_entry.grid(row=3, column=1, padx=5, pady=5, sticky="n")

        self.ResponseFactor_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Response Factor")
        self.ResponseFactor_entry.grid(row=4, column=0, padx=5, pady=5, sticky="n")

        self.ActivityThreshold_var = ctk.StringVar(value="Activity Threshold")  # Default value
        self.ActivityThreshold_entry = ctk.CTkOptionMenu(self.parameters_frame, variable=self.ActivityThreshold_var, values=["VL", "L", "ML", "M", "MH", "H", "VH"], fg_color="white", text_color="gray")
        self.ActivityThreshold_entry.grid(row=4, column=1, padx=5, pady=5, sticky="n")

        # Initially enabled save button
        self.save_button = ctk.CTkButton(self.parameters_frame, text="Save Parameters", command=self.save_parameters, state="enabled")
        self.save_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10, sticky="n")

        self.invalid_input_label = ctk.CTkLabel(self.parameters_frame, text="Invalid Input. Please enter numeric values.", font=("Helvetica", 12), text_color="red")
        self.valid_input_label = ctk.CTkLabel(self.parameters_frame, text="Parameters Saved!", font=("Helvetica", 12), text_color="green")

    def init_AAIR(self):
        for widget in self.parameters_frame.winfo_children():
            widget.destroy()
        for i in range(10):
            self.parameters_frame.grid_rowconfigure(i, weight=1)
        for j in range(2):
            self.parameters_frame.grid_columnconfigure(j, weight=1)

        # Pacemaker parameters label
        parameters_label = ctk.CTkLabel(self.parameters_frame, text="Pacemaker Parameters", font=("Helvetica", 12))
        parameters_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Entry boxes for parameters
        self.LRL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="LRL")
        self.LRL_entry.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        self.URL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="URL")
        self.URL_entry.grid(row=1, column=1, padx=5, pady=5, sticky="n")

        self.AtrAMP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrAMP")
        self.AtrAMP_entry.grid(row=2, column=0, padx=5, pady=5, sticky="n")

        self.AtrPW_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrPW")
        self.AtrPW_entry.grid(row=2, column=1, padx=5, pady=5, sticky="n")

        self.AtrSens_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrSens")
        self.AtrSens_entry.grid(row=3, column=0, padx=5, pady=5, sticky="n")

        self.ARP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="ARP")
        self.ARP_entry.grid(row=3, column=1, padx=5, pady=5, sticky="n")

        self.PVARP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="PVARP")
        self.PVARP_entry.grid(row=4, column=0, padx=5, pady=5, sticky="n")

        self.ReactionTime_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Reaction Time")
        self.ReactionTime_entry.grid(row=4, column=1, padx=5, pady=5, sticky="n")

        self.RecoveryTime_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Recovery Time")
        self.RecoveryTime_entry.grid(row=5, column=0, padx=5, pady=5, sticky="n")

        self.ResponseFactor_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Response Factor")
        self.ResponseFactor_entry.grid(row=5, column=1, padx=5, pady=5, sticky="n")

        self.ActivityThreshold_var = ctk.StringVar(value="Activity Threshold")  # Default value
        self.ActivityThreshold_entry = ctk.CTkOptionMenu(self.parameters_frame, variable=self.ActivityThreshold_var, values=["VL", "L", "ML", "M", "MH", "H", "VH"], fg_color="white", text_color="gray")
        self.ActivityThreshold_entry.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="n")

        # Initially enabled save button
        self.save_button = ctk.CTkButton(self.parameters_frame, text="Save Parameters", command=self.save_parameters, state="enabled")
        self.save_button.grid(row=7, column=0, columnspan=2, padx=5, pady=10, sticky="n")

        self.invalid_input_label = ctk.CTkLabel(self.parameters_frame, text="Invalid Input. Please enter numeric values.", font=("Helvetica", 12), text_color="red")
        self.valid_input_label = ctk.CTkLabel(self.parameters_frame, text="Parameters Saved!", font=("Helvetica", 12), text_color="green")

    def init_VVIR(self):
        for widget in self.parameters_frame.winfo_children():
            widget.destroy()
        for i in range(8):
            self.parameters_frame.grid_rowconfigure(i, weight=1)
        for j in range(2):
            self.parameters_frame.grid_columnconfigure(j, weight=1)

        # Pacemaker parameters label
        parameters_label = ctk.CTkLabel(self.parameters_frame, text="Pacemaker Parameters", font=("Helvetica", 12))
        parameters_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Entry boxes for parameters
        self.LRL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="LRL")
        self.LRL_entry.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        self.URL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="URL")
        self.URL_entry.grid(row=1, column=1, padx=5, pady=5, sticky="n")

        self.VenAMP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VenAMP")
        self.VenAMP_entry.grid(row=2, column=0, padx=5, pady=5, sticky="n")

        self.VenPW_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VenPW")
        self.VenPW_entry.grid(row=2, column=1, padx=5, pady=5, sticky="n")

        self.VenSens_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VenSens")
        self.VenSens_entry.grid(row=3, column=0, padx=5, pady=5, sticky="n")

        self.VRP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VRP")
        self.VRP_entry.grid(row=3, column=1, padx=5, pady=5, sticky="n")

        self.ReactionTime_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Reaction Time")
        self.ReactionTime_entry.grid(row=4, column=0, padx=5, pady=5, sticky="n")

        self.RecoveryTime_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Recovery Time")
        self.RecoveryTime_entry.grid(row=4, column=1, padx=5, pady=5, sticky="n")

        self.ResponseFactor_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Response Factor")
        self.ResponseFactor_entry.grid(row=5, column=0, padx=5, pady=5, sticky="n")

        self.ActivityThreshold_var = ctk.StringVar(value="Activity Threshold")  # Default value
        self.ActivityThreshold_entry = ctk.CTkOptionMenu(self.parameters_frame, variable=self.ActivityThreshold_var, values=["VL", "L", "ML", "M", "MH", "H", "VH"], fg_color="white", text_color="gray")
        self.ActivityThreshold_entry.grid(row=5, column=1, padx=5, pady=5, sticky="n")

        # Initially enabled save button
        self.save_button = ctk.CTkButton(self.parameters_frame, text="Save Parameters", command=self.save_parameters, state="enabled")
        self.save_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10, sticky="n")

        self.invalid_input_label = ctk.CTkLabel(self.parameters_frame, text="Invalid Input. Please enter numeric values.", font=("Helvetica", 12), text_color="red")
        self.valid_input_label = ctk.CTkLabel(self.parameters_frame, text="Parameters Saved!", font=("Helvetica", 12), text_color="green")


    # Create the pacemaker page after logging in
    def init_pacemaker_page(self):
        # Clear the login frame and ensure it's destroyed
        self.login_frame.pack_forget()
        self.login_frame.destroy()

        self.state("zoomed")

        # Create the navbar frame at the top with a smaller height
        self.navbar_frame = ctk.CTkFrame(self, fg_color="white", height=40)
        self.navbar_frame.pack(side="top", fill="x", expand=False)

        # Logout button
        logout_button = ctk.CTkButton(
            self.navbar_frame,
            text="Logout",
            cursor="hand2",
            command=self.show_login_page,
            fg_color="red",
            text_color="white",
            font=("Arial", 12)
        )
        logout_button.pack(side="right", padx=5)

        # Change password button
        change_password_button = ctk.CTkButton(
            self.navbar_frame,
            text="Change Password",
            cursor="hand2",
            command=self.change_password_page,
            fg_color="white",
            border_width=1,
            text_color="black",
            font=("Arial", 12)
        )
        change_password_button.pack(side="right", padx=5)

        # Logo image setup
        logo_original_image = Image.open("assets/Pacemaker logo.png")
        logo_resized_image = logo_original_image.resize((150, 100))
        self.logo_image = ImageTk.PhotoImage(logo_resized_image)

        # Logo label
        logo_label = ctk.CTkLabel(
            self.navbar_frame,
            image=self.logo_image,
            text=""
        )
        logo_label.pack(side="left", padx=5)

        # GitHub link
        github_image = Image.open("assets/github.png")
        resized_github_image = github_image.resize((40, 40))
        self.github_image = ImageTk.PhotoImage(resized_github_image)

        link2 = ctk.CTkLabel(self.navbar_frame, image=self.github_image, cursor="hand2", text="")
        link2.pack(side="right", padx=5)
        link2.bind("<Button-1>", lambda e: callback("https://github.com/fostej26/3K04"))
        link2.image = self.github_image

        # Content frame setup
        self.content_frame = ctk.CTkFrame(self, border_width=2, border_color="gray", fg_color="white")
        self.content_frame.pack(fill="both", expand=True)

        # Configure content frame grid
        for i in range(16):
            self.content_frame.grid_rowconfigure(i, weight=1)
            self.content_frame.grid_columnconfigure(i, weight=1)

        # Connection status frame
        connection_status_frame = ctk.CTkFrame(self.content_frame, fg_color="white", border_width=2, border_color="gray")
        connection_status_frame.grid(row=0, column=0, rowspan=2, columnspan=2, padx=5, pady=5, sticky="nsew")

        self.connection_status_label = ctk.CTkLabel(connection_status_frame, text="Not connected", font=("Helvetica", 12))
        self.connection_status_label.pack(padx=5, pady=5, side="top")

         # This frame houses the buttons for actually connecting/disconnecting the PM
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
            command= self.connect_pm,
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
            command= self.disconnect_pm,
            fg_color="white",
            border_width=2,  # Background color
            text_color="black",  # Text color (foreground)
            border_color="gray",
            font=("Arial", 12)
        )
        disconnect_pm_button.grid(row=1, column=0, padx=0, pady=5, sticky="nsew")

        # Pacemaker modes frame
        pacemaker_modes_frame = ctk.CTkFrame(self.content_frame, fg_color="white", border_width=2, border_color="gray")
        pacemaker_modes_frame.grid(row=4, column=0, rowspan=5, columnspan=2, padx=5, pady=10, sticky="nsew")

        for i in range(5):
            pacemaker_modes_frame.grid_rowconfigure(i, weight=1)
        pacemaker_modes_frame.grid_columnconfigure(0, weight=1)

        # Variable to track pacemaker mode selection
        self.pacemaker_mode_var = ctk.StringVar(value="")

        def mode_selected(*args):
            if self.pacemaker_mode_var.get():
                self.save_button.configure(state="normal")  # Enable save button if a mode is selected

        # Trace changes in pacemaker mode selection
        self.pacemaker_mode_var.trace_add("write", mode_selected)

        # Pacemaker modes label
        pacemaker_modes_label = ctk.CTkLabel(pacemaker_modes_frame, text="Pacemaker Modes", font=("Helvetica", 12))
        pacemaker_modes_label.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        # Radio buttons for modes
        AOO_button = ctk.CTkRadioButton(pacemaker_modes_frame, text="AOO", font=("Helvetica", 12),
                        variable=self.pacemaker_mode_var, value="AOO", command=self.init_AOO)
        AOO_button.grid(row=1, column=0, padx=5, pady=2, sticky="n")

        VOO_button = ctk.CTkRadioButton(pacemaker_modes_frame, text="VOO", font=("Helvetica", 12),
                                        variable=self.pacemaker_mode_var, value="VOO", command=self.init_VOO)
        VOO_button.grid(row=2, column=0, padx=5, pady=2, sticky="n")

        AAI_button = ctk.CTkRadioButton(pacemaker_modes_frame, text="AAI", font=("Helvetica", 12),
                                        variable=self.pacemaker_mode_var, value="AAI", command=self.init_AAI)
        AAI_button.grid(row=3, column=0, padx=5, pady=2, sticky="n")

        VVI_button = ctk.CTkRadioButton(pacemaker_modes_frame, text="VVI", font=("Helvetica", 12),
                                        variable=self.pacemaker_mode_var, value="VVI", command = self.init_VVI)
        VVI_button.grid(row=4, column=0, padx=5, pady=2, sticky="n")

        AOOR_button = ctk.CTkRadioButton(pacemaker_modes_frame, text="AOOR", font=("Helvetica", 12),
                                        variable=self.pacemaker_mode_var, value="AOOR", command=self.init_AOOR)
        AOOR_button.grid(row=1, column=1, padx=5, pady=2, sticky="n")

        VOOR_button = ctk.CTkRadioButton(pacemaker_modes_frame, text="VOOR", font=("Helvetica", 12),
                                         variable=self.pacemaker_mode_var, value="VOOR", command=self.init_VOOR)
        VOOR_button.grid(row=2, column=1, padx=5, pady=2, sticky="n")

        AAIR_button = ctk.CTkRadioButton(pacemaker_modes_frame, text="AAIR", font=("Helvetica", 12),
                                         variable=self.pacemaker_mode_var, value="AAIR", command=self.init_AAIR)
        AAIR_button.grid(row=3, column=1, padx=5, pady=2, sticky="n")

        VVIR_button = ctk.CTkRadioButton(pacemaker_modes_frame, text="VVIR", font=("Helvetica", 12),
                                         variable=self.pacemaker_mode_var, value="VVIR", command=self.init_VVIR)
        VVIR_button.grid(row=4, column=1, padx=5, pady=2, sticky="n")

        # Pacemaker parameters frame
        self.parameters_frame = ctk.CTkFrame(self.content_frame, fg_color="white", border_width=2, border_color="gray")
        self.parameters_frame.grid(row=9, column=0, rowspan=6, columnspan=2, padx=5, pady=10, sticky="nsew")

        for i in range(7):
            self.parameters_frame.grid_rowconfigure(i, weight=1)
        self.parameters_frame.grid_columnconfigure(0, weight=1)

        # Pacemaker parameters label
        parameters_label = ctk.CTkLabel(self.parameters_frame, text="Pacemaker Parameters", font=("Helvetica", 12))
        parameters_label.grid(row=0, column=0, padx=5, pady=5, sticky="n")

        # Entry boxes for parameters ##FIX FOR ALL MODES
        self.LRL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="LRL")
        self.LRL_entry.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        self.URL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="URL")
        self.URL_entry.grid(row=2, column=0, padx=5, pady=5, sticky="n")

        self.AtrAMP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrAMP")
        self.AtrAMP_entry.grid(row=3, column=0, padx=5, pady=5, sticky="n")

        self.AtrPW_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrPW")
        self.AtrPW_entry.grid(row=4, column=0, padx=5, pady=5, sticky="n")

        # Initially disabled save button
        self.save_button = ctk.CTkButton(self.parameters_frame, text="Save Parameters", command=self.save_parameters, state="disabled")
        self.save_button.grid(row=5, column=0, padx=5, pady=10, sticky="n")

        

        self.pacemaker_mode_var.trace_add("write", mode_selected)

        # Enable save button when pacemaker_mode_var is changed
        def mode_selected(*args):
            if self.pacemaker_mode_var.get():
                self.save_button.configure(state="normal")

        self.invalid_input_label = ctk.CTkLabel(self.parameters_frame, text="Invalid Input. Please enter numeric values.", font=("Helvetica", 12), text_color="red")
        self.valid_input_label = ctk.CTkLabel(self.parameters_frame, text="Parameters Saved!", font=("Helvetica", 12), text_color="green")

        # Electrogram graphs frame setup
        self.egraphs_frame = ctk.CTkFrame(self.content_frame, fg_color="white")
        self.egraphs_frame.grid(row=0, column=2, rowspan=15, columnspan=15, padx=5, pady=10, sticky="nsew")

        for i in range(16):
            self.egraphs_frame.grid_rowconfigure(i, weight=1)
        self.egraphs_frame.grid_columnconfigure(0, weight=1)

        # Electrogram labels
        egraphs_label = ctk.CTkLabel(self.egraphs_frame, text="Electrogram Plots", font=("Helvetica", 24))
        egraphs_label.grid(row=0, column=0, rowspan=1, padx=5, pady=5, sticky="n")

        ventricle_label = ctk.CTkLabel(self.egraphs_frame, text="Ventricle Electrogram", font=("Helvetica", 16))
        ventricle_label.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        atrial_label = ctk.CTkLabel(self.egraphs_frame, text="Atrial Electrogram", font=("Helvetica", 16))
        atrial_label.grid(row=8, column=0, padx=5, pady=5, sticky="n")

        # Call the functions for making the plots
        self.ventricular_electrogram()
        self.atrium_electrogram()
        self.doSerial()


    # Function for creating the change password page when the change PW button is clicked
    def change_password_page(self):

        # Delete/Hide previous frames (navbar and content)
        self.content_frame.pack_forget()
        self.content_frame.destroy()
        self.navbar_frame.pack_forget()
        self.navbar_frame.destroy()

        # Create the change password frame
        self.change_password_frame = ctk.CTkFrame(self)
        self.change_password_frame.pack(padx=20, pady=20)
        self.state("zoomed")

        # Import the custom logo from the assets folder, resize, and place in a TKlabel
        logo_original_image = Image.open("assets/Pacemaker logo.png")
        logo_resized_image = logo_original_image.resize((300, 200))
        self.logo_image = ImageTk.PhotoImage(
            logo_resized_image)

        logo_label = ctk.CTkLabel(
            self.change_password_frame,
            image=self.logo_image,
            text=""
        )
        logo_label.pack(pady=10)

        # Label and entry for inputting the username
        username_label = ctk.CTkLabel(self.change_password_frame, text="Enter username:")
        username_label.pack(pady=5)

        username = ctk.CTkEntry(self.change_password_frame, width=200)
        username.pack(pady=5)

        # Label and entry for inputting the password
        password_label = ctk.CTkLabel(self.change_password_frame, text="Enter new password:")
        password_label.pack(pady=5)

        newpassword = ctk.CTkEntry(self.change_password_frame, width=200)
        newpassword.pack(pady=5)

        # Message label for displaying status
        info_label = ctk.CTkLabel(self.change_password_frame, text = " ")
        info_label.pack(pady=10)

        # Button that invokes the change PW backend function
        # The Lambda expression ensures the command only activates after the button is clicked
        enter_info_button = ctk.CTkButton(self.change_password_frame, text="Change",
                                          command=lambda: self.enter_info(username.get(), newpassword.get(),
                                                                          info_label))

        enter_info_button.pack(pady=10)

        # Return to the pacemaker page button
        back_button = ctk.CTkButton(self.change_password_frame, text="Back", command=self.show_pacemaker_page)
        back_button.pack(pady=10)

    # Function for setting up the login page
    def show_login_page(self):
        # Clear existing frames (like the pacemaker page)
        for widget in self.winfo_children():
            widget.destroy()  # Destroy all child widgets in the main window

        self.init_login_page()

    # Function for setting up the PM page
    def show_pacemaker_page(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.init_pacemaker_page()

    # Backend function for creating Matplot charts

    # 1 -- ventricle electrogram
    def ventricular_electrogram(self):

        # Create a blank window for the animation
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_title("Ventricle Electrogram")
        ax.set_ylabel("Voltage (V)")
        ax.grid()

        # Initialize the line dataset and line width
        line, = ax.plot([], [], lw=2)

        # Set the limits of our graph
        ax.set_xlim(0, 5000)
        ax.set_ylim(-1.5, 5)

        # Animation function (i is the frame)
        def animate(i):

           
            n = np.arange(len(self.x))

            # Append the values to the previously empty x and y data sets
            line.set_ydata(self.x)
            line.set_xdata(n)
            return line,

        # Call the animation function and draw to the egraphs_frame
        ani = animation.FuncAnimation(fig, animate, frames=5000, interval=50, blit=True)
        canvas = FigureCanvasTkAgg(fig, master=self.egraphs_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=2, column=0, padx=5, pady=5, sticky="nsew")



    def atrium_electrogram(self):

        # Create a blank window for the animation
        fig, ax = plt.subplots(figsize=(12, 6))  # Adjust size as needed
        ax.set_title("Atrium Electrogram")
        ax.set_ylabel("Voltage (V)")
        ax.grid()

        # Initialize the line dataset and line width
        line, = ax.plot([], [], lw=3)

        # Set the limits of our graph
        ax.set_xlim(0, 5000)
        ax.set_ylim(-1.5, 5)

        # Animation function (i is the frame)
        def animate(i):

            n = np.arange(len(self.y))

            print(len(self.y))

            # Append the values to the previously empty x and y data sets
            line.set_ydata(self.y)
            line.set_xdata(n)
            return line,

        # Call the animation function and draw to the egraphs_frame
        ani = animation.FuncAnimation(fig, animate, frames=5000, interval=50, blit=True)
        canvas = FigureCanvasTkAgg(fig, master=self.egraphs_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=9, column=0, padx=5, pady=5, sticky="nsew")

    def doSerial(self):
        if self.newserial and self.newserial.is_open:
            nextByte = self.newserial.read(1)
            if int.from_bytes(nextByte) == 7:
                arr = bytearray(108)
                self.newserial.readinto(arr)
                read_atrData = struct.unpack('10f', arr[28:68])
                read_ventData = struct.unpack('10f', arr[68:108])

                for y_val in read_atrData:
                    self.y.append(y_val)
                for x_val in read_ventData:
                    self.x.append(x_val)
                self.y = self.y[-10000:]
                self.x = self.x[-10000:]
            else:
                self.newserial.reset_input_buffer()
                print('unexpected:')
                print(nextByte)
        self.after(ms= 20, func= self.doSerial)




    def connect_pm(self):
        """Attempts to connect to the pacemaker."""
        try:
            self.newserial = serial.Serial(
                port="COM6", 
                baudrate=115200, 
                timeout=10, 
                parity=serial.PARITY_NONE, 
                stopbits=serial.STOPBITS_ONE, 
                bytesize=serial.EIGHTBITS
            )
            self.update_connection_status()  # Update the label on successful connection
        except serial.SerialException as e:
            self.newserial = None
            print(f"Failed to connect: {e}")
            self.update_connection_status()

    def isConnected(self):
        """Returns the connection status as a string."""
        if self.newserial and self.newserial.is_open:
            return f"Pacemaker is connected on {self.newserial.port}"
        else:
            return "Pacemaker is not connected. Please check the connection."

    def update_connection_status(self):
        """Updates the connection status label."""
        status_text = self.isConnected()
        self.connection_status_label.configure(text=status_text)

    def disconnect_pm(self):
        """Attempts to disconnect from the pacemaker."""
        if self.newserial and self.newserial.is_open:
            self.newserial.close()
            status_text = "Disconnected from pacemaker."
        else:
            status_text = "No connection to disconnect."
        self.connection_status_label.configure(text=status_text)

# Add entry boxes for pacemaker values - save pacemaker values in users.txt
# Add confirm button for select pacemaker mode
# Consider the ranges for the programmable data


# Start the event loop
if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    window = Window()
    window.mainloop()