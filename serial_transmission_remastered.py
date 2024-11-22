import struct
import json
import os
import serial

# Serial port setup
port = serial.Serial()
port.baudrate = 115200
port.port = 'COM3'
port.timeout = 10

port.open()
print(port.is_open)

flag = True
data_counts = 0
arr = 0

# Load valid usernames from users.txt
# def load_users(file_name='users.txt'):
#     if not os.path.exists(file_name):
#         print(f"Error: {file_name} does not exist.")
#         return []
#     with open(file_name, 'r') as file:
#         return [line.strip() for line in file.readlines()]

# Write parameters to JSON under the given username
def write_to_json(username, params_dict, file_name='parameters.json'):
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            json.dump({}, file)

    with open(file_name, 'r+') as file:
        data = json.load(file)
        if username not in data:
            data[username] = []
        data[username].append(params_dict)
        file.seek(0)
        json.dump(data, file, indent=4)

# Class to store parameters
class Params:
    def __init__(self, data):
        self.sync_byte = data[0]
        self.mode = data[1]
        self.lrl = data[2]
        self.url = data[3]
        self.atr_pulse_amplitude = struct.unpack('f', data[4:8])
        self.atr_pulse_width = struct.unpack('f', data[8:12])
        self.atrial_sensitivity = struct.unpack('H', data[12:14])
        self.vent_pulse_amplitude = struct.unpack('f', data[14:18])
        self.vent_pulse_width = struct.unpack('f', data[18:22])
        self.ventricle_sensitivity = struct.unpack('H', data[22:24])
        self.vrp = struct.unpack('H', data[24:26])
        self.arp = struct.unpack('H', data[26:28])
        self.fix_av_delay = struct.unpack('H', data[28:30])
        self.max_sensor_rate = data[30]
        self.reaction_time = data[31]
        self.response_time = data[32]
        self.response_factor = data[33]
        self.recovery_time = data[34]
        self.activity_threshold = data[35]
        self.atrial_data = list(struct.unpack('10f', data[36:77]))
        self.ventricle_data = list(struct.unpack('10f', data[77:138]))

    def to_dict(self):
        return self.__dict__

# Prompt for username
users = load_users()
if not users:
    print("No valid users found. Exiting.")
    exit()

username = input("Enter your username: ").strip()
if username not in users:
    print("Invalid username. Exiting.")
    exit()

# Main data processing loop
while flag:
    first_byte = port.read(1)
    if len(first_byte) == 1 and int.from_bytes(first_byte, byteorder='big') == 1:
        second_byte = port.read(1)
        if len(second_byte) == 1 and int.from_bytes(second_byte, byteorder='big') == 1:
            arr = bytearray(137)
            port.readinto(arr)

            # Parse the byte array into parameters
            params = Params(arr)

            # Save the parameters under the given username
            write_to_json(username, params.to_dict())
        else:
            port.reset_input_buffer()
            print('Unexpected message format: flushing input and resetting')
    else:
        port.reset_input_buffer()
        print('Unexpected message format: flushing input and resetting')

    data_counts += 1