import random
import time
import sys
import statistics
sys.setrecursionlimit(10000)
'''global runMedian
runMedian = True'''

def partition(a, L, R, P): #Partition begin
    while L <= R: #as long as pivot conditions met

        while a[L] < P: #left swap
            L += 1

        while a[R] > P: #right swap
            R -= 1

        if L <= R:
            a[L], a[R] = a[R], a[L]
            L += 1 #accounts for an extra step
            R -= 1

    return L

def quicksort(A, L, R):  
    
    if L >= R: #when the indexes connect, end recursion
        return

    #left = A[L]  #  TEST 1
    #right = A[R] #TEST 2
    #middle = A[(L+R)//2] #TEST 3
    randomize = A[random.randint(L, R)] #TEST 4

    P = randomize #the pivot, to be easily changed

    j = partition(A, L, R, P) #partition begin

    quicksort(A, L, j-1)
    quicksort(A, j, R)
    return A


def Q1():
    #A=[1,2,3,4,5,6,7,8,9,10]
    A=[]
    for i in range(10000): #creating array as requested
        A.append(random.randint(1, 500))
    A.sort() #pre-sorted array

    st = time.time()
    quicksort(A, 0, len(A)-1) 
    #print(quicksort(A, 0, len(A)-1))
    return (time.time()-st) #easy clock

def Q2():
    A=[]
    for i in range(10000):
        A.append(random.randint(1,500))
    A.sort() #pre=sorted array

    percent = int(len(A)* 0.05 ) #taking only the first 5% of the array and shuffling
    for i in range(percent): 
        hold = random.randint(0, len(A)-1) #shuffle swaps two random indexes
        swap = random.randint(0, len(A)-1)
        A[hold], A[swap] = A[swap], A[hold]

    st = time.time()
    quicksort(A, 0, len(A)-1)
    #print(quicksort(A, 0, len(A)-1))
    return (time.time()-st)

def Q3():
    A=[]
    for i in range(10000):
        A.append(random.randint(1, 500)) #UNSORTED ARRAY
    
    percent = int(len(A) * 1.00) #shuffle 100% of the array (1.00)
    for i in range(percent):
        hold = random.randint(0, len(A)-1) #same shuffle method
        swap = random.randint(0, len(A)-1)
        A[hold], A[swap] = A[swap], A[hold]

    st = time.time()
    quicksort(A, 0, len(A)-1)
    #print(quicksort(A, 0, len(A)-1))
    return (time.time()-st)

def Q4():
    A = []
    for i in range(10000):
        A.append(random.randint(1, 500))
    A.sort() #SORTED ARRAY

    for i in range(1, 10, 1): #splits into 10 pieces for 10% each
        percentL = int(len(A) * ((0.1)*(i-1))) #calculated left wall
        percentR = int(len(A) * (i*0.1)) #calculated right wall
        for j in range(percentL, percentR, 1): #iterates through only that 10%
            hold = random.randint(percentL, percentR-1) #chooses values only from that 10%
            swap = random.randint(percentL, percentR-1)
            A[hold], A[swap] = A[swap], A[hold] #shuffle

    st = time.time()
    quicksort(A, 0, len(A)-1)
    #print(quicksort(A, 0, len(A)-1))
    return (time.time()-st)

def Q5():
    A = []
    for i in range(10000):
        A.append(random.randint(1, 500))
    A.sort() #SORTED ARRAY

    for i in range(250):
        A.append(random.randint(1, 500)) #adding on extra UNSORTED values to a sorted array
    
    st = time.time()
    quicksort(A, 0, len(A)-1)
    #print(quicksort(A, 0, len(A)-1))
    return (time.time()-st)

def Q6():
    A = []
    for i in range(10000):
        A.append(random.randint(1, 500))
    A.sort() #SORTED ARRAY 

    B = []
    for i in range(10000-1, 0, -1):
        B.append(A[i]) #kind of brute force, simply iterating backwards and adding to B
    
    st = time.time()
    quicksort(A, 0, len(A)-1)
    #print(quicksort(A, 0, len(A)-1))
    return (time.time()-st)




#calculator
C = []

for i in range(3): #runs a few times
    C.append(Q6())

avg = statistics.mean(C) #calculate average time 

print(C)
print("mean =", avg) #printer





#Attempt at median, got stuck on consistently sorting and selecting
'''def Median(A, L, R):
    B = []
    holder = 0
    for i in range(3):
        B.append(A[random.randint(L, R)])
    test = True
    while test:
        if B[1] < B[0]:
            B[0], B[1] = B[1], B[0]
        elif B[2] < B[1]:
            B[1], B[2] = B[2], B[1]
        elif B[2] < B[0]:
            B[0], B[2] = B[2], B[0]
        if B[0] < B[1] and B[0] < B[2] and B[1] < B[2]:
            test = False
    print(B)
    for k in range(0, len(A)-1, 1):
        if B[1] == A[k]:
            holder = k
    return B[1] '''
