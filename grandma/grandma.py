#!/usr/bin/env python

"""
grandma is a collection of testing tools and it is all about simplicity.
The name was given in admiration of a woman who repeatedly walked the Appalachian trail
with little concern about the hiking gear she used (Emma Rowena Gatewood).
If I remember right, instead of a backpack she used a laundry-bag and
instead of a tent she used a plastic shower curtain. In this way she 
invented the ultralight backpacking movement.

TODO:
o equivalence partitioning
o boundary-value analysis
o heuristics
o priority (give me the next 100 testcases with prio 3)


Automated Combinatorial Test Methods - Beyond Pairwise Testing,
D. Richard Kuhn and Dr. Raghu Kacker, National Institute of Standards and Technology

With the NASA application, for example, 
67 percent of the failures were triggered by only a single parameter value, 
93 percent by 2-way combinations, and 
98 percent by 3-way combinations. The detection rate curves for the other
applications are similar, reaching 
100 percent detection with 4-way to 6-way interactions.
"""

from random import randint
import itertools
#import collections
from collections import OrderedDict
#from grandma 
import jenny_wrapper

def run_constraints(results, constraints):
    """
    Run the constraints on the testcases to identify the 'type' of the 
    test case (positive test/ negative test)
    """
    for r in results:
        # check constraints
        r['_negative'] = False
        for c in constraints:
            if not eval(c, dict(__builtins__=None, True=True, False=False), r):
                r['_negative'] = True
    
    return results


def pairwise(input):
    """Determine all pairs based on the covering array"""
    

def combine(input):
    """Deliver all pairs"""
    keys = input.keys()
    result = []
    length = 0
    for k in keys:
        length = max(length, len(input[k]))
        # transfere into cyclic iterator
        input[k] = itertools.cycle(input[k])
    # now create the combinations
    for i in xrange(0,length):
        r = {}
        for k in keys:
            r[k] = input[k].next()
        result.append(r)
        #result.append({x: input[x].next() for x in keys})
    return result


def combine_t_way(way, input):
    return combine(input)


def all_pairs(data, constraints):
    """
    Run combinatorial analysis on your imput data and apply the given
    constraints.
    """

    # equivalence classes
    # full set
    # all pairs

    # start, end, and one in the middle
    input = {}
    keys = data.keys()

    for k in keys:
        input[k] = []
        for v in data[k]:
            sme = [] # start, middle, end
            if (isinstance(v, basestring) or 
                not isinstance(v, collections.Iterable)):
                sme = v
            elif len(v) <= 3:
                sme = v
            else:
                sme = [v[0]] # first
                sme.append(v[randint(1,len(v)-3)]) # middle
                sme.append(v[-1]) # last
            input[k].append(sme)

    result = combine(input)
    
    return run_constraints(result, constraints)


def t_ways(dims, t=6, incompats={}, reqs={}):
    """Hand over the testcase creation to jenny."""
    return jenny_wrapper.create_test_cases(dims, t, incompats=incompats, reqs=reqs)   


def main():
    """Demonstrate the use of the test generator"""
    # helpers
    #h = {
    #    'small': xrange(0, 9),
    #    'nominal': xrange(10, 14),
    #    'large': xrange(15, 24),
    #    'xLarge': xrange(25, 48),
    #    'xxLarge': xrange(49, 72),
    #    'xxxLarge': xrange(73, 255),
    #    'ridiculouslyLarge': xrange(256, 1638)}

    """dims = {
        'font': ['arial', 'tahoma', 'brushScript', 'monotypeCorsive'],
        'bold':   [True, False],
        'italic': [True, False],
        'strikethrough': [True, False],
        'underline': [True, False],
        'color': ['black', 'yellow', 'white', 'blue', 'red', 'green'],
        'size': ['small', 'nominal', 'large', 'xLarge', 'xxLarge', 'xxxLarge', 'ridiculouslyLarge']
    }"""
    dims = OrderedDict({
        'font': ['arial', 'tahoma', 'brushScript', 'monotypeCorsive'],
        'bold':   [True, False],
        'italic': [True, False],
        'strikethrough': [True, False],
        'underline': [True, False],
        'color': ['black', 'yellow', 'white', 'blue', 'red', 'green'],
        'size': ['small', 'nominal', 'large', 'xLarge', 'xxLarge', 'xxxLarge', 'ridiculouslyLarge']
    })
    
        #[h['small'], h['nominal'], h['large'], h['xLarge'],
        #    h['xxLarge'], h['xxxLarge'], h['ridiculouslyLarge']]}

    #incompats = []      
    # separate positive from negative tests
    #constraints = [
    #    "False if font == 'brushScript' and italic == False and bold == True else True",
    #    "False if font == 'monotypeCorsive' and bold != italic else True",
    #    "False if bold == True else True"]
    #incompats = [{'font': ['brushScript', 'monotypeCorsive'], 'italic': False, 'bold': True},
    #            {'font': 'monotypeCorsive', 'italic': True, 'bold': False}]
    incompats = [
        OrderedDict({'font': ['brushScript', 'monotypeCorsive'], 'italic': False, 'bold': True}),
        OrderedDict({'font': 'monotypeCorsive', 'italic': True, 'bold': False})]
        
    reqs = []
    
    testcases = t_ways(dims, 5, incompats=incompats, reqs=reqs)
    #print testcases
    for t in testcases:
        print t


if __name__ == '__main__':
    main()
