#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <Wire.h>
#include <SPI.h>

#include "hcsr04.h"

#define addr 0x1C

// put function declarations here:
void connectToWiFi(const char*, const char*);
void mma8452Init();

const char* ssid     = "DESKTOP-O2OLJ1H 8056";         // The SSID (name) of the Wi-Fi network you want to connect to
const char* password = "L5w7393^";     // The password of the Wi-Fi network
WiFiClient client;
HTTPClient http;
String servername = "http://192.168.97.253:5000";
String urlGetAction = servername + "/get_action/";
String urlAddAcc = servername + "/add_acc/";

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

  mma8452Init();
  connectToWiFi(ssid, password);
}

void loop() {
unsigned int data[7];

  // Request 7 bytes of data
  Wire.requestFrom(addr, 7);
  
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

  String addAcc = urlAddAcc + "?x_axis=" + xAccl + "&y_axis=" + yAccl + "&z_axis=" + zAccl;
  String getAction = urlGetAction;

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
}

// put function definitions here:
void connectToWiFi(const char* ssid, const char* password) {
  WiFi.begin(ssid, password);
   Serial.println("Connecting");
   while(WiFi.status() != WL_CONNECTED) {
     delay(500);
     Serial.print(".");
   }
   Serial.println("");
   Serial.print("Connected to WiFi network with IP Address: ");
   Serial.println(WiFi.localIP());
}

void mma8452Init(){
   // Start I2C Transmission
  Wire.beginTransmission(addr);
  // Select control register
  Wire.write(0x2A);
  // StandBy mode
  Wire.write((byte)0x00);
  // Stop I2C Transmission
  Wire.endTransmission();

  // Start I2C Transmission
  Wire.beginTransmission(addr);
  // Select control register
  Wire.write(0x2A);
  // Active mode
  Wire.write(0x01);
  // Stop I2C Transmission
  Wire.endTransmission();

  // Start I2C Transmission
  Wire.beginTransmission(addr);
  // Select control register
  Wire.write(0x0E);
  // Set range to +/- 2g
  Wire.write((byte)0x00);
  // Stop I2C Transmission
  Wire.endTransmission();
  delay(300);
}
