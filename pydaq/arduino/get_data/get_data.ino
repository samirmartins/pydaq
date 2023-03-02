// Code that should be in arduino in order to acquire data from a specific port
int analogInputPort = A0; // Port that will be used to acquire data

int analogValue; // an integer variable to store the potentiometer reading
void setup() 
{ 
  // Initializing serial communication :
  Serial.begin(9600);
}

void loop() 
{ 
  analogValue = analogRead(analogInputPort); // Reading input
  Serial.println(analogValue); // Printing on serial
}