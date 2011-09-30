from exceptions import ValueError
from collections import OrderedDict

data = {
    "p1": ["v1_1", "v1_2", "v1_3"],
    "p2": ["v2_1", "v2_2", "v2_3", "v2_4"],
    "p3": ["v3_1", "v3_2", "v3_3", "v3_4", "v3_5"]
}
    
def run_app(*args):
    """This is a sample app for demonstration purposes."""
    print 'keys: ' + str(data.keys())
    if len(args) <> 3:
        raise ValueError('The run_app function requires 3 parameters!')
    for p in range(3):
        print 'args: ' + str(args)
        if not(args[p] in data[data.keys()[p]]):
            raise ValueError('Parameter ' + args[p] +
                ' not in defined range of ' + data.keys()[p] + '!')
    return True

