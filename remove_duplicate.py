from typing import List


def remove_duplicate(A: List[int]) -> List[int]:
    last_index, i = 0, 0
    while last_index != len(A) - 1:
        if A[i] == A[last_index]:
            last_index += 1
        else:
            i += 1
            A[i] = A[last_index]

    for j in range(i + 1, len(A)):
        A[j] = 0

    return A


if __name__ == "__main__":
    A = [1, 2, 2, 6, 7, 7, 7, 7, 7, 7, 9, 10, 44, 44]
    print(remove_duplicate(A))
