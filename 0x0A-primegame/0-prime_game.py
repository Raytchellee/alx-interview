#!/usr/bin/python3
"""Prime game solution"""


def getPrimes(idx):
    """Prime game solution"""
    numbers = []
    diff = [True] * (idx + 1)
    for num in range(2, idx + 1):
        if diff[num]:
            numbers.append(num)
            for idy in range(num, idx + 1, num):
                diff[idy] = False
    return numbers


def isWinner(x, nums):
    """Prime game solution"""
    if x is None or nums is None or x == 0 or nums == []:
        return None
    count_m = count_b = 0
    for idy in range(x):
        all_primes = getPrimes(nums[idy])
        if len(all_primes) % 2 == 0:
            count_b += 1
        else:
            count_m += 1
    if count_m > count_b:
        return 'Maria'
    elif count_b > count_m:
        return 'Ben'
    return None
