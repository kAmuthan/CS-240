import time
A=[2,3,4,6,7,8,3,2] 


def unimode_max(A):
    n = len(A)  # o(1)
    if n == 1:  # o(1)
        return A[0] #o(1)
    elif A[n//2-1]>A[n//2]: #o(1)
        return unimode_max(A[:n//2]) #O(log(n))
    else: #o(1)
        return unimode_max(A[n//2:])  # O(log(n))
#O(1+1+1+1(log(n))+1(log(n)))
#O(3+2log(n))
#O(2log(n))
A=[]
for i in range(2**24):
    A.append(i)
for i in range(10):
    A.append(10-i)
start=time.time()
print(unimode_max(A))
print(time.time()-start)
