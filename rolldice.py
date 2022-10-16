import random



def rolldice(x):
    l= []
    for i in range(x+1):
        l.append(random.randint(1,6))
    count = 0
    for y in l :
        count += y
    return count
    
print(rolldice(3344444))