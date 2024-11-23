class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        def help(n):
            if n == 1:
                return True
            if n<1:
                return False
            
            return n%3==0 and help(n/3)
        
        return help(n)
        