import random,sys
print('ROCK , PAPER , SCISSOR') 
#these variables keep track of number of wins,loss and tie .
wins = 0
losses = 0
ties = 0

while True : #The main game loop
    print('%s Wins, %sLosses, %s Ties' % (wins,losses,ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissor (q)uit')
        playermove = input() 
        if playermove == 'q' :
            sys.exit() #quit the programme
        if playermove == 'r' or playermove=='p' or playermove =='s':
            break #break from player loop 
        print('one of the r , p , s or q .')
    if playermove == 'r' :
            print('Rock versus')
    elif playermove == 'p' :
            print('Paper versus')
    elif playermove == 's' :
            print('Scissor versus')
    randommove = random.randint(1,3) #Display hat the computer chooses
    if randommove == 1 :
        computermove = 'r'
        print('Rock')
    elif randommove == 2 :
        computermove = 'p'
        print('Paper')
    elif randommove == 3 :
        computermove = 's'
        print('Scissors')
        if playermove == computermove :
            print('Its a tie')           #Displaying the scores
            ties += 1
        elif playermove == 'r' and computermove == 's' :
            print('You Win!')
            wins += 1
        elif playermove == 'r' and computermove == 'p' :
            print('you Loss!')
            losses += 1
        elif playermove == 'p' and computermove == 'r':
            print('you Win!')
            wins += 1
        elif playermove == 'p' and computermove == 's':
            print('You Loss!')
            losses += 1
        elif playermove == 's' and computermove == 'p':
            print ('You Win!')
            wins += 1
        elif playermove == 's' and computermove == 'r':
            print('YOU LOSS!')
            losses += 1