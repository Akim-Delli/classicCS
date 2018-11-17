def parity(n: int) -> int:
    """
    O(n) time complexity
    :param n:
    :return:
    """

    parity_count: int = 0

    while n:
        parity_count ^= n & 1
        n = n >> 1

    return parity_count


if __name__ == '__main__':
    print(parity(14))
