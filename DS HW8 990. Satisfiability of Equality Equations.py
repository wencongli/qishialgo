
Runtime: 44 ms, faster than 67.27% of Python3 online submissions for Satisfiability of Equality Equations.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Satisfiability of Equality Equations.

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # all of the equal letters should form a connected component
        # if we see an inequality equation, those 2 letters
        # should belong to different sets
        parent=[i for i in range(26)]
        
        def find(ind):
            if parent[ind]!=ind:
                parent[ind]=find(parent[ind])
            return parent[ind]
        
        def union(x,y):
            xroot=find(x)
            yroot=find(y)
            if xroot!=yroot:
                parent[xroot]=yroot
        
        for eq in equations:
            if eq[1]=='=':
                a=ord(eq[0])-ord('a')
                b=ord(eq[-1])-ord('a')
                union(a,b)
                
        for eq in equations:
            if eq[1]=='!':
                a=ord(eq[0])-ord('a')
                b=ord(eq[-1])-ord('a')
                if find(a)==find(b):
                    return False
                
        return True
