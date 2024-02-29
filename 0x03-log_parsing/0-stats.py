#!/usr/bin/python3
"""Checking the cause of error"""


import sys

statusCodeCounts = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
totalSize = 0
lineCounter = 0

try:
    for line in sys.stdin:
        lineList = line.split(" ")
        if len(lineList) > 4:
            code = lineList[-2]
            size = int(lineList[-1])
            if code in statusCodeCounts.keys():
                statusCodeCounts[code] += 1
            totalSize += size
            lineCounter += 1

        if lineCounter == 10:
            lineCounter = 0
            print('File size: {}'.format(totalSize))
            for key, value in sorted(statusCodeCounts.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(totalSize))
    for key, value in sorted(statusCodeCounts.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
