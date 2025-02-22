class RandomizedSet:

    def __init__(self):
        self.dct= {}
        self.lst =[]
        

    def insert(self, val: int) -> bool:
        if val in self.dct:
            return False
        
        l = len(self.lst)
        self.lst.append(val)
        self.dct[val] = l
        return True
        

    def remove(self, val: int) -> bool:

        if val not in self.dct:
            return False
        
        ind = self.dct[val]
        self.lst[ind] = self.lst[-1]
        
        self.dct[self.lst[-1]] = ind
        self.lst.pop()
        del self.dct[val]

        return True
        
        
        

    def getRandom(self) -> int:
        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()