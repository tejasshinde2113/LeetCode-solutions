class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return 0
        if x<=2:
            return 1
        
        start = 1
        end = x//2


        while start <=end:
            mid = start + (end-start)//2

            sq = mid*mid
            if sq == x:
                return mid
            elif sq>x:
                end = mid-1
            else:
                start = mid+1
        return end