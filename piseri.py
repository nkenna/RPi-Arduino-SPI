import random
import serial
import time

ser = serial.Serial('/dev/ttyACM2', 9600)

while True:
    print(ser.readline())
    num = random.randint(1, 5)
    print(num)

    ser.write(bytes(str(num), 'utf-8'))
    print(str(num))
    time.sleep(5)
