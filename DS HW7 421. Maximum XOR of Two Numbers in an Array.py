#Idea1: bit manipulation, check prefix one-by-one
#Runtime: 136 ms, faster than 80.14% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.
#Memory Usage: 19.3 MB, less than 100.00% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # using bit manipulation, using prefix numbers
        maximum=0
        mask=0
        for i in range(31, -1, -1):
            mask|=1<<i
            s={num&mask for num in nums}
            target=maximum|(1<<i)
            # s is the set of PREFIX for all of numbers
            if any(target^num in s for num in s):
                maximum=target
        return maximum
            

idea2: Trie tree
Runtime: 556 ms, Your runtime beats 33.21 % of python3 submissions.

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # using trie to record the "word"(value) we have seen
        trie=[None, None]
        def insert(num):
            temp=num
            digits=[]
            while temp:
                digits.append(temp&1)
                temp>>=1
            while len(digits)<31:
                digits.append(0)
            digits.reverse()
            p=trie
            for digit in digits:
                if p[digit] is None:
                    p[digit]=[None, None]
                p=p[digit]
        
        def check(num):
            temp=num
            digits=[]
            while temp:
                digits.append(temp&1)
                temp>>=1
            while len(digits)<31:
                digits.append(0)
            digits.reverse()
            maximum=0
            p=trie
            for base, digit in enumerate(digits):
                if p[digit^1]:
                    p=p[digit^1]
                    maximum|=1<<(31-1-base)
                else:
                    p=p[digit]
            return maximum
        
        largest=0
        for val in nums:
            insert(val)
            largest=max(largest, check(val))
        return largest
