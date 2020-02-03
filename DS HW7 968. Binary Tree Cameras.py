Runtime: 44 ms, faster than 62.55% of Python3 online submissions for Binary Tree Cameras.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Tree Cameras.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.numcamera=0
        if root is None:
            return self.numcamera
        
        def traverse(root, parent):
            if root is None:
                return True
            # if root.left is None and root.right is None:
                
                
            ChildMonitored=True
            rootMonitored=False
            
            ChildMonitored&=traverse(root.left, root)
            if root.left:
                rootMonitored|=root.left.val
            
            ChildMonitored&=traverse(root.right, root)
            if root.right:
                rootMonitored|=root.right.val
            
            if rootMonitored:
                if ChildMonitored:
                    return True
                else:
                    root.val=1
                    self.numcamera+=1
                    return True
            else:
                if not ChildMonitored:
                    root.val=1
                    self.numcamera+=1
                    return True
                else:
                    if parent:
                        # leaf node, with parent, we should install camera at parent
                        return False
                    else:
                        root.val=1
                        self.numcamera+=1
                    return True
            
            
        traverse(root, None)
        return self.numcamera
