class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1]
        tot =1
        for num in nums[:len(nums)-1]:
            tot *= num
            res.append(tot)
        tot = 1
        for  ind in range(len(nums)-2,-1,-1):
            tot *= nums[ind+1] 
            res[ind]*=tot
        
        return res
           

        