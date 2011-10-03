from exceptions import ValueError

data = {
    'font': ['arial', 'tahoma', 'brushScript', 'monotypeCorsive'],
    'bold':   [True, False],
    'italic': [True, False],
    'strikethrough': [True, False],
    'underline': [True, False],
    'color': ['black', 'yellow', 'white', 'blue', 'red', 'green'],
    'size': ['small', 'nominal', 'large', 'xLarge', 'xxLarge', 'xxxLarge', 'ridiculouslyLarge']
}

    
def run_app(**params):
    """This is a simple sample app for demonstration purposes."""
    for p in params.keys():
        if not(params[p] in data[p]):
            raise ValueError('Parameter ' + params[p] +
                ' not in defined range of ' + p + '!')
    return True

