#!/usr/bin/env python

"""
This is a wrapper for the C function "jenny.c"

See http://burtleburtle.net/bob/math/jenny.html for
a description of jenny.

This script is based on a wrapper which I found here:
http://www.kimbly.com/blog/000340.html

I introduced the use of Python Dictionaries to ease automated test case 
creation.
"""

import re, sys
from subprocess import Popen, PIPE
import itertools
import collections


def find_dim_of_feat(readable_feature, dims):
    for dim in dims:
        for feat in dim:
            if feat == readable_feature:
                return dim
    raise "Unable to find feature '%s'" % readable_feature

    
def readable_feat_to_jenny_feat(dim, readable_feature, dims):
    """converts "feature name" to "1a" format """
    keys = dims.keys()
    dim_index = keys.index(dim)
    feat_index = dims[dim].index(readable_feature)
    return "%d%s" % (dim_index+1, chr(feat_index + ord('a')))
    raise "Unable to find feature '%s'" % readable_feature


def jenny_feat_to_readable_feat(jenny_feature, dims):
    """converts "1a" format to "feature name" """
    keys = dims.keys()
    pattern = re.compile('([0-9]+)([a-zA-Z]+)')
    dim_index, feature_index = pattern.match(jenny_feature).group(1, 2)
    dim = keys[int(dim_index) - 1]
    feature_name = dims[dim][ord(feature_index) - ord('a')]
    return dim, feature_name


def jenny_result_to_test(line, dims):
    """ converts "1a 2c 3d" to "(this one) (that one) (the other one)" """
    try:
        could_not_cover = 0
        if line.startswith("Could not cover tuple "):
            line = line[21:]
            could_not_cover = 1

        ret = {}
        for feature in line.strip(" ").rstrip("\r\n ").split(" "):
            dim, feature_name = jenny_feat_to_readable_feat(feature, dims)
            ret[dim] = feature_name

        if could_not_cover:
            sys.stderr.write("Could not cover tuple %s\n" % ret)
            return None

        return ret
    except:
        sys.stderr.write("Error parsing jenny output line: '%s'\n" % line)
        raise


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
    cmd = "./jenny/jenny -n%d" % arity
    # add dimensions to command line
    for k in keys:
        cmd += " %d" % len(dims[k])

    #for depender_feat, dependee_feat in reqs:
    #    for incompat_feat in find_dim_of_feat(dependee_feat, dims):
    #        if incompat_feat <> dependee_feat:
    #            incompats.append([depender_feat, incompat_feat])

    # add incompats to command line
    for inc in incompats:
        inc_keys = inc.keys()
        if len(inc_keys) > 0:
            # put single values into a list
            values = [[x] if (isinstance(x, basestring) or 
                not isinstance(x, collections.Iterable)) else x for x in inc.values()]
            inc_prod = itertools.product(*values)
            for n in inc_prod:
                cmd += ' -w' + ''.join(
                    [readable_feat_to_jenny_feat(x, n[i], dims) for i,x in enumerate(inc_keys)])

    p = Popen(cmd, shell=True, stdout=PIPE)
    jenny_tests = p.stdout.readlines()
    for test in jenny_tests:
        readable_test =  jenny_result_to_test(test, dims)
        tests.append(readable_test)
        #if readable_test <> None:
            #print readable_test

    #sys.stderr.write("Total test cases required: %d\n" % len(tests))
    return tests

