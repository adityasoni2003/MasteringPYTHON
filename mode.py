import random

def mode(numbers):
    count = {}
    mostfrequent = None
    mostfrequentcount = 0
    if len(numbers) == 0:
        return None
    for i in numbers:
        if i not in count :
            count[i] = 0
        count[i] += 1
        if count[i] > mostfrequentcount :
            mostfrequent = i
            mostfrequentcount = count[i]
    return mostfrequent

assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1
l = [1,2,2,2,2,4,44,4,5,6,66,4,55,4,3,3,4,3,4,3,4,34,33333,2,2,2,4,4,4,4,4,4,4,4]

print(mode(l))