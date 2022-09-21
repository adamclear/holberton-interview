#!/usr/bin/python3
''' 0-minoperations task '''


def minOperations(n):
    ''' Calculates the fewest number of operations needed to result
    in exactly n characters in the file. '''
    if n < 2 or n is None:
        return 0
    numOps = 0
    while n > 1:
        max = n + 1
        for x in range(2, max):
            if n % x == 0:
                n = n // x
                numOps += x
                break

    return numOps
