/*
 * motor.c
 *
 *  Created on: Jun 14, 2023
 *      Author: Michał
 */


#include "motor.h"

void left_forward(){

	  HAL_GPIO_WritePin(GPIOB, GPIO_PIN_13, 0);
	  HAL_GPIO_WritePin(GPIOB, GPIO_PIN_14, 1);
}

void left_backward(){

	  HAL_GPIO_WritePin(GPIOB, GPIO_PIN_13, 1);
	  HAL_GPIO_WritePin(GPIOB, GPIO_PIN_14, 0);
}

void left_stop(){
	  HAL_GPIO_WritePin(GPIOB, GPIO_PIN_13, 0);
	  HAL_GPIO_WritePin(GPIOB, GPIO_PIN_14, 0);
}

void right_forward(){

	  HAL_GPIO_WritePin(GPIOA, GPIO_PIN_9, 1);
	  HAL_GPIO_WritePin(GPIOA, GPIO_PIN_10, 0);
}

void right_backward(){

	  HAL_GPIO_WritePin(GPIOA, GPIO_PIN_9, 0);
	  HAL_GPIO_WritePin(GPIOA, GPIO_PIN_10, 1);
}

void right_stop(){
	  HAL_GPIO_WritePin(GPIOA, GPIO_PIN_9, 0);
	  HAL_GPIO_WritePin(GPIOA, GPIO_PIN_10, 0);
}
