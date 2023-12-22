# import heapq

# class Minheap:
#     def __init__(self):
#         self.heap=[]
        
#     def push(self,item):
#         heapq.heappush(self.heap,item)
        
#     def is_empty(self):
#             return len(self.heap)==0
        
#     def pop(self):    
#         if not self.is_empty:
#              return heapq.heappop(self.heap)
       
#     def peek(self):     
#         if not self.is_empty():
#             return self.heap[0]
#         else:
#             raise IndexError("empty")
    
#     def disp(self):
#         print(self.heap)
  
# h=Minheap()

# h.push(10)    
# h.push(30)  
# h.push(20)  
# h.push(40)    
# h.push(35)
# h.push(32)  
# h.push(25)    

# print(h.heap)

import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)
        else:
            raise IndexError("pop from an empty heap")

    def peek(self):
        if not self.is_empty():
            return self.heap[0]
        else:
            raise IndexError("peek from an empty heap")

    def is_empty(self):
        return len(self.heap) == 0

# Example usage:
min_heap = MinHeap()

min_heap.push(30)
min_heap.push(10)
min_heap.push(40)
min_heap.push(25)
min_heap.push(32)
min_heap.push(20)
min_heap.push(35)

print("Min heap:", min_heap.heap)

while not min_heap.is_empty():
    print("Popped:", min_heap.pop())


