from functools import reduce
import operator

def interleave_5_4(*iterables):
    print (list(reduce(operator.add, (zip(*iterables)))))