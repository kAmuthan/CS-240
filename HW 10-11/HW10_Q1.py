# Find where C(n,k) is odd
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
    return n*fact(n-1)

def comb(n, k):  # This is the efficient way to calc C(n.k)
p = 1
k = min(k, n-k)
for i in range(k):
p *= n-i
return p//fact(k)
for i in range(5, 50):
for j in range(3, 50):
x = comb(i, j)
if x % 2 == 1:
print('o', end='')
else:
print("")
