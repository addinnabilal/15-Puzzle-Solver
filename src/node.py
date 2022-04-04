import copy
import numpy as np

# initial variable
goalState = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
n = 4
size = n*n

# class node merepresentasikan simpul berupa puzzle board pada suatu saat 
class node:
    def __init__(self, board, parent, cost, level):
        self.board = board
        self.parent = parent
        self.cost = cost
        self.level = level

    # agar pengurutan di priority queue dilakukan dari cost yang terkecil hingga terbesar
    def __lt__(self, next):
        return self.cost < next.cost

def newNode(parent, emptyTilePosition, newEmptyTilePosition, prevLevel):
    parentBoard = parent.board
    newBoard = copy.deepcopy(parentBoard)

    # posisi empty block sebelumnya
    prevEmptyX = emptyTilePosition[0]
    prevEmptyY = emptyTilePosition[1]

    # posisi empty block yang baru
    newEmptyX = newEmptyTilePosition[0]
    newEmptyY = newEmptyTilePosition[1]

    # perpindahan empty block dilakukan
    newBoard[prevEmptyX][prevEmptyY] = parentBoard[newEmptyX][newEmptyY]
    newBoard[newEmptyX][newEmptyY] = parentBoard[prevEmptyX][prevEmptyY]

    # menginisialisasi nilai level(langkah) dan cost terbaru
    newLevel = prevLevel + 1
    newCost = newLevel + calculateMisplacedTiles(newBoard)

    return node(newBoard, parent, newCost, newLevel)

# fungsi untuk menghitung jumlah ubin tidak kosong yang tidak terdapat pada susunan akhir
def calculateMisplacedTiles(board):
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] != goalState[i][j]:
                count+=1
    return count