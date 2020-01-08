'''
Runtime: 76 ms, faster than 100.00% of Python online submissions for The Skyline Problem.
Memory Usage: 16.7 MB, less than 62.50% of Python online submissions for The Skyline Problem.
'''

import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # maintain an activeheap, heap element: (-height, -end, start, building_ind)
        # active means that when we consider building i [start_i, end_i]
        # all of the buildings which ends < start_i should be removed
        activeheap=[]
        keypoint=[]
        
        # a trick is to add a sentinel node to avoid boundary check
        heapq.heappush(activeheap, (0, -float("inf"), -1, -1))
        
        for ind, bu in enumerate(buildings):
            nstart, nend, nheight = bu
            
            # extract the maxheap top element
            negmxheight, negmxend, mxstart, mxind = activeheap[0]
            mxheight, mxend = -negmxheight, -negmxend
            
            # if the new element is contained within the max element, skip it
            if nstart>=mxstart and nend<=mxend and nheight<=mxheight:
                continue
            
            # step 1: check if elements in active heap goes expired or not
            # if the max element is expired, pop it out, 
            # and use the FarEnd to record the rightmost end till now
            FarEnd=-1
            while(activeheap and mxend<nstart):
                heapq.heappop(activeheap)
                FarEnd=max(FarEnd, mxend)
                
                # since we have sentinel, heap is always not empty
                mxheight, mxend = -activeheap[0][0], -activeheap[0][1]
                if FarEnd<mxend:
                    # there is an intersection between FarEnd and remaining heap top
                    keypoint.append([FarEnd, mxheight])
            
            # extract the maxheap top element again
            mxheight, mxend = -activeheap[0][0], -activeheap[0][1]
            
            # step 2: if the new element is higher than the max element, record it
            if nheight>mxheight:
                # here we need to avoid duplicate points with same x-coordinate
                if keypoint and nstart==keypoint[-1][0]:
                    if nheight>keypoint[-1][1]:
                        keypoint[-1][1]=nheight
                else:
                    keypoint.append([nstart, nheight])
                    
            # don't forget to record the current building!
            heapq.heappush(activeheap, (-nheight, -nend, nstart, ind))
            
            
        # step 3: we also need to clear the activeheap
        # the same process as step 1:
        FarEnd=-1
        mxheight, mxend = -activeheap[0][0], -activeheap[0][1]
        while(activeheap):
            heapq.heappop(activeheap)
            FarEnd=max(FarEnd, mxend)
            if not activeheap:
                break
            mxheight, mxend = -activeheap[0][0], -activeheap[0][1]
            if FarEnd<mxend:
                keypoint.append([FarEnd, mxheight])
                
        return keypoint
                
