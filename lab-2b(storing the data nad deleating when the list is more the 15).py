import serial 
import RPi.GPIO as GPIO
import time

values = []

ser=serial.Serial("/dev/ttyUSB0",9600)
ser.baudrate=9600

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

while True:
    try:
        read_ser= ser.readline().decode().strip()
        if read_ser == "":
            continue

        parts = read_ser.split(",")
        if len(parts)!= 2:
            print(read_ser)
            continue
        temp = int(parts[0])
        hum = int(parts[1])

        values.append([temp, hum])

        temp_list = [pair[0] for pair in values]
        hum_list = [pair[1] for pair in values]

        avg_temp = sum(temp_list) / len(temp_list)
        avg_hum = sum(hum_list)/ len (hum_list)

    except ValueError:
        print(read_ser)
        continue
    print(f"temp: {temp}, Humidity: {hum}, avg temperature: {avg_temp}, avg humidity: {avg_hum}")

    if len(values)==15:
        print("list cleared.")
        values=[]

    time.sleep(0.1)