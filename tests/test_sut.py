#!/usr/bin/env python

import unittest
#import grandma
from nose.tools import ok_, assert_false
from sample_sut import sut
from grandma.grandma import t_ways

def test_sut():
    """Use grandma to test the SUT."""

    data = {
        "p1": ["v1_1", "v1_2", "v1_3"],
        "p2": ["v2_1", "v2_2", "v2_3", "v2_4"],
        "p3": ["v3_1", "v3_2", "v3_3", "v3_4", "v3_5"]
        }

    constraints = []

    # 3-way test: with three parameters this is a full test
    tests = t_ways(data, 3)
    
    # run all the tests on the SUT
    for t in tests:
        ok_(sut(**t), '%s test failed!' % t)
    

def test_negative_sut():
    """Use grandma to test the SUT."""
    # also one negative test
    assert_false(sut("x", "y", "z")) 


