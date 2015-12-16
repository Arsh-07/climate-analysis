#function to test temperature conversion
from temp_conversion import *
from nose.tools import *

def test_value():
	assert fahr_to_kelvin(20.0) == 266.4833333333333

def zero_kelvin():
	assert round (fahr_to_kelvin(-459.67),2) == 0.00

@raises(TypeError)
def test_temp_string():
	assert fahr_to_kelvin("Some Temperature")

@raises(TypeError)
def test_null_temp():
	assert fahr_to_kelvin()
