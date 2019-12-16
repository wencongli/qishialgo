‘’’
Runtime: 48 ms, faster than 99.81% of Python3 online submissions for Min Stack.
Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Min Stack.
‘’’

import sys
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min=sys.maxsize
        self.stack=[]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min=min(self.min, x)

    def pop(self) -> None:
        try:
            if self.min==self.stack[-1]:
                if(len(self.stack)>1):
                    self.min=min(self.stack[:-1])
                else:
                    self.min=sys.maxsize
            self.stack.pop()
        except:
            print("stack underflow!")

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
