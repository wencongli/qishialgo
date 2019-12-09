# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import sys
import heapq
class Val_Node:
    def __init__(self, val, node):
        self.val=val
        self.node=node
    def __lt__(self, other):
        return self.val<other.val

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # make a head node and return head.next
        head=ListNode(-1)
        curr=head
        if(len(lists)==0):
            return None
        
        queue=[]
        for element in lists:
            if element is not None:
                heapq.heappush(queue, Val_Node(element.val, element))
            
        while (len(queue)>0):
            # if queue is not empty
            smallnode=heapq.heappop(queue)
            nxt_node = smallnode.node
            curr.next=nxt_node
            curr=curr.next
            nxt_node=nxt_node.next
            if nxt_node:
                # if nxt_node is not None, push into queue
                heapq.heappush(queue, Val_Node(nxt_node.val, nxt_node))
            
        return head.next
