class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.dct ={}
        self.capacity = capacity
        
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self,element):
        back = self.right.prev 
        front = back.next

        back.next = element
        element.prev = back
        element.next = front
        front.prev = element
    
    def remove(self,element):

        prev_node = element.prev
        next_node = element.next
        prev_node.next = next_node
        next_node.prev = prev_node


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

        if len(self.dct) > (self.capacity):
            
            least = self.left.next
            self.remove(least)

            del self.dct[least.key]


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)