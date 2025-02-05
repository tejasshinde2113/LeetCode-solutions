class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-a for a in nums]
        
        cnt=0
        
        heapq.heapify(heap)
        
        while k>0:
            k-=1
            if k==0:
                return -heap[0]
            
            heapq.heappop(heap)
        

        