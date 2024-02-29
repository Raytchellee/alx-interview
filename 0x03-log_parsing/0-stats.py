#!/usr/bin/python3
"""Checking the cause of error"""


import sys
import signal


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


def print_stats():
    total_size = sum(file_sizes.values())
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
file_sizes = {}

line_count = 0

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 7:
            ip, _, _, date, _, status, size = parts[:7]
            if status.isdigit() and int(status) in status_codes:
                status_code = int(status)
                file_size = int(size)
                file_sizes[line_count] = file_size
                status_codes[status_code] += 1
                line_count += 1
                if line_count % 10 == 0:
                    print_stats()
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
