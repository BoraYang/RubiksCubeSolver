#include <AccelStepper.h>

const int LED_PIN = 13;
const int LED_ON = HIGH;
const int LED_OFF = LOW;

const int STEPPER_ENABLED = HIGH;
const int STEPPER_DISABLED = LOW;

const int STEPPER_COMMON_PIN = 21;
const int STEPPER_1_STEP_PIN = 12;
const int STEPPER_1_DIR_PIN = 13  ;

const int STEPPER_2_STEP_PIN = 10;
const int STEPPER_2_DIR_PIN = 11;

const int STEPPER_3_STEP_PIN = 8;
const int STEPPER_3_DIR_PIN = 9;

const int STEPPER_4_STEP_PIN = 6;
const int STEPPER_4_DIR_PIN = 7;

const int STEPPER_5_STEP_PIN = 4;
const int STEPPER_5_DIR_PIN = 5;

const int STEPPER_6_STEP_PIN = 2;
const int STEPPER_6_DIR_PIN = 3;

String content = "";
String movesArray[20];
char character;
int moves=0;
long stepDelay = 1500;  //motor speed; 
                      //put a LOWER number to INCREASE the speed
                      //put a HIGHER number to DECREASE the speed

AccelStepper stepper1(1, STEPPER_1_STEP_PIN, STEPPER_1_DIR_PIN);
AccelStepper stepper2(1, STEPPER_2_STEP_PIN, STEPPER_2_DIR_PIN);
AccelStepper stepper3(1, STEPPER_3_STEP_PIN, STEPPER_3_DIR_PIN);
AccelStepper stepper4(1, STEPPER_4_STEP_PIN, STEPPER_4_DIR_PIN);
AccelStepper stepper5(1, STEPPER_5_STEP_PIN, STEPPER_5_DIR_PIN);
AccelStepper stepper6(1, STEPPER_6_STEP_PIN, STEPPER_6_DIR_PIN);

void setup()
{
  Serial.begin(9600);
  
 // initialize the motor
 pinMode(STEPPER_COMMON_PIN, OUTPUT);
 digitalWrite(STEPPER_COMMON_PIN, HIGH);

 // enable the motors
 stepper1.enableOutputs();
 stepper2.enableOutputs();
 stepper3.enableOutputs();
 stepper4.enableOutputs();
 stepper5.enableOutputs();
 stepper6.enableOutputs();

 // set the speed command
 stepper1.setMaxSpeed(50000);
 stepper1.setSpeed(50000);
 
 stepper2.setMaxSpeed(50000);
 stepper2.setSpeed(50000);
 
 stepper3.setMaxSpeed(50000);
 stepper3.setSpeed(50000);

 stepper4.setMaxSpeed(50000);
 stepper4.setSpeed(50000);
 
 stepper5.setMaxSpeed(50000);
 stepper5.setSpeed(50000);

 stepper6.setMaxSpeed(50000);
 stepper6.setSpeed(50000);
}

void loop()
{
  
  //content = "";

  if(Serial.available() > 0 ){
    getSerial();
  }
  
  if(moves > 0){

    getMoves();
    Serial.println("done");
  }
  
  

}

void getSerial(){
  while(Serial.available() != 0) {
    character = Serial.read();
    
    if(character != 'x'){
      content.concat(character);
    
    }
    
    else{

       movesArray[moves] = content;
       content="";
       moves++;
    }
    
  }
}

void getMoves(){
     int y;
    for (y=0; y<moves ; y++){
      Serial.println(movesArray[y]);
      sendMoveToMotor(movesArray[y]);
     
    }
    moves = 0;
    
}

void step1() {
    digitalWrite(STEPPER_1_STEP_PIN, HIGH);
    delayMicroseconds(stepDelay);
    digitalWrite(STEPPER_1_STEP_PIN, LOW);
    delayMicroseconds(stepDelay);
}

void step2() {
    digitalWrite(STEPPER_2_STEP_PIN, HIGH);
    delayMicroseconds(stepDelay);
    digitalWrite(STEPPER_2_STEP_PIN, LOW);
    delayMicroseconds(stepDelay);
}

void step3() {
    digitalWrite(STEPPER_3_STEP_PIN, HIGH);
    delayMicroseconds(stepDelay);
    digitalWrite(STEPPER_3_STEP_PIN, LOW);
    delayMicroseconds(stepDelay);
}

void step4() {
    digitalWrite(STEPPER_4_STEP_PIN, HIGH);
    delayMicroseconds(stepDelay);
    digitalWrite(STEPPER_4_STEP_PIN, LOW);
    delayMicroseconds(stepDelay);
}

