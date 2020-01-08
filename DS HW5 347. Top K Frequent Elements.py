import collections
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # build up a minheap
        # minheap element: (freq, num)
        minheap=[]
        freq=collections.Counter()
        for num in nums:
            freq[num]+=1
            
        for ele, fq in freq.most_common():
            heapq.heappush(minheap, (fq, ele))
            while(len(minheap)>k):
                heapq.heappop(minheap)
              
        ret=[]
        while(minheap):
            fq, ele = heapq.heappop(minheap)
            ret.append(ele)
            
        ret.reverse()
        return ret
