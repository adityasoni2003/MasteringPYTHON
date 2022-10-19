for i in range(99,1,-1):
    print('%s bottles of beer on the wall,'%(i))
    print('%s bottles of beer,'%(i))
    print('Take one down,')
    print('Pass it around,')
    if i-1 == 1:
        print('1 bottle of beer on the wall,')
        print('1 bottle of beer,')
        print('Take one down,')
        print('Pass it around,')
        print('No more bottles of beer on the wall!')