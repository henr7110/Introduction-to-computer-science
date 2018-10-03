def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    import pylab
    import numpy
    pylab.hist(values,numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.title(title)
    
