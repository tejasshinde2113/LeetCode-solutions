class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        def check(arr,r):
            if len(arr)== len(nums):
                res.append(arr[:])
                return
            
            for i in range(0,len(r)):
                if i>0 and r[i]==r[i-1]:
                    continue
                check(arr+[r[i]],r[:i]+r[i+1:])
        check([],nums)
        return (res)