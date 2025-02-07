class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        maj = nums[0]
        cnt = 1
        for n in nums:
            if n == maj:
                cnt+=1
            else:
                cnt-=1
            if cnt ==0:
                maj = n
                cnt+=1
        return maj
        