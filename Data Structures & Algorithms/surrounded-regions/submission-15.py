class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        table = [[0] * COL for _ in range(ROW)]

        def dfs(table, row, col):
            if row < 0 or row == ROW or col < 0 or col == COL:
                return
            
            if board[row][col] == 'X':
                return
            
            if table[row][col] == 1:
                return

            table[row][col] = 1
            dfs(table, row-1, col)
            dfs(table, row+1, col)
            dfs(table, row, col-1)
            dfs(table, row, col+1)
        for row in range(ROW):
            if board[row][0] == 'O':
                dfs(table, row, 0)
            if board[row][COL-1] == 'O':
                dfs(table, row, COL-1)

        for col in range(COL):
            if board[0][col] == 'O':
                dfs(table, 0, col)
            if board[ROW-1][col] == 'O':
                dfs(table, ROW-1, col)
        for row in range(ROW):
            for col in range(COL):
                if table[row][col] == 0 and board[row][col] == 'O':
                    board[row][col] = 'X'
                
