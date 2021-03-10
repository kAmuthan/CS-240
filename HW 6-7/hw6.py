#hw6 Q1
import math
global count

def q1():
    a=270
    b=192
    while b != 0:
        temp = a%b
        a=b
        b=temp
    print (a)

def q2():
    a=[0,1,1,0,1,1,0,0]
    b=[1,0,0,1,0,1,1,1]
    final=[0]*len(a)
    carry=0
    for i in range(len(a), 0):
        temp=a[i]+b[i]+carry
        final[i]=temp
        carry=temp%2
    final[len(a)]=carry
    print (final)

count=0
x = 1234567891011121314151617181920212223242526272829303132333435363
y = 1357911131517192123252729313335373941434547495153555759616365676

k= 1234
l= 5678

"""
def karatsuba(x,y):
    global count
    count+=1
    lenX=int(math.log10(x+.001)+1)
    lenY=int(math.log10(y+.001)+1) 
    length= max(lenX,lenY)

    if x<10 or y<10:
        return x*y
    else:
        a=x//(10**(length//2))
        b=x%(10**(length//2))
        c=y//(10**(length//2))
        d=y%(10**(length//2))

        AC=karatsuba(a,c)
        BD=karatsuba(b,d)
        final=karatsuba(a+b,c+d)-AC-BD

        return (10**length)*AC+10**int(length/2)*final+BD
"""
def kara(x,y):
    global count
    count+=1
    n=max(int(math.log10(x+.001))+1, int(math.log10(y+.001))+1)

    if x<10 or y<10:
        return x*y
    else:
            a,b=int(x//(10**(n//2))), x%int((10**(n//2)))
            c, d = int(y//(10**(n//2))), y % int((10**(n//2)))
    z2=kara(a,c)
    z0=kara(b,d)
    z1= kara(a+b,c+d)-z2-z0

    return 10**(2*(n//2))*z2+10**(n//2)*z1+z0

print (karatsuba(k,l), '\n')
print (count)

def q3():
    

