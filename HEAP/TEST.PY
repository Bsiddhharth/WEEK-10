# import heapq

# class minheap:
#     def __init__(self):
#         self.heap=[]
    
#     def push(self,data):
#         heapq.heappush(self.heap,data)
        
#     def is_empty(self):
#         return len(self.heap)==0
    
#     def pop(self):
#         if not self.is_empty():
#            return heapq.heappop(self.heap)        
#         else:
#             raise IndexError("empty")
        
#     def peek(self):
#         if not self.is_empty():
#             return self.heap[0]
#         else:
#               raise IndexError("empty")
          
#     def sort(self):
#       while self.heap:  
#         print(self.pop(),end=" ")    
          
#     def pushpop(self,item):
#         heapq.heappushpop(self.heap,item)
        
        
# h=minheap()

# # h.push(30)        
# # h.push(10)   
# # h.push(40)        
# # h.push(25)   
# # h.push(32)   
# # h.push(35)   
# # h.push(20)  
# h.push(15)
# h.push(10)
# h.push(8)
# h.push(16)
# h.push(30)
# h.push(20)
# h.push(50)
 
# print(h.peek())
# print(h.heap)
# # while h.heap:
# #     print(h.pop())

# # h.sort()
# h.pushpop(39)
# print(h.heap)

# ---------------------------------------------------------------

# class maxheap:
#     def __init__(self):
#        self.heap=[]
       
#     def push(self,item):
#         heapq.heappush(self.heap,-item)
        
#     def is_empty(self):
#         return len(self.heap)==0
    
#     def pop(self):
#         if not self.is_empty():
#             return -heapq.heappop(self.heap)     
#         else:
#             raise IndexError("empty")
        
#     def peek(self):       
#         if not self.is_empty():
#             return -self.heap[0]
        
#     def disp(self):
#         print([-x for x in self.heap])    

#     def pushpop(self,item):
#         heapq.heappushpop(self.heap,-item)
        
# h=maxheap()        

# h.push(15)
# h.push(10)
# h.push(8)
# h.push(16)
# h.push(30)
# h.push(20)
# h.push(50)


# h.disp()

# while h.heap:
#     print(h.pop())

# ---------------------------------------------------------

def heapify(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2
    
    if left < n and arr[left] > arr[largest]:
        largest=left
      
    if right < n and arr[right] > arr[largest]:
        largest=right
        
    if largest != i:
        arr[i],arr[largest]=arr[largest],arr[i]       
        heapify(arr,n,largest)
        
        
def heap_sort(arr):
    n=len(arr)
    
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
        
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0],arr[i]
        heapify(arr,i,0)
        
arr=[12, 11, 13, 5, 6, 7]  
heap_sort(arr)              
print(arr)        