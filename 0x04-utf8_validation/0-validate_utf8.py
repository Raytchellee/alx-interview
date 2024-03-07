#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Check Validation"""
    bytes_to_check = 0

    start_byte_mask = 1 << 7
    trailing_byte_mask = 1 << 6

    for byte in data:
        current_byte_mask = 1 << 7

        if bytes_to_check == 0:
            while current_byte_mask & byte:
                bytes_to_check += 1
                current_byte_mask = current_byte_mask >> 1

            if bytes_to_check == 0:
                continue

            if bytes_to_check == 1 or bytes_to_check > 4:
                return False

        else:
            if not (byte & start_byte_mask):
                return False
            if byte & trailing_byte_mask:
                return False

        bytes_to_check -= 1

    if bytes_to_check == 0:
        return True

    return False
