class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        visit = visit = [[0 for _ in range(n)] for _ in range(m)]


        def dfs(row,col,index):
            if index == len(word):
                return True
            if row < 0 or row >= m or col < 0 or col >= n or visit[row][col] or board[row][col] != word[index]:
                return False  # Out of bounds, already visited, or mismatch

            visit[row][col] = 1  # Mark cell as visited
            
            for x, y in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                if dfs(row + x, col + y, index + 1):
                    return True
                    
            visit[row][col] = 0  
            return False




        for i,row in enumerate(board):
            for j, col in enumerate(row):
                if word[0] == col:
                    visit[i][j]==1
                    if dfs(i,j,0):
                        return True

        return False

        