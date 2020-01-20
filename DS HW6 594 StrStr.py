'''
1.KMP
Your submission beats 65.60% Submissions!
'''

class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """
    def strStr2(self, source, target):
        # write your code here
        # KMP
        if target is None or source is None:
            return -1
        if not target:
            return 0
        if not source:
            return -1
            
        m,n = len(source), len(target)
        if m<n:
            return -1
            
        nxt=[-1 for _ in range(n)]
        j=-1
        
        # next array
        for i in range(1, n):
            while j>-1 and target[j+1]!=target[i]:
                j=nxt[j]
            if target[j+1]==target[i]:
                j+=1
            nxt[i]=j
        
        # print(nxt)
        i,j = 0, -1
        while i<m and j<n-1:
            while j>-1 and source[i]!=target[j+1]:
                j=nxt[j]
            if source[i]==target[j+1]:
                j+=1
            i+=1
            
        # note: final value for j is n-1, not n
        if j>=n-1:
        # we find a match in source file, before source file comes to end
            return i-n
        return -1
                
               


# 2.rolling hash
'''
# each time, (hash function*base+chr)%MOD
MOD: prime number
base: kinds of choices we have
'''

class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """
    def strStr2(self, source, target):
        # write your code here
        # Rolling hash
        if target is None or source is None:
            return -1
        if not target:
            return 0
        if not source:
            return -1
            
        m,n = len(source), len(target)
        if m<n:
            return -1
        
        BASE=256
        MOD=10**9+7
        target_hash=0
        multiple=1
        for i, ch in enumerate(target):
            multiple=(multiple*BASE)%MOD
            target_hash=(target_hash*BASE+ord(ch))%MOD
            
        source_hash=0
        for i,ch in enumerate(source):
            source_hash=(source_hash*BASE+ord(ch))%MOD
            if i>=n:
                source_hash=(source_hash-multiple*ord(source[i-n]))%MOD
            if i>=n-1:
                # compare target and source[i-n+1: i+1]
                if source_hash==target_hash:
                    j,k = i-n+1, 0
                    found=True
                    while k<n:
                        if source[j]!=target[k]:
                            found=False
                            break
                        j+=1
                        k+=1
                    if found:
                        return i-n+1
                        
        return -1
