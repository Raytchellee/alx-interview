#!/usr/bin/python3
"""UTF-8 Validation"""

def validUTF8(data):
    def is_start_byte(byte):
        """UTF-8 Validation"""
        return (byte >> 7) == 0 or \
               (byte >> 5) == 0b110 or \
               (byte >> 4) == 0b1110 or \
               (byte >> 3) == 0b11110

    def is_continuation_byte(byte):
        return (byte >> 6) == 0b10

    remaining_bytes = 0

    for byte in data:
        if remaining_bytes > 0:
            if not is_continuation_byte(byte):
                return False
            remaining_bytes -= 1
        else:
            if not is_start_byte(byte):
                return False
            if (byte >> 5) == 0b110:
                remaining_bytes = 1
            elif (byte >> 4) == 0b1110:
                remaining_bytes = 2
            elif (byte >> 3) == 0b11110:
                remaining_bytes = 3

    return remaining_bytes == 0
