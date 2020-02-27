# dorfmodbus

**modbus** for the chaosdorf 4.0 infrastructure 

## installation / requirements

```bash
pip3 install requirements.txt
```

## cli sender

for an interactive CLI to send bytes manually, start
```bash
python startCliSender
```

You can enter the bytes as HEX-values  
Example:  
```
Enter HEX values to send: 0x0 0x5 0x0 0x0 0xff 0x0 0x8d 0xeb
sending:  b'\x00\x05\x00\x00\xff\x00\x8d\xeb\x00\x00'
```

```
Enter HEX values to send: 0 5 0 0 0 0 cc 1b
sending:  b'\x00\x05\x00\x00\x00\x00\xcc\x1b\x00\x00'
```

## todo

* programmer
* sniffer
