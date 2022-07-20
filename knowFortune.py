import random 
def getanswer(answernumber):
    if answernumber == 1:
        return 'You are Lucky'
    elif answernumber == 2:
        return 'Today not good for you'
    elif answernumber == 3:
        return 'cant be decided'
    elif answernumber == 4:
        return ' be aware from dogs'
    elif answernumber == 5:
        return 'Can get your love of life'
    elif answernumber == 6:
        return 'Dont go outside today'
    elif answernumber == 7:
        return 'you gonna make it today'
    elif answernumber == 8:
        return 'You are champ today'
    elif answernumber == 9:
        return 'Bad time starts from now'
r = random.randint(1,9)
Fortune = getanswer(r)
print(Fortune)