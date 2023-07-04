#include <Arduino.h>

#define sound_speed 3.43

//pin defines
#define echo_pin 0
#define trigger_pin 2

//returns the distance in cm
float check_distance();