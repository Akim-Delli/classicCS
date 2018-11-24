from typing import List


def increment_integer_as_array(A: List) -> List:

    carry = 0
    for i in reversed(range(len(A))):
        if carry + A[i] + 1 >= 10:
            carry = 1
            A[i] = 10 - (A[i] + 1)
        else:
            A[i] = carry + A[i]
            break

    return A
