import serial
import struct

port = serial.Serial()

port.baudrate = 115200
port.port = 'COM4'
port.timeout = 10

port.open()

print(port.is_open)

flag = True
data_counts = 0

arr = 0

def output_data(array, count):
    for i in range(0, len(array)):
        print(f'Count: {count}, Byte #: {i}, Value: {array[i]}')



#def send_params_to_pacemaker()

# class Params:
#     def __init__(self, pacing_mode, lower_rate_limit, upper_rate_limit, atrial_amplitude, atrial_pulse_width,
#                      atrial_sensitivity, ventricular_amplitude, ventricular_pulse_width, ventricular_sensitivity,
#                      vrp, arp, fixed_av_delay, maximum_sensor_rate, reaction_time, response_factor,
#                      recovery_time, activity_threshold):
#             self.pacing_mode = pacing_mode
#             self.lower_rate_limit = lower_rate_limit
#             self.upper_rate_limit = upper_rate_limit
#             self.atrial_amplitude = atrial_amplitude
#             self.atrial_pulse_width = atrial_pulse_width
#             self.atrial_sensitivity = atrial_sensitivity
#             self.ventricular_amplitude = ventricular_amplitude
#             self.ventricular_pulse_width = ventricular_pulse_width
#             self.ventricular_sensitivity = ventricular_sensitivity
#             self.vrp = vrp
#             self.arp = arp
#             self.fixed_av_delay = fixed_av_delay
#             self.maximum_sensor_rate = maximum_sensor_rate
#             self.reaction_time = reaction_time
#             self.response_factor = response_factor
#             self.recovery_time = recovery_time
#             self.activity_threshold = activity_threshold


# class SerialPacket:
#     # map serial packet data in here creating a params obj in the init

#     pass
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
        #self.atrial_data = list(struct.unpack('10f', data[36:77]))
        #self.ventricle_data = list(struct.unpack('10f', data[77:138]))



while flag:
    first_byte = port.read(1)
    if len(first_byte) == 1 and int.from_bytes(first_byte, byteorder='big') == 1:
        arr = bytearray(137)
        port.readinto(arr)

        # Parse the byte array into parameters
        params = Params(arr)

        # Save the parameters under the given username
        output_data(arr, data_counts)
    else:
        port.reset_input_buffer()
        print('Unexpected message format: flushing input and resetting')

    data_counts += 1

        