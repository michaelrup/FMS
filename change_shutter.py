#!/usr/bin/python
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

stepPins = [7,22,24,18]

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
file = open("/etc/openhab2/scripts/shutterstatus.txt", "r")
oldStatus = int(file.read())
file = open("/etc/openhab2/scripts/shutterstatus.txt", "w")

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

waitTime = 2 / float(1000)
stepNum = 55 * stepPerc 

# Initialise variables
stepCounter = 0

# Start main loop
for i in range(stepNum):
    for pin in range(0, 4):
        xpin = stepPins[pin]
        if seq[stepCounter][pin] != 0:
            GPIO.output(xpin, True)
        else:
            GPIO.output(xpin, False)
       
    stepCounter += stepDir

  # If we reach the end of the sequence
  # start again
    if (stepCounter >= stepCount):
        stepCounter = 0
    if (stepCounter < 0):
        stepCounter = stepCount + stepDir

  # Wait before moving on
    time.sleep(waitTime)
for pin in stepPins:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

GPIO.cleanup()
