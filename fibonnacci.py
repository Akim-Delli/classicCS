def fib1(n: int) -> int:
    """
    fibonnaci number using recursion
    :param n: int
    :return: fibonnaci number : int
    """
    if n < 2:
        return n
    return fib1(n - 1) + fib1(n - 2)


def fib2(n: int) -> int:
    if n == 0: return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next

    return next


# ---------------------------------------------------------------
from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1}


def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]


# ---------------------------------------------------------------

from functools import lru_cache


@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n - 1) + fib4(n - 2)


# ---------------------------------------------------------------

from typing import Generator


def fib_series(n: int) -> Generator[int, None, None]:
    """
    Fibanacci Serie using a Generator
    :param n: int
    :return: int
    """
    yield 0  # special case
    if n > 0: yield 1  # special case
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next


# ---------------------------------------------------------------
if __name__ == '__main__':
    n = 10
    print(f'Finacci number for {n} is {fib1(n)} using recursion')
    print(f'Finacci number for {n} is {fib2(n)} using loop')
    print(f'Finacci number for {n} is {fib3(n)} using recursion and memoisation')
    print(f'Finacci number for {n} is {fib3(n)} using recursion and automatic memoisation')

    for i in fib_series(n):
        print(f'The Fibonacci serie for {n} first elements is {i}')

    fib1("abc")
