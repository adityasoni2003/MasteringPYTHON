from logging.config import valid_ident


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

def ValidDate(year,month,day):
    

    if not (1 <= month <= 12):

        return False

    if isleapYear(year) and month == 2 and day == 29:

        return True

    if month in (1, 3, 5, 7, 8, 10, 12) and not (1 <= day <= 31):

        return False

    elif month in (4, 6, 9, 11) and not (1 <= day <= 30):

        return False

    

    elif month == 2 and not (1 <= day <= 28):

        return False
   
    return True
    
''' 
    if isleapYear(year) == False:
        if month <= 12:
            if month == 2 and day <= 28:
                return True
            elif month == 4 or 6 or 9 or 11 and day <= 30 :
                return True
            elif month == 1 or 3 or 5 or 7 or 8 or 10 or 12 and day <= 31 :
                return True
            else:
                return False
        else :
            return False
    else:
        if month <= 12:
            if month == 2 and day <= 29:
                return True
            elif month == 4 or 6 or 9 or 11 and day <= 30 :
                return True
            elif month == 1 or 3 or 5 or 7 or 8 or 10 or 12 and day <= 31 :
                return True
            else:
                return False
        else :
            return False
        '''
        
print(ValidDate(2022,4,4))