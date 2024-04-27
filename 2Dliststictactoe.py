board = [[0,0,0],[0,0,0],[0,0,0]]

isWinner = False

def showBoard():
    print(board[0])
    print(board[1])
    print(board[2])

def xTurn():
    col = input("it's X's turn, which column?")
    row = input("and which row?")
    board[int(row)][int(col)] = "x"
    checkForWin("x")

def yTurn():
    col = input("it's Y's turn, which column?")
    row = input("and which row?")
    board[int(row)][int(col)] = "y"
    checkForWin("y")

def checkForWin(winner):
    #horizontal
    if board[0][0] == board[0][1] == board[0][2] == winner or board[1][0] == board[1][1] == board[1][2] == winner or board[2][0] == board[2][1] == board[2][2] == winner:
        print(winner, " is the winner!")
    #diagonal
    if board[0][0] == board[1][1] == board[2][2] == winner or board[0][2] == board[1][1] == board[2][0] == winner :
        print(winner, " is the winner!")
    #vertical
    if board[0][0] == board[1][0] == board[2][0] == winner or board[0][1] == board[1][1] == board[2][1] == winner or board[0][2] == board[1][2] == board[2][2] == winner :
        print(winner, " is the winner!")

while isWinner == False:
    showBoard()
    xTurn()
    showBoard()
    yTurn()



