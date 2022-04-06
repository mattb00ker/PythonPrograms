import serial

PORT = "/dev/tty.usbmodem1412"

BAUD = 115200

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

try:
    while True:
        data = s.readline().rstrip()

        data_s = data.split(" ")
        x, y, z = data_s[0], data_s[1], data_s[2]
        a, b = data_s[3], data_s[4]
        print(x, y, z)
        print(a, b)

finally:
    s.close()
