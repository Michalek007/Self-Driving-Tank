/*
 * tank.c
 *
 *  Created on: Jun 14, 2023
 *      Author: Michał
 */

#include "tank.h"
#include "motor.h"

void turn_left(){
	right_forward();
	left_backward();
	// przerwanie
}
void turn_right(){
	left_forward();
	right_backward();
	// przerwanie
}
void move_forward(){
	left_forward();
 	right_forward();
	// przerwanie
}
void move_backward(){
	left_backward();
	right_backward();
	// przerwanie
}
