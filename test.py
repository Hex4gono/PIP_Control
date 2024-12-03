import serial

ser = serial.Serial('COM1', 9600)

while True:
    print(ser.read_until(b"stop"))
    wawa = ser.read_until(b"stop")
    wawa = wawa[wawa.find(b"start") + 5 :wawa.find(b"stop")]
    wawa = wawa.strip().decode("utf-8",'ignore').split(",")
    print(wawa)
