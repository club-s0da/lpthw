# Function to print out a standard TicTacToe board display:
def display_board(board):
    print('\n *100')
    print('   |   |  ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |  ')
    print('-----------')
    print('   |   |  ')
    print(' '+board[4]+ ' | '+board[5]+' | '+board[6])
    print('   |   |  ')
    print('-----------')
    print('   |   |  ')
    print(' '+board[1]+ ' | '+board[2]+' | '+board[3])
    print('   |   |  ')

# Function to assign marker, X or O, to player 1 or player 2
def player_input():
    '''OUTPUT = player1_marker, player2_marker = player_input() '''
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, please select your marker, X or O: ').upper()
        player1 = marker
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'

    return (player1,player2)

# A function to place marker, X or O, on the board:
def place_marker(board,marker,position):
    # All this below is to make sure input is a digit and is within range(1,10)
    position = 'cats'
    acceptable_range = range(1,10)
    within_range = False

    while position.isdigit() == False or within_range == False:

        position = input("Please choose a position (1-9): ")

        if position.isdigit() == False:
            print("Sorry, that is not a digit.")

        if position.isdigit() == True:
            if int(position) in acceptable_range:
                within_range = True
            else:
                print("Sorry, that number is not in range.")
                pass
# THIS part below is the ONLY part that really matters!
# ..that does what we want the function to do!
    board[int(position)] = marker

# Function to check for winning combinations:
def win_check(board, mark):
        return ((board[7] == board[4] == board[1] == mark) or
        (board[8] == board[5] == board[2] == mark) or
        (board[9] == board[6] == board[3] == mark) or
        (board[7] == board[8] == board[9] == mark) or
        (board[4] == board[5] == board[6] == mark) or
        (board[1] == board[2] == board[3] == mark) or
        (board[7] == board[5] == board[3] == mark) or
        (board[1] == board[5] == board[9] == mark))

# Using random module to decide which player goes first:
def choose_first():
    import random
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# Function to check for empty spaces on the board (returns a boolean)
def space_check(board,position):
    return board[position] == ' '
    # If True, the position is empty!!

# Function checks if the board is FULL, True if full, False if not!
def full_board_check(board):
    for n in range(1,10):
        if space_check(board,n): # So, if THIS function is True, return False!
            return False # board has empty space somewhere!
        return True # board is FULL if True

# Function to ask for the player's next position AND,
# ..uses space_check() function to check if the position is free
# I don't fully get this one.......??????
def player_choice(board):
    position = 0

    while position not in range(1,10) or not space_check(board,position):
        position = int(input('Choose your next position, 1-9: '))

# Function to ask player if they want to play again and returns boolean True if yes
def replay():
    return input('Do you want to play again, Yes or No: ').lower().startswith('y')




# Now the LOGIC to tie it all together!!!

# REMINDER: These are my functions below:
# def display_board(board): --> displays board
# def player_input(): --> assigns marker to X or O to player 1 or 2
# def place_marker(board,marker,position): --> places marker
# def win_check(board, mark): --> checks for winning combos
# def choose_first(): --> choooses which player 1 or player 2 goes first
# def space_check(board,position): --> checks if empty space on board
# def full_board_check(board): --> checks if board is full (if it's a draw)
# def player_choice(board): --> user input to choose next position
# def replay(): --> asks to play game, yes if continue, no breaks

print('Welcome to Tic Tac Toe!')

# Here we defined some things that DIDN'T have to be defined above
while True:
    current_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn+' will go first.')

    play_game = input('Are you ready to play? Enter Y or N: ')
    if play_game.lower == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(current_board)
            index_position = player_choice(current_board)
            place_marker(current_board,player1_marker,index_position)

            if win_check(current_board,player1_marker):
                display_board(current_board)
                print('Congratulations, Player 1 wins the game!')
                game_on = False
            else:
                if full_board_check(current_board):
                    display_board(current_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            display_board(current_board)
            index_position = player_choice(current_board)
            place_marker(current_board,player2_marker,index_position)

            if win_check(current_board,player2_marker):
                display_board(current_board)
                print('Congratulations, Player 2 wins the game!')
                game_on = False
            else:
                if full_board_check(current_board):
                    display_board(current_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break
