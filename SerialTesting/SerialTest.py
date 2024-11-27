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
    for i in range(0, len(array)):
        print(f'Count: {count}, Byte #: {i}, Value: {array[i]}')

    read_atrPulseAmp = struct.unpack('<f', array[3:7])
    read_atrPulseWidth = struct.unpack('<f', array[7:11])
    print(read_atrPulseAmp)
    print(read_atrPulseWidth)

while flag:

    if data_counts == 100:
        # Send data
        print('sending to pacemaker')
        
        byte_0 = struct.pack('<B', 55)
        byte_1 = struct.pack('<B', 2)
        byte_2 = struct.pack('<B', 75)
        byte_3 = struct.pack('<B', 105)
        atr_pulseAmp = 3.45742
        bytes4_7 = struct.pack('<f', atr_pulseAmp)
        atr_pulseWidth = 1.523
        bytes8_11 = struct.pack('<f', atr_pulseWidth)
        bytes12_13 = struct.pack('<H', 280)
        vent_pulseAmp = 2.78
        bytes14_17 = struct.pack('<f', vent_pulseAmp)
        vent_pulseWidth = 0.6
        bytes18_21 = struct.pack('<f', vent_pulseWidth)
        bytes22_23 = struct.pack('<H', 320)
        bytes24_25 = struct.pack('<H', 165)
        bytes26_27 = struct.pack('<H', 98)
        bytes28_29 = struct.pack('<H', 436)
        byte_30 = struct.pack('<B', 55)
        byte_31 = struct.pack('<B', 2)
        byte_32 = struct.pack('<B', 70)
        byte_33 = struct.pack('<B', 100)
        byte_34 = struct.pack('<B', 70)
        byte_35 = struct.pack('<B', 100)

        byte_arr = byte_0 + byte_1 + byte_2 + byte_3 + bytes4_7 + bytes8_11 + bytes12_13 + bytes14_17 + bytes18_21 + bytes22_23 + bytes24_25 + bytes26_27 + bytes28_29 + byte_30 + byte_31 + byte_32 + byte_33 + byte_34 + byte_35
        port.write(byte_arr)

    if data_counts == 110:
        print('110 recieves - exiting')
        flag = False


    first_byte = port.read(1)

    # Check that first "sync" byte is correct
    if int.from_bytes(first_byte) == 1:

        arr = bytearray(137)
        port.readinto(arr)
        output_data(arr, data_counts)
        data_counts = data_counts + 1

    else:
        port.reset_input_buffer()
        print('Unexpected message format: flushing input and resetting')
        print(first_byte)

port.close()