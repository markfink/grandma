#!/usr/bin/env python

from math import radians, sin


def sut_sin(x):
    """
    Sample SUT used to demonstrate heuristic test oracles.
    """
    result = sin(radians(x))
    
    print 'sin(%f) = %s' % (x, result)
    return result

