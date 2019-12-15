‘’’
Runtime: 204 ms, faster than 90.75% of Python3 online submissions for Maximal Rectangle.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Maximal Rectangle.
‘’’
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # from other's idea
        nrows=len(matrix)
        if nrows==0: 
            return 0
        ncols=len(matrix[0])
        if ncols==0:
            return 0
        ret=0
        # using DP algo
        # for entry (i,j), find the highest height H[j] from (i,j) to above
        # H[j] is the num of consecutive '1' from (i,j) to above
        # L[j] record the shortest common left expansion from row i-H[j]+1 to row i
        # R[j] record the shortest common right expansion from row i-H[j]+1 to row i
        H=[0]*ncols
        L=[0]*ncols
        R=[ncols]*ncols
        
        for i in range(nrows):
            # left_bound and right_bound is the bound of the consecutive '1'
            # in the row i
            left_bound, right_bound = 0, ncols
            # scan from left to right to update left
            for j in range(ncols):
                char=matrix[i][j]
                if char=='0':
                    # H returns to 0, update left_bound
                    H[j]=0
                    L[j]=0
                    left_bound=j+1
                else:
                    # height increases by 1
                    H[j]+=1
                    L[j]=max(left_bound, L[j])
                    
            # scan from right to left to update right
            for j in range(ncols-1,-1,-1):
                char=matrix[i][j]
                if char=='0':
                    R[j]=ncols
                    right_bound=j
                else:
                    R[j]=min(right_bound, R[j])
                    ret=max(ret, H[j]*(R[j]-L[j]))
                    
        return ret
