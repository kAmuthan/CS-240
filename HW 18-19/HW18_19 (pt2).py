import random
import math
import matplotlib.pyplot as plt
#worked with Yip and others

def dist(a,b): #distance equation
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def closestPair(START): #closest pair by using brute
    holder= len(START)
    min= dist(START[0], START[1])
    final= (START[0], START[1])

    if holder == 2:
        return dist(START[0], START[1]), START[0], START[1]
    
    for i in range(0, holder):
        for j in range(i+1, holder):
            d = dist(START[i], START[j])
            if d<min:
                min= d
                final= (START[i], START[j])
    return final

def delta(x): #using delta to locate close pairs
    L = x[:len(x)//2]
    R = x[len(x)//2:]
    delta_L = dist(closestPair(L)[0], closestPair(L)[1])
    delta_R = dist(closestPair(R)[0], closestPair(R)[1])

    if delta_L < delta_R:
        return closestPair(L)
    else:
        return closestPair(R)

random.seed(10)
main= []
x= []
y= []

for i in range(10):
    tempX = round(20*random.random() - 10, 2)
    x.append(tempX)

    tempY = round(20*random.random() - 10, 2)
    y.append(tempY)

    main.append((tempX,tempY))

plt.scatter(x,y) #creating plot
sorted_x = sorted(main, key=lambda tempX: tempX[0])
sorted_y = sorted(main, key=lambda tempY: tempY[0])

L= sorted_x[:len(sorted_x)//2]
R= sorted_y[len(sorted_x)//2:]

deltaMain= dist(delta(sorted_x)[0], delta(sorted_x)[1]) #create delta for the main 

median = (sorted_x[len(sorted_x)//2-1][0] + sorted_x[len(sorted_x)//2][0])/2

strip = [] #create the strip
for pair in sorted_y:
    if pair[0] < median + deltaMain and pair[0] > median - deltaMain:
        strip.append(pair)

final = deltaMain
finalPair = delta(sorted_x)
length = len(strip)
for i in range(length):
    for j in range(1, min(7, length-i)):
            if dist(strip[i], strip[i+j]) < final:
                final = dist(strip[i], strip[i+j])
                finalPair = (strip[i], strip[i+j])

plt.axvline(x=median) #plotting median lines for each delta 
plt.axvline(x=median+deltaMain, color="red")
plt.axvline(x=median-deltaMain, color="red")
plt.plot(finalPair[0][0], finalPair[0][1], 'or', color="red")
plt.plot(finalPair[1][0], finalPair[1][1], 'or', color="red")
plt.plot(closestPair(L)[0][0], closestPair(L)[0][1], 'or', color="yellow")
plt.plot(closestPair(L)[1][0], closestPair(L)[1][1], 'or', color="yellow")
plt.plot(closestPair(R)[0][0], closestPair(R)[0][1], 'or', color="green")
plt.plot(closestPair(R)[1][0], closestPair(R)[1][1], 'or', color="green")
plt.show()
