class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res =[]
        def check(cnt,arr):
            res.append(arr[:])
            
            for i in range(cnt,len(nums)):
                check(i+1,arr+[nums[i]])
        
        check(0,[])
        return res

        