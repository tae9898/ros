#include <Wire.h>
#include <Servo.h>
#include <stdlib.h>
Servo servo;

void setup() {
  // put your setup code here, to run once:
  pinMode(7,OUTPUT);
  pinMode(6,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  if(Serial.available()){
    String input = Serial.readStringUntil(' ');
    int degree;
    degree = input.toInt();
    Serial.println(degree);
    if(degree>200){
      Serial.println('a');
      digitalWrite(7,1);
      digitalWrite(6,0);
     
      delay(100);
    }
    else if(degree<200){
      digitalWrite(7,0);
      digitalWrite(6,1);
      delay(100);
    }

    //input == '0';

    
  }
  Serial.flush();

}
