import random


def password(x):
    
    
    pw = []
    
    spchar = '~!@#$%^&*()_+' #in question these were special chars given
    lowerchar = 'abcdefghijklmnopqrstwuvxyz'
    upperchar = 'ABCDEFGHIJKLMNOPQRSTWUVXYZ'
    numbers = '1234567890'

    all_Characters = spchar + lowerchar + upperchar + numbers
    
    if x < 12 :
        x = 12
    pw.append(spchar[random.randint(0,13)])
    pw.append(lowerchar[random.randint(0,25)])
    pw.append(upperchar[random.randint(0,25)])
    pw.append(numbers[random.randint(0,9)])
    while len(pw) < x:

        pw.append(all_Characters[random.randint(0,len(all_Characters))])
        
        
        random.shuffle(pw)
        
    return ''.join(pw)
    
        
        
        
         
print(password(13))
