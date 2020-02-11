class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ret=0
        if(0==len(matrix)):
            return 0
        
        nrows=len(matrix)
        ncols=len(matrix[0])
        direction=[[-1,0],[0,-1],[1,0],[0,1]]
        cache=[[-1 for j in range(ncols)] for i in range(nrows)]
        def DFS (i,j):
            if cache[i][j]!=-1:
                return cache[i][j]
            # return the number of steps increasing from i,j
            # add a cache: cache[i][j]
            # note: if node A is smaller than node B,
            # even node A is marked as visited, it doesn't matter
            # Actually, visited is essentially unnecessary
            # visited.add((i,j))
            final_length=1
            for d in range(4):
                newi, newj = i+direction[d][0], j+direction[d][1]
                # within range
                if (newi>=0 and newi<nrows and newj>=0 and newj<ncols):
                    # increasing
                    if(matrix[newi][newj]>matrix[i][j]):
                        length=1+DFS(newi,newj)
                        if(length>final_length):
                            final_length=length
            # restore path
            # visited.remove((i,j))
            cache[i][j]=final_length
            return final_length
            
        # visited=set()
        for i in range(nrows):
            for j in range(ncols):
                ret=max(ret, DFS(i,j))
                    
        return ret
