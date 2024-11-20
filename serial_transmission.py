import serial

port = serial.Serial()

port.baudrate = 115200
port.port = 'COM6'
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

class Params:
    def __init__(self, pacing_mode, lower_rate_limit, upper_rate_limit, atrial_amplitude, atrial_pulse_width,
                     atrial_sensitivity, ventricular_amplitude, ventricular_pulse_width, ventricular_sensitivity,
                     vrp, arp, fixed_av_delay, maximum_sensor_rate, reaction_time, response_factor,
                     recovery_time, activity_threshold):
            self.pacing_mode = pacing_mode
            self.lower_rate_limit = lower_rate_limit
            self.upper_rate_limit = upper_rate_limit
            self.atrial_amplitude = atrial_amplitude
            self.atrial_pulse_width = atrial_pulse_width
            self.atrial_sensitivity = atrial_sensitivity
            self.ventricular_amplitude = ventricular_amplitude
            self.ventricular_pulse_width = ventricular_pulse_width
            self.ventricular_sensitivity = ventricular_sensitivity
            self.vrp = vrp
            self.arp = arp
            self.fixed_av_delay = fixed_av_delay
            self.maximum_sensor_rate = maximum_sensor_rate
            self.reaction_time = reaction_time
            self.response_factor = response_factor
            self.recovery_time = recovery_time
            self.activity_threshold = activity_threshold


class SerialPacket:
    # map serial packet data in here creating a params obj in the init

    pass




while flag:
    first_byte = port.read(1)
    # Check that first "sync" byte is correct
    if int.from_bytes(first_byte) == 1:
        second_byte = port.read(1)

        # Check what type of message is being recieved, read proper amount of bytes accordingly
        if int.from_bytes(second_byte) == 1:
            arr = bytearray(102)
            port.readinto(arr)
            output_data(arr, data_counts)

        # Other message types here
        else:
            port.reset_input_buffer()
            print('Unexpected message format: flushing input and resetting')

    else:
        print('Unexpected message format: flushing input and resetting')

    data_counts = data_counts + 1
        