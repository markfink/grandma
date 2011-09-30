#! /usr/bin/env python

from pylab import *
from os.path import basename
from sample_sut_sin_wrong import sut_sin_wrong

def draw_chart():
    """Draws sample chart"""
    title("Sample SUT sin(x)")
    xlabel('Angle')
    ylabel('sin(x)')

    x = xrange(0, 361)
    y = [sut_sin(i) for i in x] 
    
    plot(x, y, linewidth=1.0, color='orange')

    axes().axis([0, None, None, None])
    axis('tight')

    #linestyle '--', '-.', ':', '_'
    grid(True, color='grey', alpha=0.25, linestyle=':')

    #legend(loc=0) # 0 for optimized legend placement

    savefig(basename(__file__).split('.')[0]+'.png')


if __name__ == '__main__':
    draw_chart()


