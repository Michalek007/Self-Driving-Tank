#include "hcsr04.h"

float check_distance()
{
    digitalWrite(trigger_pin, LOW);
    delay(1);

    digitalWrite(trigger_pin, HIGH); //set the trigger high for 1ms
    delayMicroseconds(12); //minimum 10us pulse

    //reset back to 0
    digitalWrite(trigger_pin, LOW);

    int time_delay = pulseIn(echo_pin, 1);
    
    float distance = time_delay * sound_speed / 2; //distance in meters

    return distance / 100; // return in cm
}
