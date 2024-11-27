import struct
import json
import os
import serial

port = serial.Serial()
# Serial port setup
def connect_serial_port():
    try:
        port.baudrate = 115200
        port.port = 'COM5'
        port.timeout = 10

        port.open()
    except serial.SerialException as e:
        return e
    
def connection_status():
    return port.is_open

def get_port():
    return port.port

def close_serial():
    port.close()
    global counter
    counter = 0

def get_current_serial_counter():
    return counter
    
data_counts = 0
arr = 0

counter =  0
atr_graphing_data = []
vent_graphing_data = []

# Load valid usernames from users.txt
# def load_users(file_name='users.txt'):
#     if not os.path.exists(file_name):
#         print(f"Error: {file_name} does not exist.")
#         return []
#     with open(file_name, 'r') as file:
#         return [line.strip() for line in file.readlines()]

# Write parameters to JSON under the given username
# def write_to_json(username, params_dict, file_name='parameters.json'):
#     if not os.path.exists(file_name):
#         with open(file_name, 'w') as file:
#             json.dump({}, file)

#     with open(file_name, 'r+') as file:
#         data = json.load(file)
#         if username not in data:
#             data[username] = []
#         data[username].append(params_dict)
#         file.seek(0)
#         json.dump(data, file, indent=4)

# Class to store parameters
class Params:
    def __init__(self, data):
        self.name = data[0]
        if self.name == 1:
            self.name = 'AOO'
        elif self.name == 2:
            self.name = 'VOO'
        elif self.name == 3:
            self.name = 'AAI'
        elif self.name == 4:
            self.name = 'VVI'
        elif self.name == 5:
            self.name = 'AOOR'
        elif self.name == 6:
            self.name = 'VOOR'
        elif self.name == 7:
            self.name = 'AAIR'
        elif self.name == 8:
            self.name = 'VVIR'
        else:
            self.name = 'Unknown'

        self.LRL = str(data[1])
        self.URL = str(data[2])
        self.AtrAMP = str(struct.unpack('f', data[3:7])[0])
        self.AtrPW = str(struct.unpack('f', data[7:11])[0])
        self.VenAMP = str(struct.unpack('f', data[11:15])[0])
        self.VenPW = str(struct.unpack('f', data[15:19])[0])
        self.ARP = str(struct.unpack('H', data[21:23])[0])
        self.VRP = str(struct.unpack('H', data[19:21])[0])
        self.ReactionTime = str(data[24])
        self.RecoveryTime = str(data[26])
        self.ResponseFactor = str(data[25])
        self.ActivityThreshold = data[27]

        if self.ActivityThreshold == 0:
            self.ActivityThreshold = 'VL'
        elif self.ActivityThreshold == 1:
            self.ActivityThreshold = 'L'
        elif self.ActivityThreshold == 2:
            self.ActivityThreshold = 'ML'
        elif self.ActivityThreshold == 3:
            self.ActivityThreshold = 'M'
        elif self.ActivityThreshold == 4:
            self.ActivityThreshold = 'MH'
        elif self.ActivityThreshold == 5:
            self.ActivityThreshold = 'H'
        elif self.ActivityThreshold == 6:
            self.ActivityThreshold = 'VH'

        self.MaxSensorRate = str(data[23])

    def to_dict(self):

        return self.__dict__
    

def get_atr_vent_graphing_data():
    return atr_graphing_data, vent_graphing_data


def send_data(data):
    """Function to send data over serial."""
    if port.is_open:
        # Convert data to bytes and send
        port.write(data)
        print(f"Sent data: {data}")
    else:
        print("Port is not open, cannot send data.")

def verify_data(current_username, current_mode, data, file_name='parameters.json'):
    """Function to verify data against stored parameters for the current user and mode."""
    print(f"Verifying data for user: {current_username}, mode: {current_mode}")
    # Load the stored parameters
    with open(file_name, 'r') as file:
        stored_data = json.load(file)
    
    # Ensure stored_data is a list
    if not isinstance(stored_data, list):
        print("Error: Stored data is not a list.")
        return False
    
    # Find the data for the current user
    user_data = next((ud for ud in stored_data if ud.get("username") == current_username), None)
    if not user_data:
        print(f"No data found for user: {current_username}")
        return False
    
    # Find the parameters for the current mode
    mode_params = next((mode for mode in user_data.get("modes", []) if mode.get("name") == current_mode), None)
    if not mode_params:
        print(f"No parameters found for mode: {current_mode}")
        return False
    
    # Compare each parameter
    for key, param_value in mode_params.items():
        if key in data:
            data_value = data[key]
            try:
                param_value = float(param_value)
                data_value = float(data_value)
                if abs(param_value - data_value) / param_value > 0.05:
                    print(f"Mismatch in {key}: {param_value} vs {data_value}")
                    return False
            except ValueError:
                if param_value != data_value:
                    print(f"Mismatch in {key}: {param_value} vs {data_value}")
                    return False
        else:
            print(f"Missing key in data: {key}")
            return False
    
    print("Data matches stored parameters for the current user and mode.")
    return True


# Prompt for username
# users = load_users()
# if not users:
#     print("No valid users found. Exiting.")
#     exit()

# username = input("Enter your username: ").strip()
# if username not in users:
#     print("Invalid username. Exiting.")
#     exit()

# Main data processing loop
def check_serial_port(username,mode):
    if port.is_open:
        first_byte = port.read(1)
        if len(first_byte) == 1 and int.from_bytes(first_byte, byteorder='big') == 7:
            arr = bytearray(108)
            port.readinto(arr)

            # Parse the byte array into parameters
            params = Params(arr)
            print(verify_data(username,mode, params.to_dict(), 'parameters.json'))
            # Save the parameters under the given username
            # write_to_json(username, params.to_dict())
            
            global atr_graphing_data
            global vent_graphing_data

            atr_data = struct.unpack('10f', arr[28:68])
            vent_data = struct.unpack('10f', arr[68:108])

            for atr_item in atr_data:
                atr_graphing_data.append(atr_item)

            for vent_item in vent_data:
                vent_graphing_data.append(vent_item)

            atr_graphing_data = atr_graphing_data[-5000:]
            vent_graphing_data = vent_graphing_data[-5000:]

        else:
            port.reset_input_buffer()
            print('Unexpected message format: flushing input and resetting')