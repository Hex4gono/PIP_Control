import serial

ser = serial.Serial('COM1', 19200)

while True:
    print(ser.read_until(b"|s"))
    wawa = ser.read_until(b"|s")
    wawa = wawa[wawa.find(b"s|") + 2 :wawa.find(b"|s")]
    wawa = wawa.strip().decode("utf-8",'ignore').split(",")
    print(wawa)
