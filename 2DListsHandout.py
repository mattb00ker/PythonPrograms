board = [[0,0,0],[0,0,0],[0,0,0]]

isWinner = False

def showBoard():
    print(board[0])
    print(board[1])
    print(board[2])

def xTurn():
    col = int(input("It's X's turn, which column?"))
    row = int(input("and which row?"))
    board[row][col] = "x"
    checkForWin("x")

def yTurn():
    col = int(input("It's Y's turn, which column?"))
    row = int(input("and which row?"))
    board[row][col] = "y"
    checkForWin("y")

def checkForWin(winner):
    #horizontal
    if board[0][0] == board[0][1] == board[0][2] == winner or board[1][0] == board[1][1] == board[1][2] == winner or board[2][0] == board[2][1] == board[2][2] == winner:
        print(winner, " is the winner!")
    #diagonal

    #vertical


while isWinner == False:
    showBoard()
    xTurn()
    showBoard()
    yTurn()



