#HW 1, PROGRAM 1: (product_without)
#-(product_without) -
#Write the program discussed in class that is O(n) ie it only requires 
# single loops rather than nested loops to find an array of products of an array, 
# save for the ith element. So[3, 7, 5, 6, 9] returns
# [1890, 810, 1134, 945, 630]. Your computer lacks a division routine.

A = [3, 7, 5, 6, 9]
print ('starter array:'), A


#array to hold products
length = len(A)
left = [0]*length
right = [0]*length
product = [0]*length

#correcting start locations
left[0]=1
right[length-1]=1

#left
for i in range(1, len(left)):
    left[i] = A[i-1]*left[i-1]
    

#right
for i in range(len(right)-1, -1, -1):
    temp2 *= A[i]
    right[i] = temp2






#HW 2
#smallest_window)
#Write the program that finds the smallest "window" that needs 
# to be sorted in an array in order for the entire array to be sorted. 
# So given the array A = [3, 7, 5, 6, 9] you should return left = 1 
# and right = 3 since the elements A[1], A[2], and A[3] are out of order. 
# Use the algorithm discussed in class which requires 2 passes through the array.

product[0] = right[1]
product[length-1] = left[length-2]

for i in range(1, length-1):
    product[i] = left[i-1]*right[i+1]
print(product)
