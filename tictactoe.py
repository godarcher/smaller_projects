
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
    print(" " + play_board[1] + "| " + play_board[2] + "| " + play_board[3])
    print("---------")
    print(" " + play_board[4] + "| " + play_board[5] + "| " + play_board[6])
    print("---------")
    print(" " + play_board[7] + "| " + play_board[8] + "| " + play_board[9])


def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[3] == le and bo[5] == le and bo[7] == le))


def playMove():
    run = True
    while run:
        move = input("Please select a position to place an 'X' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_Is_Free(move):
                    run = False
                    insert_piece("x", move)
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
            if isWinner(play_boardCopy, let):
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
    print("welcome tic tac toe")
    print_playboard(play_board)
    while not(isplay_boardFull(play_board)):
        if not(isWinner(play_board, "o")):
            playMove()
            print_playboard(play_board)
        else:
            print("Sorry, O's won this time! ")
            break
        if not(isWinner(play_board, "x")):
            move = compMove()
            if move == 0:
                print("Tie game")
            else:
                insert_piece("o", move)
                print("Computer placed an 'o' in position", move, ":")
                print_playboard(play_board)
        else:
            print("X's won this time! Good job")
            break
    if isplay_boardFull(play_board):
        print("Tie game")


main()
