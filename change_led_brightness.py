#!/usr/bin/python

# Importing libraries
import wiringpi
import sys
import math

# Exit if no brightness is specified
if len(sys.argv) == 1:
	sys.exit(1)

# Setup wiringPin in PWM mode
LED = 1     # PWM Pin in wiringPi notation
wiringpi.wiringPiSetup()
wiringpi.pinMode(LED, 2)

# Calculate new PWM frequency
val = int(float(sys.argv[1]) * 10.24)
val = math.fabs(val - 1024)

# Changing PWM frequency
wiringpi.pwmWrite(LED, int(val))

# Writing new brightness to storage file
file = open("/etc/openhab2/scripts/ledbrightness.txt", "w")
file.write(str(int(float(sys.argv[1]))))

