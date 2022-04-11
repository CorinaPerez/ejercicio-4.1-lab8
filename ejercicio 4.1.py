import serial
import matplotlib.pyplot as plt
import time
from base64 import decode

ser = serial.Serial('COM4', 9600, timeout=1)
punto = 0
fig, b = plt.subplots()
plt.ion()
maxlen = 40
x = []
y = []

while True:
    data = ser.readline().decode().strip()
    time.sleep(1)
    plt.xlabel('Horas')
    plt.ylabel('Temperatura')
    if data:
        data = float(data)
        print(data)
        x.append(punto)
        y.append(data)
        if len(x) > maxlen:
            x = x[1:]
            y = y[1:]
        plt.plot(x, y, color='r')
        punto += 1
        plt.pause(0.01)
        b.clear()
        plt.ylim([0, 50])
        plt.show()