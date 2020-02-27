from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder

import Modules.Utils


class ManualSender:

    def __init__(self):
        self.client = Modules.Utils.get_client()
        self.client.connect()

    def run_interactive(self):
        while True:
            user_input = input("Enter HEX values to send: ")
            if user_input == '':
                #user_input = '0x05 0x00 0x01 0x01 0x00'
                #user_input = '0x0 0x5 0x0 0x0 0x0 0x0 0xcc 0x1b'
                user_input = '0x0 0x5 0x0 0x0 0xff 0x0 0x8d 0xeb'

            hex_list = []
            for hex_val in user_input.split(" "):
                if hex_val.startswith('0x'):
                    hex_list.append(int(hex_val, 0))
                else:
                    hex_list.append(int(hex_val, 16))

            self.send(hex_list)

    def send(self, hex_list):
        builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                       wordorder=Endian.Little)
        for hex_val in hex_list:
            builder.add_8bit_uint(hex_val)

        Modules.Utils.append_crc(builder)

        print('sending: ', builder.to_string())
        payload = builder.build()
        for char in payload:
            self.client.send(char)



