from IPython.display import clear_output

board = """
 {s1:^3} | {s2:^3} | {s3:^3}
-----+-----+-----
 {s4:^3} | {s5:^3} | {s6:^3}
-----+-----+-----      123
 {s7:^3} | {s8:^3} | {s9:^3}       456
                       789  
"""

def initialize_board(play):
    for n in range(9):
        play["s{}".format(n+1)] = ""

def show_board(play):
    """ display the playing board.  We take a dictionary with the current state of the board
    We rely on the board string to be a global variable"""
    print(" TIC-TAC-TOE GAME" , "\n", "Player 1: symbol 'x'; Player 2: symbol 'o'")
    print(board.format(**play))

def get_move(n, xo, play):
    """ ask the current player, n, to make a move -- make sure the square was not 
        already played.  xo is a string of the character (x or o) we will place in
        the desired square """
    valid_move = False
    while not valid_move:
        idx = input("Player {}, enter your move (1-9): ".format(n))

        # Test if the input is an integer
        try:
            idx = int(idx)

            # Verify that the integer is between 1 and 9
            if idx < 1 or idx > 9:
                valid_move = False
                print("Invalid move, type an integer number between 1 and 9.")
            else:
                valid_move = True

        except ValueError:
            print("Invalid move, type an integer number between 1 and 9.")


        if valid_move == True:

            if play["s{}".format(idx)] == "":
                play["s{}".format(idx)] = xo
            else:
                print("Invalid, that cell is already occupied.")
                valid_move = False

def victory_move(xo, play):

    winning_moves = [(1,2,3), (4,5,6), (7,8,9), (1,5,9), (3,5,7), (1,4,7), (2,5,8), (3,6,9)]

    victory = False

    # Loop over the different winning moves
    for i in winning_moves:
        
        # Loop over the necessary position to win the game
        for k in range(0,3):

            # If there is the same symbol thrice, then it's a win
            if play[f"s{i[k]}"]==xo:
                victory = True
            else: 
                victory = False
                break

        if victory == True:
            break

    return victory

def play_game():
    """ play a game of tic-tac-toe """
    
    play ={}
    initialize_board(play)
    show_board(play)

    n = [0, 1]
    symb=['x', 'o']
    alt = 0
    victory=False

    for moves in range(9): 

        # The player move is taken as an input  
        get_move(n[alt], symb[alt], play)

        # Clearing output board after each move
        clear_output()
        
        # The updated board is displayed
        show_board(play) 

        # Verify if one of the player won
        victory = victory_move(symb[alt], play)
        if victory == True:
            break

        # Player change
        if alt == 0:
            alt = 1
        else:
            alt = 0 
    8
    # Game result is printed out
    if victory == True:
        print(f"Player {n[alt]+1} (symbol '{symb[alt]}') wins!")
    else:
        print("Tie!")
