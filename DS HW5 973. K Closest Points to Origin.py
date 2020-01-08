'''
Runtime: 656 ms, faster than 31.86% of Python online submissions for K Closest Points to Origin.
Memory Usage: 17.9 MB, less than 37.74% of Python online submissions for K Closest Points to Origin.
'''

import heapq

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        def dist(point):
            return point[0]**2+point[1]**2
        
        # maintain a maxheap of size K
        # element in maxheap: (-distance, ind)
        maxheap=[]
        for i, point in enumerate(points):
            d=dist(point)
            if len(maxheap)<K:
                heapq.heappush(maxheap, (-d, i))
            else:
                top=-maxheap[0][0]
                if d<top:
                    heapq.heappushpop(maxheap, (-d, i))
                    
        ret=[]
        while(maxheap):
            negdist, ind = heapq.heappop(maxheap)
            ret.append(points[ind])
            
        return ret
        
