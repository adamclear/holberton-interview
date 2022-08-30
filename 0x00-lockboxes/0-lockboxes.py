#!/usr/bin/env python3
''' This module attempts to solve the Lockboxes problem '''


def canUnlockAll(boxes):
    ''' Returns True if all boxes can be opened, otherwise False '''
    unlockedBoxes = [0]
    obtainedNewKey = True
    # Loop through boxes until loop where no more new keys found
    while obtainedNewKey is True:
        obtainedNewKey = False
        x = 0
        while x < len(boxes):
            # Check if we have the key to this box
            if x in unlockedBoxes:
                for key in boxes[x]:
                    # If a new key is found add to list and reset indicator
                    if key not in unlockedBoxes:
                        unlockedBoxes.append(key)
                        obtainedNewKey = True
            x += 1

    # Loop through unlocked boxes and if there are any missing numbers
    # between 0 and length of boxes, return false
    x = 0
    while x < len(boxes):
        if x not in unlockedBoxes:
            return False
        x += 1

    return True
