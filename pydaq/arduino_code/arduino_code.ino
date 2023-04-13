/* Code that should be loaded in arduino in order to acquire data from a specific port (analogInputPort) and
 send data from another one (digitalOutputPort)
 Author:    Samir Angelo Milani Martins
             - https://www.samirmartins.com.br
             - https://www.github.com/samirmartins/

 */

int analogInputPort = A0; // Port that will be used to acquire data
const int digitallOutputPort = 13; // Port that will be used to send data

int inputValue; // A variable to store data that will be sent to digitalOutputPort 
int analogValue; // A variable to store data from analogInputPort

void setup() 
{ 
  // Initializing serial communication :
  Serial.begin(2000000);

  // Setting up digitalOutputPort
  pinMode(digitallOutputPort, OUTPUT);

}

void loop() 
{ 

  // Reading data from serial and sending it to digital output
  if (Serial.available() > 0) // Check if there is data from serial
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

    // Reading data from arduino and printing on serial
  analogValue = analogRead(analogInputPort); // Reading input
  Serial.println(analogValue); // Printing on serial

}