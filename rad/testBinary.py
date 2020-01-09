from pymodbus.client.sync import ModbusSerialClient

#import os
#from elevate import elevate

#def is_root():
#    return os.getuid() == 0

#print("before ", is_root())
#elevate()
#print("after ", is_root())

client = ModbusSerialClient(method='binary',
                            port="/dev/ttyUSB0",
                            baudrate=9600)

#client.write_coil(1, 1)
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.constants import Endian

def off():
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_8bit_uint(0x01)
    builder.add_8bit_uint(0x05)
    builder.add_8bit_uint(0x00)
    builder.add_8bit_uint(0x01)
    builder.add_8bit_uint(0x00)  # here!
    builder.add_8bit_uint(0x00)
    builder.add_8bit_uint(0x9c)  # here checksum
    builder.add_8bit_uint(0x0a)  # here checksum
    return builder.build()

def on():
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_8bit_uint(0x01)
    builder.add_8bit_uint(0x05)
    builder.add_8bit_uint(0x00)
    builder.add_8bit_uint(0x01)
    builder.add_8bit_uint(0x01)  # here!
    builder.add_8bit_uint(0x00)
    builder.add_8bit_uint(0x9d)  # here checksum
    builder.add_8bit_uint(0x9a)  # here checksum
    return builder.build()

#01 05 00 01 01 00 9d 9a 	No. 1 relay ON
#01 05 00 01 00 00 9c 0a 	No. 1 relay off


payload = on()

address = 1
# Can write registers
# registers = builder.to_registers()
# client.write_registers(address, registers, unit=1)

# Or can write encoded binary string


import time
onOff = True
while True:
    if onOff:
        payload = on()
    else:
        payload = off()
    onOff = not onOff

    client.write_registers(address, payload, skip_encode=True, unit=1)
    time.sleep(3)

result = client.read_coils(1, 1)
print(result)
client.close()