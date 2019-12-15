‘’’
Runtime: 128 ms, faster than 51.86% of Python3 online submissions for Remove Invalid Parentheses.
Memory Usage: 13.5 MB, less than 42.10% of Python3 online submissions for Remove Invalid Parentheses.

Using BFS to search for the Shortest Path
‘’’

import collections
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if len(s)==0:
            return [""]
        # step is the number of removal
        # self.step=0
        # found is True if we find 1 valid solution, with minimum number of removal
        self.found=False
        result=set()
        # use visited to avoid duplicate visit
        visited=set()
        prv=collections.deque()
        nxt=collections.deque()
        nxt.append(s)
        while(len(nxt)>0 and not self.found):
            prv, nxt = nxt, prv
            while (len(prv)>0):
                s_new=prv.popleft()
                if len(s_new)==0:
                    result.add(s_new)
                    continue
                # explore s_new:
                # left and right are the flags indicating 
                # if left/right parentheses need to be removed
                left=False
                right=False
                sum=0
                for char in s_new:
                # iterate over each char in s
                    if char=='(':
                        sum+=1
                    elif char==')':
                        sum-=1
                    if sum<0:
                        # if num of right larger than num of left
                        # we have to remove >=1 right parenthese
                        right=True
                # if num of left>num of right, we have to remove >=1 left
                left=sum>0
                # s_new is valid if no parenthese need to be removed
                # record s_new into result
                if ((not left) and (not right)):
                    self.found=True
                    result.add(s_new)
                elif (self.found):
                # if at current level, already has solution
                # and current s_new is invalid
                # pruning
                    continue
                else:
                # s_new invalid, and valid solution not found yet
                # extend all status from s_new
                    for i in range(len(s_new)):
                        s_nxt=s_new[:i]+s_new[i+1:]
                        if (s_nxt in visited):
                            continue
                        char=s_new[i]
                        if left and char=='(':
                            visited.add(s_nxt)
                            nxt.append(s_nxt)
                        elif right and char==')':
                            visited.add(s_nxt)
                            nxt.append(s_nxt)
                            
        return list(result)
