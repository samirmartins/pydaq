/* Code that should be loaded in arduino in order to acquire data from a specific port (analogInputPort) and
 send data from another one (digitalOutputPort)
 Author:    Samir Angelo Milani Martins
             - https://www.samirmartins.com.br
             - https://www.github.com/samirmartins/
 */

int analogInputPort = A0; // Port that will be used to acquire data
const int digitalOutputPort = 13; // Port that will be used to send PWM signal

int inputValue; // A variable to store data that will be sent to digitalOutputPort 
int analogValue; // A variable to store data from analogInputPort

void setup() 
{ 
  // Initializing serial communication :
  Serial.begin(115200);

  // Setting up digitalOutputPort for PWM
  pinMode(digitalOutputPort, OUTPUT);
}

void loop() 
{ 
  // Reading data from serial and sending it to digital output as PWM
  if (Serial.available() > 0) // Check if there is data from serial
  {
    // Read the oldest byte in the serial buffer:
    inputValue = Serial.parseInt();  // Read the duty cycle value sent by Python
    
    // Ensure the value is within the 0-255 range for PWM
    inputValue = constrain(inputValue, 0, 255); 

    // Send PWM signal to the output pin based on the received duty cycle
    analogWrite(digitalOutputPort, inputValue); // PWM value (0 to 255)
  }

  // Reading data from the analog input and sending it to the serial monitor
  analogValue = analogRead(analogInputPort); // Reading analog input
  Serial.println(analogValue); // Printing the analog input value on serial
}