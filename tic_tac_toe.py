from random import randrange
count = 0
def display_board(board):
     # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print('''
          +-------+-------+-------+
          |       |       |       |
          |  ''',board[0][0],'''  |  ''',board[0][1],'''  |  ''',board[0][2],'''  |
          |       |       |       |
          +-------+-------+-------+
          |       |       |       |
          |  ''',board[1][0],'''  |  ''',board[1][1],'''  |  ''',board[1][2],'''  |
          |       |       |       |
          +-------+-------+-------+
          |       |       |       |
          |  ''',board[2][0],'''  |  ''',board[2][1],'''  |  ''',board[2][2],'''  |
          |       |       |       |
          +-------+-------+-------+
          ''')
    return board


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

    move = int(input('Enter your move: '))
    if move not in range(1,10):
        move = int(input('Enter your move: '))
        
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == move:
                board[i][j] = 'O'
        display_board(board)
    make_list_of_free_fields(board)
    
    return board,'O'

    '''  if move == 1:
        board[0][0] = 'O'
    elif move == 2:
        board[0][1] = 'O'
    elif move == 3:
        board[0][2] = 'O'
    elif move == 4:
        board[1][0] = 'O'
    elif move == 6:
        board[1][2] = 'O'
    elif move == 7:
        board[2][0] = 'O'
    elif move == 8:
        board[2][1] = 'O'
    elif move == 9:
        board[2][2] = 'O'
        '''

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    empty_square = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                empty_square.append((i,j))
    return empty_square

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    winning_flag = ''
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
        winning_flag = 'X'
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        winning_flag = 'X'
    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        winning_flag = 'X'
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        winning_flag = 'X'
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        winning_flag = 'X'
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        winning_flag = 'X'
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        winning_flag = 'X'
    elif board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
        winning_flag = 'X'
    elif board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
        winning_flag = 'O'
    elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
        winning_flag = 'O'
    elif board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
        winning_flag = 'O'
    elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        winning_flag = 'O'
    else:
        winning_flag = ''
    #print('Winning flag ', winning_flag)
    if winning_flag == 'X':
        print('I won')
        return True
    elif winning_flag == 'O':
        print('You won')
        return True
    else:
        return False
count = 0
def draw_move(board):
    # The function draws the computer's move and updates the board.
    global count
    flag = False
    if count == 0:
        board[1][1] = 'X'
        display_board(board)
        count += 1
    else:
        while flag != True:
            for i in range(3):
                j = randrange(3)
                field = i,j
                if field in make_list_of_free_fields(board):
                    board[i][j] = 'X'
                    flag = True
                    break

            display_board(board)
    make_list_of_free_fields(board)
    return (board,  'X')     


board = [[1,2,3],[4,5,6],[7,8,9]]
sign = ''

while victory_for(board, sign)!= True:
    
    board, sign = draw_move(board)
    if victory_for(board,sign) == True:
        break
    board, sign = enter_move(board)
    

   
    