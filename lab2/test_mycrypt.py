#!/usr/bin/python
# -*- coding: utf-8
#Pasanen Leena
'''
Unit tests for mycrypt function. Basically ROT13, but also
capitalize or uncapitalize, and for numbers, replace with shifted
versions.

tr 'A-Za-z0-9=!"#€%&/()' 'n-za-mN-ZA-M=!"#€%&/()0-9'

If characters outside allowed ones are used as input, raise ValueError.
'''

import timeit
import pytest #Make sure you have th 'pytest' library installed in your Python environment ('pip install pytest')
import mycrypt


@pytest.mark.parametrize("test_input,expected", [
    ("a", "N"),
    ("b", "O"),
    ("abc", "NOP"),
    ("abc123", 'NOP!"#'),
    ("4", u'€')
])
def test_encode(test_input, expected):
    '''Verify that strings given above match the expected results'''
    assert(mycrypt.encode(test_input)) == expected


@pytest.mark.parametrize("test_input", [
    '123', '!"#','abc'])
def test_encode_decode(test_input):
    '''Verify that decoding an encoded string returns original string'''
    assert(mycrypt.decode(mycrypt.encode(test_input))) == test_input


@pytest.mark.parametrize("invalid_input", ['+','å','ä','ö'])
def test_invalid_char(invalid_input):
    '''Invalid characters should result in ValueError'''
    with pytest.raises(ValueError):
        mycrypt.encode(invalid_input)


@pytest.mark.parametrize("invalid_input",[1,[1,2],1.15])#Modify this list to include other invalid types
def test_invalid_types(invalid_input):
    '''Invalid parameter types should raise TypeError'''
    with pytest.raises(TypeError):
        mycrypt.encode(invalid_input)

@pytest.mark.parametrize("invalid_input", ["2"*2000,"3"*1500]) #Add test_lengths
def test_length(invalid_input):
    '''Invalid input length should result in ValueError'''
    with pytest.raises(ValueError):
        mycrypt.encode(invalid_input)

def test_timing():
    '''Test whether encoding runs in approximately constant time'''
    single_char_time = timeit.timeit(
        stmt='mycrypt.encode("a"*1000)',
        setup='import mycrypt',
        number=1000
    )
    long_string_time = timeit.timeit(
        stmt='mycrypt.encode("a"*1000000)',
        setup='import mycrypt',
        number=1000
    )
    assert single_char_time < long_string_time * 1.1  # Checking if the time scales roughly linearly
