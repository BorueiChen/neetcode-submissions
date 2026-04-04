class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])

        def dfs(row, col, start, visited):
            if start == len(word):
                return True

            if [row, col] in visited or row not in range(ROW) or col not in range(COL) or \
            board[row][col] != word[start]:
                return False
            
            visited.append([row, col])
            res = dfs(row-1, col, start + 1, visited) or \
            dfs(row+1, col, start + 1, visited) or \
            dfs(row, col-1, start + 1, visited) or \
            dfs(row, col+1, start + 1, visited)
            visited.pop()
            return res
            



        for r in range(ROW):
            for c in range(COL):
                if dfs(r, c, 0, []):
                    return True
        
        return False