'''
Method 1: with relaxation, all nodes

Runtime: 476 ms, faster than 96.61% of Python3 online submissions for Network Delay Time.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Network Delay Time.
'''

class pair:
    # using a new class to speed up the min value finding
    # by using heapq
    def __init__(self, next_node , weight):
        self.next=next_node
        self.weight=weight
    def __lt__(self, node):
        return self.weight<node.weight 

import heapq
import sys

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # using Dijstra's algo
        # find out the maximum time needed (if all can be visited)
        if(1==N):
            return 0
        
        # first, build the graph adjacency list
        # note: adj_list[0] is blank, because there's no node #0
        # later on, only need to check adj_list[1:]
        adj_list=[dict() for i in range(N+1)]
        # a node can not be visited if there's no in-degree of that,
        # unless that node is the starting node
        can_visit=set()
        for edge in times:
            u,v,w=edge
            can_visit.add(v)
            adj_list[u][v]=w
        
        # sanity check
        for i in range(1, N+1):
            if i not in can_visit and i!=K:
                return -1
         
	# build the min-heap for Dijstra
        distance=[]
        for i in range(1,N+1):
            if i==K:
                distance.append(pair(K,0))
            else:
                if i in adj_list[K]:
                    distance.append(pair(i,adj_list[K][i]))
                else:
                    distance.append(pair(i,sys.maxsize))
        heapq.heapify(distance)
        
        max_length=0
        visited=dict()
        while(len(distance)>0):
            new_pair = heapq.heappop(distance)
            next_node, weight = new_pair.next, new_pair.weight
            # the element with the shortest path from K is poped out
            # info: node number, weight
            if (weight==sys.maxsize):
                # cannot reach any other nodes
                break
            visited[next_node]=weight
            max_length=weight
            for pr in distance:
		# if the existence of "next_node", can help to relax the pair "pr"
                if pr.next in adj_list[next_node]:
                    if pr.weight>weight+adj_list[next_node][pr.next]:
                        pr.weight=weight+adj_list[next_node][pr.next]
                        
            heapq.heapify(distance)
        
        if len(visited)==N:
            # all of the nodes can be reached
            return max_length
        else:
            return -1

'''
Method 2: without relaxation, only to accessible nodes

Runtime: 500 ms, faster than 83.45% of Python3 online submissions for Network Delay Time.
Memory Usage: 14.6 MB, less than 69.23% of Python3 online submissions for Network Delay Time.
'''

import heapq
import sys

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # using Dijstra's algo
        # find out the maximum time needed (if all can be visited)
        if(1==N):
            return 0
        
        # first, build the graph adjacency list
        # note: adj_list[0] is blank, because there's no node #0
        # later on, only need to check adj_list[1:]
        adj_list=[dict() for i in range(N+1)]
        # a node can not be visited if there's no in-degree of that,
        # unless that node is the starting node
        can_visit=set()
        for edge in times:
            u,v,w=edge
            can_visit.add(v)
            adj_list[u][v]=w
        
        # sanity check
        for i in range(1, N+1):
            if i not in can_visit and i!=K:
                return -1
        
        # build the min-heap for Dijstra
        # make a tuple (weight, nxt_node) for each accessible node
        # tuple can be sorted by weight
        distance=[]
        heapq.heappush(distance, (0,K))
        
        max_length=0
        visited=dict()
        while(len(distance)>0):
            weight, node = heapq.heappop(distance)
            # the element with the shortest path from K is poped out
            # info: node number, weight
            if node in visited:
                continue
            visited[node]=weight
            max_length=weight
            for nei in adj_list[node]:
                # "nei" is the neighbor can be visited from "node"
                if nei not in visited:
                    heapq.heappush(distance, (weight+adj_list[node][nei], nei))
        
        if len(visited)==N:
            # all of the nodes can be reached
            return max_length
        else:
            return -1
