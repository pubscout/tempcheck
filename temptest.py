#!/usr/bin/env python3

import tempcheck as TemperatureClass
import unittest

class TemperatureTest(unittest.TestCase):

    def test_correct1(self):
        T_in = TemperatureClass.Temperature(round(84.2), 'fahrenheit')
        T_resp = TemperatureClass.Temperature(round(543.5), 'rankine')
        self.assertTrue(T_in.compare(T_resp.unit, T_resp.base))
        
    def test_correct2(self):
        T_in = TemperatureClass.Temperature(round(-45.14), 'celsius')
        T_resp = TemperatureClass.Temperature(round(227.51), 'kelvin')
        self.assertTrue(T_in.compare(T_resp.unit, T_resp.base))
        
    def test_incorrect1(self):
        T_in = TemperatureClass.Temperature(round(-317.33), 'kelvin')
        T_resp = TemperatureClass.Temperature(round(110.5), 'fahrenheit')
        self.assertFalse(T_in.compare(T_resp.unit, T_resp.base))
        

if __name__ == '__main__':
    unittest.main()
