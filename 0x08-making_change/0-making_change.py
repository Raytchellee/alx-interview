#!/usr/bin/python3
"""Make change algorithm"""


def makeChange(coins, total):
    """Make cange function"""
    if total < 1:
        return 0

    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            num_coins += 1

    return num_coins if total == 0 else -1
