#! /usr/bin/env python

from pylab import *
from os.path import basename
from sample_sut_ziggzagg import sut_ziggzagg

def draw_chart():
    """Draws sample chart"""
    title("Sample SUT ziggzagg(x)")
    xlabel('Angle')
    ylabel('ziggzagg(x)')

    x = xrange(0, 361)
    y = [sut_sin(i) for i in x] 
    
    plot(x, y, linewidth=1.0, color='r')

    axes().axis([0, None, None, None])
    axis('tight')

    #linestyle '--', '-.', ':', '_'
    grid(True, color='grey', alpha=0.25, linestyle=':')

    #legend(loc=0) # 0 for optimized legend placement

    savefig(basename(__file__).split('.')[0]+'.png')


if __name__ == '__main__':
    draw_chart()


