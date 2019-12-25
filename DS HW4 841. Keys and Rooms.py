'''
Method 1: DFS
Runtime: 64 ms, faster than 90.39% of Python3 online submissions for Keys and Rooms.
Memory Usage: 13.4 MB, less than 72.73% of Python3 online submissions for Keys and Rooms.
'''

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # step 1: build graph
        N=len(rooms)
        # "rooms" is essentially a adjacency list 
        
        # step 2: DFS/BFS
        visited=set()
        def DFS(ind):
            visited.add(ind)
            for nei in rooms[ind]:
                if nei not in visited:
                    DFS(nei)
        
        DFS(0)
        return len(visited)==N

'''
Method 2: BFS using queue
Runtime: 60 ms, faster than 97.25% of Python3 online submissions for Keys and Rooms.
Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Keys and Rooms.
'''

import collections
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # step 1: build graph
        N=len(rooms)
        # "rooms" is essentially a adjacency list 
        
        # step 2: DFS/BFS
        visited=set()
        visited.add(0)
        q=collections.deque([0])
        
        while(len(q)>0):
            ind=q.popleft()
            for nei in rooms[ind]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        
        return len(visited)==N
