import logging
logging.basicConfig(level=logging.DEBUG)

from pymodbus.client.sync import ModbusSerialClient
import utils

client = ModbusSerialClient(method='binary',
                            port="/dev/ttyUSB0",
                            baudrate=9600)

UNIT_ID = 0x01

from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.constants import Endian

def off():
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_8bit_uint(UNIT_ID)  # Unit ID
    builder.add_8bit_uint(0x05)  # function ID
    builder.add_8bit_uint(0x00)
    builder.add_8bit_uint(0x01)  # coil ID
    builder.add_8bit_uint(0x00)  # data, here: off
    builder.add_8bit_uint(0x00)
    #builder.add_8bit_uint(0x9c)  # here checksum
    #builder.add_8bit_uint(0x0a)  # here checksum
    utils.appendCrc(builder)

    return builder.build()

def on():
    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    builder.add_8bit_uint(UNIT_ID)  # Unit ID
    builder.add_8bit_uint(0x05)  # function ID
    builder.add_8bit_uint(0x00)
    builder.add_8bit_uint(0x01)  # coil ID
    builder.add_8bit_uint(0x01)  # data, here: on
    builder.add_8bit_uint(0x00)
    #builder.add_8bit_uint(0x9d)  # here checksum
    #builder.add_8bit_uint(0x9a)  # here checksum
    utils.appendCrc(builder)

    return builder.build()

#01 05 00 01 01 00 9d 9a 	No. 1 relay ON
#01 05 00 01 00 00 9c 0a 	No. 1 relay off


payload = on()

import time


'''
for chr in on():
    client._send(chr)
print(client.recv(1024))
time.sleep(1)

for chr in off():
    client._send(chr)
print(client.recv(1024))
'''
client.connect()

onOff = True
while True:
    if onOff:
        payload = on()
    else:
        payload = off()
    onOff = not onOff

    for chr in payload:
        client.send(chr)

    print('client.recv:', client.recv(1024))

    time.sleep(1)

client.close()
