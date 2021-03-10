#HW 1, PROGRAM 1: (product_without)

a = [3, 7, 5, 6, 9]
print ('starter array:'), a


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
    left[i] = a[i-1]*left[i-1]
    

#right
for i in range(len(right)-1, -1, -1):
    temp2 *= A[i]
    right[i] = temp2

#combining
product[0] = right[1]
product[length-1] = left[length-2]

for i in range(1, length-1):
    product[i] = left[i-1]*right[i+1]
print(product)
