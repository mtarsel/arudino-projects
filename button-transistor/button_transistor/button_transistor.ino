/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
  The circuit:
 * LED connected from digital pin 13 to ground.
  * Note: On most Arduino boards, there is already an LED on the board
 connected to pin 13, so you don't need any extra components for this example.
  
 Created 1 June 2005
 By David Cuartielles
 http://arduino.cc/en/Tutorial/Blink
 based on an orginal by H. Barragan for the Wiring i/o board
 */

int lockPin =  9;    // Relay connected to digital pin 2   <-----Change this to pin 2
int buttonPin =  2;    // Relay connected to digital pin 2   <-----Change this to pin 2

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

// The setup() method runs once, when the sketch starts

void setup()   {                
  Serial.begin(9600);
  
  // initialize the digital pin as an output:
  pinMode(lockPin, OUTPUT);   
  pinMode(buttonPin, OUTPUT);
  
  digitalWrite(lockPin,LOW);  
}

// the loop() method runs over and over again,
// as long as the Arduino has power

void loop()                     
{
  
 if(digitalRead(buttonPin) == HIGH){
     Serial.println("button press detected");
     digitalWrite(lockPin, HIGH);
     delay(2000);
     digitalWrite(lockPin, LOW);
 }
}
