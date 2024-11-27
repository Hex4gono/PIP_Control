
int digitalPins[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13};
int analogPins[] = {A0, A1, A2, A4};


void setup() 
{
  Serial.begin(9600);
  
  for (int i = 2; i < sizeof(digitalPins); i++) 
  {
    pinMode(i, INPUT_PULLUP);
  }
}

void loop() 
{
  String data = "[";



  // Leer pines analógicos  (el sizeof / size of es porque aparentemente c++ lee el tamano en bytes y no cant de elementos)
  for (int i = 0; i < sizeof(analogPins)  / sizeof(analogPins[0]) ; i++) 
  {
    //hace falta revertir las coordenadas de uno de los joysticks por la forma del circuito
    if (i == 0 || i == 1) // si estamos en la primera o segunda iteracion (js 1)
    {
      data += (1023 - analogRead(analogPins[i])) - 515;
    } else {
      data += analogRead(analogPins[i]) - 515;
    }

    if (i < sizeof(analogPins) / sizeof(analogPins[0]) - 1);
    {
      data += ", "; 
    }
  }

  // Leer pines digitales (deben ser revertidos porque uso la resistencia interna pullup)
  for (int i = 2; i < sizeof(digitalPins)  / sizeof(digitalPins[0]); i++) 
  {

    data += ", ";
    // invierte los valores por el pullup
    if (digitalRead(i) == HIGH) 
    {
      data += "0";
    } else {
      data += "1";  
    }

  }

  data += "]";
  Serial.println(data);
  delay(100);
  int valueA0 = analogRead(A0); // Leer A0
  int valueA1 = analogRead(A1); // Leer A1
/*
// debug
  Serial.print("A0: ");
  Serial.print(1023 - valueA0);
  Serial.print(" | A1: ");
  Serial.println(1023 - valueA1);

 // A3 dejo de funcionar de la maldita nada asi que tuve que remplazarlo
  Serial.print("A2: ");
  Serial.print(analogRead(A2));
  Serial.print(" | A4: ");
  Serial.println(analogRead(A4));
*/
  delay(30); 
}
