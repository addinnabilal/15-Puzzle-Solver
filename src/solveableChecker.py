from utils import *
from node import *

# untuk menghitung X, mereturn 0 bila ubin kosong di kondisi awal berada
# pada posisi (i,j) = (genap, genap) atau (ganjil, ganjil) dan sebaliknya
def emptyPositionValue(board) :
    for i in range(n):    
        for j in range(n):
            if board[i][j]==16 :
                if i%2 == j%2 :
                    print("X = 0")
                    return 0
                else:
                    print("X = 1")
                    return 1

# fungsi kurang(i)
def kurangPerIndex(array, i):
    count = 0
    for j in range(size) :
        if  j>i and array[j]<array[i]:
            count+=1
    return count

# fungsi sum(kurang(i)), i=1...16
def kurang(array):
    count = 0
    for i in range(1, size + 1):
        # cari posisi/index ubin bernomor i
        for j in range(size):
            if array[j]==i:
                result=kurangPerIndex(array, j)
                count += result
                print ("kurang(" + str(i) +") = " + str(result))
    print("sum(kurang(i)) =", count)
    return count

def isSolveable(board) :
    value = kurang(convertTo1D(board)) + emptyPositionValue(board)
    print("Nilai sum(kurang(i)) + X = ", value)
    # puzzle solveable bila jumlah fungsi kurang dengan i=1...15 dan X bernilai genap
    if value % 2 ==0 :
        return True
    else:
        return False