class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
        
def closestt(root,target):
    if root is None:
        return None
    
    closest=root.data
    
    while root:
        if abs(root.data-target) < abs(target-closest):
            closest=root.data
            
        if target< root.data:
            root=root.left
        elif target> root.data:
            root=root.right
        return closest
    return closest          

root = Node(15)
root.left = Node(7)
root.right = Node(20)
root.left.left = Node(3)
root.left.right = Node(12)
root.right.left = Node(17)
root.right.right = Node(22)

t = 15

print(closestt(root,t))                            
    