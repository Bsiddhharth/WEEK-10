import heapq

class maxheap:
    def __init__(self):
        self.heap=[]
       
    def push(self,data):
        heapq.heappush(self.heap,-data)   
    
    def is_empty(self):
        return len(self.heap)==0
    
    def pop(self):
        if not self.is_empty() :
            return -heapq.heappop(self.heap)
        else:
            raise IndexError("empty")
    def peek(self):
        if not self.is_empty():
            return -self.heap[0]
    def disp(self):
          print( [-x for x in self.heap] )
 
        


h=maxheap()

h.push(10)         
h.push(20)
h.push(30)
h.push(50)
h.push(8)
h.push(16)
h.push(15)

h.disp()


