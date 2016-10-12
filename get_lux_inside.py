#!/usr/bin/python

# Import TSL2561 library
from tsl2561 import TSL2561

if __name__ == "__main__":
	tsl = TSL2561() # Setup 
	print tsl.lux() # Print current lux value


