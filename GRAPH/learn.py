# from collections import deque
# class graph:
#     def __init__(self):
#         self.graph={}
        
#     def add_vertex(self,vertex):
#         self.graph[vertex]=[vertex]
        
#     def add_edges(self,vert1,vert2):
#         if vert1 in self.graph:
#             self.graph[vert1].append(vert2)
#         else:
#             self.graph[vert1]=[vert2]
            
#         if vert2 in self.graph:
#             self.graph[vert2].append(vert1)
#         else:
#             self.graph[vert2]=[vert1]
            
#     def delete(self,vert):
#         if vert in self.graph:
#             del self.graph[vert]
            
#             for i in self.graph:
#                 if vert in self.graph[i]:
#                     self.graph.remove(vert)
                    
#     def bfs(self,start):
#         visited=set()
#         queue=deque([start])
        
#         while queue:
#             vert=queue.popleft()
#             if vert not in visited:
#                 print(vert,end=" ")
#                 visited.add(vert)
#                 queue.extend(i for i in self.graph[vert] if i not in visited)
                
#     def dfs(self,start,visited=None):
#         if visited is None:
#             visited=set()
            
#         if start not in visited :
#             print(start,end=" ")
#             visited.add(start)
#             for i in self.graph[start]:
#                 self.dfs(i,visited)  
                
    
#     def disp(self):
#         for i,j in self.graph.items():
#             print(f"{i}: {j}") 
                      
                

# g=graph()

# g.add_vertex('A')
# g.add_vertex('B')
# g.add_vertex('C')
# g.add_vertex('D')           
# g.add_vertex('E')
# g.add_vertex('F')

# g.add_edges('A','B')
# g.add_edges('A','C')
# g.add_edges('C','D')
# g.add_edges('B','D')
# g.add_edges('D','E')

# g.disp()

# # print(g.all_paths('A','E'))
# # print(g.all_paths('A','F'))
# # print(g.shortest_path('A','E'))

# g.bfs('A')
# print()
# g.dfs('A')


from collections import deque

class graph:
    def __init__(self):
        self.graph={}
       
    def add_vertex(self,vertex):
        self.graph[vertex]=[]
        
    def add_edges(self,vert1,vert2):

        if vert1 in self.graph and vert2 in self.graph:
            self.graph[vert1].append(vert2)
            self.graph[vert2].append(vert1)

    def disp(self)    :
        for i,j in self.graph.items():
            print(f"{i}:{j}")
            
            
    def all_paths(self,start,end,path=[]):
        path=path+[start]
        
        if start == end:
            return [path]
        
        if start not in self.graph:
            return None
        
        all_path=[]
        
        for node in self.graph[start]:
            if node  not in path:
                new=self.all_paths(node,end,path)
                for i in new:
                    all_path.append(i)
        return all_path
    
    def shortest_path(self,start,end,path=[]):
        path=path+[start]
        
        if start==end:
            return [path]
        if start not in self.graph:
            return None
        
        short=None
        
        for node in self.graph[start]:
            if node not in path:
                n=self.shortest_path(node,end,path)
                if n:
                    if short is None or len(n)<len(short):
                        short=n
        return short                
    
    def delete(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            
            for i in self.graph:
                if vertex in self.graph[i]:
                    self.graph[i].remove(vertex)
        
            
    
g=graph()
g.add_vertex('1') 
g.add_vertex('2') 
g.add_vertex('3') 
g.add_vertex('4')                        
g.add_vertex('5')

g.add_edges('1','2')
g.add_edges('2','3')
g.add_edges('1','4')
g.add_edges('3','5')
g.add_edges('3','4') 

g.disp()  
print(g.all_paths('1','4'))  
print(g.shortest_path('1','3'))
                             
            