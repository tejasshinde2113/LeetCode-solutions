
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []

        count = Counter(nums)

        for ke, v in count.items():
            heapq.heappush(heap,(-v,ke))
        
        
        res =[]
        temp = k        
        while temp >0:
            val = heapq.heappop(heap)[1]
            res.append(val)
            temp-=1
        return res[:k]
