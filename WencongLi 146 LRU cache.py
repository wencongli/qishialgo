# use linked list to implement
class LinkNode:
    def __init__(self, key=None, val=None):
        # doubly linked node
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.length=0
        self.capacity=capacity
        # head and tail are two empty nodes to point to the first and last node
        self.head=LinkNode()
        self.tail=LinkNode()
        self.head.next=self.tail
        self.tail.prev=self.head
        self.map=dict()
        
    def delete(self, node):
        node.prev.next=node.next
        node.next.prev=node.prev
        self.length-=1
        
    def add(self, node):
        # if full capacity
        if (self.length==self.capacity):
            self.map.pop(self.head.next.key)
            self.delete(self.head.next)

        # add the node to the tail
        self.tail.prev.next=node
        node.prev=self.tail.prev
        node.next=self.tail
        self.tail.prev=node
        self.length+=1
        
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node=self.map[key]
        self.delete(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node=self.map[key]
            node.val=value
            self.delete(node)
        else:
            node=LinkNode(key, value)
            self.map[key]=node
        self.add(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
