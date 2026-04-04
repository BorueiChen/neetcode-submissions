class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set() 
        pos_diag = set() # r + c
        neg_diag = set() # r - c

        res = []
        board = [['.'] * n for _ in range(n)]

        def dfs(r):
            if r == n:
                res.append(["".join(e) for e in board])
                return
            
            for c in range(n):
                if c in col or r+c in pos_diag or r-c in neg_diag or board[r][c] == 'Q':
                    continue
                
                col.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                board[r][c] = 'Q'
                dfs(r+1)
                col.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
                board[r][c] = '.'
        dfs(0)
        return res