
#! This code enables persons to play tic tac toe inside the console

# This is the playboard for this game (global), it is empty at declaration
play_board = [' ' for x in range(10)]


def insert_piece(piece, pos):
    # ? This function inserts a piece to a certain position
    # * It takes as input the piece to put and a position to put
    play_board[pos] = piece


def space_Is_Free(position):
    # ? This function checks if a space on the playing board is currenlty free
    # * It takes as input a position and uses the global play_board
    return play_board[position] == " "


def print_playboard(play_board):
    # ? This function prints the current playing board
    # * it takes as input the actual play_board which is a global variable
    print("")
    print(" " + play_board[1] + " | " + play_board[2] + " | " + play_board[3])
    print("---|---|---")
    print(" " + play_board[4] + " | " + play_board[5] + " | " + play_board[6])
    print("---|---|---")
    print(" " + play_board[7] + " | " + play_board[8] + " | " + play_board[9])
    print("")


def is_Winner(board, piece):
    # ? This function checks if any of the two players have won
    # * It does this by hardcoded win definitons, with input board and possible inputs
    return (
        (board[7] == piece and board[8] == piece and board[9] == piece) or
        (board[4] == piece and board[5] == piece and board[6] == piece) or
        (board[1] == piece and board[2] == piece and board[3] == piece) or
        (board[1] == piece and board[4] == piece and board[7] == piece) or
        (board[2] == piece and board[5] == piece and board[8] == piece) or
        (board[3] == piece and board[6] == piece and board[9] == piece) or
        (board[1] == piece and board[5] == piece and board[9] == piece) or
        (board[3] == piece and board[5] == piece and board[7] == piece)
    )


def play_Move():
    # ? This function plays a move
    # * It uses the global play_board for this

    # We declare not_done bool as an later exit condition
    not_done = True

    # Continue as long as exit condition is not fulfilled
    while not_done:

        # Take user input
        move_to_make = input(
            "Please select a position to place an 'X' (1-9): ")

        try:
            # We convert the input to an integer
            move_to_make = int(move_to_make)

            # We check if the integer is inside the playing field
            if move_to_make > 0 and move_to_make < 10:
                if space_Is_Free(move_to_make):
                    run = False
                    insert_piece("x", move_to_make)
                else:
                    print("Sorry this space is occupied")
            else:
                print("Please type the number within the range")
        except:
            print("Please type a number. ")


def compMove():
    possibleMoves = [x for x, letter in enumerate(
        play_board) if letter == ' ' and x != 0]
    move = 0
    for let in ['o', 'x']:
        for i in possibleMoves:
            play_boardCopy = play_board[:]
            play_boardCopy[i] = let
            if is_Winner(play_boardCopy, let):
                move = i
                return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    if 5 in possibleMoves:
        move = 5
        return move
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isplay_boardFull(play_board):
    if play_board.count(" ") > 1:
        return False
    else:
        return True


def main():
    print("")
    print("Welcome to tic tac toe!")
    print_playboard(play_board)
    while not(isplay_boardFull(play_board)):
        if not(is_Winner(play_board, "o")):
            play_Move()
            print_playboard(play_board)
        else:
            print("")
            print("You have lost this game. ")
            break
        if not(is_Winner(play_board, "x")):
            move = compMove()
            if move == 0:
                print("")
                print("It is a tie game, good job!")
            else:
                insert_piece("o", move)
                print("Computer placed an 'o' in position", move, ":")
                print_playboard(play_board)
        else:
            print("")
            print("You have won, good job!")
            break
    if isplay_boardFull(play_board):
        print("")
        print("It is a tie game, good job!")


main()
