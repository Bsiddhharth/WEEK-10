from collections import deque
class graph:
    def __init__(self):
        self.graph={}
        
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
            
    def add_edges(self,vertex1,vertex2):
        # for bidirectional
        # if vertex1 in self.graph:
        #     self.graph[vertex1].append(vertex2)
        # else:
        #     self.graph[vertex1]=[vertex2]
            
        
        # if vertex2 in self.graph:    
        #     self.graph[vertex2].append(vertex1)
        # else:
        #     self.graph[vertex2]=[vertex1]    
        
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2) 
            self.graph[vertex2].append(vertex1)
            
    def all_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph:
            return []

        all_paths = []
        for node in self.graph[start]:
            if node not in path:
                new_paths = self.all_paths(node, end, path)
                for new_path in new_paths:
                    all_paths.append(new_path)
        return all_paths
    
    def shortest_path(self,start,end,path=[]):
        path=path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        s=None
        for node in self.graph:
            if node not in path:
                new=self.shortest_path(node,end,path)
                if new:
                    if s is  None or len(new)<len(s):
                        s=new
        return new                
                            
             
        
     
      
    def disp(self):
        for i,j in self.graph.items():
            print(f"{i} : {j}")        
        
    def delete(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            
            # for i in self.graph:
            #     self.graph[i]=[j for j in self.graph[i] if j!=i]    
            for i in self.graph:
                if vertex in self.graph[i]:
                    self.graph[i].remove(vertex) 
                    
  
    def bfs(self,start):   
        visited=set()
        queue=deque([start])       
        
        while queue:
            vert=queue.popleft()
            if vert not in visited:
                print(vert,end=" ")
                visited.add(vert)   
                queue.extend(i for i in self.graph[vert] if i not in visited)   
    
    def dfs(self,start,visited=None):
        if visited is None:
            visited=set()
            
        if start not in visited:
            print(start,end=' ')
            visited.add(start)
            for i in self.graph[start]:
                self.dfs(i,visited)           
             
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

