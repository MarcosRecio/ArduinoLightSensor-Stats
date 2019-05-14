// Here we defind the light sensor pin number on Arduino
// It should be analog in, if you plug that in A0, we define 
// int lightSensorPin = 0; 

int lightSensorPin = 0; 

void setup() {
  // Here we defind the port speed connection
  Serial.begin(38400);
}

void loop() {
  // Here we read data from the light sensor
  float val = analogRead(lightSensorPin);
  // And then just write the value to the port to your PC
  Serial.println(val);
  // We want to keep our reading regular, lte say each 100 milliseconds
  delay(100);
}
