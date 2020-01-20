import collections
class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.s=collections.Counter()
        
    def add(self, number):
        # write your code here
        self.s[number]+=1
    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for num in self.s:
            gap=value-num
            if gap in self.s:
                if gap==num and 1==self.s[gap]:
                    continue
                return True
        return False
