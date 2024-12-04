import serial

ser = serial.Serial('COM1', 9600)

while True:
    buffer = b""
    while b"|s" not in buffer:
        buffer += ser.read(ser.in_waiting)
    print(buffer)  
    buffer = buffer[buffer.find(b"s|")+ 2 : buffer.find(b"|s")]
    wawa = buffer.strip().decode("utf-8",'ignore').split(",")
    print(wawa)
    
    
    """
    print(ser.read(ser.in_waiting))
    wawa = ser.read(ser.in_waiting)
    wawa = wawa[wawa.find(b"s|") + 2 :wawa.find(b"|s")]
    wawa = wawa.strip().decode("utf-8",'ignore').split(",")
    print(wawa)
    """
