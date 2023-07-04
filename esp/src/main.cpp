#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <Wire.h>
#include <SPI.h>

#include "hcsr04.h"

#define Addr 0x1C

const char* ssid     = "DESKTOP-O2OLJ1H 8056";         // The SSID (name) of the Wi-Fi network you want to connect to
const char* password = "L5w7393^";     // The password of the Wi-Fi network
String url_get_action = "http://192.168.1.22:5000/get_action/";
String url_add_acc = "http://192.168.1.22:5000/add_acc/";
WiFiClient client;
HTTPClient http;

void setup() {

  pinMode(trigger_pin, OUTPUT);
  pinMode(echo_pin, INPUT);
  
  // Initialise SPI communication as MASTER
  SPI.begin();
  // Initialise I2C communication as MASTER
  Wire.begin(4, 5);
  // Initialise Serial Communication, set baud rate = 9600
  Serial.begin(9600);
  delay(10);
  Serial.println('\n');

   // Start I2C Transmission
  Wire.beginTransmission(Addr);
  // Select control register
  Wire.write(0x2A);
  // StandBy mode
  Wire.write((byte)0x00);
  // Stop I2C Transmission
  Wire.endTransmission();

  // Start I2C Transmission
  Wire.beginTransmission(Addr);
  // Select control register
  Wire.write(0x2A);
  // Active mode
  Wire.write(0x01);
  // Stop I2C Transmission
  Wire.endTransmission();

  // Start I2C Transmission
  Wire.beginTransmission(Addr);
  // Select control register
  Wire.write(0x0E);
  // Set range to +/- 2g
  Wire.write((byte)0x00);
  // Stop I2C Transmission
  Wire.endTransmission();
  delay(300);
  
  WiFi.begin(ssid, password);             // Connect to the network
  Serial.print("Connecting to ");
  Serial.print(ssid); Serial.println(" ...");

  int i = 0;
  while (WiFi.status() != WL_CONNECTED) { // Wait for the Wi-Fi to connect
    delay(1000);
    Serial.print(++i); Serial.print(' ');
  }

  Serial.println('\n');
  Serial.println("Connection established!");  
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP());         // Send the IP address of the ESP8266 to the computer
}

void loop() {
unsigned int data[7];

  // Request 7 bytes of data
  Wire.requestFrom(Addr, 7);
  
  // Read 7 bytes of data
  // staus, xAccl lsb, xAccl msb, yAccl lsb, yAccl msb, zAccl lsb, zAccl msb
  if(Wire.available() == 7) 
  {
    data[0] = Wire.read();
    data[1] = Wire.read();
    data[2] = Wire.read();
    data[3] = Wire.read();
    data[4] = Wire.read();
    data[5] = Wire.read();
    data[6] = Wire.read();
  }

  // Convert the data to 12-bits
  int xAccl = ((data[1] * 256) + data[2]) / 16;
  if (xAccl > 2047)
  {
    xAccl -= 4096;
  }
    
  int yAccl = ((data[3] * 256) + data[4]) / 16;
  if (yAccl > 2047)
  {
    yAccl -= 4096;
  }
    
  int zAccl = ((data[5] * 256) + data[6]) / 16;
  if (zAccl > 2047)
  {
    zAccl -= 4096;
  }

  // Output data to serial monitor
  Serial.print("Acceleration in X-Axis : ");
  Serial.println(xAccl);
  Serial.print("Acceleration in Y-Axis : ");
  Serial.println(yAccl);
  Serial.print("Acceleration in Z-Axis : ");
  Serial.println(zAccl);

  String addAcc = url_add_acc + "?x_axis=" + xAccl + "&y_axis=" + yAccl + "&z_axis=" + zAccl;
  String getAction = url_get_action;

  // server authentication, insert user and password below
  //http.setAuthorization("REPLACE_WITH_SERVER_USERNAME", "REPLACE_WITH_SERVER_PASSWORD");

  // getting data from rest-api
  http.begin(client, getAction.c_str());
  int httpResponseCode = http.GET();
  
  if (httpResponseCode>0) {
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);
    String payload = http.getString();
    Serial.println(payload);
    SPI.transfer(payload[13]);
    // logic for tank controls
  }
  else {
    Serial.print("Error code: ");
    Serial.println(httpResponseCode);
  }
  
  // sending data to rest-api
  http.begin(client, addAcc.c_str());
  http.POST("");

  // getting values from hcsr04
  // float dist = check_distance();
  // Serial.println(dist);

  delay(100);
  
}