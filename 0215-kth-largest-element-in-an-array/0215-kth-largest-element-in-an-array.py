class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        for a in nums:
            heapq.heappush(heap,-a)
        
        while k>0:
            

            k-=1
            if k==0:
                return -heap[0]
            
            heapq.heappop(heap)
        

        