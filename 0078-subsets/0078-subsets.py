class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def back(num,arr):
            if arr not in res:
                res.append(arr)
            if num == len(nums):
                return
            if num<len(nums)-1:
                back (num+1,arr+[nums[num+1]])
            back(num+1,arr)
        
        back(-1,[])
        return res
        