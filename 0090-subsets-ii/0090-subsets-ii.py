class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res =[]
        def check(cnt,arr):
            res.append(arr[:])
            
            for i in range(cnt,len(nums)):
                if i > cnt and nums[i]==nums[i-1]:
                    continue
                check(i+1,arr+[nums[i]])
        
        check(0,[])
        return res