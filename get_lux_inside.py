#!/usr/bin/python
from tsl2561 import TSL2561


if __name__ == "__main__":
	tsl = TSL2561() #Sensor connected with nothing to addr 
	print tsl.lux();


