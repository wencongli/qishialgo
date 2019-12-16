‘’’
Runtime: 68 ms, faster than 98.31% of Python3 online submissions for Binary Search Tree Iterator.
Memory Usage: 19 MB, less than 100.00% of Python3 online submissions for Binary Search Tree Iterator.
‘’’

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        # self.lst is used to record the in-order traversal result
        self.lst=[]
        stack=[]
        p=root
        while((len(stack)>0) or (p is not None)):
            if(p):
                stack.append(p)
                p=p.left
            else:
                p=stack.pop()
                self.lst.append(p.val)
                p=p.right
        self.ind=0
        self.length=len(self.lst)
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        if(self.ind>=self.length):
            return None
        ret=self.lst[self.ind]
        self.ind+=1
        return ret

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.ind<self.length


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
