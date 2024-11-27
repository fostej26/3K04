import serial
import struct

port = serial.Serial()

port.baudrate = 115200
port.port = 'COM5'
port.timeout = 10

port.open()
port.flush()

flag = True
data_counts = 0

arr = 0

def output_data(array, count):
    for i in range(0, len(array)):
        read_accelData = struct.unpack('<f', array[1:5])
        print(f'activity: {array[5]}, adapredRate: {array[0]}, Target: {read_accelData}')

while flag:

    if data_counts == 5000:
        print('500 recieves - exiting')
        flag = False


    first_byte = port.read(1)

    # Check that first "sync" byte is correct
    if int.from_bytes(first_byte) == 1:

        arr = bytearray(6)
        port.readinto(arr)
        output_data(arr, data_counts)
        data_counts = data_counts + 1

    else:
        port.reset_input_buffer()
        print('Unexpected message format: flushing input and resetting')
        print(first_byte)

port.close()