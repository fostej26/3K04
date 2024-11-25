import struct
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

from serial_transmission_remastered import *

from yarl import URL

def checkparams(Name, LRL, URL, AtrAMP, AtrPW, VenAMP, VenPW, ARP, VRP, ReactionTime, RecoveryTime, ResponseFactor, ActivityThreshold,MaxSensorRate):
    if Name == "AOO":
        if not (is_float(LRL) and 30 <= float(LRL) <= 175):
            return False
        if not (is_float(URL) and 50 <= float(URL) <= 175):
            return False
        if not (is_float(AtrAMP) and 0 <= float(AtrAMP) <= 5):
            return False
        if not (is_float(AtrPW) and 0.05 <= float(AtrPW) <= 1.9):
            return False
        return True
    
    if Name == "VOO":
        if not (is_float(LRL) and 30 <= float(LRL) <= 175):
            return False
        if not (is_float(URL) and 50 <= float(URL) <= 175):
            return False
        if not (is_float(VenAMP) and 0 <= float(VenAMP) <= 5):
            return False
        if not (is_float(VenPW) and 0.05 <= float(VenPW) <= 1.9):
            return False
        return True
    
    if Name == "AAI":
        if not (is_float(LRL) and 30 <= float(LRL) <= 175):
            return False
        if not (is_float(URL) and 50 <= float(URL) <= 175):
            return False
        if not (is_float(AtrAMP) and 0 <= float(AtrAMP) <= 5):
            return False
        if not (is_float(AtrPW) and 0.05 <= float(AtrPW) <= 1.9):
            return False
        if not (is_float(ARP) and 150 <= float(ARP) <= 500):
            return False
        return True
    
    if Name == "VVI":
        if not (is_float(LRL) and 30 <= float(LRL) <= 175):
            return False
        if not (is_float(URL) and 50 <= float(URL) <= 175):
            return False
        if not (is_float(VenAMP) and 0 <= float(VenAMP) <= 5):
            return False
        if not (is_float(VenPW) and 0.05 <= float(VenPW) <= 1.9):
            return False
        if not (is_float(VRP) and 150 <= float(VRP) <= 500):
            return False
        return True
    
    if Name == "AOOR":
        if not (is_float(LRL) and 30 <= float(LRL) <= 175):
            return False
        if not (is_float(URL) and 50 <= float(URL) <= 175):
            return False
        if not (is_float(AtrAMP) and 0 <= float(AtrAMP) <= 5):
            return False
        if not (is_float(AtrPW) and 0.05 <= float(AtrPW) <= 1.9):
            return False
        if not (is_float(ReactionTime) and 10 <= float(ReactionTime) <= 50):
            return False
        if not (is_float(RecoveryTime) and 2 <= float(RecoveryTime) <= 16):
            return False
        if not (is_float(ResponseFactor) and 1 <= float(ResponseFactor) <= 16):
            return False
        if not ActivityThreshold != "Activity Threshold":
            return False
        if not (is_float(MaxSensorRate) and 50 <= float(MaxSensorRate) <= 175):
            return False
        return True
    
    if Name == "VOOR":
        if not (is_float(LRL) and 30 <= float(LRL) <= 175):
            return False
        if not (is_float(URL) and 50 <= float(URL) <= 175):
            return False
        if not (is_float(VenAMP) and 0 <= float(VenAMP) <= 5):
            return False
        if not (is_float(VenPW) and 0.05 <= float(VenPW) <= 1.9):
            return False
        if not (is_float(ReactionTime) and 10 <= float(ReactionTime) <= 50):
            return False
        if not (is_float(RecoveryTime) and 2 <= float(RecoveryTime) <= 16):
            return False
        if not (is_float(ResponseFactor) and 1 <= float(ResponseFactor) <= 16):
            return False
        if not ActivityThreshold != "Activity Threshold":
            return False
        if not (is_float(MaxSensorRate) and 50 <= float(MaxSensorRate) <= 175):
            return False
        return True
    
    if Name == "AAIR":
        if not (is_float(LRL) and 30 <= float(LRL) <= 175):
            return False
        if not (is_float(URL) and 50 <= float(URL) <= 175):
            return False
        if not (is_float(AtrAMP) and 0 <= float(AtrAMP) <= 5):
            return False
        if not (is_float(AtrPW) and 0.05 <= float(AtrPW) <= 1.9):
            return False
        if not (is_float(ARP) and 150 <= float(ARP) <= 500):
            return False
        if not (is_float(ReactionTime) and 10 <= float(ReactionTime) <= 50):
            return False
        if not (is_float(RecoveryTime) and 2 <= float(RecoveryTime) <= 16):
            return False
        if not (is_float(ResponseFactor) and 1 <= float(ResponseFactor) <= 16):
            return False
        if not ActivityThreshold != "Activity Threshold":
            return False
        if not (is_float(MaxSensorRate) and 50 <= float(MaxSensorRate) <= 175):
            return False
        return True
    
    if Name == "VVIR":
        if not (is_float(LRL) and 30 <= float(LRL) <= 175):
            return False
        if not (is_float(URL) and 50 <= float(URL) <= 175):
            return False
        if not (is_float(VenAMP) and 0 <= float(VenAMP) <= 5):
            return False
        if not (is_float(VenPW) and 0.05 <= float(VenPW) <= 1.9):
            return False
        if not (is_float(VRP) and 150 <= float(VRP) <= 500):
            return False
        if not (is_float(ReactionTime) and 10 <= float(ReactionTime) <= 50):
            return False
        if not (is_float(RecoveryTime) and 2 <= float(RecoveryTime) <= 16):
            return False
        if not (is_float(ResponseFactor) and 1 <= float(ResponseFactor) <= 16):
            return False
        if not ActivityThreshold != "Activity Threshold":
            return False
        if not (is_float(MaxSensorRate) and 50 <= float(MaxSensorRate) <= 175):
            return False
        return True
    
    else:
        return False

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
        self.ARP = 0
        self.VRP = 0
        self.ReactionTime = 0
        self.RecoveryTime = 0
        self.ResponseFactor = 0
        self.ActivityThreshold = 0
        self.MaxSensorRate = 0

    def set_name(self, name):
        self.name = name

    def set_params(self, LRL, URL, AtrAMP, AtrPW, VenAMP, VenPW, ARP, VRP, ReactionTime, RecoveryTime, ResponseFactor, ActivityThreshold, MaxSensorRate):
        self.LRL = LRL
        self.URL = URL
        self.AtrAMP = AtrAMP
        self.AtrPW = AtrPW
        self.VenAMP = VenAMP
        self.VenPW = VenPW
        self.ARP = ARP
        self.VRP = VRP
        self.ReactionTime = ReactionTime
        self.RecoveryTime = RecoveryTime
        self.ResponseFactor = ResponseFactor
        self.ActivityThreshold = ActivityThreshold
        self.MaxSensorRate = MaxSensorRate


    def get_params(self):
        return self.LRL, self.URL, self.AtrAMP, self.AtrPW, self.VenAMP, self.VenPW, self.ARP, self.VRP, self.ReactionTime, self.RecoveryTime, self.ResponseFactor, self.ActivityThreshold, self.MaxSensorRate
        
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
            ARP=safe_get(getattr(self, 'ARP_entry', None)),
            VRP=safe_get(getattr(self, 'VRP_entry', None)),
            ReactionTime=safe_get(getattr(self, 'ReactionTime_entry', None)),
            RecoveryTime=safe_get(getattr(self, 'RecoveryTime_entry', None)),
            ResponseFactor=safe_get(getattr(self, 'ResponseFactor_entry', None)),
            ActivityThreshold=safe_get(getattr(self, 'ActivityThreshold_entry', None)),
            MaxSensorRate=safe_get(getattr(self, 'MaxSensorRate_entry', None))
        )

        if checkparams(self.mode.name, self.mode.LRL, self.mode.URL, self.mode.AtrAMP, self.mode.AtrPW, self.mode.VenAMP, self.mode.VenPW, self.mode.ARP, self.mode.VRP, self.mode.ReactionTime, self.mode.RecoveryTime, self.mode.ResponseFactor, self.mode.ActivityThreshold, self.mode.MaxSensorRate):
            self.invalid_input_label.grid_remove()
            self.valid_input_label.grid(row=6, column=0, padx=5, pady=5, sticky="n")
        else:
            self.valid_input_label.grid_remove()
            self.invalid_input_label.grid(row=6, column=0, padx=5, pady=5, sticky="n")
            return

        mode_num = 0
        if self.mode.name == 'AOO':
            mode_num = 1
        elif self.mode.name == 'VOO':
            mode_num = 2
        elif self.mode.name == 'AAI':
            mode_num = 3
        if self.mode.name == 'VVI':
            mode_num = 4
        elif self.mode.name == 'AOOR':
            mode_num = 5
        elif self.mode.name == 'VOOR':
            mode_num = 6
        if self.mode.name == 'AAIR':
            mode_num = 7
        elif self.mode.name == 'VVIR':
            mode_num = 8

        byte_0 = struct.pack('<B', 40)

        byte_1 = struct.pack('<B', mode_num)
        byte_2 = struct.pack('<B', 0 if (self.mode.LRL == '') else int(self.mode.LRL))
        byte_3 = struct.pack('<B', 0 if (self.mode.URL == '') else int(self.mode.URL))
        bytes4_7 = struct.pack('<f', 0 if (self.mode.AtrAMP == '') else float(self.mode.AtrAMP))
        bytes8_11 = struct.pack('<f', 0 if (self.mode.AtrPW == '') else float(self.mode.AtrPW))
        bytes12_15 = struct.pack('<f', 0 if (self.mode.VenAMP == '') else float(self.mode.VenAMP))
        bytes16_19 = struct.pack('<f', 0 if (self.mode.VenPW == '') else float(self.mode.VenPW))
        bytes20_21 = struct.pack('<H', 0 if (self.mode.VRP == '') else int(self.mode.VRP))
        bytes22_23 = struct.pack('<H', 0 if (self.mode.ARP == '') else int(self.mode.ARP))
        byte_24 = struct.pack('<B', 0 if (self.mode.MaxSensorRate == '') else int(self.mode.MaxSensorRate))
        byte_25 = struct.pack('<B', 0 if (self.mode.ReactionTime == '') else int(self.mode.ReactionTime))
        byte_26 = struct.pack('<B', 0 if (self.mode.ResponseFactor == '') else int(self.mode.ResponseFactor))
        byte_27 = struct.pack('<B', 0 if (self.mode.RecoveryTime == '') else int(self.mode.RecoveryTime))
        byte_28 = struct.pack('<B', 0 if (self.mode.ActivityThreshold == '') else int(self.activity_thresh_converter(self.mode.ActivityThreshold)))

        byte_arr = byte_0 + byte_1 + byte_2 + byte_3 + bytes4_7 + bytes8_11 + bytes12_15 + bytes16_19 + bytes20_21 + bytes22_23 + byte_24 + byte_25 + byte_26 + byte_27 + byte_28
        send_data(byte_arr)
        
        mode_data = {
            "name": self.mode.name,
            "LRL": self.mode.LRL,
            "URL": self.mode.URL,
            "AtrAMP": self.mode.AtrAMP,
            "AtrPW": self.mode.AtrPW,
            "VenAMP": self.mode.VenAMP,
            "VenPW": self.mode.VenPW,
            "ARP": self.mode.ARP,
            "VRP": self.mode.VRP,
            "ReactionTime": self.mode.ReactionTime,
            "RecoveryTime": self.mode.RecoveryTime,
            "ResponseFactor": self.mode.ResponseFactor,
            "ActivityThreshold": self.mode.ActivityThreshold,
            "MaxSensorRate": self.mode.MaxSensorRate
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
                for i, mode in enumerate(user["modes"]):
                    if mode["name"] == mode_name:
                        user["modes"][i] = mode_data
                        break
                else:
                    user["modes"].append(mode_data)
                break
        else:
            users.append({"username": username, "modes": [mode_data]})

        with open("parameters.json", "w") as f:
            json.dump(users, f, indent=4)

    def activity_thresh_converter(self, thresh):
        # "VL", "L", "ML", "M", "MH", "H", "VH"
        if thresh == 'VL':
            return 0
        elif thresh == 'L':
            return 1
        elif thresh == 'ML':
            return 2
        elif thresh == 'M':
            return 3
        elif thresh == 'MH':
            return 4
        elif thresh == 'H':
            return 5
        elif thresh == 'VH':
            return 6
        else:
            return 0


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
        self.LRL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="LRL (30-175ppm)")
        self.LRL_entry.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        self.URL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="URL (50-175ppm)")
        self.URL_entry.grid(row=2, column=0, padx=5, pady=5, sticky="n")

        self.AtrAMP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrAMP (0-5V)")
        self.AtrAMP_entry.grid(row=3, column=0, padx=5, pady=5, sticky="n")

        self.AtrPW_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrPW (0.05-1.9ms)")
        self.AtrPW_entry.grid(row=4, column=0, padx=5, pady=5, sticky="n")

        # Initially disabled save button
        self.save_button = ctk.CTkButton(self.parameters_frame, text="Save Parameters", command=self.save_parameters, state="enabled")
        self.save_button.grid(row=5, column=0, padx=5, pady=10, sticky="n")

        self.invalid_input_label = ctk.CTkLabel(self.parameters_frame, text="Invalid Input. Please enter values within the specified range.", font=("Helvetica", 12), text_color="red")
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
        self.LRL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="LRL (30-175ppm)")
        self.LRL_entry.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        self.URL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="URL (50-175ppm")
        self.URL_entry.grid(row=2, column=0, padx=5, pady=5, sticky="n")

        self.VenAMP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VenAMP (0-5V)")
        self.VenAMP_entry.grid(row=3, column=0, padx=5, pady=5, sticky="n")

        self.VenPW_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VenPW (0.05-1.9ms)")
        self.VenPW_entry.grid(row=4, column=0, padx=5, pady=5, sticky="n")

        # Initially disabled save button
        self.save_button = ctk.CTkButton(self.parameters_frame, text="Save Parameters", command=self.save_parameters, state="enabled")
        self.save_button.grid(row=5, column=0, padx=5, pady=10, sticky="n")

        self.invalid_input_label = ctk.CTkLabel(self.parameters_frame, text="Invalid Input. Please enter values within the specified range.", font=("Helvetica", 12), text_color="red")
        self.valid_input_label = ctk.CTkLabel(self.parameters_frame, text="Parameters Saved!", font=("Helvetica", 12), text_color="green")

    def init_AAI(self):
        for widget in self.parameters_frame.winfo_children():
            widget.destroy()
        for i in range(9):
            self.parameters_frame.grid_rowconfigure(i, weight=1)
        self.parameters_frame.grid_columnconfigure(0, weight=1)

        # Pacemaker parameters label
        parameters_label = ctk.CTkLabel(self.parameters_frame, text="Pacemaker Parameters", font=("Helvetica", 12))
        parameters_label.grid(row=0, column=0, padx=5, pady=5, sticky="n")

        # Entry boxes for parameters ##FIX FOR ALL MODES
        self.LRL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="LRL (30-175ppm)")
        self.LRL_entry.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        self.URL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="URL (50-175ppm)")
        self.URL_entry.grid(row=2, column=0, padx=5, pady=5, sticky="n")

        self.AtrAMP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrAMP (0-5V)")
        self.AtrAMP_entry.grid(row=3, column=0, padx=5, pady=5, sticky="n")

        self.AtrPW_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrPW (0.05-1.9ms)")
        self.AtrPW_entry.grid(row=4, column=0, padx=5, pady=5, sticky="n")

        self.ARP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="ARP (150-500ms)")
        self.ARP_entry.grid(row=5, column=0, padx=5, pady=5, sticky="n")

        # Initially disabled save button
        self.save_button = ctk.CTkButton(self.parameters_frame, text="Save Parameters", command=self.save_parameters, state="enabled")
        self.save_button.grid(row=6, column=0, padx=5, pady=10, sticky="n")

        self.invalid_input_label = ctk.CTkLabel(self.parameters_frame, text="Invalid Input. Please enter values within the specified range.", font=("Helvetica", 12), text_color="red")
        self.valid_input_label = ctk.CTkLabel(self.parameters_frame, text="Parameters Saved!", font=("Helvetica", 12), text_color="green")
    
    def init_VVI(self):
        for widget in self.parameters_frame.winfo_children():
            widget.destroy()
        for i in range(9):
            self.parameters_frame.grid_rowconfigure(i, weight=1)
        self.parameters_frame.grid_columnconfigure(0, weight=1)

        # Pacemaker parameters label
        parameters_label = ctk.CTkLabel(self.parameters_frame, text="Pacemaker Parameters", font=("Helvetica", 12))
        parameters_label.grid(row=0, column=0, padx=5, pady=5, sticky="n")

        # Entry boxes for parameters ##FIX FOR ALL MODES
        self.LRL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="LRL (30-175ppm)")
        self.LRL_entry.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        self.URL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="URL (50-175ppm)")
        self.URL_entry.grid(row=2, column=0, padx=5, pady=5, sticky="n")

        self.VenAMP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VenAMP (0-5V)")
        self.VenAMP_entry.grid(row=3, column=0, padx=5, pady=5, sticky="n")

        self.VenPW_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VenPW (0.05-1.9ms)")
        self.VenPW_entry.grid(row=4, column=0, padx=5, pady=5, sticky="n")

        self.VRP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VRP (150-500ms)")
        self.VRP_entry.grid(row=6, column=0, padx=5, pady=5, sticky="n")

        # Initially disabled save button
        self.save_button = ctk.CTkButton(self.parameters_frame, text="Save Parameters", command=self.save_parameters, state="enabled")
        self.save_button.grid(row=7, column=0, padx=5, pady=10, sticky="n")

        self.invalid_input_label = ctk.CTkLabel(self.parameters_frame, text="Invalid Input. Please enter values within the specified range.", font=("Helvetica", 12), text_color="red")
        self.valid_input_label = ctk.CTkLabel(self.parameters_frame, text="Parameters Saved!", font=("Helvetica", 12), text_color="green")

    def init_AOOR(self):
        for widget in self.parameters_frame.winfo_children():
            widget.destroy()
        for i in range(7):
            self.parameters_frame.grid_rowconfigure(i, weight=1)
        for j in range(2):
            self.parameters_frame.grid_columnconfigure(j, weight=1)

        # Pacemaker parameters label
        parameters_label = ctk.CTkLabel(self.parameters_frame, text="Pacemaker Parameters", font=("Helvetica", 12))
        parameters_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Entry boxes for parameters
        self.LRL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="LRL (30-175ppm)")
        self.LRL_entry.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        self.URL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="URL (50-175ppm)")
        self.URL_entry.grid(row=1, column=1, padx=5, pady=5, sticky="n")

        self.AtrAMP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrAMP (0-5V)")
        self.AtrAMP_entry.grid(row=2, column=0, padx=5, pady=5, sticky="n")

        self.AtrPW_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrPW (0.05-1.9ms)")
        self.AtrPW_entry.grid(row=2, column=1, padx=5, pady=5, sticky="n")

        self.ReactionTime_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Reaction Time (10-50s)")
        self.ReactionTime_entry.grid(row=3, column=0, padx=5, pady=5, sticky="n")

        self.RecoveryTime_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Recovery Time (2-16mins)")
        self.RecoveryTime_entry.grid(row=3, column=1, padx=5, pady=5, sticky="n")

        self.ResponseFactor_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Response Factor (1-16)")
        self.ResponseFactor_entry.grid(row=4, column=0, padx=5, pady=5, sticky="n")

        self.ActivityThreshold_var = ctk.StringVar(value="Activity Threshold")  # Default value
        self.ActivityThreshold_entry = ctk.CTkOptionMenu(self.parameters_frame, variable=self.ActivityThreshold_var, values=["VL", "L", "ML", "M", "MH", "H", "VH"], fg_color="white", text_color="gray")
        self.ActivityThreshold_entry.grid(row=5, column=0,columnspan=2, padx=5, pady=5, sticky="n")

        self.MaxSensorRate_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Max Sensor Rate (50-175ppm)")
        self.MaxSensorRate_entry.grid(row=4, column=1, padx=5, pady=5, sticky="n")

        # Initially enabled save button
        self.save_button = ctk.CTkButton(self.parameters_frame, text="Save Parameters", command=self.save_parameters, state="enabled")
        self.save_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10, sticky="n")

        self.invalid_input_label = ctk.CTkLabel(self.parameters_frame, text="Invalid Input. Please enter values within the specified range.", font=("Helvetica", 12), text_color="red")
        self.valid_input_label = ctk.CTkLabel(self.parameters_frame, text="Parameters Saved!", font=("Helvetica", 12), text_color="green")

    def init_VOOR(self):
        for widget in self.parameters_frame.winfo_children():
            widget.destroy()
        for i in range(7):
            self.parameters_frame.grid_rowconfigure(i, weight=1)
        for j in range(2):
            self.parameters_frame.grid_columnconfigure(j, weight=1)

        # Pacemaker parameters label
        parameters_label = ctk.CTkLabel(self.parameters_frame, text="Pacemaker Parameters", font=("Helvetica", 12))
        parameters_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Entry boxes for parameters
        self.LRL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="LRL (30-175ppm)")
        self.LRL_entry.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        self.URL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="URL (50-175ppm")
        self.URL_entry.grid(row=1, column=1, padx=5, pady=5, sticky="n")

        self.VenAMP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VenAMP (0-5V)")
        self.VenAMP_entry.grid(row=2, column=0, padx=5, pady=5, sticky="n")

        self.VenPW_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VenPW (0.05-1.9ms)")
        self.VenPW_entry.grid(row=2, column=1, padx=5, pady=5, sticky="n")

        self.ReactionTime_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Reaction Time (10-50s)")
        self.ReactionTime_entry.grid(row=3, column=0, padx=5, pady=5, sticky="n")

        self.RecoveryTime_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Recovery Time (2-16mins)")
        self.RecoveryTime_entry.grid(row=3, column=1, padx=5, pady=5, sticky="n")

        self.ResponseFactor_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Response Factor (1-16)")
        self.ResponseFactor_entry.grid(row=4, column=0, padx=5, pady=5, sticky="n")

        self.ActivityThreshold_var = ctk.StringVar(value="Activity Threshold")  # Default value
        self.ActivityThreshold_entry = ctk.CTkOptionMenu(self.parameters_frame, variable=self.ActivityThreshold_var, values=["VL", "L", "ML", "M", "MH", "H", "VH"], fg_color="white", text_color="gray")
        self.ActivityThreshold_entry.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="n")

        self.MaxSensorRate_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Max Sensor Rate (50-175ppm)")
        self.MaxSensorRate_entry.grid(row=4, column=1, padx=5, pady=5, sticky="n")

        # Initially enabled save button
        self.save_button = ctk.CTkButton(self.parameters_frame, text="Save Parameters", command=self.save_parameters, state="enabled")
        self.save_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10, sticky="n")

        self.invalid_input_label = ctk.CTkLabel(self.parameters_frame, text="Invalid Input. Please enter values within the specified range.", font=("Helvetica", 12), text_color="red")
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
        self.LRL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="LRL (30-175ppm)")
        self.LRL_entry.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        self.URL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="URL (50-175ppm)")
        self.URL_entry.grid(row=1, column=1, padx=5, pady=5, sticky="n")

        self.AtrAMP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrAMP (0-5V)")
        self.AtrAMP_entry.grid(row=2, column=0, padx=5, pady=5, sticky="n")

        self.AtrPW_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrPW (0.05-1.9ms)")
        self.AtrPW_entry.grid(row=2, column=1, padx=5, pady=5, sticky="n")


        self.ARP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="ARP (150-500ms)")
        self.ARP_entry.grid(row=3, column=0, padx=5, pady=5, sticky="n")


        self.ReactionTime_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Reaction Time (10-50s)")
        self.ReactionTime_entry.grid(row=3, column=1, padx=5, pady=5, sticky="n")

        self.RecoveryTime_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Recovery Time (2-16mins)")
        self.RecoveryTime_entry.grid(row=4, column=0, padx=5, pady=5, sticky="n")

        self.ResponseFactor_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Response Factor (1-16)")
        self.ResponseFactor_entry.grid(row=4, column=1, padx=5, pady=5, sticky="n")

        self.ActivityThreshold_var = ctk.StringVar(value="Activity Threshold")  # Default value
        self.ActivityThreshold_entry = ctk.CTkOptionMenu(self.parameters_frame, variable=self.ActivityThreshold_var, values=["VL", "L", "ML", "M", "MH", "H", "VH"], fg_color="white", text_color="gray")
        self.ActivityThreshold_entry.grid(row=5, column=0,padx=5, pady=5, sticky="n")

        self.MaxSensorRate_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Max Sensor Rate (50-175ppm)")
        self.MaxSensorRate_entry.grid(row=5, column=1, padx=5, pady=5, sticky="n")

        # Initially enabled save button
        self.save_button = ctk.CTkButton(self.parameters_frame, text="Save Parameters", command=self.save_parameters, state="enabled")
        self.save_button.grid(row=7, column=0, columnspan=2, padx=5, pady=10, sticky="n")

        self.invalid_input_label = ctk.CTkLabel(self.parameters_frame, text="Invalid Input. Please enter values within the specified range.", font=("Helvetica", 12), text_color="red")
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
        self.LRL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="LRL (30-175ppm)")
        self.LRL_entry.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        self.URL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="URL (50-175ppm)")
        self.URL_entry.grid(row=1, column=1, padx=5, pady=5, sticky="n")

        self.VenAMP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VenAMP (0-5V)")
        self.VenAMP_entry.grid(row=2, column=0, padx=5, pady=5, sticky="n")

        self.VenPW_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VenPW (0.05-1.9ms)")
        self.VenPW_entry.grid(row=2, column=1, padx=5, pady=5, sticky="n")


        self.VRP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="VRP (150-500ms)")
        self.VRP_entry.grid(row=3, column=0, padx=5, pady=5, sticky="n")

        self.ReactionTime_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Reaction Time (10-50s)")
        self.ReactionTime_entry.grid(row=3, column=1, padx=5, pady=5, sticky="n")

        self.RecoveryTime_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Recovery Time (2-16mins)")
        self.RecoveryTime_entry.grid(row=4, column=0, padx=5, pady=5, sticky="n")

        self.ResponseFactor_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Response Factor (1-16)")
        self.ResponseFactor_entry.grid(row=4, column=1, padx=5, pady=5, sticky="n")

        self.ActivityThreshold_var = ctk.StringVar(value="Activity Threshold")  # Default value
        self.ActivityThreshold_entry = ctk.CTkOptionMenu(self.parameters_frame, variable=self.ActivityThreshold_var, values=["VL", "L", "ML", "M", "MH", "H", "VH"], fg_color="white", text_color="gray")
        self.ActivityThreshold_entry.grid(row=5, column=0, padx=5, pady=5, sticky="n")

        self.MaxSensorRate_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="Max Sensor Rate (50-175ppm)")
        self.MaxSensorRate_entry.grid(row=5, column=1, padx=5, pady=5, sticky="n")

        # Initially enabled save button
        self.save_button = ctk.CTkButton(self.parameters_frame, text="Save Parameters", command=self.save_parameters, state="enabled")
        self.save_button.grid(row=7, column=0, columnspan=2, padx=5, pady=10, sticky="n")

        self.invalid_input_label = ctk.CTkLabel(self.parameters_frame, text="Invalid Input. Please enter values within the specified range.", font=("Helvetica", 12), text_color="red")
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
        self.LRL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="LRL (select a mode)")
        self.LRL_entry.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        self.URL_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="URL (select a mode)")
        self.URL_entry.grid(row=2, column=0, padx=5, pady=5, sticky="n")

        self.AtrAMP_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrAMP (select a mode)")
        self.AtrAMP_entry.grid(row=3, column=0, padx=5, pady=5, sticky="n")

        self.AtrPW_entry = ctk.CTkEntry(self.parameters_frame, placeholder_text="AtrPW (select a mode)")
        self.AtrPW_entry.grid(row=4, column=0, padx=5, pady=5, sticky="n")

        # Initially disabled save button
        self.save_button = ctk.CTkButton(self.parameters_frame, text="Save Parameters", command=self.save_parameters, state="disabled")
        self.save_button.grid(row=5, column=0, padx=5, pady=10, sticky="n")

        

        self.pacemaker_mode_var.trace_add("write", mode_selected)

        # Enable save button when pacemaker_mode_var is changed
        def mode_selected(*args):
            if self.pacemaker_mode_var.get():
                self.save_button.configure(state="normal")

        self.invalid_input_label = ctk.CTkLabel(self.parameters_frame, text="Invalid Input. Please enter values within the specified range.", font=("Helvetica", 12), text_color="red")
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
        ax.set_xlim(-10000, 0)
        ax.set_ylim(-1, 1)

        # Animation function (i is the frame)
        def animate(i):
            
            _, vent_data = get_atr_vent_graphing_data()
           
            n = np.arange(-2*len(vent_data), 0, 2)

            # Append the values to the previously empty x and y data sets
            line.set_ydata(vent_data)
            line.set_xdata(n)
            return line,

        # Call the animation function and draw to the egraphs_frame
        ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)
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
        ax.set_ylim(-1, 1)
        ax.set_xlim(-10000, 0)

        # Animation function (i is the frame)
        def animate(i):

            atr_data, _ = get_atr_vent_graphing_data()

            n = np.arange(-2*len(atr_data), 0, 2)

            # Append the values to the previously empty x and y data sets
            line.set_ydata(atr_data)
            line.set_xdata(n)

            return line,

        # Call the animation function and draw to the egraphs_frame
        ani = animation.FuncAnimation(fig, animate, frames=1000, interval=50, blit=True)
        canvas = FigureCanvasTkAgg(fig, master=self.egraphs_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=9, column=0, padx=5, pady=5, sticky="nsew")

    def check_serial(self):
        check_serial_port()
        self.after(ms= 20, func= self.check_serial)

    def connect_pm(self):
        """Attempts to connect to the pacemaker."""
        try:
            connect_serial_port()
            self.update_connection_status()  # Update the label on successful connection
            self.after(ms= 20, func= self.check_serial)
        except serial.SerialException as e:
            self.newserial = None
            print(f"Failed to connect: {e}")
            self.update_connection_status()

    def isConnected(self):
        """Returns the connection status as a string."""
        if connection_status():
            return f"Pacemaker is connected on {get_port()}"
        else:
            return "Pacemaker is not connected. Please check the connection."

    def update_connection_status(self):
        """Updates the connection status label."""
        status_text = self.isConnected()
        self.connection_status_label.configure(text=status_text)

    def disconnect_pm(self):
        """Attempts to disconnect from the pacemaker."""
        if connection_status():
            close_serial()
            status_text = "Disconnected from pacemaker."
        else:
            status_text = "No connection to disconnect."
        self.connection_status_label.configure(text=status_text)


