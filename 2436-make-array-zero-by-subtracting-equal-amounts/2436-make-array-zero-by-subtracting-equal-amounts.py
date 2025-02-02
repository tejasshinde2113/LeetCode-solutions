class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        a = set()

        for num in nums:
            if num != 0:
                a.add(num)
        
        return len(a)

        