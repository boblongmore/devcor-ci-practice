#!/usr/bin/env python

import pytest
from devcor_app import add_values, subtract_values

def test_add_values():
    assert add_values(3,10) == 13

def test_subtract_values():
    assert subtract_values(10,5) == 5
