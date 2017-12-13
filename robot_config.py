#!/usr/bin/env python3
#The line above must be the first line in the file so the script can be run from Brickman

from ev3dev.ev3 import *
from time import sleep

###############################
# GLOBAL VARIABLES FOR MY ROBOT
###############################
lcd = Screen()                   # The EV3 display
rightMotor = LargeMotor('outA')  # The motor connected to the right wheel
leftMotor = LargeMotor('outD')   # The motor connected to the left wheel
mediumMotor = MediumMotor('outB')
button = Button()

  
