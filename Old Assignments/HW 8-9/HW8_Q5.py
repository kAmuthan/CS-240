def Ai_equals_i(A):

    n = len(A) #o(1)
    i = n//2 #o(1)

    if A[i] == i: #o(1)
        return i #o(1)
    elif A[i] > i: #o(1)
        return Ai_equals_i(A[:i]) #Olog(n)
    else: #o(1)
        return Ai_equals_i(A[i+1:]) #0log(n)


A = [-4, -3, 1, 2, 4, 8, 9, 10, 11, 12, 14, 18, 19, 22, 50, 51]
print(Ai_equals_i(A))
