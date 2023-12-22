class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
    def add_child(self,child):
        self.children.append(child)

class GeneralTree:
    def __init__(self):        
        self.root=None
        
    def add_root(self,data):
        self.root=TreeNode(data)    
      
    def add_child(self,parent,data):
        if not self.root:
            print("No root")
            return
        self._add_child(self.root,parent,data)
       
    def _add_child(self,node,parent,data):
        if node.data==parent:
            node.add_child(TreeNode(data))          
            return
        for child in node.children:
            self._add_child(child,parent,data)  
         
    def print_tree(self, node=None, level=0):
            if not node:
                node = self.root

            print("  " * level + str(node.data)+"__" )
            for child in node.children:
                self.print_tree(child, level + 1)
tree = GeneralTree()
tree.add_root("A")
tree.add_child("A", "B")
tree.add_child("A", "C")
tree.add_child("B", "D")
tree.add_child("B", "E")
tree.add_child("C", "F")
tree.add_child("F","G")
tree.add_child("G","H")
tree.print_tree()          


        
# class TreeNode:
#     def __init__(self,data):
#         self.data=data
#         self.children=[]
        
#     def add_child(self,child):
#         self.children.append(child)    
        
# class GeneralTree:
#     def __init__(self):
#         self.root=None
        
#     def add_root(self,data):
#         self.root=TreeNode(data)
        
#     def add_child(self,parent,data):
#         if not self.root:    
#              print("no root")
#              return
#         self._add_child(self.root,parent,data)
        
#     def _add_child(self,node,parent,data):
#         if node.data==parent:
#             self.add_child(TreeNode(data))     
#             return
#         for child in node.children:
#             self._add_child(child,parent,data)
            
#     def print_tree(self,node=None,level=0):
          
#           if not node:
#               node=self.root   
              
#           print(" "*level+"|__ "+str(node.data))
#           for child in node.children:
#               self.print_tree(child,level+1)        
            
# tree = GeneralTree()
# tree.add_root("A")
# tree.add_child("A", "B")
# tree.add_child("A", "C")
# tree.add_child("B", "D")
# tree.add_child("B", "E")
# tree.add_child("C", "F")

# tree.print_tree()          
                      
               