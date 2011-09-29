import jenny_wrapper


def t_ways(dims, t=2, incompats={}, reqs={}):
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
