'''
Runtime: 172 ms, faster than 95.35% of Python online submissions for Trapping Rain Water II.
Memory Usage: 13.2 MB, less than 33.33% of Python online submissions for Trapping Rain Water II.
'''

import heapq
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        # form the boundary first, then move towards inside from the lowest element
        # we need minheap
        # on the boundary, the water level is already evaluated
        # so only evaluate the unvisited INSIDE ELEMENTS
        # 1. if inside element is lower than the low element, add water to the result
        # and this inside element becomes a part of boundary, the new height is the max(boundary,inside)
        # 2. if inside element is higher than low element, no water is added
        # this inside element becomes a part of boundary, the new height is max(boundary, inside)
        
        # step 0: corner case
        m=len(heightMap)
        if m<3:
            return 0
        n=len(heightMap[0])
        if n<3:
            return 0
        
        visited=[[False for j in range(n)] for i in range(m)]
        heap=[]
        
        # step1: form the boundary
        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            visited[i][0]=True
            heapq.heappush(heap, (heightMap[i][n-1], i, n-1))
            visited[i][n-1]=True
                           
        for j in range(1, n-1):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            visited[0][j]=True
            heapq.heappush(heap, (heightMap[m-1][j], m-1, j))
            visited[m-1][j]=True
             
        dirs=[(-1,0),(0,-1),(0,1),(1,0)]
        ret=0
                           
        while(heap):
        # iterate when heap is not empty
            h, i, j = heapq.heappop(heap)
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if ni<0 or ni>=m or nj<0 or nj>=n or visited[ni][nj]:
                # if out of range or already visited
                    continue
                mx=max(heightMap[ni][nj], h)
                ret+=mx-heightMap[ni][nj]
                           
                visited[ni][nj]=True
                heapq.heappush(heap, (mx, ni, nj))
                           
        return ret
