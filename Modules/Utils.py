import pymodbus.utilities as ut
import Config.ConfigLoader as Conf


def append_crc(builder):
    crc = ut.computeCRC(ut.make_byte_string(builder.to_string()))
    #print(crc)
    hex_str = '%04x' % crc
    hex1 = int(hex_str[0] + hex_str[1], 16)
    hex2 = int(hex_str[2] + hex_str[3], 16)

    builder.add_8bit_uint(hex1)
    builder.add_8bit_uint(hex2)


def get_client():
    from pymodbus.client.sync import ModbusSerialClient
    return ModbusSerialClient(
        method='rtu',
        port=Conf.PORT,
        baudrate=Conf.BAUD_RATE
                              )
