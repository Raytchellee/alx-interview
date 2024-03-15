#!/usr/bin/python3
""" Solve N queens """
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

input = int(sys.argv[1])


def get_q(input, d=0, x=[], y=[], z=[]):
    """ finding all locations """
    if d < input:
        for v in range(input):
            if v not in x and d + v not in y and d - v not in z:
                yield from get_q(input, d + 1, x + [v], y + [d + v], z + [d - v])
    else:
        yield x


def solve_n(input):
    """ solving for value """
    vals = []
    count = 0
    for res in get_q(input, 0):
        for item in res:
            vals.append([count, item])
            count += 1
        print(vals)
        vals = []
        count = 0


solve_n(input)
