import time
from numpy import random
from priorityQueue import *
from utils import *
from solveableChecker import *
from node import *

# untuk melakukan pergeseran empty tile ke: bawah, kiri, atas, kanan
rowShift = [1,0,-1,0]
colShift = [0,-1,0,1]

def solve(initiaBoard):
    # inisialisasi variabel global
    global totalNode   
    global solutionNode

    # berisi node-node yang terurut dari cost terkecil ke terbesar
    priorQueue = priorityQueue()

    # inisialisasi root node yang berisi puzzle board dalam posisi awal
    rootCost = 0 + calculateMisplacedTiles(initiaBoard)
    rootNode = node(initiaBoard, None, rootCost, 0)

    # push root node ke priority queue
    priorQueue.push(rootNode)
    totalNode = 1

    # iterasi hingga priority queue kosong atau hingga goal state tercapai
    while not priorQueue.isEmpty():
        # current node berisi node yang sedang diperiksa
        currentNode = priorQueue.pop()

        # goal state tercapai: iterasi berhenti, masukkan ke variabel solutionNode
        if ((currentNode.board == goalState).all()) :
            totalNode += 1
            solutionNode = copy.deepcopy(currentNode)
            return
        
        # cek lokasi empty tile di node saat ini
        currentEmptyTilePosition = emptyTilePosition(currentNode.board)

        prevLevel = currentNode.level

        # bangkitkan anak dari current node dengan melakukan shifting ke bawah, kiri, atas, kanan respectively
        for i in range(4):

            newEmptyTilePosition = [currentEmptyTilePosition[0] + rowShift[i], currentEmptyTilePosition[1] + colShift[i]]
            
            #pembangkitan hanya dilakukan bila indeks tidak out of bound
            if isNotOutOfBound(newEmptyTilePosition):
                totalNode += 1
                childNode = newNode(currentNode, currentEmptyTilePosition, newEmptyTilePosition, prevLevel)
                # push child node ke priority queue
                priorQueue.push(childNode)

# fungsi rekursif yang akan mencetak node berturut-turut dari root node ke solution node
def printPath(solutionNode) :
    if solutionNode == None :
        return
    printPath(solutionNode.parent)
    print(solutionNode.board)

def main():
    print("Welcome to 15 Puzzle Solver! Choose source of your puzzle board:")
    print("[1] Input from text file \n[2] Generate random board")
    choice = int(input())
    if choice==1 :
        print("Insert file name: ")
        fileName = str(input())
        # diasumsikan file selalu tersedia
        initialBoard = readFile(fileName)
    else :
        # generate random matrix
        initialBoard = random.choice(range(1, 17), size=(4, 4), replace=False)
    
    print("\nInitial Board: ")
    print(initialBoard)
    print("\n")

    start = time.time()
    # periksa apakah puzzle solveable atau tidak
    if isSolveable(initialBoard):
        # bila solveable, jalankan prosedur solve
        print("This puzzle is solveable. Please wait!")
        solve(initialBoard)
        end = time.time()
        printPath(solutionNode)
        print("\nTotal node generated =", totalNode)
    else:
        end = time.time()
        print("Puzzle is not solveable!")
    print("Running time =", end-start, "s")

main()