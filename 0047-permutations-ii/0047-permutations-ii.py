class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        def check(ind,arr,r):
            if len(arr)== len(nums):
                res.add(tuple(arr[:]))
                return
            
            for i in range(0,len(r)):
                check(i,arr+[r[i]],r[:i]+r[i+1:])
        check(0,[],nums)
        return list(res)