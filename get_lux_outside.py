#!/usr/bin/python
from tsl2561 import TSL2561 


if __name__ == "__main__":
	tsl = TSL2561(address = 0x29) #Sensor connected with GND to addr 
	print tsl.lux();


