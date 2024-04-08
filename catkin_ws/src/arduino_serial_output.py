import serial
import time

# Open serial port
# Make sure to use the correct device name (e.g., /dev/ttyACM0, /dev/ttyUSB0)
ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)  # wait for the serial connection to initialize

while True:
    if ser.in_waiting:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
