#!/usr/bin/python

# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Define used GPIO pins
GPIO.setmode(GPIO.BOARD)
stepPins = [7,22,24,18]

# Set all pins to false
for pin in stepPins:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

# Define advanced sequence
# as shown in manufacturers datasheet
seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]
       
stepCount = len(seq)

# Set to 1 or 2 for clockwise
# Set to -1 or -2 for anti-clockwise

# Read old shutter status
file = open("/etc/openhab2/scripts/shutterstatus.txt", "r")
oldStatus = int(file.read())

file = open("/etc/openhab2/scripts/shutterstatus.txt", "w")

# Parses the command-line arguments and defines the direction and
# number of steps for the motor
if len(sys.argv)>2:
    stepPerc = int(sys.argv[2])                     
    if sys.argv[1] == "f": 
        stepDir = -2                                
        if oldStatus + stepPerc > 100: 
            stepPerc = 100 - oldStatus
            file.write("100")                       
        else:
            file.write(str(oldStatus + stepPerc))
    elif sys.argv[1] == "b": 
        stepDir = 2
        if oldStatus - stepPerc < 0: 
            stepPerc = oldStatus
            file.write("0")
        else:
            file.write(str(oldStatus - stepPerc))
else:
    sys.exit(1) 

# Define the wait time inbetween steps
waitTime = 2 / float(1000)

# Define the number of steps
stepNum = 55 * stepPerc 

stepCounter = 0

# Move the motor for stepNum steps in stepDir direction
for i in range(stepNum):
    for pin in range(0, 4):
        xpin = stepPins[pin]
        if seq[stepCounter][pin] != 0:
            GPIO.output(xpin, True)
        else:
            GPIO.output(xpin, False)
       
    stepCounter += stepDir

    if (stepCounter >= stepCount):
        stepCounter = 0
    if (stepCounter < 0):
        stepCounter = stepCount + stepDir

  # Wait after a step
    time.sleep(waitTime)

# Cleanup GPIO pins
for pin in stepPins:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

GPIO.cleanup()
