#Program the number of ways to multiply n+1 numbers at the end of the notes for 
#lecture 12 two different ways-recursively and  dynamically-(ie without recursion). Worked with Andrew on this

count = 0 #global count for recursive

def ways_to_multiply_REC(x): #RECURSIVE catalan calculator
    global count
    count += 1
    holder = 0 #final value to be returned

    if x <=1: #base case
        return 1

    for i in range(x):
        holder +=  ways_to_multiply_REC(i) * ways_to_multiply_REC(x-i-1) #catalan equation as discussed

    return holder

def printer_REC(y): #printer
    global count
    count=0
    print("REC")
    print("NUM: ", y)
    print("OUTPUT:", ways_to_multiply_REC(y))
    print("COUNTER: ", count)
    print("------------------")

printer_REC(3)
printer_REC(5)
printer_REC(6)
printer_REC(10)

print("///////////////////////////")
print("///////////////////////////")

def ways_to_multiply_DYN(x): #DYNAMIC catalan calculator

    if x <= 1: #base case
        return 1
    
    c = [0]*(x+1) #setting up array

    c[0]=1 #must exclude 0 and 1
    c[1]=1

    for i in range(2, x+1): #must start at 2 becuase 0 and 1 are accounted for
        for k in range(i):
            c[i] += c[k] * c[i-k-1] #catalan equation, except iterating through an array instead of calling recursively 

    return c[x]


def printer_DYN(y): #printer
    print(">>DYN")
    print("NUM: ", y)
    print("OUTPUT:", ways_to_multiply_REC(y))
    print("------------------")

printer_DYN(3)
printer_DYN(5)
printer_DYN(6)
printer_DYN(10)