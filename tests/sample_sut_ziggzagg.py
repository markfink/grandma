#!/usr/bin/env python

#from math import radians, sin


def sut_ziggzagg(x):
    """
    Sample SUT used to demonstrate heuristic test oracles.
    """
    if x <= 90.0:
        result = float(x)/90.0
    elif 90.0 < x <= 270.0:
        result = 1.0 - float(x-90.0)/90
    elif 270.0 < x <= 360.0:
        result = -1.0 + float(x-270.0)/90
    else:
        result = 0.0
    
    #print 'sin(%f) = %s' % (x, result)
    return result

