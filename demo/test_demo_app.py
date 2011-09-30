#!/usr/bin/env python

import unittest
#from nose.tools import ok_
from collections import OrderedDict
from grandma.grandma import t_ways
from demo_app import run_app


def oracle_demo_app(p1, p2, p3):
    """Demo the use of an oracle"""
    return True

def check_one_case(args):
    """Helper function calling demo app and oracle"""
    res = run_app(*args)
    ocl = oracle_demo_app(*args)
    assert res == ocl


def test_luschi():
    """This is a very weak test since it only contains on sample set of parameters."""
    check_one_case(['v1_1', 'v2_2', 'v3_3'])


def test_powerfull():
    """This is a very powerfull test ."""

    spec = OrderedDict({
        "p1": ["v1_1", "v1_2", "v1_3"],
        "p2": ["v2_1", "v2_2", "v2_3", "v2_4"],
        "p3": ["v3_1", "v3_2", "v3_3", "v3_4", "v3_5"]
    })
    tests = t_ways(spec, 3)
    #tests = [('v1_1', 'v2_2', 'v3_3'), ('v1_1', 'v2_2', 'v3_3'), ('v1_1', 'v2_2', 'v3_3')]

    for t in tests:
        print 'test: ' + str(t)
        yield check_one_case, t.values()