# def save_parameters(self):
#     try:
#         # Retrieve and validate inputs
#         lrl = int(self.LRL_entry.get())
#         url = int(self.URL_entry.get())
#         atr_amp = float(self.AtrAMP_entry.get())
#         atr_pw = float(self.AtrPW_entry.get())

#         # Add validation logic for ranges (example ranges; replace with actual device specs)
#         if not (30 <= lrl <= 175):
#             raise ValueError("LRL must be between 30 and 175.")
#         if not (50 <= url <= 175):
#             raise ValueError("URL must be between 50 and 175.")
#         if not (0.0 <= atr_amp <= 5.0):
#             raise ValueError("Atrial Amplitude must be between 0.0 and 5.0 volts.")
#         if not (0.05 <= atr_pw <= 1.9):
#             raise ValueError("Atrial Pulse Width must be between 0.05 and 1.9 ms.")

#         # Construct a bytearray or other data structure
#         params = bytearray(20)  # Example size; adjust based on your data structure
#         params[0:1] = lrl.to_bytes(1, 'little')  # Example for LRL
#         params[1:2] = url.to_bytes(1, 'little')  # Example for URL
#         struct.pack_into('f', params, 2, atr_amp)  # Example for atr_amp
#         struct.pack_into('f', params, 6, atr_pw)  # Example for atr_pw

#         # Call the send_data() function
#         send_data(params)

#     except ValueError as ve:
#         # ctk error handling msg here
#         pass
#     except Exception as e:
#         # ctk error handling msg here

#         pass


# Add entry boxes for pacemaker values - save pacemaker values in users.txt
# Add confirm button for select pacemaker mode
# Consider the ranges for the programmable data


# Start the event loop
if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    window = Window()
    window.mainloop()