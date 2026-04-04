class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROWS, self.COLS = len(board), len(board[0])
        self.visited = set()
        def dfs(row, col, idx):
            if idx == len(word):
                return True
            
            if (row < 0 or row >= self.ROWS or col < 0 or col >= self.COLS or (row, col) in self.visited or
            board[row][col] != word[idx]):
                return False
            self.visited.add((row, col))
            res = dfs(row + 1, col, idx+1) or dfs(row - 1, col, idx+1) or dfs(row, col+1, idx+1) or dfs(row, col-1, idx+1)
            self.visited.remove((row, col))
            return res

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if dfs(row, col, 0):
                    return True
        return False
