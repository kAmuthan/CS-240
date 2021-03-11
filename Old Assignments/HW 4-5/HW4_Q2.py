A=[0,1,2,3,4,5,6,7,8]
print(A)

#Write a function wrap_by_k ( lst, k) that wraps an array lst around by k values.
def reverse(A,left,right):
    diff=(right-left)//2+1
    for i in range(diff):
        A[left+i], A[right-i]= A[right-i],A[left+i]
def wrap_by_k(A,k):
    reverse(A,len(A)-k,len(A)-1)

    reverse(A,0,len(A)-k-1)

    reverse(A,0,len(A)-1)

wrap_by_k(A,3)
print(A)
