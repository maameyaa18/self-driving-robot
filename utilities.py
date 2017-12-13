#!/usr/bin/env python3
#The line above must be the first line in the file so the script can be run from Brickman

from robot_config import * 

###############################
# A SET OF USEFUL 'UTILITY' FUNCTIONS FOR DISPLAYING INFO
###############################

# Print some given text on the LCD display on a given line number and a given indentation level
# (the height of a line and width of an ident are set at 10 pixels each)
def print2Screen(lineNum, indent, text):
  lcd.draw.text((10*indent, 10*lineNum), text)
  lcd.update()  

# Print a warning message both to the LCD display and the terminal
def giveWarning(message):
  message = "WARNING: "+message
  print2Screen(10, 0, message)
  print(message) 

# Print an error message both to the LCD display and the terminal
def giveError(message):
  message = "ERROR: "+message
  print2Screen(11, 0, message)
  print(message) 

###############################
# A SET OF USEFUL 'UTILITY' FUNCTIONS FOR MOVEMENT
###############################

# Start the motor moving straight at a desired speed (forward if speed is positive and backwards
# if speed is negative), provided the speeds are within safe limits
def startDrivingStraight(desiredSpeed):
  if (desiredSpeed <= 1000 and desiredSpeed >= -1000):
    leftMotor.run_forever(speed_sp=desiredSpeed)
    rightMotor.run_forever(speed_sp=desiredSpeed)
  else:
    giveError("Trying to drive too fast")
    sleep(5)

def startTurning(desiredSpeedLeft, desiredSpeedRight):
  if (desiredSpeedLeft <= 1000 and desiredSpeedLeft >= -1000 and 
      desiredSpeedRight <= 1000 and desiredSpeedRight >= -1000):
    leftMotor.run_forever(speed_sp=desiredSpeedLeft)
    rightMotor.run_forever(speed_sp=desiredSpeedRight)
  else:
    giveError("Trying to turn too fast")
    sleep(5)
    
def coastToStopDriving():
  rightMotor.stop(stop_action='coast')
  leftMotor.stop(stop_action='coast')
  
def brakeToStopDriving():
  rightMotor.stop(stop_action='brake')
  leftMotor.stop(stop_action='brake')
  
  
###############################
# TEST SCRIPTS
###############################

# Test displaying messages on the LCD screen
def testDisplay():
  print("Testing display")
  print2Screen(0, 0, "hello world")
  print2Screen(1, 0, "how are you doing today?")
  print2Screen(2, 1, "fine, thanks")
  sleep(5)
  print("Done with display test")

# Test various movements
def testMovement():
  print("Testing movement")
  startDrivingStraight(700)
  sleep(3)
  brakeToStopDriving()
  sleep(3)
  startDrivingStraight(-350)
  sleep(3)
  coastToStopDriving()
  sleep(3)
  startTurning(500, 200)
  sleep(3)
  startTurning(-200, 200)
  sleep(3)
  brakeToStopDriving()
  print("Done with movement test")
  
  # Function to cap a certain amount of speed
def capSpeed(speed, maxSpeed):
  if (speed > maxSpeed):
    speed = maxSpeed
  elif (speed <-maxSpeed):
    speed = maxSpeed
  return speed 

#Function to control amr grabbing

def grabObject(m,open_speed,close_speed,move):
  m.run_to_rel_pos(position_sp=open_speed, speed_sp=200, stop_action="brake")
  m.wait_while('running')
  leftMotor.run_to_rel_pos(position_sp= move, speed_sp=200, stop_action="brake")
  rightMotor.run_to_rel_pos(position_sp=move, speed_sp=200, stop_action="brake")
  leftMotor.wait_while('running')
  rightMotor.wait_while('running')
  m.run_to_rel_pos(position_sp=-close_speed, speed_sp=200, stop_action="brake")
  m.wait_while('running')
  


def calculateError(xValue,camMid):
  error = xValue - camMId
  return error

  
def spinToSearch(enc):
  leftMotor.run_to_rel_pos(position_sp=enc, speed_sp= 100, stop_action="brake")
  rightMotor.run_to_rel_pos(position_sp=-enc, speed_sp=100, stop_action="brake")
  
  

  
  
  

  
# Test script
if __name__ == '__main__':
  print("Starting testing")
  testDisplay()
  testMovement()
  print("Done with testing")
  
