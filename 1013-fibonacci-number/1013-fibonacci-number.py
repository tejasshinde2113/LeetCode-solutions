class Solution:
    def __init__(self):

        self.hm = {}
    def fib(self, n: int) -> int:
        if n in self.hm:
            return self.hm[n]
        if n ==0:
            return 0
        if n==1:
            return 1
        
        self.hm[n]=self.fib(n-1)+self.fib(n-2)
        return self.hm[n]