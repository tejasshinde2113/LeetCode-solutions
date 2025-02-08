class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        
        lst = [1,1]
        res = 0
        for i in range(2,n):
            res = lst[i-1]+lst[i-2]
            lst.append(res)
        
        return res
