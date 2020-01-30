from pymodbus.client.sync import ModbusSerialClient

#import os
#from elevate import elevate

#def is_root():
#    return os.getuid() == 0

#print("before ", is_root())
#elevate()
#print("after ", is_root())

client = ModbusSerialClient(method='rtu',
                            port="/dev/ttyUSB0",
                            baudrate=9600)
#client.write_coil(1, 1)
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.constants import Endian


import time
onOff = True


#client.write_coil(0, True)

isOk = True
count = 1
while isOk:
    # read the setable devices
    result = client.read_coils(count-1, count)

    if not result.isError():
        print(result.bits)
    else:
        print('ERROR')
        break
    count += 1

'''
for i in range(0, 8):
    # read only inputs
    result = client.read_discrete_inputs(i, 2)
    if not result.isError():
        print(result.bits)
    else:
        print('ERROR')
'''

'''
for i in range(0, 8):
    result = client.read_input_registers(i, 2)
    if not result.isError():
        print(result.bits)
    else:
        print('ERROR')
'''

print("Crash at", count)
#print(result)
client.close()
