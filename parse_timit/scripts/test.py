#!/usr/bin/env python
"""
This is a small demo file that helps teach how to adjust figure sizes
for matplotlib

"""

import matplotlib
print "using MPL version:", matplotlib.__version__
matplotlib.use("WXAgg") # do this before pylab so you don'tget the default back end.

import pylab
import matplotlib.numerix as N

# Generate and plot some simple data:
x = N.arange(0, 2*N.pi, 0.1)
y = N.sin(x)

pylab.plot(x,y)
F = pylab.gcf()

# Now check everything with the defaults:
DPI = F.get_dpi()
print "DPI:", DPI
DefaultSize = F.get_size_inches()
print "Default size in Inches", DefaultSize
print "Which should result in a %i x %i Image"%(DPI*DefaultSize[0], DPI*DefaultSize[1])
# the default is 100dpi for savefig:
F.savefig("test1.png")
# this gives me a 797 x 566 pixel image, which is about 100 DPI

# Now make the image twice as big, while keeping the fonts and all the
# same size
F.set_size_inches( (DefaultSize[0]*2, DefaultSize[1]*2) )
Size = F.get_size_inches()
print "Size in Inches", Size
F.savefig("test2.png")
# this results in a 1595x1132 image

# Now make the image twice as big, making all the fonts and lines
# bigger too.

F.set_size_inches( DefaultSize )# resetthe size
Size = F.get_size_inches()
print "Size in Inches", Size
F.savefig("test3.png", dpi = (200)) # change the dpi
# this also results in a 1595x1132 image, but the fonts are larger.