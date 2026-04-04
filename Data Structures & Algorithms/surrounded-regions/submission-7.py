class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROW, COL = len(board), len(board[0])

        def dfs(row, col, visited):
            if row < 0 or row == ROW or col < 0 or col == COL:
                return False
            if board[row][col] == 'X':
                return True
            if (row, col) in visited:
                return True
            visited.add((row, col))
            return dfs(row+1, col, visited) and dfs(row-1, col, visited) and\
            dfs(row, col+1, visited) and dfs(row, col-1, visited)
        
        def flip(board, visited):
            for row, col in visited:
                board[row][col] = 'X'

        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == 'O':
                    visited = set()
                    if dfs(row, col, visited):
                        flip(board, visited)
        