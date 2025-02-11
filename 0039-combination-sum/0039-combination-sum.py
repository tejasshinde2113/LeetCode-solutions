class Solution:
    def combinationSum(self, ca: List[int], target: int) -> List[List[int]]:

        res =[]
        def check(s,arr,ind):
            if s> target:
                return False
            if s== target:
                res.append(arr)
                return
            
            for i in range(ind,len(ca)):
                check(ca[i]+s,arr + [ca[i]]   ,i)
        check(0,[],0)
        return res
        