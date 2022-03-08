#This is a simple tic tac toe game 
theboard = {
        'top-L':' ',
        'top-M':' ',
        'top-R':' ',
        'mid-L':' ',
        'mid-M':' ',
        'mid-R':' ',
        'low-L':' ',
        'low-M':' ',
        'low-R':' ',
        }

def printboard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'

def winnercheck(board):
    vert_L = []
    vert_M = []
    vert_R = []
    hor_T = []
    hor_M = []
    hor_L = []
    cross_L = []
    cross_R = []
    vert_L.extend([board['top-L'], board['mid-L'], board['low-L']])
    vert_M.extend([board['top-M'], board['mid-M'], board['low-M']])
    vert_R.extend([board['top-R'], board['mid-R'], board['low-R']])
    hor_T.extend([board['top-L'], board['top-M'], board['top-R']])
    hor_M.extend([board['mid-L'], board['mid-M'], board['mid-R']])
    hor_L.extend([board['low-L'], board['low-M'], board['low-R']])
    cross_L.extend([board['top-L'], board['mid-M'], board['low-R']])
    cross_R.extend([board['top-R'], board['mid-M'], board['low-L']])

    if 'X' or 'O' in vert_L:
        if vert_L[0] == vert_L[1] == vert_L[2]:
            return True, vert_L[0]
        else:
            return False, 0
    elif 'X' or 'O' in vert_M:
        if vert_M[0] == vert_M[1] == vert_M[2]:
            return True, vert_M[0]
        else:
            return False, 0
    elif 'X' or 'O' in vert_R:
        if vert_R[0] == vert_R[1] == vert_R[2]:
            return True, vert_R[0]
        else:
            return False, 0
    elif 'X' or 'O' in hor_T:
        if hor_T[0] == hor_T[1] == hor_T[2]:
            return True, hor_T[0]
        else:
            return False, 0

    elif 'X' or 'O' in hor_M:
        if hor_M[0] == hor_M[1] == hor_M[2]:
            return True, hor_M[0]
        else:
            return False, 0
    elif 'X' or 'O' in hor_L:
        if hor_L[0] == hor_L[1] == hor_L[2]:
            return True, hor_L[0]
        else:
            return False, 0
    elif 'X' or 'O' in cross_L:
        if cross_L[0] == cross_L[1] == cross_L[2]:
            return True, cross_L[0]
        else:
            return False, 0
    elif 'X' or 'O' in cross_R:
        if cross_R[0] == cross_R[1] == cross_R[2]:
            return True, cross_R[0]
        else:
            return False, 0


for _ in range(9):
    printboard(theboard)
    print('Turn for {}, move to which space?'.format(turn))
    print('Options are : top-L, top-M, top-R, mid-L, mid-M, mid-R, low-L, low-M, low-R')
    test = False
    while test == False:
        move = input('Enter your move: ')
        if move in theboard.keys():
            piece = theboard.get(move, 0)
            if piece == 'X' or piece == 'O':
                print('Position filled up with {}, Try again'.format(piece))
                test = False
            else:
                test = True
        else:
            print('Enter a valid board position :')
            test = False

    theboard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    winner, winnersymb = winnercheck(theboard)
    if winner == True:
        print('{} has won the match'.format(winnersymb))
        break
    else:
        continue

printboard(theboard)



