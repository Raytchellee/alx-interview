#!/usr/bin/python3
"""Prime game solution"""


def is_prime(n):
  """Prime game function"""
  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True

def isWinner(x, nums):
  """Winner game function"""
  def get_winner(n):
    if n == 1:
      return "Ben"
    if n % 2 == 0:
      return "Ben"
    return "Maria"

  winners = []
  for n in nums:
    prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))
    winners.append(get_winner(prime_count))

  maria_wins = winners.count("Maria")
  ben_wins = winners.count("Ben")

  if maria_wins > ben_wins:
    return "Maria"
  elif ben_wins > maria_wins:
    return "Ben"
  else:
    return None