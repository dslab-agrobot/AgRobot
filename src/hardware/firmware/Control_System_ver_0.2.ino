/*
   Control System Source Code

                  Version 0.2


   FINISHED

   1. LED and POWER control Function is now added.

   2. Add software limitation to avoid wrong move commands.

   3. Use Hardware limitation to help calibrate the Y-axis.


   TO DO

   1. Add RELIABLE sensor to mesure the distance to the end of the track.



*/
#include <Wire.h>

//Digital Input Pins

//Define Pin Locations for Motors

//DC Motor Pins
//DC Motor 1 for Left-Front Wheel
#define M11 22
#define M12 23
#define M1P 2

//DC Motor 2 for Right-Front Wheel
#define M21 24
#define M22 25
#define M2P 3

//DC Motor 3 for Left-Rear Wheel
#define M31 26
#define M32 27
#define M3P 4

//DC Motor 4 for Right-Rear Wheel
#define M41 28
#define M42 29
#define M4P 5

////Stepper Motor Pins
////Stepper Motor 1 and 2 for X Axis
//#define S1D 30
//#define S1E 31
//#define S1S 32
//
////Stepper Motor 3 for Y Axis
//#define S2D 33
//#define S2E 34
//#define S2S 35

////Stepper Motor 4 for Z Axis
//#define S3D 36
//#define S3E 37
//#define S3S 38

//DC Motors Relay Enable Pin
#define M1EN 40
#define M2EN 41
#define M3EN 42
#define M4EN 43

//Main Power and LED Control Pin
#define LEDR 44
#define LEDG 45
#define LEDW 46
#define POWER 47

//Analog Input Pins
//Battery Pack Voltage, Use Devide Network to Map 0-14.4V to 0-4.096V
//#define Batt_Volt 0
#define LED 13
#define VER 0.2

const int PWM_percent = 100;
const int Steps_per_1mm = 800;

long x_position = 0;
long y_position = 0;
long x_overall = 0;
long y_overall = 0;

bool End_Signal = LOW;

void setup() {
  Serial.begin(115200);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(22, OUTPUT);
  pinMode(23, OUTPUT);
  pinMode(24, OUTPUT);
  pinMode(25, OUTPUT);
  pinMode(26, OUTPUT);
  pinMode(27, OUTPUT);
  pinMode(28, OUTPUT);
  pinMode(29, OUTPUT);
  pinMode(30, OUTPUT);
  pinMode(31, OUTPUT);
  pinMode(32, OUTPUT);
  pinMode(33, OUTPUT);
  pinMode(34, OUTPUT);
  pinMode(35, OUTPUT);
  pinMode(36, OUTPUT);
  pinMode(37, OUTPUT);
  pinMode(38, OUTPUT);
  pinMode(40, OUTPUT);
  pinMode(41, OUTPUT);
  pinMode(42, OUTPUT);
  pinMode(43, OUTPUT);
  pinMode(44, OUTPUT);
  pinMode(45, OUTPUT);
  pinMode(46, OUTPUT);
  pinMode(47, OUTPUT);

  Serial.println("Y-axis Calibrating!!!");
  digitalWrite(LED, HIGH);
  digitalWrite(10, HIGH);
  digitalWrite(8, 0);
  delay(100);
  for (long i = 0; i < 100000; i++)
  {
    if (End_Signal != HIGH)
    {
      for (long j = 0; j < 100; j++)
      {
        digitalWrite(9, HIGH);
        delay(0.5);
        digitalWrite(9, LOW);
        delay(0.5);
      }
    }
    else
    {
      break;
    }
  }
  delay(100);
  for (long i = 0; i < 20000; i++)
  {
    digitalWrite(9, HIGH);
    delay(0.5);
    digitalWrite(9, LOW);
    delay(0.5);
  }
  delay(100);
  digitalWrite(8, 1);
  Serial.println("Y-axis Calibrated!!!");
  digitalWrite(LED, LOW);
}

