
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
