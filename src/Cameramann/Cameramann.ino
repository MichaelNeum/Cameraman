#include <Servo.h>

#define servoPin 6

Servo myServo;
String inputString = "";
bool stringComplete = false;

void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin);
}

void loop() {
  if(stringComplete) {
    int num = inputString.toInt();
    inputString = "";
    myServo.write(map(num, 0, 550, 180, 0));
    stringComplete = false;
  }

}

void serialEvent() {
  while(Serial.available()) {
    char inChar = (char)Serial.read();
    if(inChar == 'f') stringComplete = true;
    else if(inChar != '\n') inputString += inChar;
  }
}
