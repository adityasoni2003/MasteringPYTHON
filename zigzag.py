import time,sys
indent = 0 # How many spaces to indent
indentIncreasing = True #whether the indent increasing or not
try :
    while True : #the main programme loop
        print(' '*indent, end='')
        print('*********')
        time.sleep(0.1) #pause for 1/10 second
        
        if indentIncreasing:
            indent += 1 
            if indent == 20:
                # Change direction:
                indentIncreasing = False
        else :
            #decrease the number of spaces
            indent -= 1
            if indent == 0 :
                indentIncreasing = True
except KeyboardInterrupt :
    sys.exit()