void loop()
{
  String comdata = "";
  long x_data = 0;
  long y_data = 0;
  long x_time = 0;
  long y_step = 0;
  bool MIN1 = 0;
  bool MIN2 = 0;
  bool y_dir;

  while (Serial.available() > 0)
  {
    comdata += char(Serial.read());
    delay(2);
  }
  if (comdata.length() > 0)
  {
    Serial.println("Data Received!");
    Serial.println(comdata);
    if (comdata[0] == 'X')
    {
      String x_data_s = "";
      x_data_s = comdata[2];
      x_data_s += comdata[3];
      x_data_s += comdata[4];
      x_data_s += comdata[5];
      x_data = x_data_s.toInt();
      if (comdata[1] == '+')
      {
        x_position += x_data;
        MIN1 = 1;
        MIN2 = 0;
      }
      else if (comdata[1] == '-')
      {
        x_position -= x_data;
        MIN1 = 0;
        MIN2 = 1;
      }
      else
      {
        Serial.println("X-axis Command Error!!!");
        return;
      }
      digitalWrite(LED, HIGH);
      x_time = 2 * 1000 * x_data / PWM_percent;
      //1000 means 1000ms in one second, x_data is Distance in mm
      //PWM_percent / 2 Equals to speed
      //10 is Speed which is Equal 10mm/s, PWM_percent at this time is 100
      digitalWrite(M11, MIN1);
      digitalWrite(M12, MIN2);
      digitalWrite(M21, MIN1);
      digitalWrite(M22, MIN2);
      digitalWrite(M31, MIN1);
      digitalWrite(M32, MIN2);
      digitalWrite(M41, MIN1);
      digitalWrite(M42, MIN2);
      digitalWrite(M1EN, 1);
      digitalWrite(M2EN, 1);
      digitalWrite(M3EN, 1);
      digitalWrite(M4EN, 1);
      delay(200);
      analogWrite(M1P, PWM_percent);
      analogWrite(M2P, PWM_percent);
      analogWrite(M3P, PWM_percent);
      analogWrite(M4P, PWM_percent);
      delay(x_time);
      digitalWrite(M1EN, 0);
      digitalWrite(M2EN, 0);
      digitalWrite(M3EN, 0);
      digitalWrite(M4EN, 0);
      digitalWrite(M11, 0);
      digitalWrite(M12, 0);
      digitalWrite(M21, 0);
      digitalWrite(M22, 0);
      digitalWrite(M31, 0);
      digitalWrite(M32, 0);
      digitalWrite(M41, 0);
      digitalWrite(M42, 0);
      delay(200);
      //x_overall
      x_overall += x_data;
      Serial.print("X-axis Position is:");
      Serial.print(x_position);
      Serial.print("; X has already Moved:");
      Serial.print(x_overall);
      Serial.println(".");
      Serial.println("X-axis Command Executed OK!!!");
      digitalWrite(LED, LOW);
    }
    else if (comdata[0] == 'Y')
    {
      String y_data_s = "";
      y_data_s = comdata[2];
      y_data_s += comdata[3];
      y_data_s += comdata[4];
      y_data = y_data_s.toInt();

      if (comdata[1] == '+')
      {
        y_position += y_data;
        if (y_position > 980)
        {
          Serial.println("Y-axis Command Overrange!!!");
          y_position -= y_data;
          return;
        }
        y_dir = 1;
      }
      else if (comdata[1] == '-')
      {
        y_position -= y_data;
        if (y_position < 10)
        {
          Serial.println("Y-axis Command Overrange!!!");
          y_position += y_data;
          return;
        }
        y_dir = 0;
      }
      else
      {
        Serial.println("Y-axis Command Error!!!");
        return;
      }
      digitalWrite(LED, HIGH);
      y_step = y_data * Steps_per_1mm;
      digitalWrite(10, y_dir);
      digitalWrite(8, 0);
      delay(100);
      for (long i = 0; i < y_step; i++)
      {
        digitalWrite(9, HIGH);
        delay(0.5);
        digitalWrite(9, LOW);
        delay(0.5);
      }
      delay(100);
      digitalWrite(8, 1);
      y_overall += y_data;
      Serial.print("Y-axis Position is:");
      Serial.print(y_position);
      Serial.print("; Y has already Moved:");
      Serial.print(y_overall);
      Serial.println(".");
      if ((y_position == 970) | (y_position == 20))
      {
        Serial.println("Y-axis is at the end.");
      }
      else if ((y_position > 970) | (y_position < 20))
      {
        Serial.println("Y-axis is near the end.");
      }
      Serial.println("Y-axis Command Executed OK!!!");
      digitalWrite(LED, LOW);
    }
    else if (comdata[0] == 'V')
    {
      Serial.print("Firmware Version is ");
      Serial.print(VER);
      Serial.println("!");
    }
    else if (comdata[0] == 'R')
    {
      if (comdata[1] == '+')
      {
        digitalWrite(LEDR, HIGH);
        Serial.println("Red LED Turned ON!!!");
      }
      else if (comdata[1] == '-')
      {
        digitalWrite(LEDR, LOW);
        Serial.println("Red LED Turned OFF!!!");
      }
    }
    else if (comdata[0] == 'G')
    {
      if (comdata[1] == '+')
      {
        digitalWrite(LEDG, HIGH);
        Serial.println("Green LED Turned ON!!!");
      }
      else if (comdata[1] == '-')
      {
        digitalWrite(LEDG, LOW);
        Serial.println("Green LED Turned OFF!!!");
      }
    }
    else if (comdata[0] == 'W')
    {
      if (comdata[1] == '+')
      {
        digitalWrite(LEDW, HIGH);
        Serial.println("White LED Turned ON!!!");
      }
      else if (comdata[1] == '-')
      {
        digitalWrite(LEDW, LOW);
        Serial.println("White LED Turned OFF!!!");
      }
    }
    else if (comdata[0] == 'P')
    {
      if (comdata[1] == '+')
      {
        digitalWrite(POWER, HIGH);
        Serial.println("Main Power Turned ON!!!");
      }
      else if (comdata[1] == '-')
      {
        digitalWrite(POWER, LOW);
        Serial.println("Main Power Turned OFF!!!");
      }
    }
    else
    {
      Serial.println("Command Error!!!");
      return;
    }
  }
}
