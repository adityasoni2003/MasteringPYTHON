def isleapYear(x):
    if x % 4 == 0 :
        
        if x % 100 == 0 :
            if x % 400 == 0:
                return True
            else :
                return False
        return True
    else :
        return False
    assert isLeapYear(1999) == False

    assert isLeapYear(2000) == True

    assert isLeapYear(2001) == False

    assert isLeapYear(2004) == True

    assert isLeapYear(2100) == False

    assert isLeapYear(2400) == True
    
print(isleapYear(2100))
