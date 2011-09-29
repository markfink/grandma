#!/usr/bin/env python

from math import radians, sin


def sut_sin_error(x):
    """
    Sample SUT used to demonstrate heuristic test oracles.
    """
    if x < 120.0 or 140.0 <= x:
        result = sin(radians(x))
    else:
        result = -sin(radians(x))
    
    #print 'sin(%f) = %s' % (x, result)
    return result

