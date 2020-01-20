'''
Runtime: 1500 ms, faster than 5.04% of Python3 online submissions for Sliding Window Median.
Memory Usage: 15.9 MB, less than 20.00% of Python3 online submissions for Sliding Window Median.
'''
# re-implement my own heap class, to enable element deletion in O(logn) based on given array-index

import heapq
import collections


# only implement minheap
class ownheap:
    def __init__(self, capacity):
        # make sure minheap (larger portion) has more elements than maxheap(small portion)
        self.heap=[]
        # dict: arr_index --> heap index
        self.dict=dict()
        self.capacity=capacity
        self.size=0
        
    def add(self, val, arr_ind):
        self.size+=1
        self.heap.append([val, arr_ind])
        self.dict[arr_ind]=len(self.heap)-1
        self.siftup(len(self.heap)-1)
        
        
    def delete(self, arr_ind):
        self.size-=1
        heap_ind=self.dict[arr_ind]
        val, ind =self.heap[heap_ind]
        # print("before delete: arr_ind:",arr_ind, ", heap_ind:", heap_ind )
        # print(self.heap, self.dict)
        self.heap[heap_ind]=self.heap[-1]
        self.dict[self.heap[-1][1]]=heap_ind
        self.heap.pop()
        self.dict.pop(arr_ind)
        # print("after delete:", self.heap, self.dict)
        
        if heap_ind<len(self.heap):
            self.siftup(heap_ind)
            self.siftdown(heap_ind)
            
        return [val, ind]    
        
    def pop(self):
        if not self.heap:
            return -1
        top_arrind=self.heap[0][1]
        return self.delete(top_arrind)
    
    def top(self):
        if not self.heap:
            return -1
        return self.heap[0][0]
            
    def parent(self, i):
        return (i-1)//2
    def leftchild(self, i):
        return 2*i+1
    def rightchild(self, i):
        return 2*i+2
        
    def siftup(self, heap_ind):
        if 0==heap_ind:
            return 
        par=self.parent(heap_ind)
        if self.heap[par][0]>self.heap[heap_ind][0]:
            # swap is needed
            par_arrind, curr_arrind = self.heap[par][1], self.heap[heap_ind][1]
            self.heap[par], self.heap[heap_ind] = \
            self.heap[heap_ind], self.heap[par]
            
            self.dict[par_arrind], self.dict[curr_arrind] = \
            heap_ind, par
            self.siftup(par)
        
    def siftdown(self, heap_ind):
        left=self.leftchild(heap_ind)
        if left>=len(self.heap):
            return 
        mn=self.heap[heap_ind][0]
        mnind=heap_ind
        if self.heap[left][0]<mn:
            mn=self.heap[left][0]
            mnind=left
            
        right=self.rightchild(heap_ind)
        if right<len(self.heap) and self.heap[right][0]<mn:
            mn=self.heap[right][0]
            mnind=right
            
        if mnind!=heap_ind:
            cur_arrind, child_arrind = self.heap[heap_ind][1], self.heap[mnind][1]
            self.heap[heap_ind], self.heap[mnind] = \
            self.heap[mnind], self.heap[heap_ind]
            
            self.dict[cur_arrind], self.dict[child_arrind] = \
            mnind, heap_ind
            self.siftdown(mnind)

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        maxheap=ownheap(k//2)
        minheap=ownheap(k-k//2)
        odd=k%2
        ret=[]
        
        for i, num in enumerate(nums):
            if i<k:
                maxheap.add(-num, i)
                negval, ind = maxheap.pop()
                minheap.add(-negval, ind)
                if minheap.size-maxheap.size>1:
                    val, ind = minheap.pop()
                    maxheap.add(-val, ind)
            else:
                to_delete=nums[i-k]
                if i-k in maxheap.dict:
                    maxheap.delete(i-k)
                else:
                    minheap.delete(i-k)
                maxheap.add(-num, i)
                negval, ind = maxheap.pop()
                minheap.add(-negval, ind)
                if minheap.size-maxheap.size>1:
                    val, ind = minheap.pop()
                    maxheap.add(-val, ind)
            #print("i, num:", i, num)
            #print("maxheap:", maxheap.heap, maxheap.dict)
            #print("minheap:", minheap.heap, minheap.dict)
            if i>=k-1:
                if odd:
                    ret.append(minheap.top())
                else:
                    # note!! value in maxheap is negative
                    ret.append((minheap.top()-maxheap.top())/2.0)
        return ret
