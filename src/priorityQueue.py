from heapq import heappush, heappop

# class priorityQueue mengurutkan node dari cost terkecil hingga terbesar
class priorityQueue:
    def __init__(self):
        self.heap = []

    # push node baru ke priority queue
    def push(self, k):
        heappush(self.heap, k)

    # pop node dari priority queue
    def pop(self):
        return heappop(self.heap)
    
    # cek apakah priority queue kosong
    def isEmpty(self):
        return self.heap == []