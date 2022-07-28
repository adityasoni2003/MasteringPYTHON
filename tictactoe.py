theboard={'TOP-L':' ','TOP-M':' ','TOP-R':' ',
          'MID-L':' ','MID-M':' ','MID-R':' ',
          'LOW-L':' ','LOW-M':' ','LOW-R':' ' }
def printboard(board):
    print(board['TOP-L']+'|'+board['TOP-M']+'|'+board['TOP-R'])
    print('-+-+-')
    print(board['MID-L']+'|'+board['MID-M']+'|'+board['MID-R'])
    print('-+-+-')
    print(board['LOW-L']+'|'+board['LOW-M']+'|'+board['LOW-R'])
printboard(theboard)
turn='X'
for i in range(9):
    printboard(theboard)
    print('Turn for',turn,'.Move on which space?')
    move=input()
    theboard[move]=turn
    if turn =='X':
        turn = 'O'
    else:
        turn='X'
printboard(theboard)