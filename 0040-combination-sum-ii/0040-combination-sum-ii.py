class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
        res=[]
        c.sort()
        


        def check(total,arr,ind):
            if total == target:
                res.append(arr[:])
                return
            if total > target:
                return
            
            for i in range(ind,len(c)):
                if i > ind and c[i]==c[i-1]:
                    continue
                check(total+c[i] , arr+[c[i]], i+1)

        
        check(0,[],0)
        return (res)