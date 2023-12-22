import heapq

class minheap:
    def __init__(self):
        self.heap=[]
        
    def is_empty(self):
        return len(self.heap)==0
    
    def push(self,data):
        heapq.heappush(self.heap,data)
        
    def pop(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)
        return None

    def peek(self):
        if not self.is_empty():
            return self.heap[0]
        else:
            raise IndexError("empty")
    
    def disp(self):
        print([x for x in self.heap])
       
    def pop(self,data) :
        x=None
        for i,j in enumerate(self.heap):
            if j==data:
                x=i 
                break
        if x is not None:
                return -self.heap.pop(x)
        return None        

m=minheap()
m.push(30)
m.push(10)
m.push(40)
m.push(25)
m.push(32)
m.push(20)
m.push(35)

m.disp()

m.pop(25)
m.disp()


# def heapify(arr,n,i):
#     largest=i
#     left=i*2 +1
#     right=i*2+2
    
#     if left<n and arr[left]>arr[largest]:
#         largest=left
      
#     if right < n and arr[right]> arr[largest]:
#         largest=right
        
#     if largest !=i:
#         arr[largest],arr[i]=arr[i],arr[largest]
#         heapify(arr,n,largest)
        
#     return arr 

# def heapsort(arr):
#     n=len(arr)
    
#     for i in range(n//2 -1,-1,-1):
#         heapify(arr,n,i)  
#     print(arr)
#     for i in range(n-1,0,-1):
#         arr[i],arr[0]=arr[0],arr[i]
#         heapify(arr,i,0)
        
        
# arr=[7,6,5,13,11,12]             
# # heapsort(arr)
# print(arr)
        

def heapify(arr,n,i):
    largest=i
    left=i*2+1
    right=i*2+2
    
    if left<n and arr[left]> arr[largest]:
        largest=left
        
    if right<n and arr[right]>arr[largest]:
        largest=right
        
    if largest !=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        heapify(arr,n,largest)
    return arr

def heap_sort(arr):
    n=len(arr)
    
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
        
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)

arr=[7,6,5,13,11,12]             
heap_sort(arr)
print(arr)         
                            