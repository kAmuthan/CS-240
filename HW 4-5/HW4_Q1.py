A = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(A)

#Write a function wrap_by_k ( lst, k) that wraps an array lst around by k values.


def reverse(A):
    diff = (len(A))//2+1
    for i in range(diff):
        A[i], A[len(A)-i] = A[len(A)-i], A[i]


def wrap_by_k(A, k):
    reverse(A)


wrap_by_k(A, 3)
print(A)
