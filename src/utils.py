import numpy as np

goalState = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
n = 4
size = n*n

# baca file dan simpan ke array 2d/matrix
def readFile(fileName):
    array2D = np.loadtxt(fileName, dtype=int)
    return array2D

# untuk mengubah array 2d ke array 1d
def convertTo1D(array2D) :
    return array2D.flatten()

# fungsi untuk memeriksa apakah posisi terdapat di luar/di dalam indeks terdefinisi
def isNotOutOfBound(position):
    return position[0]>=0 and position[0]<n and position[1]>=0 and position[1]<n

# fungsi untuk memeriksa posisi empty tile
def emptyTilePosition(board) :
    for i in range(n):    
        for j in range(n):
            if board[i][j]==16 :
                return [i,j]