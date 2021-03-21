import random


def player2start():
    return random.randint(0,1)

# This function checks and applies the user's move on the board
def userTurn(board):
    moveRow=int(input("Select Row (1 to 3): "))
    moveCol=int(input("Select Column (1 to 3):"))
    # Checks move availability
    while(board[moveRow][moveCol]!=0):
        print("This move is unavailable, please choose another box !")
        showBoard(board)
        moveRow=int(input("Select Row (1 to 3): "))
        moveCol=int(input("Select Column (1 to 3):"))
        moveRow-=1
        moveCol-=1
    
    board[moveRow][moveCol]=-1
  
    return board
    
# This function checks if the board is at a winning state and returns a value
# correspond to the appropriate player. 10 is for AI, -10 is for Player (user) and 0 is for tie
def boardEvaluation(board):
    sumDiag=0
    sumAntiDiag=0
    for i in range(3):
        rowSum=sum(board[i][:]) # Calculates sum of every Row of the board
        colSum=0
        for row in board: colSum+=row[i]    # Calculates the sum of every Column of the board
        sumDiag+=board[i][i]    # Stores the sum of main Diagonal
        sumAntiDiag+=board[i][2-i]  # Stores the sum of Antidiagonal

        if rowSum==3 or colSum==3:  # Checks if AI wins via columns or rows conditions
            return 10
        elif rowSum==-3 or colSum==-3: # Checks if Player wins via columns or rows conditions
            return -10
    if sumDiag==3 or sumAntiDiag==3: # Checks if AI wins via diag or antidiag conditions
        return 10
    elif sumDiag==-3 or sumAntiDiag==-3: # Checks if Player wins via diag or antidiag conditions
        return -10
    else:   # If none of the above is valid
        return 0


# Checks if the board is full or there any more available moves    
def fullBoard(board):
    for row in board:
        for element in row:
            if element==0:
                return False
    return True

# Minimax algortihm recursive implementation
def minimaxAlg(board,isMaximize):
    # Checks if board is at a winning state and returns board's value (10 or -10)
    if(boardEvaluation(board)==10 or boardEvaluation(board)==-10):
        return boardEvaluation(board)
    elif(fullBoard(board)==True):   #Cheecks if the board is full and returs board's value (0)
        return boardEvaluation(board)
    # Maximizers Turn (AI)
    if isMaximize==1:
        bestMax=-11
        for i in range(3):
            for j in range(3):
                if board[i][j]==0:
                    board[i][j]=1   # Maximizer's move under investigation
                    bestMax=max(bestMax,minimaxAlg(board,0))  # Calls minimax to check the value 
                    board[i][j]=0   # Undo investigated move
        return bestMax  # Returns best move for the mazimizer
    # Minimizers Turn (Player)          
    elif isMaximize==0: 
        bestMin=11
        for i in range(3):
            for j in range(3):
                if board[i][j]==0:
                    board[i][j]=-1 # Minimizer's move under investigation
                    bestMin=min(bestMin,minimaxAlg(board,1)) # Calls minimax to check the value
                    board[i][j]=0 # Undo investigated move
        return bestMin  # Returns best move for the minimizer
                
        
    


# This function uses minimaxAlg and decides which is the best move for the AI to play.
# Returns the row and column which correspond to the best move
def bestMove(board):
    bestValue=-11 # Initializing bestValue to a very small value

    for i in range(3):
        for j in range(3):
            # First move of the maximizer    
            if board[i][j]==0:
                board[i][j]=1 # Move under investigation
                currValue=minimaxAlg(board,0) # Minimizer's turn 
                if(currValue>bestValue): # If we step on a move with better value than the previous
                    bestRow=i # We store its row
                    bestCol=j # And column
                    bestValue=currValue # And se this move's value as the new "bestValue"
                board[i][j]=0 # Undo under investigation move
    return bestRow,bestCol # Return the position (i and j) of the new best move


# This functions just applies the best move on the board
def aiMove(board):
    [i,j]=bestMove(board)
    board[i][j]=1
    return board

# This is an auxiliary function. It maps board numbers to symbols and prints the board.
# Will be replaced by graphics, but still usefull for debugging
def showBoard(board):
    for row in board:
        print("")
        for element in row:
            if element==-1:
                print('X', end=" ")
            elif element==1:
                print('O', end=" ")
            else:
                print('_', end=" ")
    print("")
    print("")

# This Function checks if we are on a terminal state and declares the winner
def gameIsOver(board):
    if boardEvaluation(board)==-10:
        print("The Winner is X !")
        return True
    elif boardEvaluation(board)==10:
        print("The Winner is O !")
        return True
    elif fullBoard(board):
        print("It's a tie !")
        return True
    else:
        return False


########## Function Calling ##########
    
#Board initialisation
board=[[0,0,0],
    [0,0,0],
    [0,0,0]]

while(1):
    showBoard(board)
    if gameIsOver(board): break
    board=userTurn(board)
    board=aiMove(board)
    




    



