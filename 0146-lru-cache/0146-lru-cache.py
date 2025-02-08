class Node:
    def __init__(self, key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dct ={}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def insert(self,comp):
        p = self.right.prev 
        p.next = comp
        comp.prev = p
        comp.next = self.right
        self.right.prev = comp
    
    def remove(self,comp):
        n = comp.prev

        n.next = comp.next
        comp.next.prev = n

    def get(self, key: int) -> int:
        if key in self.dct:
            self.remove(self.dct[key])
            self.insert(self.dct[key])
            return self.dct[key].val
        return -1    

    def put(self, key: int, value: int) -> None:
        
        if key in self.dct:
            self.remove(self.dct[key])
            del self.dct[key]
        
        self.dct[key] = Node(key,value)
        self.insert(self.dct[key])

        if len(self.dct) > self.cap:
            l = self.left.next
            self.remove(l)
            del self.dct[l.key]
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)