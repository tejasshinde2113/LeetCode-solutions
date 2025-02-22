class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero=0
        one=0
        res =0
        dct ={}
        for i,num in enumerate(nums):
            if num:
                one+=1
            else:
                zero+=1
            
            if one-zero not in dct:
                dct[one-zero]=i

            if one == zero:
                res = one + zero
            else:
                res = max(res,i-dct[one-zero])
        return res



        