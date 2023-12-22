class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def insert(root,data):
    if root is None:
        return Node(data)
    
    else:
        if root.data == data:
            return root
        elif root.data < data:
            root.right=insert(root.right,data)
        else:
            root.left=insert(root.left,data)            
    return root        


        
def preorder(root):
     if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
        
def closest(root,target):
    if root is None:
        return None
    
    closest=root.data
    
    while root:
        if abs(target- root.data) < abs(target - closest):
            closest=root.data
         
        # if target==root.data:
        #     closest=root.data
        if target < root.data:
            root=root.left
        elif target>root.data:
            root=root.right
        else:
            return  closest
    return closest

def minval(root):
    curr=root
    while curr:
       curr=curr.left
    return curr    


def delete(root,data):
    if root is None:
        return root
    if data < root.data:
        root.left=delete(root.left,data)
    elif data> root.data:
        root.right=delete(root.right,data)      
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.data=minval(root.right).data
        root.right=delete(root.right,root.data)  
        # root.data=maxval(root.left).data
        # root.left=delete(root.left,root.data)   
    return root   

            
        
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)        
    
preorder(r)    
t=30
print()
print(closest(r,t))
delete(r,40)
preorder(r)




# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=self.right=None
        
# def  insert(root,data)      :
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

# def contains(root,data):
#     if root is None or root.data==data:
#         return root is not None
#     if root.data<data:
#         return contains(root.right,data)
#     return contains(root.left,data)    



# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.data,end=" ")
#         inorder(root.right)
        
# def minval(root):
#     curr=root
#     while curr:
#         curr=curr.left
#     return curr

# # def maxval(root):
# #     curr=root.right
# #     while curr:
# #         curr=curr.right
# #     return curr    
            
# def preorder(root):
#      if root:
#         print(root.data,end=" ")
#         preorder(root.left)
#         preorder(root.right)
        
# def postorder(root):
#     if root:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.data,end=" ")  
        
# def delete(root,data):
#     if root is None:
#         return root
#     if data < root.data:
#         root.left=delete(root.left,data)
#     elif data> root.data:
#         root.right=delete(root.right,data)      
#     else:
#         if root.left is None:
#             return root.right
#         elif root.right is None:
#             return root.left
#         root.data=minval(root.right).data
#         root.right=delete(root.right,root.data)  
#         # root.data=maxval(root.left).data
#         # root.left=delete(root.left,root.data)   
#     return root    

# def closest(root,target):
#     if root is None:
#         return None
    
#     closest=root.data
    
#     while root:
#         if abs(target- root.data) < abs(target - closest):
#             closest=root.data
         
#         # if target==root.data:
#         #     closest=root.data
#         if target < root.data:
#             root=root.left
#         elif target>root.data:
#             root=root.right
#         else:
#             return  closest
#     return closest
    
            
           
        
        
# r=Node(5)        
# r=insert(r,3)
# r=insert(r,7)
# r=insert(r,2)
# r=insert(r,4)
# r=insert(r,8)
# r=insert(r,6)

# r=Node(15)        
# r=insert(r,12)
# r=insert(r,7)
# r=insert(r,14)
# r=insert(r,27)
# r=insert(r,20)
# r=insert(r,23)
# r=insert(r,88)
# r=insert(r,8)
# inorder(r)

# print()

# preorder(r)
# print()

# postorder(r)

# print()

# # delete(r,20)
# inorder(r)
# print()
# t=3
# print(closest(r,t))
# # print(minvalue(r))  
# # print(maxvalue(r)) 
            
        