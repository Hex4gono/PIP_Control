
int digitalPins[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
int analogPins[] = {A0, A1, A2, A3};


void setup() {
  Serial.begin(9600);
  
  for (int i = 0; i < sizeof(digitalPins); i++) {
    pinMode(i, INPUT);
  }
}

void loop() {
  String data = "[";



  // Leer pines analógicos
  for (int i = 0; i < sizeof(analogPins); i++) {
    data += analogRead(analogPins[i]);
    if (i < sizeof(analogPins) - 1) {
      data += ", "; 
    }
  }

  // Leer pines digitales
  for (int i = 0; i < sizeof(digitalPins); i++) {
    data += digitalRead(digitalPins[i]);
    if (i < sizeof(digitalPins) - 1 || sizeof(analogPins) > 0) {
      data += ", "; 
    }
  }

  data += "]";
  Serial.println(data);
  delay(100);
}
