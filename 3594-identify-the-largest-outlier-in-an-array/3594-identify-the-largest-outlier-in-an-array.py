class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        tracker = Counter(nums)
        total = sum(nums)
        out = float('-inf')
        for num in nums:
            tracker[num]-=1
            total = total - num

            if total % 2 ==0 and tracker[total//2]:
                out = max(out,num)
                
            tracker[num]+=1
            total = total + num

        return out



        