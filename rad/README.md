# Research and Development

basic figuring stuff out files and tests

## requirements

```bash
pip3 install requirements.txt
```

## device

get the device path where the serial adapter is located  
(with ```dmesg```, for example)  

for **TESTING ONLY** on ubuntu 18.04 set the rights for the device to 777
```bash
sudo chmod 777 /dev/ttyUSB0
```
Or add yourself to the group ```dialout```


## EXCEPTIONS

This specific function may return an object of type ```pymodbus.exceptions.ModbusIOException``` in case of error, therefore any function could return an exception instead of throwing it.

```python
state = client.write_coil(0, onOff, unit=99)
```

every result has .isError()
```python
state.isError()
```

```
Modbus Error: [Input/Output] Modbus Error: [Invalid Message] Incomplete message received, expected at least 2 bytes (0 received)
<class 'pymodbus.exceptions.ModbusIOException'>
```

https://github.com/riptideio/pymodbus/issues/298#issuecomment-386175043


## Debugging

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```
