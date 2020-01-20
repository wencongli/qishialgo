Your submission beats 46.00% Submissions!

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        capacity=len(hashTable)
        newcap=capacity*2
        firstptr=[None for _ in range(newcap)]
        lastptr=[None for _ in range(newcap)]
        # print(newcap)
        '''
        for node is
        
        '''
        for i,node in enumerate(hashTable):
            if node is None or node.val is None:
                continue
            p=node
            while p:
                val=p.val
                rehash=val%newcap
                newnode=ListNode(val)
                if lastptr[rehash] is None:
                    lastptr[rehash]=newnode
                    firstptr[rehash]=newnode
                else:
                    lastptr[rehash].next=newnode
                    lastptr[rehash]=newnode
                p=p.next
        return firstptr
