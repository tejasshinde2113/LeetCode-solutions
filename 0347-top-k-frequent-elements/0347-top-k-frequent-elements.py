class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        bub = [[] for a in range(len(nums)+1)]

        for key,val in count.items():
            bub[val].append(key)

        i=0
        res = []
        for a in range(len(bub)-1,-1,-1):
            if bub[a]:
                for val in bub[a]:
                    res.append(val)
                    i+=1
                    if i==k:
                        return res