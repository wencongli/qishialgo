Runtime: 84 ms, faster than 18.69% of Python3 online submissions for Recover Binary Search Tree.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Recover Binary Search Tree.


# using Morris traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # using Morris traversal
        p=root
        if root is None:
            return
        
        prev=TreeNode(-float('inf'))
        swap=[None, None]
        
        def visit(p, prev):
            if prev.val>p.val:
                if swap[0] is None:
                    swap[0]=prev
                swap[1]=p
        
        while p:
            # print(p.val)
            if p.left is None:
                visit(p, prev)
                prev=p
                p=p.right
            else:
                q=p.left
                while q.right!=None and q.right!=p:
                    q=q.right
                if q.right==None:
                    q.right=p
                    p=p.left
                else:
                    q.right=None
                    visit(p, prev)
                    prev=p
                    p=p.right
            
        
        # print(swap)          
        swap[0].val, swap[1].val = swap[1].val, swap[0].val
        return
