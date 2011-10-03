import itertools as it
from functools import partial
from operator import itemgetter, and_, or_, concat
from random import sample


"""
So far I have not been able to replace the jenny.c program since the algorithm is better (compacter solution) and it is still way faster.
But I decided to keep this solution arround so that I can continue the work later.

jenny.c:
1601 solutions, 0m1.104s

Combinatorial Testing Algorithm in Python:
1884 solutions, 0m46.263s

Here a short overview about the current algorithm:

A testcase can cover one or more tests. The problem is to find an optimal
solution consisting of a minimal set of testcases which cover all tests.

o Start with an empty set of testcases
o Take one test and see if it is NOT incompatible, then
    o Go through the set of testcases and see if it is already covered
    o If it is not covered then add it to the testcase where it fits best
      (most of the features are already covered and it does not render
      the testcase incompatible)
"""

def t_ways(dims, t=2, incompats={}, reqs={}):
    """Hand over the testcase creation to jenny."""
    # if dims is smaller than t then use dims
    t = min(len(dims), t)
    
    def get_products(keys):
        # helper to get products from keys in the following form:
        # [('bold', True), ('color', 'black')]
        values  = itemgetter(*keys)(dims)
        product = it.product(*values)
        return map(partial(zip, keys), product)
            

    def check_incompatible(test):
        # check wether the test has an incompatibility
        # {'font': ['brushScript', 'monotypeCorsive'], 'italic': False, 'bold': True}
        # [('bold', True), ('color', 'black')]

        for i in incompats:
            # does the test match?
            if reduce(and_, ( (test.has_key(k) and (test[k]==i[k] or 
                                isinstance(i[k], (list)) and test[k] in i[k]))
                             for k in i.keys() )):
                #print 't'
                return True
        # TODO: check for sufficient 'Freiheitsgrade'
        #print 'f'
        return False

        
    def insert_test(test):
        # insert the if it is not already covered
        best = len(test)+1
        position = None
                
        for i,tc in enumerate(testcases):
            # check if a merge is possible
            # it can not be merged if the overlapping features differ
            if reduce(or_, ( (test.has_key(k) and test[k] != tc[k]) for k in tc.keys() )):
                continue
            # conjunct
            conj = test.copy()
            conj.update(tc)
            
            # see if it already contained (also not incompatible!)
            if len(conj) == len(tc):
                return
            
            # the test is not contained 
            # find the best fit that is not an incompatibility
            if check_incompatible(conj):
                continue
            else:
                dist = len(conj) - len(tc)
                if dist <= best:
                    best = dist
                    position = i
         
        # insert the test
        if position == None:
            testcases.append(test)
        else:
            testcases[position].update(test)
         

    def get_feature_incompats(tc, feature):
        # get the incompatibilities for a feature
        # does testcase + feature match a incompat then return the 
        # members of the feature
        res = []
        for i in incompats:
            if not i.has_key(feature):
                continue
            if reduce(and_, ( (tc.has_key(k) and (tc[k]==i[k] or 
                                isinstance(i[k], (list)) and tc[k] in i[k])) 
                             for k in i.keys() if k != feature)):
                res.append(i[feature])
        return res


    # list all the combinations
    # get someting like the following:
    # [('bold', 'color'), ('bold', 'strikethrough')
    comb = it.combinations(dims, t)
    
    # generate all the tests from the combinations
    tests = it.chain.from_iterable(it.imap(get_products, comb))

    # start with an empty set of testcases
    testcases = [] # each testcase is a dictionary
    
    # all tests must be covered by testcases
    for t in tests:
        # if a test has incompatibilities it is ignored
        test = dict(t)
        if not check_incompatible(test):
            insert_test(test)
    
    # fill up the testcases by avoiding incompatibilities
    for tc in testcases:
        for f in dims.keys():
            if not tc.has_key(f):
                d = dims[f]
                if not isinstance(d, (list)):
                    d = [d]
                d = [x for x in d if not x in get_feature_incompats(tc, f)]
                tc[f] = sample(d, 1)[0]

    return testcases


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

    dims = {
        'font': ['arial', 'tahoma', 'brushScript', 'monotypeCorsive'],
        'bold':   [True, False],
        'italic': [True, False],
        'strikethrough': [True, False],
        'underline': [True, False],
        'color': ['black', 'yellow', 'white', 'blue', 'red', 'green'],
        'size': ['small', 'nominal', 'large', 'xLarge', 'xxLarge', 'xxxLarge', 'ridiculouslyLarge']
    }
    
        #[h['small'], h['nominal'], h['large'], h['xLarge'],
        #    h['xxLarge'], h['xxxLarge'], h['ridiculouslyLarge']]}

    incompats = []      
    # separate positive from negative tests
    #constraints = [
    #    "False if font == 'brushScript' and italic == False and bold == True else True",
    #    "False if font == 'monotypeCorsive' and bold != italic else True",
    #    "False if bold == True else True"]
    incompats = [{'font': ['brushScript', 'monotypeCorsive'], 'italic': False, 'bold': True},
                {'font': 'monotypeCorsive', 'italic': True, 'bold': False}]
        
    reqs = []
    
    #testcases = t_ways(dims, 5, incompats=incompats, reqs=reqs)
    testcases = t_ways(dims, 6, incompats=incompats, reqs=reqs)
    #print testcases
    #for i in testcases:
    #    for x in i:
    #        print list(x)
    for t in testcases:
        print t
    print len(testcases)


if __name__ == '__main__':
    main()
