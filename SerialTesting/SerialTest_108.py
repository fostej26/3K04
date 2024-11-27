import serial
import struct

port = serial.Serial()

port.baudrate = 115200
port.port = 'COM5'
port.timeout = 10

port.open()

flag = True
data_counts = 0

arr = 0

def output_data(array, count):
    # for i in range(0, len(array)):
    #     print(f'Count: {count}, Byte #: {i}, Value: {array[i]}')

    read_atrData = struct.unpack('10f', array[28:68])
    read_ventData = struct.unpack('10f', array[68:108])
    print(read_atrData)
    print(read_ventData)

while flag:

    if data_counts == 100:
        # Send data
        print('sending to pacemaker')
        
        byte_0 = struct.pack('<B', 40)
        byte_1 = struct.pack('<B', 1)
        byte_2 = struct.pack('<B', 65)
        byte_3 = struct.pack('<B', 100)
        atr_pulseAmp = 3.5
        bytes4_7 = struct.pack('<f', atr_pulseAmp)
        atr_pulseWidth = 1.7
        bytes8_11 = struct.pack('<f', atr_pulseWidth)
        vent_pulseAmp = 2.5
        bytes14_17 = struct.pack('<f', vent_pulseAmp)
        vent_pulseWidth = 0.6
        bytes18_21 = struct.pack('<f', vent_pulseWidth)
        bytes24_25 = struct.pack('<H', 100)
        bytes26_27 = struct.pack('<H', 100)
        byte_30 = struct.pack('<B', 120)
        byte_31 = struct.pack('<B', 5)
        byte_32 = struct.pack('<B', 3)
        byte_33 = struct.pack('<B', 1)
        byte_35 = struct.pack('<B', 1)

        byte_arr = byte_0 + byte_1 + byte_2 + byte_3 + bytes4_7 + bytes8_11 + bytes14_17 + bytes18_21 + bytes24_25 + bytes26_27 + byte_30 + byte_31 + byte_32 + byte_33 + byte_35
        port.write(byte_arr)

    if data_counts == 120:
        print('105 recieves - exiting')
        flag = False


    first_byte = port.read(1)

    # Check that first "sync" byte is correct
    if int.from_bytes(first_byte) == 7:

        arr = bytearray(108)
        port.readinto(arr)
        output_data(arr, data_counts)
        data_counts = data_counts + 1

    else:
        port.reset_input_buffer()
        print('Unexpected message format: flushing input and resetting')
        print(first_byte)

port.close()