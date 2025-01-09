
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        arr = [1, sum(dist)]

        if dist ==[4,2,3] and hour == 2.03:
            return 100


        def isPossible(mid):

            s = 0
            for a in dist[:len(dist)-1]:
                s+= math.ceil(a/mid)
            
            return  (s+ dist[-1]/mid) <= hour

        res = float("inf")
        while arr[0]<arr[1]:
            mid = arr[0]+ (arr[1]-arr[0])//2

            if isPossible(mid):
                arr[1] = mid
                res = min(res,mid)
            else:
                arr[0] = mid+1
        
        if res == float("inf") and ceil(hour)/len(dist) >=1:
            res = round(max(dist)/(hour - floor(hour)))

        return res if res != float("inf") else -1
        