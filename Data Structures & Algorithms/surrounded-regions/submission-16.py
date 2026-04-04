class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])

        def dfs(table, row, col):
            if row < 0 or row == ROW or col < 0 or col == COL:
                return
            
            if board[row][col] == 'X':
                return
            
            if table[row][col] == 'T':
                return

            table[row][col] = 'T'
            dfs(table, row-1, col)
            dfs(table, row+1, col)
            dfs(table, row, col-1)
            dfs(table, row, col+1)
        for row in range(ROW):
            if board[row][0] == 'O':
                dfs(board, row, 0)
            if board[row][COL-1] == 'O':
                dfs(board, row, COL-1)

        for col in range(COL):
            if board[0][col] == 'O':
                dfs(board, 0, col)
            if board[ROW-1][col] == 'O':
                dfs(board, ROW-1, col)
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == 'T':
                    board[row][col] = 'O'
                
