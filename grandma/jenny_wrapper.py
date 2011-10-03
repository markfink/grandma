#!/usr/bin/env python

"""
This is a wrapper for the jenny C extension.

I introduced Dictionaries to ease automated test case creation.
"""

import itertools
import collections
from jenny import jenny

def readable_feat_to_jenny_feat(dim, readable_feature, dims):
    """converts "feature name" to "1a" format """
    keys = dims.keys()
    dim_index = keys.index(dim)
    feat_index = dims[dim].index(readable_feature)
    return "%d%s" % (dim_index+1, chr(feat_index + ord('a')))
    raise "Unable to find feature '%s'" % readable_feature


def jenny_to_tests(tests, dims):
    """ converts "(0, 0, 0, 0, 2, 0, 5)" to real tests"""
    for t in tests:
        yield {d: dims[d][t[i]] for i,d in enumerate(dims.keys())}
    

def create_test_cases(dims, arity, incompats=[], reqs=[]):
    """
    dims is an array of arrays of feature names.

    incompats is an array of arrays of feature names.  The first feature in 
    each list should not be used with any of the subsequent features.

    reqs is an array of feature name pairs.  The first feature in each
    pair requires the second in the pair; meaning it is incompatible with
    all the other features in the same dimension as the second feature.

    arity=1 means test each feature at least once
    arity=2 means test each feature in combination with every other feature
    arity=3 means test all feature triples
    ... and so on.
    """
    tests = [] # the generated testcases
    keys = dims.keys()
    cmd = ['from_grandma', '-n%d' % arity]
    cmd += ['%d' % len(dims[k]) for k in keys]

    # add incompats to command line
    for inc in incompats:
        inc_keys = inc.keys()
        if len(inc_keys) > 0:
            # put single values into a list
            values = [[x] if (isinstance(x, basestring) or 
                not isinstance(x, collections.Iterable)) else x for x in inc.values()]
            inc_prod = itertools.product(*values)
            for n in inc_prod:
                cmd.append('-w' + ''.join(
                    [readable_feat_to_jenny_feat(x, n[i], dims) for i,x in enumerate(inc_keys)]))

    #print 'cmd: ' + str(cmd)
    jenny_tests = jenny(*cmd)
    
    # return generator
    return jenny_to_tests(jenny_tests, dims)

