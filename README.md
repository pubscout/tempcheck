# tempcheck
Temperature conversion validation

Validates a given temperature and temperature unit
(Fahrenheit, Celsius, Kelvin or Rankine) has been
converted correctly.

The script will convert a given temperature and unit
to the desired unit and compare it to the given
temperature, reporting if the given temperature is
correct or not. All values given and generated
are rounded to the ones place.

Depends on Pint:

pip install pint

Usage:
 tempcheck.py [-h] Temp InUnit ConvUnit Response

 Temp     - Base temperature to convert
 InUnit   - Base temperature unit
 ConvUnit - Unit to convert to
 Response - Student's response to validate

Examples:
 python tempcheck.py -45.14 Celsius Kelvin 227.51
  --> correct

 python tempcheck.py 444.5 Rankine Celsius -30.5
  --> incorrect



Unit tests live in temptest.py:
 pytest -v temptest.py
