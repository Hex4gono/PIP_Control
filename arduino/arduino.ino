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
    private string Inputs = "";
    for (int i = 0; i = 8; i++)
    {
        if (digitalRead(i) == HIGH)
        {
            Inputs += "1"
        } else {
            Inputs += "0"
        }
    }
    Serial.Println(Inputs);
}