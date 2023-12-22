# class TreeNode:
#     def __init__(self,data):
#         self.data=data
#         self.children=[]
        
#     def add_child(self,child) :
#         self.children.append(child)   
        
# class GeneralTree:
#     def __int__(self):
#         self.root=None
       
#     def add_root(self,data):
#         self.root=TreeNode(data)    
        
#     def add_child(self,parent,data):
#         if not self.root:
#             print("No root")
#             return
        
#         self._add_child(self.root,parent,data)
    
#     def _add_child(self,node,parent,data) :
#         if node.children == parent:
#             node.add_child(TreeNode(data))       
#             return 
#         for child in node.children:
#             self._add_child(child,parent,data)
            
            
#     def print_tree(self,node=None,level=0):
#         if not node:
#                     node=self.root
#         print(" "+level+str(node.data)+"__")
#         for child in node.children:
#             self.print_tree(child,level+1)            
        
        
# -----------------------------------------------------------------        



# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=self.right=None
        
# def insert(root,data):
#     if root is None:
#         return Node(data)
    
#     else:
#         if root.data==data:
#             return root
#         elif root.data < data:
#             root.right=insert(root.right,data)
#         else:
#             root.left=insert(root.left,data)
#     return root 
  
# def contains(root,data):
#     if root is None or root.data==data:
#         return root is not None
#     if data<root.data:
#         return contains(root.left,data)
#     return contains(root.right,data) 
    
# def minval(root):
#     curr=root
#     while curr.left:
#         curr=curr.left
#     return curr.data
      
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

# def delete(root, data):
#     if root is None:
#         return root
#     if data < root.data:
#         root.left = delete(root.left, data)
#     elif data > root.data:
#         root.right = delete(root.right, data)
#     else:
#         if root.left is None:
#             return root.right
#         elif root.right is None:
#             return root.left
#         root.data = minval(root.right).data
#         root.right = delete(root.right, root.data)
#     return root
        
# r=Node(15)        
# r=insert(r,12)
# r=insert(r,7)
# r=insert(r,14)
# r=insert(r,27)
# r=insert(r,20)  
# r=insert(r,23)
# r=insert(r,88)

# inorder(r)
# print()
# postorder(r) 
# print()
# preorder(r)           
        
# print()
# print(contains(r,12))
# # print(f"does the  table contains the req element= {contains(r,12)}")
# print(minval(r.right))

# delete(r,20)
# inorder(r)
# ---------------------------------------

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=self.right=None
        
# def insert(root,data):
#     if root is None:
#         return Node(data)
    
#     else:
#         if root.data==data:
#             return root
#         elif root.data<data:
#             root.right=insert(root.right,data)
#         else:
#             root.left=insert(root.left,data)       
#     return root        
    
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
        
# def postorder(root) :
#     if root:
#         postorder(root.data,end=" ")
#         postorder(root.data,end=" ") 
#         print(root.data,end=" ")
 
# def contains(root,data):                            
#         if root is None or root.data==data:
#             return root is not None
#         if root.data< data:
#             return contains(root.right,data)
#         return contains(root.left,data)
    
# def minval(root):
#     curr=root
#     while curr:
#         curr=curr.left
#     return curr    

# def delete(root,data):
#     if root is None:
#         return root
#     if data< root.data:
#         root.left= delete(root.left,data)
#     elif data>root.data:
#         root.right=delete(root.right,data)
#     else:
#         if root.left is None:
#             return root.right
#         elif root.right is None:
#             return root.left
#         root.data=minval(root.right).data
#         root.right=delete(root.right,root.data)     
#     return root

# def closest(root,target):
#     if root is None:
#         return root
    
#     close=root.data
#     while root:
#         if  abs(target - root.data) < abs(target - close):
#             close=root.data
            
#         if target< root.data:
#             root=root.left
#         elif target > root.data:
#             root=root.right        
#         else:
#             return root
#     return root    


# ------------------------------------------------
class graph:
    def __init__(self):
        self.graph={}
        
    def add_vertex(self,vertex) :        
        self.graph[vertex]=[]
        
    def add_edges(self,vert1,vert2):
        if vert1 in self.graph:
            self.graph[vert1].append(vert2)
        else:
            self.graph[vert1]=[vert2]
            
        if vert2 in self.graph:
            self.graph[vert2].append(vert1)
        else:
            self.graph[vert2]=[vert1  ]              

    def all_paths(self,start,end,path=[]):
        path=path+[start]
        
        if start==end:
            return [path]
        
        if start  not in self.graph:
            return []
        
        all_paths=[]
        
        for node in self.graph[start]:
            if node not in path:
                new=self.all_path(node,end,path)
                for x in new:
                     all_paths.append(x)
                     
        return all_paths             
    
    def short_path(self,start,end,path=[]):
        path=path+[start]
        
        if start==end:
            return [path]
        
        if start not in self.graph:
            return []
        
        s_path=None
        
        for node in self.graph[start]:
            if node not in path:
                s=self.short_path(node,end,path)
                if s:
                    if s_path is None or len(s_path)>len(s):
                        s_path=s
        return s
    
    def delete(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            
            # for i in self.graph:
            #     self.graph[i]=[j for j in self.graph[i] if j!=i]    
            for i in self.graph:
                if vertex in self.graph[i]:
                    self.graph[i].remove(vertex) 
    
    
    def disp(self):
        for i,j in self.graph.items():
            print(f"{i} : {j}  ")
    
    
    
      
        
g=graph()

g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')           
g.add_vertex('E')
g.add_vertex('F')

g.add_edges('A','B')
g.add_edges('A','C')
g.add_edges('C','D')
g.add_edges('B','D')
g.add_edges('D','E')

g.disp()

g.delete('A')
print()

g.disp()


# print(g.all_paths('A','E'))
# print(g.all_paths('A','F'))
# print(g.shortest_path('A','E'))                