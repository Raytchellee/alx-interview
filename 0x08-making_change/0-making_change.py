#!/usr/bin/python3
"""Make change algorithm"""


def makeChange(coins, total):
    """Make cange function"""
    if total < 1:
        return 0

    max_val = total + 1
    dp = [max_val] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] < max_val else -1
