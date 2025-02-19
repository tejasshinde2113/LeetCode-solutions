class Solution:
    def combinationSum(self, c: List[int], target: int) -> List[List[int]]:
        res=set()


        def check(total,arr,ind):
            if total == target:
                res.add(tuple(arr[:]))
                return
            if total > target:
                return
            
            for i in range(ind,len(c)):
                check(total+c[i] , arr+[c[i]], i)

        
        check(0,[],0)
        return list(res)
        