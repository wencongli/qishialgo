'''
Method 1: deque
Runtime: 928 ms, faster than 48.15% of Python3 online submissions for Shortest Subarray with Sum at Least K.
Memory Usage: 19.5 MB, less than 25.00% of Python3 online submissions for Shortest Subarray with Sum at Least K.
'''

import collections
import sys

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        # maintain an increasing deque.
        # before putting into deque, an element is minuend
        # after putting into deque, an element is subtractor
        
        # there are 2 cases for element not in the deque
        # 1. as a subtractor, already find a pair, so remove out of deque
        # 2. as a subtractor, replaced by a later & smaller element
        
        # S is the summation array, S[i] is summation of [0,i)
        n=len(A)
        S=[0]*(n+1)
        for i in range(1, n+1):
            S[i]=S[i-1]+A[i-1]
            
        # q stores the index
        q=collections.deque()
        shortest=sys.maxsize
        for ind in range(len(S)):
            # case 1: already find a pair, so remove out of deque
            while len(q)>0 and S[ind]-S[q[0]]>=K:
                shortest=min(shortest, ind-q.popleft())
            # case 2: a subtractor replaced by a later & smaller element
            while len(q)>0 and S[ind]<=S[q[-1]]:
                q.pop()
            # every element needs to enqueue at the beginning
            q.append(ind)
            
        if sys.maxsize==shortest:
            return -1
        else:
            return shortest

