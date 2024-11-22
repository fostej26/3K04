import serial

port = serial.Serial()

port.baudrate = 115200
port.port = 'COM3'
port.timeout = 10

port.open()

print(port.is_open)

flag = True
data_counts = 0

arr = 0

def output_data(array, count):
    for i in range(0, len(array)):
        print(f'Count: {count}, Byte #: {i}, Value: {array[i]}')

while flag:
    first_byte = port.read(1)
    # Check that first "sync" byte is correct
    if len(first_byte) == 1 and int.from_bytes(first_byte, byteorder='big') == 1:
        second_byte = port.read(1)

        # Check what type of message is being received, read proper amount of bytes accordingly
        if len(second_byte) == 1 and int.from_bytes(second_byte, byteorder='big') == 1:
            arr = bytearray(102)
            port.readinto(arr)
            output_data(arr, data_counts)

        # Other message types here
        else:
            port.reset_input_buffer()
            print('Unexpected message format: flushing input and resetting')

    else:
        port.reset_input_buffer()
        print('Unexpected message format: flushing input and resetting')

    data_counts += 1

        