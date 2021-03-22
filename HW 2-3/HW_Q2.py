#(largest_subarray_sum)
#Write the program that finds the largest sum of a contiguous 
# subarray of integers. ie(See directions following a and b below)
import random 
t=100

a=[]
for int in range(t):
    a.append(random.randint(-2*t,2*t))

b = [34, -50, 42, 14, -5, 86]
#[34, -50, 42, 14, -5, 86] should return 137 since [42, 14, -5, 86] 
# is the largest sum for consecutive elements.

#QUESTION 2A
def sub_list(n):
    holder =0
    for i in range (n-1,-1,-1):
        for j in range(i+1):
            total=sum_between(n,i,j)
        if total>holder:
            holder=total
    return holder

def sum_between(x,y,z):
    sum=0
    for k in range (y,z+1):
        sum+=a[k]
    return sum

#necessary to have nested for loops, and external counts to 
# figure out the subset sums. the order of this method is On^2


#QUESTION 2B
def smart_sub_sum(a):
    n=len(a)
    forwardA=[0]*n
    backA=[0]*n
    forwardA[0]=max(a[0],0)
    for i in range(1,n):
        forwardA[i]=max(0, a[i]+forwardA[i-1])

    backA[n-1]=max(a[n-1],0)
    for i in range(n-2,-1,-1):
        backA[i]=max(0,a[i]+backA[i+2])
    maxright=0
    maxleft=0
    for i in range(n):
        if maxright<forwardA[i]:
            maxright=forwardA[i]
            right=i
        if maxleft<backA[n-i-1]:
            maxleft=backA[n-i-1]
            left=n-i-1
    return left,right
