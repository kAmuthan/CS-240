#How many 0's are at the end of 100!
def fives(n):
    count=0
    while n%5==0:
        n=n//5
        count+=1
    return count

def num_zeroes(n):
    num_0s=0
    for i in range(5,n+1,5):
        num_0s += fives(i)
    return num_0s

print(num_zeroes(100))