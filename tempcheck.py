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
        self.base = self._Q(round(value), self.unit)


    @property
    def fahrenheit(self):
        """ Returns Fahrenheit temperature value """
        if self.unit == self.ureg.degF:
            return self.base
        #ureg_unit = vars(self)[self.unit]
        return self.base.to(self.ureg.degF)

    @property
    def celsius(self):
        """ Returns Celcius temperature value """
        if self.unit == self.ureg.degC:
            return self.base
        return self.base.to(self.ureg.degC)

    @property
    def kelvin(self):
        """ Returns Kelvin temperature value """
        if self.unit == self.ureg.kelvin:
            return self.base
        return self.base.to(self.ureg.kelvin)

    @property
    def rankine(self):
        """ Returns Rankin temperature value """
        if self.unit == self.ureg.degR:
            return self.base
        return self.base.to(self.ureg.degR)

    def compare(self, unit, value):
        """ Compares self.base to given temperature """
        converted = self.base.to(unit)
        converted = self._Q(round(converted.magnitude), converted.units)
        if converted == value:
            return True
        else:
            return False


def main(argv):
    args = get_parser().parse_args(argv[1:])

    # Compare all values rounded to the ones place
    T_in = Temperature(args.Temp, args.InUnit)
    T_resp = Temperature(args.Response, args.ConvUnit)
    #print("Base: %s\nResponse: %s" % (T_in.base, T_resp.base))

    if T_in.compare(T_resp.unit, T_resp.base):
        print("correct")
    else:
        print("incorrect")
        sys.exit(1)



if __name__ == "__main__":
    sys.exit(main(sys.argv))
