#!/usr/bin/env python3

import sys
import argparse
import pint

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
    in_tmp = args.Temp
    in_unit = args.InUnit
    conv_unit = args.ConvUnit
    resp_tmp = args.Response
    ureg = pint.UnitRegistry()
    _Q = ureg.Quantity

    #print("%s %s %s %s" % (in_tmp, in_unit, conv_unit, resp_tmp))

    if in_unit in ['F', 'f', 'Fahrenheit', 'fahrenheit']:
        home = _Q(in_tmp, ureg.degF)
    elif in_unit in ['C', 'c', 'Celsius', 'celsius']:
        home = _Q(in_tmp, ureg.degC)
    elif in_unit in ['K', 'k', 'Kelvin', 'kelvin']:
        home = _Q(in_tmp, ureg.kelvin)
    elif in_unit in ['R', 'r', 'Rankine', 'rankine']:
        home = _Q(in_tmp, ureg.degR)
    else:
        # Invalid/unsupported temperature unit
        print("Invalid")
        sys.exit(1)

    if conv_unit in ['F', 'f', 'Fahrenheit', 'fahrenheit']:
        #Convert to Fahrenheit
        conv_tmp = home.to('degF')
        resp_ureg = _Q(resp_tmp, ureg.degF)
    elif conv_unit in ['C', 'c', 'Celsius', 'celsius']:
        #Convert to Celsius
        conv_tmp = home.to('degC')
        resp_ureg = _Q(resp_tmp, ureg.degC)
    elif conv_unit in ['K', 'k', 'Kelvin', 'kelvin']:
        #Convert to Kelvin
        conv_tmp = home.to('kelvin')
        resp_ureg = _Q(resp_tmp, ureg.kelvin)
    elif conv_unit in ['R', 'r', 'Rankine', 'rankine']:
        #Convert to Rankine
        conv_tmp = home.to('degR')
        resp_ureg = _Q(resp_tmp, ureg.degR)
    else:
        # Invalid/unsupported temperature unit
        print("Invalid")
        sys.exit(1)

    print("home:  %s" % home)
    print("resp_ureg: %s" % resp_ureg)
    print("conv_tmp: %s" % conv_tmp)

    if resp_ureg == conv_tmp:
        print("correct")
    else:
        print("incorrect")
        sys.exit(1)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
