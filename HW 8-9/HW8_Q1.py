Q = [1, 4, 10, 7, 15, 16, 17, 2, 18, 5, 8, 9, 11, 12, 13, 14]

length = 16


def merge2(C, D):
    B = []
    length = len(C)+len(D)
    i = 0
    j = 0
    for k in range(length):
        if i >= len(C):  # Once you are done with
            B.append(D[j])  # C fill in rest of D
            j += 1
        elif j >= len(D):  # Once you are done with
            B.append(C[i])  # D fill in rest of C
            i += 1
        elif C[i] < D[j]:
            B.append(C[i])
            i += 1
        else:
            B.append(D[j])
            j += 1
    return B
    print(merge2(C, D))


def merge_sort(A):
    if len(A) <= 1:
        return A
    else:
        frontA = merge_sort(A[:len(A)//2])
        backA = merge_sort(A[len(A)//2:])
        return merge2(frontA, backA)


print(merge_sort(Q))
