def getsmallest(list):
    if len(list) == 0:
        return None
    smallest = list[0]
    for i in list : 
        if i < smallest :
            smallest = i
        else :
            return smallest
print(getsmallest([1,2,3,4,5,6]))