/*
 Door Lock with a button and transistor.
 
 The code below will keep the door locked until you push the button, then the door will be unlocked for 2 seconds
 
 Supplies:
 12 volt electro-magnetic door lock
 12 volt battery
 Darlyinton TIP120 transistor
 Push button
 Some LEDs
 */

int lockPin =  9;    // electric lock connected to digital pin 2   
int buttonPin =  2;    // button connected to digital pin 2   

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

// The setup() method runs once, when the sketch starts
void setup()   { 
  
  //hit Ctrl + Shift + M to see output  
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
  
 //check if button is pressed (the voltage is high)
 if(digitalRead(buttonPin) == HIGH){
   
     //debugging code...
     //Serial.println("button press detected");
     
     //send a high voltage to the electric lock and then the door can be opened
     digitalWrite(lockPin, HIGH);
     
     //wait 2 seconds
     delay(2000);
     
     //lock door again
     digitalWrite(lockPin, LOW);
 }
}
