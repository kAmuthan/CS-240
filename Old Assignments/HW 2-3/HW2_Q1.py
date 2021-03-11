#HW 2, Problem 1
def linear(list1, target):
    i = 0
    notfound = True
    while notfound:
        notfound = (target != list1[i])
        i += 1
    return i-1


def binary(list1, target):
    top = len(list1)-1
    bottom = 0
    while bottom < top:
        mid = (top+bottom)//2
        if target == list1[mid]:
            return mid
        elif target < list1[mid]:
            top = mid - 1
        else:
            bottom = mid + 1
    return mid


# Test both on a simple list
list1 = [1, 3, 6, 7, 11, 12, 18, 21]
print(linear(list1, 7))
print(binary(list1, 7))
