'''
Idea 1: re-implement the heap functionality
Runtime: 232 ms, faster than 29.28% of Python online submissions for Sliding Window Maximum.
Memory Usage: 19.7 MB, less than 6.90% of Python online submissions for Sliding Window Maximum.
'''

import heapq

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # use a maxheap to maintain the max
        # use a dictionary as the functionality of pointer, 
        # to record the position of node in the heap
        # key: array_index; value: heap_position
        posdict=dict()
        heap=[]
        # perform heap by myself
        def parent(ind):
            return (ind-1)//2
        def left(ind):
            return 2*ind+1
        def right(ind):
            return 2*ind+2
        
        ret=[]
        n=len(nums)
        def siftup(heap, ind, posdict):
            if 0==ind:
                return
            pind=parent(ind)
            if heap[pind]<heap[ind]:
                # swap the value
                # the mapping for array index needs to be updated
                parentarrind, currarrind = heap[pind][1], heap[ind][1]
                heap[pind], heap[ind] = heap[ind], heap[pind]
                posdict[parentarrind], posdict[currarrind] = ind, pind
                siftup(heap, pind, posdict)
            
        def siftdown(heap, ind, posdict):
            leftchild, rightchild = left(ind), right(ind)
            if leftchild>=k:
                return
            mx=heap[ind]
            mxind=ind
            if heap[leftchild]>mx:
                mx=heap[leftchild]
                mxind=leftchild
            if rightchild<k and heap[rightchild]>mx:
                mx=heap[rightchild]
                mxind=rightchild
            
            # current "ind" needs to be replaced by max of the 3 elements
            if mxind!=ind:
            # swap is needed
                currarrind, childarrind = heap[ind][1], heap[mxind][1]
                heap[ind], heap[mxind] = heap[mxind], heap[ind]
                posdict[currarrind], posdict[childarrind] = mxind, ind
                siftdown(heap, mxind, posdict)
            
        for i in range(n):
            if i<k:
            # build up the heap
                heap.append((nums[i], i))
                heappos=len(heap)-1
                posdict[i]=heappos
                siftup(heap, heappos, posdict)
                # maintain heap property: sift up and sift down
            else:
                to_delete=i-k
                heappos=posdict[to_delete]
                # replace the to_delete position with the new value and new index
                # and then maintain the heap property
                heap[heappos]=(nums[i],i)
                posdict[i]=heappos
                siftup(heap, heappos, posdict)
                siftdown(heap, heappos, posdict)
                
            # print("arrind:", i, "heap:", heap)
            if len(heap)==k:
            # if window is built up, append the heap top to result
                ret.append(heap[0][0])
                
        return ret


'''
idea 2: decreasing deque
Your runtime beats 85.75 % of python submissions.
'''

import heapq
import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # maintain a decreasing deque
        # pop front if the front element gets expired
        # pop back if the back element <= the new element
        queue=collections.deque()
        ret=[]
        for i, num in enumerate(nums):
            # if back element is small, delete it
            while queue and nums[queue[-1]]<=num:
                queue.pop()
            
            queue.append(i)
            # if front element is expired, delete it
            while queue and queue[0]<i-k+1:
                queue.popleft()
            
            if i>=k-1:
                ret.append(nums[queue[0]])
        return ret
                
