import random

# Sukuriamas tuščias žaidimo lentos sąrašas su 9 langeliais
board = [" ", " ", " ",
        " ", " ", " ",
        " ", " ", " "]
players = {"X": 0, "O": 0} #Žaidėjų laimėjimų skaičius, pradedant nuo 0
currentPlayer = "X"
winner = None
gameRunning = True

# game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# take player input
def playerInput(board):

    try:
        inp = int(input("Select a spot 1-9: "))
        if inp < 1 or inp > 9:
            print("Invalid input! Please select a number between 1 and 9.")
            return
        if board[inp-1] == " ":
            board[inp-1] = currentPlayer
        else:
            print("Player is already at that spot.")
    except ValueError:
        print(("Invalid input! Please enter a valid number."))



# check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != " ":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != " ":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        winner = board[3]
        return True


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != " ":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != " ":
        winner = board[2]
        return True


def checkIfWin(board):
    global gameRunning
    if checkHorizontle(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        players[winner] += 1
        print(f"Player X wins: {players['X']}, Player O wins: {players['O']}")
        gameRunning = False

    elif checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        players[winner] += 1
        print(f"Player X wins: {players['X']}, Player O wins: {players['O']}")
        gameRunning = False

    elif checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        players[winner] += 1
        print(f"Player X wins: {players['X']}, Player O wins: {players['O']}")
        gameRunning = False


def checkIfTie(board):
    global gameRunning
    if " " not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False


# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
while True:
    while gameRunning:
        printBoard(board)
        playerInput(board)
        checkIfWin(board)
        checkIfTie(board)
        switchPlayer()

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Goodbye! Thanks for playing.")
        break
    else:
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        currentPlayer = "X"
        winner = None
        gameRunning = True



