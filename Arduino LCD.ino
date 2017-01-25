//load libraries
#include <Wire.h>
#include <LCD.h>
#include <LiquidCrystal_I2C.h>
#define trigPin 12
#define echoPin 13
//Define variables

#define I2C_ADDR          0x27        //Define I2C Address where the PCF8574A is
#define BACKLIGHT_PIN      3
#define En_pin             2
#define Rw_pin             1
#define Rs_pin             0
#define D4_pin             4
#define D5_pin             5
#define D6_pin             6
#define D7_pin             7

//Initialise the LCD
LiquidCrystal_I2C      lcd(I2C_ADDR, En_pin, Rw_pin, Rs_pin, D4_pin, D5_pin, D6_pin, D7_pin);
String line;
char receive;
boolean done = false;
int lineNo;
void setup()
{
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  //Define the LCD as 16 column by 2 rows
  lcd.begin (16, 2);

  //Switch on the backlight
  lcd.setBacklightPin(BACKLIGHT_PIN, POSITIVE);
  lcd.setBacklight(HIGH);

  //Initial Message
  lcd.setCursor(0, 0);
  lcd.print("WELCOME");
  lcd.setCursor(0, 1);
  lcd.print("WELCOME");

}


void loop() {
  long duration, distance;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);

  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration / 2) / 29.1;

  Serial.println(distance);
  if (distance < 100) {
    lcd.setBacklight(1);
  }
  else {
    lcd.setBacklight(0);
  }
  delay(500);
  //----------------------------------------------------
  done = false;
  if (Serial.available() > 0) {
    lineNo = (int) Serial.read() - 48;
    delay(100);
  }
  while (Serial.available() > 0) {
    receive = Serial.read();
    line += receive;
    done = true;
  }
  if (done) {
    lcd.clear();
    lcd.setCursor(0, lineNo);
    lcd.print(line);
    line = "";
  }
}
