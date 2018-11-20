# Given an integer return the reverse integer without using a string
#  eg : 12345 -> 54321


def reverse_integer(n: int) -> int:
    """
    reverse an integer , eg 12345 -> 54321
    :param n: int
    :return: reversed n
    """
    summation: int = 0
    remainder: int = n

    while remainder:
        last_digit: int = remainder % 10
        remainder //= 10
        summation = 10 * summation + last_digit

    return summation


if __name__ == "__main__":
    print(reverse_integer(12345))
