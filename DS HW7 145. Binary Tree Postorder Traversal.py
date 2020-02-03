
# Idea 1: stack, previous node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ret=[]
        if root is None:
            return ret
        stack=[]
        prev, p=None, root
        while p or stack:
            if p:
                stack.append(p)
                p=p.left
            else:
                p=stack.pop()
                if p.right is None or p.right==prev:
                    # visit p
                    ret.append(p.val)
                    prev=p
                    p=None
                else:
                    stack.append(p)
                    p=p.right
        return ret
            

# idea 2: morris traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        dummy=TreeNode(-1)
        dummy.left=root
        p=dummy
        
        def reverse_traverse(node, root):
            ret=[]
            p=node
            while p and p!=root:
                ret.append(p.val)
                p=p.right
            ret.reverse()
            return ret
        
        ans=[]
        while p:
            if p.left:
                q=p.left
                while q.right!=None and q.right!=p:
                    q=q.right
                if q.right==None:
                    # make a thread
                    q.right=p
                    p=p.left
                else:
                    ans+=reverse_traverse(p.left, p)
                    q.right=None
                    p=p.right
            else:
                p=p.right
        return ans
