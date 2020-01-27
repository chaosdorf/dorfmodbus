from pymodbus.client.sync import ModbusSerialClient
from pymodbus.utilities import computeCRC
import pymodbus.utilities as ut
client = ModbusSerialClient(method='binary',
                            port="/dev/ttyUSB0",
                            baudrate=9600)

#client.write_coil(1, 1)
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.constants import Endian
import utils

def change():
    #Current address 01 is changed to 09
    #01 10 00 00 00 01 02 00 09 66 56

    builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                   wordorder=Endian.Little)
    #builder.add_8bit_uint(0x00)
    #builder.add_8bit_uint(0x10)
    #builder.add_8bit_uint(0x00)
    #builder.add_8bit_uint(0x00)
    #builder.add_8bit_uint(0x00)
    #builder.add_8bit_uint(0x01)
    #builder.add_8bit_uint(0x02)
    #builder.add_8bit_uint(0x00)
    #builder.add_8bit_uint(0x09)

    #builder.add_8bit_uint(0x01)  # Unit ID
    #builder.add_8bit_uint(0x10)  # function ID
    #builder.add_8bit_uint(0x00)
    #builder.add_8bit_uint(0x00)  # coil ID
    #builder.add_8bit_uint(0x00)  # data, here: on
    #builder.add_8bit_uint(0x01)
    #builder.add_8bit_uint(0x02)
    #builder.add_8bit_uint(0x00)
    #builder.add_8bit_uint(0x09)

    builder.add_8bit_uint(0x01)  # Unit ID
    builder.add_8bit_uint(0x10)  # function ID
    builder.add_8bit_uint(0x00)
    builder.add_8bit_uint(0x00)  # coil ID
    builder.add_8bit_uint(0x00)  # data

    builder.add_8bit_uint(0x01)
    builder.add_8bit_uint(0x02)
    builder.add_8bit_uint(0x00)
    builder.add_8bit_uint(0x09)

    builder.build()
    utils.appendCrc(builder)
    print('TMP:', builder)

    #print(computeCRC(str(builder).encode()))
    #crc = computeCRC(ut.make_byte_string(builder.to_string()))
    #print(crc)
    #hexStr = '%04x' % crc
    #hex1 = int(hexStr[0] + hexStr[1], 16)
    #hex2 = int(hexStr[2] + hexStr[3], 16)
    ##print(hex(hex2))
    ##builder.add_8bit_uint(0x66)
    ##builder.add_8bit_uint(0x56)

    #builder.add_8bit_uint(hex1)
    #builder.add_8bit_uint(hex2)

    return builder.build()

address = 1
client.write_registers(address, change(), skip_encode=True)
