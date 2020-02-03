# Idea: return value of the recursion function only contains path on 1 side
when evaluate the maximum path sum, consider path on 2 sides

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max=-float('inf')
        def DFS(node):
            if node is None:
                return 0
            left=DFS(node.left)
            right=DFS(node.right)
            localsum=node.val
            if left>0:
                localsum+=left
            if right>0:
                localsum+=right
            self.max=max(self.max, localsum)
            
            maxsub=max(left, right)
            return node.val+max(0, maxsub)
        DFS(root)
        return self.max
