#!/usr/bin/python3
"""Solve lockboxes"""

def canUnlockAll(boxes):
    """Unlocking all lockboxes"""
    if len(boxes) < 1:
        return False

    visited = set()
    visited.add(0)
    idx = boxes[0][:]
    res = [0]

    while len(idx) > 0:
        current = idx.pop(0)
        if current in visited:
            continue
        visited.add(current)
        res.append(current)
        for val in boxes[current]:
            idx.append(val)

    return len(res) == len(boxes)
