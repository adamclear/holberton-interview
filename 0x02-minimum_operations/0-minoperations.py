#!/usr/bin/env python3
''' 0-minoperations task '''


def minOperations(n):
    ''' Calculates the fewest number of operations needed to result
    in exactly n characters in the file. '''
    if n < 1 or n is None:
        return 0
    numOps = 0
    while n > 1:
        for x in range(2,5):
            if n % x == 0:
                n = n / x
                numOps += x
    return numOps