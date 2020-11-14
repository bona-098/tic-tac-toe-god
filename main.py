# Python Tic Tac Toe
# Written by MysteryBlokHed

import random

running = True

board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]


def show():
    print(board[0], "|", board[1], "|", board[2])
    print("----------")
    print(board[3], "|", board[4], "|", board[5])
    print("----------")
    print(board[6], "|", board[7], "|", board[8])


def checkLine(char, spot1, spot2, spot3):
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        return True


def checkTwo(char, spot1, spot2):
    if board[spot1] == char and board[spot2] == char:
        return True


def checkAll(char):
    if checkLine(char, 0, 1, 2):
        return True
    if checkLine(char, 3, 4, 5):
        return True
    if checkLine(char, 6, 7, 8):
        return True
    if checkLine(char, 0, 3, 6):
        return True
    if checkLine(char, 1, 4, 7):
        return True
    if checkLine(char, 2, 5, 8):
        return True
    if checkLine(char, 0, 4, 8):
        return True
    if checkLine(char, 2, 4, 6):
        return True


def chooseNextPosition():
    if board[4] != "o" and board[4] != "x":
        return 4
    elif checkTwo("o", 0, 1) and board[2] != "o" and board[2] != "x":
        return 2
    elif checkTwo("o", 1, 2) and board[0] != "o" and board[0] != "x":
        return 0
    elif checkTwo("o", 0, 2) and board[1] != "o" and board[1] != "x":
        return 1
    elif checkTwo("o", 3, 4) and board[5] != "o" and board[5] != "x":
        return 5
    elif checkTwo("o", 4, 5) and board[3] != "o" and board[3] != "x":
        return 3
    elif checkTwo("o", 3, 5) and board[4] != "o" and board[4] != "x":
        return 4
    elif checkTwo("o", 6, 7) and board[8] != "o" and board[8] != "x":
        return 8
    elif checkTwo("o", 7, 8) and board[6] != "o" and board[6] != "x":
        return 6
    elif checkTwo("o", 6, 8) and board[7] != "o" and board[7] != "x":
        return 7
    elif checkTwo("o", 0, 3) and board[6] != "o" and board[6] != "x":
        return 6
    elif checkTwo("o", 3, 6) and board[0] != "o" and board[0] != "x":
        return 0
    elif checkTwo("o", 0, 6) and board[3] != "o" and board[3] != "x":
        return 3
    elif checkTwo("o", 1, 4) and board[7] != "o" and board[7] != "x":
        return 7
    elif checkTwo("o", 4, 7) and board[1] != "o" and board[1] != "x":
        return 1
    elif checkTwo("o", 1, 7) and board[4] != "o" and board[4] != "x":
        return 4
    elif checkTwo("o", 2, 5) and board[8] != "o" and board[8] != "x":
        return 8
    elif checkTwo("o", 5, 8) and board[2] != "o" and board[2] != "x":
        return 2
    elif checkTwo("o", 2, 8) and board[5] != "o" and board[5] != "x":
        return 5
    elif checkTwo("o", 0, 4) and board[8] != "o" and board[8] != "x":
        return 8
    elif checkTwo("o", 4, 8) and board[0] != "o" and board[0] != "x":
        return 0
    elif checkTwo("o", 0, 8) and board[4] != "o" and board[4] != "x":
        return 4
    elif checkTwo("o", 2, 4) and board[6] != "o" and board[6] != "x":
        return 6
    elif checkTwo("o", 4, 6) and board[2] != "o" and board[2] != "x":
        return 2
    elif checkTwo("o", 2, 6) and board[4] != "o" and board[4] != "x":
        return 4
    elif board[0] == "x" and board[4] == "o" and board[8] == "x" and board[7] != "o" and board[7] != "x" or board[
        2] == "x" and board[4] == "o" and board[6] == "x" and board[7] != "o" and board[7] != "x":
        return 7
    elif board[0] == "x" and board[4] == "o" and board[8] == "x" and board[1] != "o" and board[1] != "x" or board[
        2] == "x" and board[4] == "o" and board[6] == "x" and board[1] != "o" and board[1] != "x":
        return 1
    elif board[4] == "x" and board[2] != "o" and board[2] != "x":
        return 2
    elif checkTwo("x", 4, 6) and board[2] == "o" and board[0] != "o" and board[0] != "x":
        return 0
    elif checkTwo("x", 7, 5) and board[8] != "o" and board[8] != "x":
        return 8
    elif checkTwo("x", 3, 7) and board[6] != "o" and board[6] != "x":
        return 6
    elif checkTwo("x", 1, 3) and board[0] != "o" and board[0] != "x":
        return 0
    elif checkTwo("x", 1, 5) and board[2] != "o" and board[2] != "x":
        return 2
    elif checkTwo("x", 0, 1) and board[2] != "o" and board[2] != "x":
        return 2
    elif checkTwo("x", 1, 2) and board[0] != "o" and board[0] != "x":
        return 0
    elif checkTwo("x", 0, 2) and board[1] != "o" and board[1] != "x":
        return 1
    elif checkTwo("x", 3, 4) and board[5] != "o" and board[5] != "x":
        return 5
    elif checkTwo("x", 4, 5) and board[3] != "o" and board[3] != "x":
        return 3
    elif checkTwo("x", 3, 5) and board[4] != "o" and board[4] != "x":
        return 4
    elif checkTwo("x", 6, 7) and board[8] != "o" and board[8] != "x":
        return 8
    elif checkTwo("x", 7, 8) and board[6] != "o" and board[6] != "x":
        return 6
    elif checkTwo("x", 6, 8) and board[7] != "o" and board[7] != "x":
        return 7
    elif checkTwo("x", 0, 3) and board[6] != "o" and board[6] != "x":
        return 6
    elif checkTwo("x", 3, 6) and board[0] != "o" and board[0] != "x":
        return 0
    elif checkTwo("x", 0, 6) and board[3] != "o" and board[3] != "x":
        return 3
    elif checkTwo("x", 1, 4) and board[7] != "o" and board[7] != "x":
        return 7
    elif checkTwo("x", 4, 7) and board[1] != "o" and board[1] != "x":
        return 1
    elif checkTwo("x", 1, 7) and board[4] != "o" and board[4] != "x":
        return 4
    elif checkTwo("x", 2, 5) and board[8] != "o" and board[8] != "x":
        return 8
    elif checkTwo("x", 5, 8) and board[2] != "o" and board[2] != "x":
        return 2
    elif checkTwo("x", 2, 8) and board[5] != "o" and board[5] != "x":
        return 5
    elif checkTwo("x", 0, 4) and board[8] != "o" and board[8] != "x":
        return 8
    elif checkTwo("x", 4, 8) and board[0] != "o" and board[0] != "x":
        return 0
    elif checkTwo("x", 0, 8) and board[4] != "o" and board[4] != "x":
        return 4
    elif checkTwo("x", 2, 4) and board[6] != "o" and board[6] != "x":
        return 6
    elif checkTwo("x", 4, 6) and board[2] != "o" and board[2] != "x":
        return 2
    elif checkTwo("x", 2, 6) and board[4] != "o" and board[4] != "x":
        return 4
    else:
        random.seed()
        return random.randint(0, 8)


show()

while running:
    if checkAll("x"):
        print("~~~~~ X WINS ~~~~~")
        running = False
        break
    if checkAll("o"):
        print("~~~~~ O WINS ~~~~~")
        running = False
        break

    response = input("Select a spot: ")
    try:
        response = int(response)
    except ValueError:
        print("That is not an integer!")
        exit()

    if response < 1 or response > 9:
        print("That space does not exist!")
        exit()

    response -= 1

    if board[response] != "x" and board[response] != "o":
        board[response] = "x"

        if board[0] != 1 and board[1] != 2 and board[2] != 3 and board[3] != 4 and board[4] != 5 and board[5] != 6 and \
                board[6] != 7 and board[7] != 8 and board[8] != 9:
            if checkAll("x"):
                show()
                print("~~~~~ X WINS ~~~~~")
                running = False
                break
            if checkAll("o"):
                show()
                print("~~~~~ O WINS ~~~~~")
                running = False
                break
            show()
            print("No spots left!")
            running = False
            break
        else:
            while True:
                opponent = chooseNextPosition()

                if board[opponent] != "o" and board[opponent] != "x":
                    board[opponent] = "o"
                    break

    else:
        print("This spot is taken!")

    show()