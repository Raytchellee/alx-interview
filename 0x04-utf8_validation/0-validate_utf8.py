#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Args:
        data (list): A list of integers representing bytes of data.
    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    bytes_to_check = 0

    for byte in data:
        if bytes_to_check == 0:
            if (byte >> 5) == 0b110:
                bytes_to_check = 1
            elif (byte >> 4) == 0b1110:
                bytes_to_check = 2
            elif (byte >> 3) == 0b11110:
                bytes_to_check = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            bytes_to_check -= 1

    return bytes_to_check == 0
