#!/usr/bin/python
from tsl2561 import TSL2561 


if __name__ == "__main__":
	tsl = TSL2561(address = 0x29) # Setup
	print tsl.lux() # Print current lux value


