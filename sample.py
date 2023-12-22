# def heapify(arr,n,i):
#     largest=i
#     left=i*2 +1
#     right=i*2+2
    
#     if left < n and arr[left]>arr[largest]:
#         largest=left
        
#     if right<n and arr[right]>arr[largest]:
#         largest=right
        
#     if largest!= i:
#         arr[largest],arr[i]=arr[i],arr[largest]
#         heapify(arr,n,largest)
        
#     return arr

# def heap_sort(arr):
#     n=len(arr)
    
#     for i in range(n//2,-1,-1):
#         heapify(arr,n,i)
        
#     for i in range(n-1,0,-1):
#         arr[0],arr[i]=arr[i],arr[0]
#         heapify(arr,i,0)
        
# from collections import deque      
# def bfs(arr,start):
#       visited=set()
#       queue=deque([start])
      
#       while queue:
#           vert=queue.popleft()
#           if vert not in visited:
#               print(vert,end=" ")
#               visited.add(vert)
#               queue.extend(i for i in arr[start] if vert not in visited)                 



# def height(root):
#     curr=root
#     c,v=0,0
#     while curr:
#         curr.left
#         c+=1
#     new=root
#     while new:
#         new.right
#         v+=1
#     return max(c,v)    
        
# class tree:
#     def __init__(self,data):
#         self.root=data
#         self.children=[]
        
#     def add_child(self,child)    :
#         self.children.append(child)
        
        
        
               