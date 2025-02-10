class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)

        heap = [[-v,k] for k, v in c.items()]

        heapq.heapify(heap)
        prev = None
        lst = []
        while heap or prev:
            if prev and not heap:
                return ''

            val, ch = heapq.heappop(heap)
            lst.append(ch)
            val+=1

            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if val!=0:
                prev = [val,ch]
        
        return ''.join(lst)



        
        