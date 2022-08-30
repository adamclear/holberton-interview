#!/usr/bin/env python3
''' This module attempts to solve the Lockboxes problem '''


def canUnlockAll(boxes):
    ''' Returns True if all boxes can be opened, otherwise False '''
    unlockedBoxes = [0]
    boxList = enumerate(boxes)
    obtainedNewKey = True
    while obtainedNewKey is True:
        obtainedNewKey = False
        x = 0
        while x < len(boxes):
            if x in unlockedBoxes:
                for key in boxes[x]:
                    if key not in unlockedBoxes:
                        unlockedBoxes.append(key)
                        obtainedNewKey = True
            x += 1

    for id, box in boxList:
        if id not in unlockedBoxes:
            return False

    return True
