import random
import math
import time
import matplotlib.pyplot as plt
#worked with Yip and others

def dist(p0, p1): #distance equation
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def bruteForce(A): #brute-force application as discussed
    n = len(A)
    minDist = dist(A[0], A[1])
    final = (A[0], A[1])

    if n == 2: #base
        return A[0], A[1]

    for i in range(0, n):
        for j in range(i + 1, n): #double iteration
            distance = dist(A[i], A[j])
            if distance < minDist: #replace current minimum if a smaller is found
                minDist = distance
                final = (A[i], A[j])
    return final[0], final[1]

def closest_split_pair(Px, Py, ind): #main function
    median = Px[len(Px)//2][0]
    
    strip = []
    for point in Py: #create the strip
        if median - ind <= point[0] <= median + ind:
            strip.append(point)

    best= ind
    best_pair= Px[0], Px[1] #temporary best pair

    for i in range(len(strip)):
        for j in range(1, min(7, len(strip)-i)):
            if dist(strip[i], strip[i+j]) < best: #check for another better pair, replace
                best= dist(strip[i], strip[i+j])
                best_pair= strip[i], strip[i+j]
    return best_pair[0], best_pair[1] 

def closest_pair(Px, Py): #recursive function
    if len(Px) <= 3: #base
        return bruteForce(Px) 

    Lx = Px[:len(Px)//2] 
    Ly = Py[:len(Py)//2]  

    Rx = Px[len(Px)//2:] 
    Ry = Py[len(Py)//2:] 

    L1, L2 = closest_pair(Lx, Ly)  #recursive to find smallest distance
    R1, R2 = closest_pair(Rx, Ry)  

    ind = min(dist(L1, L2), dist(R1, R2)) #index of minimum

    s1, s2 = closest_split_pair(Px, Py, ind)

    bestDist = min(dist(L1, L2), dist(R1, R2), dist(s1, s2)) #replacing and returning the best distance
    if bestDist == dist(L1, L2):
        return L1, L2
    elif bestDist == dist(R1, R2):
        return R1, R2
    else:
        return s1, s2

random.seed(10**3)
main = []  
x = []  
y = [] 

for i in range(10**2):

    tempX = round(20 * random.random() - 10, 2)
    x.append(tempX)

    tempY = round(20 * random.random() - 10, 2)
    y.append(tempY)

    main.append((tempX, tempY))


plt.scatter(x, y) #creating plot
Px = sorted(main, key=lambda tempX: tempX[0])
Py = sorted(main, key=lambda tempY: tempY[0])

n = 5
for i in range(n):
    st = time.time()
    close = closest_pair(Px, Py)
    print(time.time()- st)
    print("Closest: ", close) #printer
    print("+++++++++++++++")

plt.scatter(x, y)

plt.plot(close[0][0], close[0][1], 'or', color="green") #highlight closest pair

plt.plot(close[1][0], close[1][1], 'or', color="green")

plt.show()
