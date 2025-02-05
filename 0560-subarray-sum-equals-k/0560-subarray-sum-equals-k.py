class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res =0
        prefix= {0:1}
        curr = 0
        for n in nums:
            curr+=n

            if curr-k in prefix:
                res+=prefix[curr-k]
            
            prefix[curr] = 1+prefix.get(curr,0)
        
        return res

        