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

int ledPin =  2;    // Relay connected to digital pin 2   <-----Change this to pin 2
const int buttonPin = 3;     // the number of the pushbutton pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

// The setup() method runs once, when the sketch starts

void setup()   {                
  // initialize the digital pin as an output:
  pinMode(ledPin, OUTPUT);  

  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);    
}

// the loop() method runs over and over again,
// as long as the Arduino has power

void loop()                     
{
   // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed.
  // if it is, the buttonState is HIGH:
  if (buttonState == HIGH) {     
    // turn LED on:    
    digitalWrite(ledPin, HIGH);  
  } 
  else {
    // turn LED off:
    digitalWrite(ledPin, LOW); 
  }
  
  
  //digitalWrite(ledPin, HIGH);   // set the LED on
  //delay(1000);                  // wait for a second
  //digitalWrite(ledPin, LOW);    // set the LED off
  //delay(1000);                  // wait for a second
}
