class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        possibility= [max(weights),sum(weights)]

        def check(mid):
            cntday =1
            currcap =0
            for weight in weights:
                currcap += weight
                if currcap  > mid:
                    cntday+=1
                    currcap = weight
                
            
            return cntday> days


        res = float('inf')
        while possibility[0] <= possibility[1]:

            mid =  (possibility[1]+possibility[0])//2

            if check(mid) :
                
                possibility[0] = mid+1
            else:
                res = min(res,mid)
                possibility[1] = mid-1
        return res        


           
        