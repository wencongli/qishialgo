
Idea1: in degree
Runtime: 100 ms, faster than 85.49% of Python3 online submissions for Course Schedule II.
Memory Usage: 14.1 MB, less than 96.43% of Python3 online submissions for Course Schedule II.


import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n=numCourses
        graph=collections.defaultdict(list)
        indegree=[0 for i in range(n)]
        for nxt, prv in prerequisites:
            graph[prv].append(nxt)
            indegree[nxt]+=1
        
        startnodes=[]
        for ind, node in enumerate(indegree):
            if 0==indegree[ind]:
                startnodes.append(ind)
                
        ret=[]
        
        while startnodes:
            curr=startnodes.pop()
            ret.append(curr)
            for nbr in graph[curr]:
                indegree[nbr]-=1
                if 0==indegree[nbr]:
                    startnodes.append(nbr)

        return ret if len(ret)==n else []
            
idea 2: DFS
Runtime: 104 ms, faster than 66.54% of Python3 online submissions for Course Schedule II.
Memory Usage: 15.7 MB, less than 60.71% of Python3 online submissions for Course Schedule II.

import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n=numCourses
        graph=collections.defaultdict(list)
        indegree=[0 for i in range(n)]
        for nxt, prv in prerequisites:
            graph[prv].append(nxt)
            indegree[nxt]+=1
        
        startnodes=[]
        for ind in range(n):
            if 0==indegree[ind]:
                startnodes.append(ind)
                
        ret=[]
        # status=0: unvisited, 1: in path; 2: visited, not in path
        status=[0 for i in range(n)]
        
        def DFS(node):
            # in-path or not
            if status[node]>0: 
                return status[node]==2
            status[node]=1
            for nbr in graph[node]:
                if not DFS(nbr):
                    return False
            status[node]=2
            ret.append(node)
            return True
        
        for node in startnodes:
            if not DFS(node):
                return []
                
        if len(ret)<n:
            return []
        
        ret.reverse()
        return ret
        
        '''
        while startnodes:
            curr=startnodes.pop()
            ret.append(curr)
            for nbr in graph[curr]:
                indegree[nbr]-=1
                if 0==indegree[nbr]:
                    startnodes.append(nbr)
        '''
        
