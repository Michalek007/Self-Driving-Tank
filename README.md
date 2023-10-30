# Self-Driving-Tank
Software for self driving tank. Embedded code for STM32 and ESP8266 + GUI (Flask app)

## API

Flask app (python) with GUI (js, html, css).
Allows to remote control of tank. Also it gathers data, saves in database and displays as graphs on website.

## STM

Code for microcontroller STM32F103C8T6 ARM Cortex M3 (C).
Controls motors and communicates with esp8266 by SPI connection.

## ESP

Code for microcontroller ESP8266 (C++). 
Reads data from MMA8452, communicates with stm32 and sends requests to api.


![image](https://github.com/Michalek007/Self-Driving-Tank/assets/101892382/c9fab7b8-7a9c-49ea-a827-c7ebed2c9c93)
