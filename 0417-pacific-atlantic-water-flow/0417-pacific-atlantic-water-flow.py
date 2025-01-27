# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         pacific = set()

#         m = len(heights)
#         n= len(heights[0])


#         visit = [[0 for a in range(n) ] for b in range(m)]
#         def dfs(row,col):

#             q = deque([(0, a) for a in range(n)] + [(b, 0) for b in range(m)])
#             while q:
                
#                 row,col = q.popleft()
#                 visit[row][col]=1
#                 if row <0 or row >=m or col <0 or col >= n:
#                     continue
                
#                 if row ==0 or col ==0:
#                     pacific.add((row,col))
#                 elif heights[row][col] >= heights[row][col-1] and (row,col-1) in pacific:
#                     pacific.add((row,col))
#                 elif heights[row][col] >= heights[row-1][col] and (row-1,col) in pacific:
#                     pacific.add((row,col))
#                 elif col+1< n and heights[row][col] >= heights[row][col+1] and (row,col+1) in pacific:
#                     pacific.add((row,col))
#                 elif row+1< m and heights[row][col] >= heights[row+1][col] and (row+1,col) in pacific:
#                     pacific.add((row,col))

#                 for x,y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#                     trow = x+row
#                     tcol = y+col
#                     if trow >=0 and trow <m and tcol <n and tcol >= 0 and visit[trow][tcol] == 0:
#                         q.append((trow,tcol))
            
#         dfs(0,0)


#         atlantic = set()



#         visit = [[0 for a in range(n) ] for b in range(m)]
#         def dfs2(row,col):

#             q = deque([(a, n - 1) for a in range(m)] + [(m - 1, b) for b in range(n)])
#             while q:
                
#                 row,col = q.popleft()
#                 visit[row][col]=1
#                 if row <0 or row >=m or col <0 or col >= n:
#                     continue
                
#                 if row ==m-1 or col ==n-1:
#                     atlantic.add((row,col))
#                 elif heights[row][col] >= heights[row][col+1] and (row,col+1) in atlantic:
#                     atlantic.add((row,col))
#                 elif heights[row][col] >= heights[row+1][col] and (row+1,col) in atlantic:
#                     atlantic.add((row,col))

#                 for x,y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#                     trow = x+row
#                     tcol = y+col
#                     if trow >=0 and trow <m and tcol <n and tcol >= 0 and visit[trow][tcol] == 0:
#                         q.append((trow,tcol))
            
#         dfs2(m-1,n-1)


#         return list(pacific.intersection(atlantic))

                
from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        m = len(heights)
        n = len(heights[0])

        visit = [[0 for a in range(n)] for b in range(m)]

        def bfs(q,ocean):
            
            while q:
                row, col = q.popleft()
                if row < 0 or row >= m or col < 0 or col >= n or visit[row][col]:
                    continue
                visit[row][col] = 1
                ocean.add((row, col))
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    trow, tcol = x + row, y + col
                    if (
                        0 <= trow < m
                        and 0 <= tcol < n
                        and (trow, tcol) not in ocean
                        and heights[trow][tcol] >= heights[row][col]
                    ):
                        q.append((trow, tcol))

        q = deque([(0, a) for a in range(n)] + [(b, 0) for b in range(m)])
        bfs(q,pacific)

        visit = [[0 for a in range(n)] for b in range(m)]

        q = deque([(a, n - 1) for a in range(m)] + [(m - 1, b) for b in range(n)])
        bfs(q,atlantic)

        # def bfs2():
        #     q = deque([(a, n - 1) for a in range(m)] + [(m - 1, b) for b in range(n)])
        #     while q:
        #         row, col = q.popleft()
        #         if row < 0 or row >= m or col < 0 or col >= n or visit[row][col]:
        #             continue
        #         visit[row][col] = 1
        #         atlantic.add((row, col))
        #         for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        #             trow, tcol = x + row, y + col
        #             if (
        #                 0 <= trow < m
        #                 and 0 <= tcol < n
        #                 and (trow, tcol) not in atlantic
        #                 and heights[trow][tcol] >= heights[row][col]
        #             ):
        #                 q.append((trow, tcol))

        # bfs2()

        return list(pacific.intersection(atlantic))
