
Idea1: DSU

import collections
class DSU:
    def __init__(self, num_vertex):
        # make set, initially every vertex belongs to its own set
        self.parent=list(range(num_vertex+1))
        self.rank=[0]*(num_vertex+1)
        
    def find(self, node):
        if self.parent[node]!=node:
            self.parent[node]=self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, x, y):
        # return False if x,y belong to different sets
        # return True if x,y already in the same set
        xroot, yroot = self.find(x), self.find(y)
        if xroot==yroot:
            return True
        # merge by rank
        if self.rank[xroot]<self.rank[yroot]:
            self.parent[xroot]=yroot
        else:
            self.parent[yroot]=xroot
            if self.rank[xroot]==self.rank[yroot]:
                self.rank[xroot]+=1
        return False
    
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # method 2: DSU
        # a new edge is used to join 2 sets
        # if 2 sets are essentially the same set, that edge is redundant
        # if union returns True, that edge is redundant
        
        dsu=DSU(1000)
        for edge in edges:
            i,j = edge
            if(dsu.union(i,j)):
                return edge
        

idea 2: DFS

Runtime: 48 ms, faster than 95.43% of Python3 online submissions for Redundant Connection.
Memory Usage: 14.1 MB, less than 28.57% of Python3 online submissions for Redundant Connection.

import collections
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph=collections.defaultdict(set)
        pathindex=dict()
        for ind, edge in enumerate(edges):
            i,j = edge
            graph[i].add(j)
            graph[j].add(i)
            pathindex[(i,j)]=ind
            pathindex[(j,i)]=ind
            
        path=[]
        pathset=dict()
        
        def DFS(node, parent):
            path.append(node)
            if node in pathset:
                # if DFS return True, we need to preserve the path
                # and analyze it later
                return True
            # pathset records the index of 
            # first occurence of the cycle intersection
            pathset[node]=len(path)-1
            
            for nbr in graph[node]:
                if nbr==parent:
                    continue
                if DFS(nbr, node):
                    # if find the cycle
                    return True
                
            # backtrack
            pathset.pop(node)
            path.pop()
            return False
        
        DFS(edges[0][0], None)
        intersect=pathset[path[-1]]
        candidate=path[intersect:]
        # print(path, intersect)
        maxindex=0
        for i in range(len(candidate)-1):
            maxindex=max(maxindex, \
                         pathindex[(candidate[i], candidate[i+1])])
            
        return edges[maxindex]
                
                
                
                
            
        
