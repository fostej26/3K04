import struct
import json
import os
import serial

port = serial.Serial()
# Serial port setup
def connect_serial_port():
    try:
        port.baudrate = 115200
        port.port = 'COM6'
        port.timeout = 10

        port.open()
        print(port.is_open)
    except serial.SerialException as e:
        return e
    
data_counts = 0
arr = 0

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
        self.mode = data[0]
        self.lrl = data[1]
        self.url = data[2]
        self.atr_pulse_amplitude = struct.unpack('f', data[3:7])
        self.atr_pulse_width = struct.unpack('f', data[7:11])
        self.vent_pulse_amplitude = struct.unpack('f', data[11:15])
        self.vent_pulse_width = struct.unpack('f', data[15:19])
        self.vrp = struct.unpack('H', data[19:21])
        self.arp = struct.unpack('H', data[21:23])
        self.max_sensor_rate = data[23]
        self.reaction_time = data[24]
        self.response_factor = data[25]
        self.recovery_time = data[26]
        self.activity_threshold = data[27]
        self.atrial_data = list(struct.unpack('10f', data[28:68]))
        self.ventricle_data = list(struct.unpack('10f', data[68:108]))

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
def check_serial_port():
    if port.is_open:
        first_byte = port.read(1)
        if len(first_byte) == 1 and int.from_bytes(first_byte, byteorder='big') == 7:
            arr = bytearray(108)
            port.readinto(arr)

            # Parse the byte array into parameters
            params = Params(arr)

            # Save the parameters under the given username
            # write_to_json(username, params.to_dict())

            atr_data = struct.unpack('10f', arr[28:68])
            vent_data = struct.unpack('10f', arr[68:108])

            for atr_item in atr_data:
                atr_graphing_data.append(atr_item)

            for vent_item in vent_data:
                vent_graphing_data.append(vent_item)

            atr_data = atr_data[-10000:]
            vent_data = vent_data[-10000:]

        else:
            port.reset_input_buffer()
            print('Unexpected message format: flushing input and resetting')