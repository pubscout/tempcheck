#!/usr/bin/env python

import sys
import argparse
import pint

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

def get_parser():
    """ Get a command line parser """
    parser = argparse.ArgumentParser()
    parser.add_argument("Temp", help='Base temperature to convert', type=float)
    parser.add_argument("InUnit", help='Base temperature unit')
    parser.add_argument("ConvUnit", help='Converted temperature unit')
    parser.add_argument("Response", help='Converted temperature', type=float)

    return parser


def main(argv):
    args = get_parser().parse_args(argv[1:])
    inTmp    = args.Temp
    inUnit   = args.InUnit
    convUnit = args.ConvUnit
    respTmp  = args.Response
    print(args)
    print("%s %s %s %s" % (inTmp, inUnit, convUnit, respTmp))

    if inUnit in ['F', 'f', 'Fahrenheit', 'fahrenheit']:
	home = Q_(inTmp, ureg.degF)
    elif inUnit in ['C', 'c', 'Celsius', 'celsius']:
	home = Q_(inTmp, ureg.degC)
    elif inUnit in ['K', 'k', 'Kelvin', 'kelvin']:
	home = Q_(inTmp, ureg.kelvin)
    elif inUnit in ['R', 'r', 'Rankine', 'rankine']:
	home = Q_(inTmp, ureg.degR)
    else:
        # Invalid/unsupported temperature unit
        print("Invalid")
        sys.exit(1)

    if convUnit in ['F', 'f', 'Fahrenheit', 'fahrenheit']:
	#Convert to Fahrenheit 
	convTmp = home.to('degF')
        resp_ureg = Q_(respTmp, ureg.degF)
    elif convUnit in ['C', 'c', 'Celsius', 'celsius']:
	#Convert to Celsius 
	convTmp = home.to('degC')
        resp_ureg = Q_(respTmp, ureg.degC)
    elif convUnit in ['K', 'k', 'Kelvin', 'kelvin']:
	#Convert to Kelvin
	convTmp = home.to('kelvin')
        resp_ureg = Q_(respTmp, ureg.kelvin)
    elif convUnit in ['R', 'r', 'Rankine', 'rankine']:
	#Convert to Rankine
	convTmp = home.to('degR')
        resp_ureg = Q_(respTmp, ureg.degR)
    else:
        # Invalid/unsupported temperature unit
        print("Invalid")
        sys.exit(1)

    print("home:  %s" % home)
    print("resp_ureg: %s" % resp_ureg)
    print("convTmp: %s" % convTmp)

    if (resp_ureg == convTmp):
        print("correct")
    else:
        print("incorrect")


if __name__ == "__main__":
    sys.exit(main(sys.argv))

