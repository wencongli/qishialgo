
Runtime: 64 ms, faster than 56.42% of Python3 online submissions for Redundant Connection II.
Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Redundant Connection II.

import collections
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parent=dict()
        n=len(edges)
        dsu=[i for i in range(n+1)]
        
        # 3 cases:
        # (1) a node has 2 parents; 
        # (2) there is a cycle; 
        # (3) a node has 2 parents and there is a cycle
        # (1) if a node has 2 parent, without cycle, remove the second parent
        # (2) if a cycle exist, without 2 parents, remove the last edge forming the cycle
        # (3) if after remove the second parent, there is still cycle, we should remove 1st parent
        firstedge, secondedge = None, None
        for edge in edges:
            i,j = edge
            if j in parent:
                firstedge=[parent[j], j]
                secondedge=edge
            else:
                parent[j]=i
                
        def find(ind):
            if dsu[ind]!=ind:
                dsu[ind]=find(dsu[ind])
            return dsu[ind]
        
        def union(x,y):
            x=find(x)
            y=find(y)
            if x==y:
                return False
            dsu[x]=y
            return True
        
        for edge in edges:
            if edge==secondedge:
                # we should skip the secondedge to see if it works
                continue
            i,j = edge
            if not union(i,j):
                # already in the same set, cycle
                if firstedge:
                    return firstedge
                else:
                    return edge
                
        # if without cycle
        return secondedge
            
