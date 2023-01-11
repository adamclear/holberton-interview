#!/usr/bin/python3
""" Contains the function for task 0 of Rain interview question. """


def rain(walls):
    """ Calculates the square units of water retained within the given
    walls. User enters heights of walls. (A list of non-negative integers)
    The function determines how much water those walls would trap.
    (In a 2D grid) """
    water = 0
    if walls:
        for x in range(1, len(walls) - 1):
            left = max(walls[x], (max(walls[:x])))
            right = max(walls[x], max(walls[x + 1:]))
            water += min(left, right) - walls[x]
    return water
