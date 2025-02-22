class Solution:
    def myPow(self, x: float, n: int) -> float:
        

        neg = False
        if n < 0:
            neg= True
            n=-n
        total=1
        while n>0:
            if n%2 !=0:
                total = total*x
                n-=1
            else:
                x = x*x
                n=n//2
        return 1/total if neg else total