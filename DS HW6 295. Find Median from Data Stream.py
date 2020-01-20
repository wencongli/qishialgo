'''
Runtime: 204 ms, faster than 53.60% of Python3 online submissions for Find Median from Data Stream.
Memory Usage: 23.5 MB, less than 46.67% of Python3 online submissions for Find Median from Data Stream.

Idea: 2 heaps
'''

import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap=[]
        self.maxheap=[]
        self.count=0

    def addNum(self, num: int) -> None:
        # step1: find which heap to add into
        self.count+=1
        if len(self.minheap)==0:
            heapq.heappush(self.minheap, num)
            return
        
        mintop=self.minheap[0]
        if num>=mintop:
            heapq.heappush(self.minheap, num)
        else:
            # need to negate the num
            heapq.heappush(self.maxheap, -num)
        
        # step2: rebalance
        while len(self.minheap)-len(self.maxheap)>1:
            mintop=heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -mintop)
            
        while len(self.maxheap)-len(self.minheap)>1:
            maxtop=-heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, maxtop)
        
        return

    def findMedian(self) -> float:
        if 0==self.count:
            return 0
        if self.count%2==0:
            return (self.minheap[0]-self.maxheap[0])/2.0
        if len(self.minheap)>len(self.maxheap):
            return self.minheap[0]
        return -self.maxheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
