#!/usr/bin/python3
'''
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total. Coin values can be assumed to be
infinite in number.
'''


def makeChange(coins, total):
    '''
    coins: A list of values representing the coins you have.
    total: The total you have to make change for.
    Returns a list of the fewest coins possible to equal the total needed,
    or -1 if not possible.
    '''
    if (total < 1):
        return 0
    changeMade = [0] * (total + 1)
    coins.sort(reverse=True)
    print(changeMade)
    for coin in coins:
        print('coin = ', coin)
        for x in range(coin, total + 1):
            if (changeMade[x - coin]):
                if (changeMade[x]):
                    print('changeMade[x]')
                    changeMade[x] = min(changeMade[x],
                                        changeMade[x - coin] + 1)
                else:
                    print('!changeMade[x]')
                    changeMade[x] = changeMade[x - coin] + 1
            elif (not x % coin):
                changeMade[x] += 1
        print(changeMade)
    return changeMade[total] if changeMade[total] else -1
