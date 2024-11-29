class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        visit = [[0 for a in range(n)] for b in range(m)]
        temp = visit
        def bfs(r,c):
            

            q=[(r,c)]
            while q:
                row,col = q.pop()
                visit[row][col]= 1
                temp[row][col]=1

                for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
                    temprow = row+x
                    tempcol = col+y

                    if 0<=temprow<m and 0<=tempcol<n and  not visit[temprow][tempcol] and board[temprow][tempcol] == "O":
                        q.append((temprow,tempcol))


        for r in range(m):
            for c in range(n):
                if not visit[r][c] and board[r][c] == "O":
                    bfs(r,c)
                    f= True
                    for a in range(m):
                        for b in range(n):
                            if not (0 < a < m-1) and temp[a][b]==1:
                                f= False
                            if not (0 < b < n-1) and temp[a][b]==1:
                                f= False
                    if f:
                        for a in range(m):
                            for b in range(n):
                                if temp[a][b]==1:
                                    board[a][b]='X'


                    temp = [[0 for a in range(n)] for b in range(m)]


        