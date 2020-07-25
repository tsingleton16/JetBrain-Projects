board = [' '] * 9

def print_board(bo):
    print(' ---------')
    print('|', bo[0], bo[1], bo[2],'|')
    print('|', bo[3], bo[4], bo[5], '|')
    print('|', bo[6], bo[7], bo[8], '|')
    print(' ---------')

def create_board(bo):
    new_board = []
    for item in board:
        new_board.append(item)
    return new_board

def winner(bo, letter):
    if bo[0] == letter and bo[1] == letter and bo[2] == letter:
        return True
    elif bo[2] == letter and bo[4] == letter and bo[5] == letter:
        return True
    elif bo[6] == letter and bo[7] == letter and bo[8] == letter:
        return True
    elif bo[0] == letter and bo[3] == letter and bo[6] == letter:
        return True
    elif bo[1] == letter and bo[4] == letter and bo[7] == letter:
        return True
    elif bo[2] == letter and bo[5] == letter and bo[8] == letter:
        return True
    elif bo[0] == letter and bo[4] == letter and bo[8] == letter:
        return True
    elif bo[2] == letter and bo[4] == letter and bo[6] == letter:
        return True
    return False
    
print_board(board)
player_board = create_board(board)

while True:
    x, y= input('Enter the coordinates: ').split()
    turn = 0
    if winner(player_board,'X'):
        print('X wins')
        break
        
    elif winner(player_board, 'O'):
        print('O wins')
        break
        
    elif  winner(board, 'X') and not winner(board,'O') and turn == 9:
        print('Draw')
        break

    if not x.isdigit() or not y.isdigit():
        print('You should enter numbers!')
        
    elif not(1 <= int(x) <=3) or not(1<= int(y) <= 3):
        print('Coordinates should be from 1 to 3!')

    elif player_board[3* (3-int(y)) + (int(x)-1)] == 'X' or player_board[3* (3-int(y)) + (int(x)-1)] == 'O':
        print('This cell is occupied! Choose another one!')  
         
    else:
        if turn % 2 == 0:
            turn += 1
            player_board[3 * (3-int(y)) + (int(x)-1)] = 'X'
            print_board(player_board)
        else:
            turn +=1
            player_board[3 * (3-int(y)) + (int(x)-1)] = ')'
            print_board(player_board)
    