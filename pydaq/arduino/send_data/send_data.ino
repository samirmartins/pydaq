// Code that should be in arduino in order to send data from a specific port
const int digitallOutputPort = 13; // Port that will be used to send data

int inputValue; // an integer variable to store the potentiometer reading
void setup() 
{ 
  // Initializing serial communication :
  Serial.begin(9600);
  pinMode(digitallOutputPort, OUTPUT);
}

void loop() 
{ 
  
  // Check if there is data from serial
  if (Serial.available() > 0) 
  {
    // Read the oldest byte in the serial buffer:
    inputValue = Serial.read();
    // if it's a '1', send HIGH to the output
    if (inputValue == '1') 
    {
      digitalWrite(digitallOutputPort, HIGH);
    }
    // if it's an '0' turn off the output:
    if (inputValue == '0') 
    {
      digitalWrite(digitallOutputPort, LOW);
    }
  }
}