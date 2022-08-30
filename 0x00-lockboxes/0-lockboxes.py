#!/usr/bin/env python3
''' This module attempts to solve the Lockboxes problem '''


def canUnlockAll(boxes):
    ''' Returns True if all boxes can be opened, otherwise False '''
    unlockedBoxes = [0]
    # Loop through unlockedBoxes adding new keys as we go
    for x in unlockedBoxes:
        for key in boxes[x]:
            if key not in unlockedBoxes:
                unlockedBoxes.append(key)

    # Loop through unlockedBoxes and if there are any missing numbers
    # between 0 and length of boxes, return false
    x = 0
    while x < len(boxes):
        if x not in unlockedBoxes:
            return False
        x += 1

    return True
