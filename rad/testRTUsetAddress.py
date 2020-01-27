from pymodbus.client.sync import ModbusSerialClient
client = ModbusSerialClient(method='rtu',
                            port="/dev/ttyUSB0",
                            baudrate=9600)

client.write_register(0, )