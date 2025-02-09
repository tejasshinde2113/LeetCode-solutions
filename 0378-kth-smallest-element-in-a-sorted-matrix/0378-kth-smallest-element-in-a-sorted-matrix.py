class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        r = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heappush(r, -matrix[i][j])
                while len(r) > k:
                    heappop(r)
                    
        return -heappop(r)
                
        