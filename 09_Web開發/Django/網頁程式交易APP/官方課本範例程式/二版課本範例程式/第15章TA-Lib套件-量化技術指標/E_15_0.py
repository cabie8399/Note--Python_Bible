import talib
import numpy
close = numpy.random.random(100)
output = talib.SMA(close,5)
print(output)