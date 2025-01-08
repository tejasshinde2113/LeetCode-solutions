import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        arr =[1,max(piles)]
        

        def isPossible(mid):
            return sum(ceil(i/mid) for i in piles) <= h


        while arr[0]<arr[1]:
            mid = (arr[1]+arr[0])//2

            if isPossible(mid):
                arr[1] = mid
            else:
                arr[0] = mid+1
        return (arr[0])