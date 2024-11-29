class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        # Proper initialization for visit
        visit = [[0 for _ in range(n)] for _ in range(m)]

        image2 = image

        def bfs(r,c,visit):

        
            visit[r][c]=1

            q=[(r,c)]

            fixed = image[r][c]
            while q:
                row, col = q[0]
                del q[0]
                image2[row][col] = color
                
                for x,y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    temprow = row + x
                    tempcol = col + y
                    if (temprow >=0 and temprow < m
                    and tempcol >=0 and tempcol < n
                    and not visit[temprow][tempcol] and image[temprow][tempcol]==fixed):
                        q.append((temprow,tempcol))
                        visit[temprow][tempcol] = 1
        
        bfs(sr,sc,visit)
        
        return image2
       
        