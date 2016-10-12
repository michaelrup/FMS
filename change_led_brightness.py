#!/usr/bin/python

import wiringpi
import sys
import math

LED = 1 #PWM Pin in wiringPi
wiringpi.wiringPiSetup()
wiringpi.pinMode(LED, 2)


if len(sys.argv) == 1:
	sys.exit(1)

#if not (0 <= sys.argv[1] <= 100):
#        sys.exit(1)

val = int(float(sys.argv[1]) * 10.24)
val = math.fabs(val - 1024)


wiringpi.pwmWrite(LED, int(val))
file = open("/etc/openhab2/scripts/ledbrightness.txt", "w")
file.write(str(int(float(sys.argv[1]))))

