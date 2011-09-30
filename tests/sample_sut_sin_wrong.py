#!/usr/bin/env python

from math import radians, sin


def sut_sin_wrong(x):
    """
    Sample SUT used to demonstrate heuristic test oracles.
    """
    result = sin(radians(x)) * abs(sin(radians(x)))
    
    print 'sin(%f) = %s' % (x, result)
    return result

