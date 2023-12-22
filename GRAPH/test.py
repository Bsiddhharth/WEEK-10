from collections import deque

class graph:
    def __init__(self):
        self.graph={}
        
    def add_vertex(self,vert):
        if vert not in self.graph:
            self.graph[vert]=[]
            
    def add_edges(self,vert1,vert2):
        if vert1 in self.graph:
            self.graph[vert1].append(vert2)
        else:
            self.graph[vert1]=[vert2]       
            
        
        if vert2 in self.graph:
            self.graph[vert2].append(vert1)
        else:
            self.graph[vert2]=[vert1]         
            
    def disp(self):
        for i,j in self.graph.items():
            print(f"{i} : {j}")                
            
            
    def all_paths(self,start,end,path=[]):
        path = path+[start]
        
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        all_paths=[]
        for node in self.graph[start]:
            if node not in path:
                new=self.all_paths(node,end,path)
                for x in new:
                     all_paths.append(x)     
        return all_paths
    
    def shortest_path(self,start,end,path=[]):
        path=path+[start]
        
        if start==end:
            return [path]
        
        if start not in self.graph:
            return []
        
        short=None
        for node in self.graph[start]:
            if node not in path:
                s=self.shortest_path(node,end,path)
                if s:
                    if short is None or len(short)>len(s):
                        short=s
        return short
    
    def bfs(self,start):
        visited=set()
        queue= deque([start])
        
        while queue:
            vert=queue.popleft()
            if vert not in  visited:
                print(vert,end=" ") 
                visited.add(vert)
                queue.extend(i for i in self.graph[vert] if i not in visited)
    
    def dfs(self,start,visited=None):
        if visited is None:
                visited=set()
        
        if start not in visited:
            print(start,end=" ")
            visited.add(start)
            for i in self.graph[start]: 
                self.dfs(i,visited)
                    
    
    
 
        
        
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

print(g.all_paths('A','E'))
print(g.all_paths('A','F'))
print(g.shortest_path('A','E'))

g.bfs('A')
print()
g.dfs('A')



        