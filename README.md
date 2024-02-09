# Self-Driving-Tank
Software for Self-driving-tank. Embedded code for STM32, ESP8266 and ESP32 + Flask app (rest-api)

## API

Flask application (Python, HTML, CSS, JS).
Allows user to remote control of tank via website. Handles requests, collects data in database and displays data in graphs & tables. 

## STM

Code for microcontroller STM32F103C8T6 ARM Cortex M3 (C).
Controls motors and communicates with esp8266 by SPI connection.

## ESP

Code for microcontroller ESP8266 (C++). 
Reads data from MMA8452 and HC-SR04, communicates with stm32 and sends POST & GET requests to api.

## RFID_RC522 & SERVO_TOF

Code for microcontroller ESP32 (C++).
Controls servo, gathers data from laser sensor and handles RFID MF RC522 module (authorisation).

![image](https://github.com/Michalek007/Self-Driving-Tank/assets/101892382/a7c24f63-60ce-4358-96c2-994baeed2ec9)
