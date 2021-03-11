A = [4, 7, 2, 3, 9, 1, 6]


def second_largest(A):
    n = len(A)
    max = A[0]
    for i in range(1, n):

        if A[i] > max:
            old_max = max
            max = A[i]
        print(i, " ", max)
    return old_max


print(second_largest(A))
