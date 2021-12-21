from os import sep

def main():
    board = [[1,2,3],[4,5,6],[7,8,9]]
    board_game = [['_','_','_'],['_','_','_'],['_','_','_']]
    sw = True
    game = True
    while game:
        draw_board(board)
        draw_board(board_game)
        sw = get_player_input(sw,board_game)

def draw_board(board):
    print('\nTic-Tac-Toe')
    print('------------')
    for i in board:
        print('',*i,sep='||',end='||\n')
        print('------------')

def get_player_input(sw,board):
    while True:
        if sw == True:
            position = int(input('X: Where would you like to place your piece (1 - 9):'))
            if checkPositions(position,board) == True:
                place_char_on_board(position,board,'X')
                return  False
        else:
            position = int(input('O: Where would you like to place your piece (1 - 9):'))
            if checkPositions(position,board) == True:
                place_char_on_board(position,board,'O')
                return True
    
def checkPositions(position,board):   
    match position:
        case (1|2|3):
            if board[0][(position-1)] == '_':
                return True
            else:
                print('That spot has already been chosen. Try again.')
                return False
        case (4|5|6):
            if board[1][int((position-1)-3)] == '_':
                return True
            else:
                print('That spot has already been chosen. Try again.')
                return False
        case (7|8|9):
            if board[2][int((position-1)-6)] == '_':
                return True
            else:
                print('That spot has already been chosen. Try again.')
                return False
        
def place_char_on_board(position,board,char):
    match position:
        case (1|2|3):
            board[0][int(position-1)] = char
            check_winner(board,char)
        case (4|5|6):
            board[1][int((position-1)-3)] = char
            check_winner(board,char)
        case (7|8|9):
            board[2][int((position-1)-6)] = char
            check_winner(board,char)

def check_winner(board,char):
    #Check trasversal lines
    if board[0][0] == char and board[0][1] == char and board[0][2] == char:
        print('Congratulations player: '+str(char)+' You win')
        return True
    elif board[1][0] == char and board[1][1] == char and board[1][2] == char:
        print('Congratulations player: '+str(char)+' You win')
        return True
    elif board[2][0] == char and board[2][1] == char and board[2][2] == char:
        print('Congratulations player: '+str(char)+' You win')
        return True
    #Check vertical lines
    elif board[0][0] == char and board[1][0] == char and board[2][0] == char:
        print('Congratulations player: '+str(char)+' You win')
        return True
    elif board[0][1] == char and board[1][1] == char and board[2][1] == char:
        print('Congratulations player: '+str(char)+' You win')
        return True
    elif board[0][2] == char and board[1][2] == char and board[2][2] == char:
        print('Congratulations player: '+str(char)+' You win')
        return True
    #Check diagonal lines
    elif board[0][0] == char and board[1][1] == char and board[2][2] == char:
        print('Congratulations player: '+str(char)+' You win')
        return True
    elif board[0][2] == char and board[1][1] == char and board[2][0] == char:
        print('Congratulations player: '+str(char)+' You win')
        return True
    else:
        return False
    
if __name__ == "__main__":
    main()