class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        heap =[]
        nums = set(nums)

        for a in nums:
            heapq.heappush(heap,a)
            if len(heap)>3:
                heapq.heappop(heap)
        
        return heap[0] if len(heap) > 2 else heap[-1]
        