void step5() {
    digitalWrite(STEPPER_5_STEP_PIN, HIGH);
    delayMicroseconds(stepDelay);
    digitalWrite(STEPPER_5_STEP_PIN, LOW);
    delayMicroseconds(stepDelay);
}

void step6() {
    digitalWrite(STEPPER_6_STEP_PIN, HIGH);
    delayMicroseconds(stepDelay);
    digitalWrite(STEPPER_6_STEP_PIN, LOW);
    delayMicroseconds(stepDelay);
}


void sendMoveToMotor(String motorString){
  
  char firstChar = motorString[0];
  char secChar = motorString[1];
 
 
 
  switch(firstChar){
   
     case 'F':
       Serial.print("Stepper 2");
       motorMove2(secChar);
       break;
     case 'R':
       Serial.print("Stepper 3");
       motorMove3(secChar);
       break;
     case 'B':
       Serial.print("Stepper 4");
       motorMove4(secChar);
       break;
     case 'L':
       Serial.print("Stepper 1");
       motorMove1(secChar);
       break;
     case 'U':
       Serial.print("Stepper 6");
       motorMove6(secChar);
       break;
     case 'D':
       Serial.print("Stepper 5");
       motorMove5(secChar);
       break;
       
  }
  
}

void motorMove1(char turnDegree){
   
  switch(turnDegree){
     case '1':
       //100 steps
       Serial.println(" moving 90 degrees CW");
       for (int i = 0; i < 100; i++) {
        step1();
      }
       break;
       
     case '2':
       //200 steps
       Serial.println(" moving 180 degrees ");
       for (int i = 0; i < 200; i++) {
        step1();
      }
       break;
     case '3': 
       //300 steps
       Serial.println(" moving 90 degrees CCW");
       for (int i = 0; i < 300; i++) {
        step1();
    }
       break;
  }
}

void motorMove2(char turnDegree){
   
  switch(turnDegree){
     case '1':
       //100 steps
       Serial.println(" moving 90 degrees CW");
       for (int i = 0; i < 100; i++) {
        step2();
      }
       break;
       
     case '2':
       //200 steps
       Serial.println(" moving 180 degrees ");
       for (int i = 0; i < 200; i++) {
        step2();
      }
       break;
     case '3': 
       //300 steps
       Serial.println(" moving 90 degrees CCW");
       for (int i = 0; i < 300; i++) {
        step2();
    }
       break;
  }
}

void motorMove3(char turnDegree){
   
  switch(turnDegree){
     case '1':
       //100 steps
       Serial.println(" moving 90 degrees CW");
       for (int i = 0; i < 105; i++) {
        step3();
      }
       break;
       
     case '2':
       //200 steps
       Serial.println(" moving 180 degrees ");
       for (int i = 0; i < 200; i++) {
        step3();
      }
       break;
     case '3': 
       //300 steps
       Serial.println(" moving 90 degrees CCW");
       for (int i = 0; i < 300; i++) {
        step3();
    }
       break;
  }
}

void motorMove4(char turnDegree){
   
  switch(turnDegree){
     case '1':
       //100 steps
       Serial.println(" moving 90 degrees CW");
       for (int i = 0; i < 100; i++) {
        step4();
      }
       break;
       
     case '2':
       //200 steps
       Serial.println(" moving 180 degrees ");
       for (int i = 0; i < 200; i++) {
        step4();
      }
       break;
     case '3':
       //300 steps
       Serial.println(" moving 90 degrees CCW"); 
       for (int i = 0; i < 300; i++) {
        step4();
    }
       break;
  }
}

void motorMove5(char turnDegree){
   
  switch(turnDegree){
     case '1':
       //100 steps
       Serial.println(" moving 90 degrees CW");
       for (int i = 0; i < 100; i++) {
        step5();
      }
       break;
       
     case '2':
       //200 steps
       Serial.println(" moving 180 degrees ");
       for (int i = 0; i < 200; i++) {
        step5();
      }
       break;
     case '3':
       //300 steps
       Serial.println(" moving 90 degrees CCW"); 
       for (int i = 0; i < 300; i++) {
        step5();
    }
       break;
  }
}

void motorMove6(char turnDegree){
   
  switch(turnDegree){
     case '1':
       //100 steps
       Serial.println(" moving 90 degrees CW");
       for (int i = 0; i < 100; i++) {
        step6();
      }
       break;
       
     case '2':
       //200 steps
       Serial.println(" moving 180 degrees ");
       for (int i = 0; i < 200; i++) {
        step6();
      }
       break;
     case '3':
       //300 steps
       Serial.println(" moving 90 degrees CCW"); 
       for (int i = 0; i < 300; i++) {
        step6();
    }
       break;
  }
}
