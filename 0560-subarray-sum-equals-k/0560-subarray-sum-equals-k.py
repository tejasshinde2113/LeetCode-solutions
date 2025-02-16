class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dct ={0:1}
        curr =0
        res =0
        for i in nums:
            curr+=i
            if curr - k in dct:
                res+= dct[curr-k]
            dct[curr] = 1+dct.get(curr,0)
        return res

        