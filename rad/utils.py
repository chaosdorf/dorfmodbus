import pymodbus.utilities as ut

def appendCrc(builder):
    crc = ut.computeCRC(ut.make_byte_string(builder.to_string()))
    print(crc)
    hexStr = '%04x' % crc
    hex1 = int(hexStr[0] + hexStr[1], 16)
    hex2 = int(hexStr[2] + hexStr[3], 16)

    builder.add_8bit_uint(hex1)
    builder.add_8bit_uint(hex2)
