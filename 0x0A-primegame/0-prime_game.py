#!/usr/bin/python3
"""Prime game solution"""


def isWinner(x, nums):
    """Prime game solution"""
    def sieve_of_eratosthenes(limit):
        """Prime game solution"""
        primes = [True] * (limit + 1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= limit:
            if primes[p]:
                for i in range(p * p, limit + 1, p):
                    primes[i] = False
            p += 1
        return primes

    def get_winner(primes):
        """Prime game solution"""
        prime_count = sum(primes)
        if prime_count % 2 == 0:
            return "Ben"
        return "Maria"

    winners = []
    max_limit = max(nums)
    primes = sieve_of_eratosthenes(max_limit)
    
    for n in nums:
        prime_count = sum(primes[:n+1])
        winners.append(get_winner(primes[:n+1]))

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
