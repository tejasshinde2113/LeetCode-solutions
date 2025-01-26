class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board[0])
        m = len(board)
        
        visit=[[0 for a in range(len(board[0]))] for b in range(len(board)) ]
        st=[]
        border=[False]

        def dfs(row,col):
            visit[row][col]=1


            for x,y in [(1,0),(0,1),(0,-1),(-1,0)]:
                trow = row+x
                tcol = col+y
                

                if 0<=trow< m and 0<=tcol<n and not visit[trow][tcol] and board[trow][tcol]=='O':
                    dfs(trow,tcol)
            
            if row == 0 or col == 0 or row == m-1 or col == n-1:
                border[0]=True
            st.append((row,col))
            

        for i,row in enumerate(board):
            for j,col in enumerate(row):
                if col == 'O' and visit[i][j] == 0:
                    dfs(i,j)
                    
                    if not border[0]:
                        for row,col in st:
                            board[row][col] = 'X'
                    border[0] = False
                    st=[]
        
        
        