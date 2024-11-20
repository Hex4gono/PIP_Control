void setup()
{
    Serial.begin(9600);
    for (int i = 0; i = 8; i++)
    {
        pinMode(i,INPUT);
    }
}
void loop()
{
    for (int i = 0; i = 8; i++)
    {
        Serial.println(digitalRead(i));
    }
}