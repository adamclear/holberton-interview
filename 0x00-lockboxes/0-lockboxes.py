#!/usr/bin/env python3
''' This module attempts to solve the Lockboxes problem '''


def canUnlockAll(boxes):
    ''' Returns True if all boxes can be opened, otherwise False '''
    availableKeys = [0]
    # Loop through availableKeys adding new keys as we go
    for x in availableKeys:
        for key in boxes[x]:
            if key not in availableKeys:
                availableKeys.append(key)

    # If there are any numbers missing from availableKeys
    # between 0 and length of boxes, return false
    x = 0
    while x < len(boxes):
        if x not in availableKeys:
            return False
        x += 1

    return True
