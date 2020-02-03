# Simple recursion, can be faster by using DP
# when we want to iterate over [i+1, i+m],
# we can utilize results from [1, m], and offset by i

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if 0==n:
            return []
        def generate(f, t):
            if f>t:
                return [None]
            if f==t:
                return [TreeNode(f)]
            ret=[]
            for i in range(f, t+1):
                left=generate(f, i-1)
                right=generate(i+1, t)
                for leftnode in left:
                    for rightnode in right:
                        root=TreeNode(i)
                        root.left=leftnode
                        root.right=rightnode
                        ret.append(root)
            return ret
        return generate(1,n)
