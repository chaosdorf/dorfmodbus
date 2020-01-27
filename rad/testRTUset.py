from pymodbus.client.sync import ModbusSerialClient
client = ModbusSerialClient(method='rtu',
                            port="/dev/ttyUSB0",
                            baudrate=9600)
#client.write_coil(1, 1)
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.constants import Endian
import time

# address = 1
# Can write registers
# registers = builder.to_registers()
# client.write_registers(address, registers, unit=1)

# Or can write encoded binary string


import time
onOff = True

isOk = True
count = 1

while isOk:
    # read the setable devices
    #result = client.read_coils(count-1, count)
    client.write_coil(1, onOff)
    print('OK', onOff)
    onOff = not onOff
    time.sleep(1)
    #if not result.isError():
    #    print(result.bits)
    #else:
    #    print('ERROR')
    #    break
    #count += 1

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