class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        cnt=0
        nums = deque(nums)
        while nums:
            if max(c.values())<2:
                return cnt
            cnt+=1
            if len(nums) <3:
                return cnt
            
            c[nums.popleft()]-=1
            c[nums.popleft()]-=1
            c[nums.popleft()]-=1
        return cnt

            
        