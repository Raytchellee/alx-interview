#!/usr/bin/python3
"""Solves N-queens puzzle"""
import sys


def init_board(n):
    """Initializes the board"""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def copy_board(board):
    """Return a copy of a chessboard."""
    if isinstance(board, list):
        return list(map(copy_board, board))
    return (board)


def get_solution(board):
    """gets all list"""
    ress = []
    for x in range(len(board)):
        for d in range(len(board)):
            if board[x][d] == "Q":
                ress.append([x, d])
                break
    return (ress)


def get_x(tab, row, col):
    """marks x on the dashboard"""
    for d in range(col + 1, len(tab)):
        tab[row][d] = "x"
    for d in range(col - 1, -1, -1):
        tab[row][d] = "x"
    for r in range(row + 1, len(tab)):
        tab[r][col] = "x"
    for r in range(row - 1, -1, -1):
        tab[r][col] = "x"
    d = col + 1
    for r in range(row + 1, len(tab)):
        if d >= len(tab):
            break
        tab[r][d] = "x"
        d += 1
    d = col - 1
    for r in range(row - 1, -1, -1):
        if d < 0:
            break
        tab[r][d]
        d -= 1
    d = col + 1
    for r in range(row - 1, -1, -1):
        if d >= len(tab):
            break
        tab[r][d] = "x"
        d += 1
    d = col - 1
    for r in range(row + 1, len(tab)):
        if d < 0:
            break
        tab[r][d] = "x"
        d -= 1


def recursive_solve(tab, row, queens, res):
    """Recursively solve the N-queens puzzle"""
    if queens == len(tab):
        res.append(get_solution(tab))
        return (res)

    for d in range(len(tab)):
        if tab[row][d] == " ":
            temp = copy_board(tab)
            temp[row][d] = "Q"
            get_x(temp, row, d)
            res = recursive_solve(temp, row + 1,
                                        queens + 1, res)

    return (res)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    res = recursive_solve(board, 0, 0, [])
    for ans in res:
        print(ans)
