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


class Temperature():
    """
    Class defining temperature conversions
    """
    def __init__(self, value, unit):
        if unit in ['F', 'f', 'Fahrenheit', 'fahrenheit']:
            self.unit = 'degF'
        elif unit in ['C', 'c', 'Celsius', 'celsius']:
            self.unit = 'degC'
        elif unit in ['K', 'k', 'Kelvin', 'kelvin']:
            self.unit = 'kelvin'
        elif unit in ['R', 'r', 'Rankine', 'rankine']:
            self.unit = 'degR'
        else:
            # Invalid/unsupported temperature unit
            print("invalid")
            sys.exit(1)

        self.ureg = pint.UnitRegistry()
        self._Q = self.ureg.Quantity
        # Ensure given value is in a 'pint forma/precision'
        self.base = self._Q(value, self.unit)


    @property
    def fahrenheit(self):
        """ Returns Fahrenheit temperature value """
        if self.unit == self.ureg.degF:
            return self.base
        #ureg_unit = vars(self)[self.unit]
        print("Converting %s to %s" % (self.base, self.ureg.degF))
        return self.base.to(self.ureg.degF)

    @property
    def celsius(self):
        """ Returns Celcius temperature value """
        if self.unit == self.ureg.degC:
            return self.base
        print("Converting %s to %s" % (self.base, self.ureg.degC))
        return self.base.to(self.ureg.degC)

    @property
    def kelvin(self):
        """ Returns Kelvin temperature value """
        if self.unit == self.ureg.kelvin:
            return self.base
        print("Converting %s to %s" % (self.base, self.ureg.kelvin))
        return self.base.to(self.ureg.kelvin)

    @property
    def rankin(self):
        """ Returns Rankin temperature value """
        if self.unit == self.ureg.degR:
            return self.base
        print("Converting %s to %s" % (self.base, self.ureg.degR))
        return self.base.to(self.ureg.degR)


def main(argv):
    args = get_parser().parse_args(argv[1:])
    in_tmp = args.Temp
    in_unit = args.InUnit
    conv_unit = args.ConvUnit
    resp_tmp = args.Response

    T_in = Temperature(in_tmp, in_unit)
    T_resp = Temperature(resp_tmp, conv_unit)
    print(T.fahrenheit)
    print(T.celsius)
    print(T.kelvin)
    print(T.rankin)

    #print("%s %s %s %s" % (in_tmp, in_unit, conv_unit, resp_tmp))
"""
    print("home:  %s" % home)
    print("resp_ureg: %s" % resp_ureg)
    print("conv_tmp: %s" % conv_tmp)

    if resp_ureg == conv_tmp:
        print("correct")
    else:
        print("incorrect")
        sys.exit(1)
"""


if __name__ == "__main__":
    sys.exit(main(sys.argv))
