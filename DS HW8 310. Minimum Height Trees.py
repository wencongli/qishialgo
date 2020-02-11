
Runtime: 272 ms, faster than 49.16% of Python3 online submissions for Minimum Height Trees.
Memory Usage: 18.7 MB, less than 37.50% of Python3 online submissions for Minimum Height Trees.


import collections
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        degree=[0 for i in range(n)]
        graph=collections.defaultdict(set)
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
            degree[i]+=1
            degree[j]+=1
            
        # figure out the leaf nodes with degree of 1
        queue=[]
        remaining=set(range(n))
        for ind in range(n):
            if degree[ind]==1:
                queue.append(ind)
        
        while len(remaining)>2:
            nxt=[]
            while queue:
                curr=queue.pop()
                remaining.remove(curr)
                for nbr in graph[curr]:
                    if nbr in remaining:
                        degree[nbr]-=1
                        if 1==degree[nbr]:
                            nxt.append(nbr)
                            
            queue=nxt
            
        return queue
        
        # BFS in-degree removal, if the len of remaining queue
        # is <=2, return
