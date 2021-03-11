#Write a program that does the bubble sort.
#  Demonstrate its complexity by empirically calculating  the 
# time to execute for arrays of various sizes and describe 
# the differences in terms of complexity
import random
import time
def bubble(A):
    timer= time.time
    n=len(A)
    for j in range(n-1):
        for i in range(n-1-j):
            if A[i+1] < A[i]:
                A[i+1],A[i]=A[i],A[i+1]
                if j==1:
                    print(A)
    timer = time.time
    print(timer)

lst = [3,4,7,2,5,6,1,9,8]
bubble(lst)