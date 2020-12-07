#define ledPin 13

String inputString = "";
bool stringComplete = false;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, false);
}

void loop() {
  if(stringComplete) {
    Serial.println(inputString);
    int num = inputString.toInt();
    inputString = "";
    if(num > 266) digitalWrite(ledPin, true);
    else digitalWrite(ledPin, false);
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
