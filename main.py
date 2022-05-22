import random
import time

def attackingQueensMatrix(queens):
    attackMatrix = [[0 for _ in range(len(queens))] for _ in range(len(queens))]

    for i in range(len(queens)):
        copyQueens = queens.copy()
        for j in range(len(queens)):
            if queens[i] == j: # That means queen is on same spot.
                attackMatrix[j][i] = attackingQueensCounter(queens)
            # Queens are moving only column-based system in 8-queens puzzle.
            # I have to move queens to every row in a same column then calculate how many queens attack on each other.
            # After the calculation phase, I need an attack matrix that shows attacks of every queens spot.
            elif copyQueens[i] != j:
                # for calculating
                copyQueens[i] = j
                attackMatrix[j][i] = attackingQueensCounter(copyQueens)
    print("Attack Matrix Display\n"
          "-----------------------")
    for i in range(8):
        for j in range(8):
            print("{:<3}".format(attackMatrix[i][j]),end="")
        print()
    print()
    return attackMatrix

def randomSpotQueens():
    columnsOfQueens = [0] * 8
    for i in range(8):
        # assigning queens to each column randomly.
        columnsOfQueens[i] = random.randint(0,7) # index-based.
    return columnsOfQueens

def createChessBoard(columns):
    board = [[0 for _ in range(len(columns))] for _ in range(len(columns))]
    for i in range(len(columns)):
        # assigning 1 for the queens on the board.
        index = columns[i] # find row
        board[index][i] = 1

    return board

def displayChessBoard(board):
    copyBoard = board.copy()
    for i in range(8):
        for j in range(8):
            # traversing each column, if it's queen(1) print "Q".
            if copyBoard[i][j] == 1:
                print("Q", end="  ")
            else:
                print("*", end="  ")
        print()
    print()


def attackingQueensCounter(queens):
    attackOfQueens = 0
    for i in range(0, len(queens) - 1):
        for j in range(i+1, len(queens)):
            if queens[i] == queens[j]: # same direction
                # print("same direction: ",queens[i], ",", queens[j])
                attackOfQueens += 1

            elif ((queens[i] - queens[j]) == i - j) or ((queens[i] - queens[j]) == -(i-j)): # same diagonal
                attackOfQueens += 1
                # print("same diagonal: ", queens[i], ",", queens[j])

    return attackOfQueens


def main():
    randomRestartArray = []
    movementArray = []
    timeArray = []
    solutionCount = 1
    for i in range(15): # Loop will be executed 15 times for solutions
        queens = randomSpotQueens()
        board = createChessBoard(queens)
        print("Queens' spot at the beginning (column & index-based)")
        print(queens)
        print()
        print("Initial State of Queens at the beginning:")
        print("-----------------------")
        displayChessBoard(board)
        print("SOLUTION", solutionCount)
        randomRestarts = 0
        movements = 0
        startTime = time.time()
        while(attackingQueensCounter(queens) > 0):
            attackMatrix = attackingQueensMatrix(queens)

            smallestAttack = 0
            smallestAttackRow = 0
            smallestAttackColumn = 0
            case = False
            smallestAttack = attackingQueensCounter(queens)
            movements += 1
            for j in range(len(queens)):
                for k in range(len(queens)):
                    if (attackMatrix[j][k] < smallestAttack):
                        smallestAttack = attackMatrix[j][k]
                        smallestAttackRow = j
                        smallestAttackColumn = k
                        case = True # That means there is a better position and smallest one has changed.

            print("Smallest attack: ", smallestAttack)
            if (case == True):
                print("Move queen", queens[smallestAttackColumn], end=" ")
                queens[smallestAttackColumn] = smallestAttackRow
                print("to",queens[smallestAttackColumn],"on the {}. column ({}. index)".format(smallestAttackColumn+1, smallestAttackColumn))
                board = createChessBoard(queens)
                print("Queens' spot after: ",queens)
                print("         Board \n"
                      "----------------------")
                displayChessBoard(board)
            else:
                print("There is no better position. I have to ruin my board and random restart")
                queens = randomSpotQueens()
                board = createChessBoard(queens)

                randomRestarts += 1

        solutionCount += 1

        endTime = time.time()
        print("Queens' spot at the end of the puzzle (column & index-based): ", queens)
        print("Let's check the board:\n"
              "----------------------")
        displayChessBoard(board)
        print("Solved!")
        randomRestartArray.append(randomRestarts)
        movementArray.append(movements)
        print()

        timeArray.append(endTime - startTime)

    print("              Program Statictics")
    print()
    print("{:<12}{:<12}{:<20}{:<20}".format("Solution", "Movement", "Random Restart", "Time"))
    print("--------    --------    --------------    -------")
    for i in range(15):
        print("", end="   ")
        print("{:<12}".format((i + 1)), end="")
        print("{:<15}".format(movementArray[i]), end="")
        print("{:<12}".format(randomRestartArray[i]), end="")
        print("{:<15.5f}".format(timeArray[i]))

main()






