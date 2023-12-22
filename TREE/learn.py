# class tree:
#     def __init__(self,data):
#         self.data=data
#         self.children=[]
#     def add_child(self,child):
#         self.children.append(child)    
        
# class generaltree:
#     def __init__(self):
#         self.root=None
        
#     def add_root(self,data):
#         self.root=tree(data) 
        
#     def add_child(self,parent,data):
#         if not self.root:
#             return "not root"        
#         self._add_child(self.root,parent,data)   
      
#     def _add_child(self,node,parent,data):
#         if node.data==parent:
#             node.add_child(tree(data))
            
#         for child in node.children:
#             self._add_child(child,parent,data)
            
#     def print_tree(self,node=None,lvl=0):
#           if not node:
#               node=self.root
          
#           print(" "*lvl+str(node.data)+"__")
#           for child in node.children:
#               self.print_tree(child,lvl+1)                 

# ------------------------------------------------

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=self.right=None
       
# def insert(root,data):
#     if root is None:
#         return Node(data)   
#     else:
#         if root.data == data:
#             return root
#         elif root.data< data:
#             root.right=insert(root.right,data)
#         else:
#             root.left= insert(root.left,data)  
            
#     return root       

# def contains(root,data):
#     if root.data is None and root.data==data:
#         return root is not None
    
#     if root.data < data:
#         return contains(root.right,data)
#     return contains(root.left,data)
        
# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.data,end=" ")
#         inorder(root.right)

# def preorder(root):
#     if root:
#         print(root.data,end=" ")
#         preorder(root.left)
#         preorder(root.right)

# def postorder(root):
#     if root:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.data,end=" ")  

# def minval(root):
#     curr=root
#     while curr:
#         curr=curr.left
#     return curr        

# def maxval(root):
#     curr=root
#     while root:
#         curr=curr.right
#     return curr    


# def delete(root,data):
#     if root.data is None :
#         return root
#     if root.data< data:
#         root.right=delete(root.right,data)
#     elif root.data>data:
#         root.left=delete(root.left,data)
    
#     else:
#         if root.left is None:
#             return root.right
#         elif root.right is None:
#             return root.left
        
#         else:
#             root.data=minval(root.right).data
#             root.right=delete(root.right,root.data)

# def closest(root,target):
#     if root.data is None:
#         return root
#     close=root.data
    
#     while root:
#         if abs(target-root.data)<abs(target- close):
#             close=root.data
            
#         if target > root.data:
#             root=root.right
            
#         elif target < root.data:
#             root=root.left
         
#         else:
#             return close
#     return close    

# ------------------------------------------------
# import heapq


# class Minheap:
#     def __init__(self):
#         self.heap = []

#     def push(self, item):
#         heapq.heappush(self.heap, item)

#     def is_empty(self):
#         return len(self.heap) == 0

#     def pop(self):
#         if not self.is_empty():
#             return heapq.heappop(self.heap)
#         else:
#             return "empty"

#     def peek(self):
#         if not self.is_empty():
#             return self.heap[0]
#         else:
#             return "empty"

#     def disp(self):
#         print(self.heap)
   
   
# class maxheap:
#     def __init__(self):
#         self.heap=[]
     
#     def is_empty(self):
#         return len(self.heap)==0
    
#     def push(self,item):
#         heapq.heappush(self.heap,-item)          

#     def pop(self):
#        if not self.is_empty():
#            return -heapq.heappop(self.heap)
#        else:
#            return "empty"
       
#     def peek(self):
#        if not self.is_empty(): 
#         return -self.heap[0]
#        else:
#            return "empty"

#     def disp(self):
#         print([-x for x in self.heap])

# h=Minheap()

# h.push(10)         
# h.push(20)
# h.push(30)
# h.push(50)
# h.push(8)
# h.push(16)
# h.push(15)

# h.disp()

# # print("sorted:",end=' ')
# while not h.is_empty():
#     print(h.pop(),end=' ')
# ------------------------------------------------

                
# def heapify(arr,n,i):
#     largest=i
#     left=2*i+1
#     right=2*i+2
    
#     if left<n and arr[left]>arr[largest]:
#         largest=left
     
#     if right < n and arr[right]>arr[largest ]:
#         largest=right
        
#     if largest!=i:
#         arr[i],arr[largest]=arr[largest],arr[i]
#         heapify(arr,n,largest)
      
#     return arr
# def heap_sort(arr):
#     n=len(arr) 
    
#     for i in range(n//2-1,-1,-1):
#         heapify(arr,n,i)
    
#     for i in range(n-1,0,-1):
#         arr[i],arr[0]=arr[0],arr[i]
#         heapify(arr,i,0)         
        
# arr=[12,11,13,5,6,7]        
# heap_sort(arr)                     
# print(arr)
   
# ------------------------------------------------

# def d( num):
#         a=[]
#         for i in range(len(num)):
#             if i<int(num[i]):
#                 a.append(num[i])
#             else:
#                 pass
#         print(a) 
        
# num="1210"    
# d(num)   
# --------------------------------------------------

# class treenode:
#     def __init__(self,data):
#         self.data=data
#         self.children=[]
        
#     def add_child(self,child):
#         self.children.append(child)
        
# class gentree:
#     def __init__(self):
#         self.root=None
        
#     def add_root(self,data):
#         self.root=treenode(data)
        
#     def add_child(self,parent,data):
#         if not self.root:
#             return "no root"
        
#         self._add_child(self.root,parent,data)
        
#     def _add_child(self,node,parent,data):
#         if node.data==parent:
#             node.add_child(treenode(data))     
#         for child in node.children:
#             self._add_child(child,parent,data)
            
#     def print(self,node=None,level=0):
#         if not node:
#             node=self.root
            
#         print(" "*level +str(node.data)+"__")
#         for child in node.children:
#             self.print(child,level+1) 
        
        
# -------------------------------------------------------------        
       
class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
        
def insert(root,data):
    if root is None:
        return Node(data)
    else:
        if root.data==data:
            return root
        elif root.data< data:
                root.right=insert(root.right,data)
        else:
            root.left=insert(root.left,data)      
    return root

def inorder(root):
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

r=Node(15)        
r=insert(r,12)
r=insert(r,7)
r=insert(r,14)
r=insert(r,27)
r=insert(r,20)
r=insert(r,23)
r=insert(r,88)
r=insert(r,8)
inorder(r)

       
            
              
            
              
    
                              
                    
            