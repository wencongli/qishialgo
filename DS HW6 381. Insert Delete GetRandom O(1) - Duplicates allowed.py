'''
Runtime: 112 ms, faster than 29.05% of Python3 online submissions for Insert Delete GetRandom O(1) - Duplicates allowed.
Memory Usage: 18.1 MB, less than 100.00% of Python3 online submissions for Insert Delete GetRandom O(1) - Duplicates allowed.

Idea: use an array to store value; use dictionary to store val->pos (or: list of pos)
'''

import collections
import random
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr=[]
        self.pos=collections.defaultdict(set)
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        flag=True
        if val in self.pos:
            flag=False
        self.pos[val].add(len(self.arr))
        self.arr.append(val)
        return flag

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.pos or len(self.pos[val])==0:
            return False
        
        lastele=self.arr[-1]
        '''
        rmvind=next(iter(self.pos[val]))
        self.pos[val].remove(rmvind)
        '''
        rmvind=self.pos[val].pop()
        
        self.arr[rmvind]=lastele
        self.pos[lastele].add(rmvind)
        self.arr.pop()
        self.pos[lastele].remove(len(self.arr))
        
        if len(self.pos[val])==0:
            self.pos.pop(val)
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.arr[random.randint(0, len(self.arr)-1)]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
