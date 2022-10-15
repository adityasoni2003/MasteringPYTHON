#Exercise5
def fizzbuzz(n):
    for i in range(1,n):
        if i%15 == 0:
            print("Fizzbuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)
x=int(input("Enter no. :"))
fizzbuzz(x)