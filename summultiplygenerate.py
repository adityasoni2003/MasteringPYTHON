from random import randint
from getsmallest import getsmallest


def getsum(list):
    sum = 0
    for i in list :
        sum += i
    return sum
def calculate(list):
    product = 1
    for i in list :
        product *= i
    return product

numbers= []
for i in range(10000):
    numbers.append(randint(1,100000))
print(numbers)
print("The smallest number in numbers is : ",getsmallest(numbers))
print("The sum of list is : ",getsum(numbers))