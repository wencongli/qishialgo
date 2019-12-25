'''
Method 1: recursion

Runtime: 24 ms, faster than 98.78% of Python3 online submissions for Symmetric Tree.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Symmetric Tree.
'''

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # method 1: recursion
        
        def check(nodeA, nodeB):
            if nodeA is None and nodeB is None:
                return True
            if nodeA is None or nodeB is None:
                # one child is None while the other is not
                return False
            if nodeA.val!=nodeB.val:
                return False
            return check(nodeA.left, nodeB.right) and check(nodeA.right, nodeB.left)
            
        if root is None:
            return True
        
        return check(root.left, root.right)

'''
Method 2: iteration
Runtime: 32 ms, faster than 84.24% of Python3 online submissions for Symmetric Tree.
Memory Usage: 13 MB, less than 91.38% of Python3 online submissions for Symmetric Tree.
'''

import collections
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # method 2: iteration
        if root is None:
            return True
        
        # queue or stack are both okay
        q=collections.deque()
        q.append(root.left)
        q.append(root.right)
        while (len(q)>0):
            nodeA=q.popleft()
            nodeB=q.popleft()
            if nodeA is None and nodeB is None:
                continue
            elif nodeA is None or nodeB is None:
                return False
            else:
                # nodeA and nodeB are both not-None
                if nodeA.val!=nodeB.val:
                    return False
                q.append(nodeA.left)
                q.append(nodeB.right)
                
                q.append(nodeA.right)
                q.append(nodeB.left)
                
        return True
        
