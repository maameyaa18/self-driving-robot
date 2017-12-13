#!/usr/bin/env python3

from utilities import *

csL = ColorSensor('in1')
csR = ColorSensor('in3')
us = UltrasonicSensor()

assert us.connected, "Connect a single US sensor to any sensor port"
assert csL.connected, "Connect a color sensor to any sensor port"
assert csR.connected, "Connect right sensor"

def followLineTillButtonPress():
  csL.mode = 'COL-COLOR'
  csR.mode = 'COL-COLOR'
  us.mode='US-DIST-CM'
  while True:
    if button.any():
      break
    else:
      distance = us.value()/10
      if distance < 10:
        brakeToStopDriving()
      elif (csL.value() == 1 and csR.value() == 6):
        startTurning(-300, 0)
      elif (csL.value() == 3 or csR.value() == 3):
        brakeToStopDriving()
      elif (csL.value() == 5 or csR.value() == 5):
        brakeToStopDriving()
      else:
        startTurning(0, -300)
      

  brakeToStopDriving()
  
if __name__ == '__main__':
  followLineTillButtonPress()