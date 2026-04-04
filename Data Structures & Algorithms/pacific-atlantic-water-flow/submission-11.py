class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        def dfs(table, row, col, prev):
            if row < 0 or ROW == row or col < 0 or col == COL or heights[row][col] < prev or table[row][col] == 1:
                return
            
            if heights[row][col] >= prev:
                table[row][col] = 1
            
            dfs(table, row-1, col, heights[row][col])
            dfs(table, row, col-1, heights[row][col])
            dfs(table, row+1, col, heights[row][col])
            dfs(table, row, col+1, heights[row][col])

        pacific_table = [[0 for _ in range(COL)] for _ in range(ROW)]
        atlantic_table = [[0 for _ in range(COL)] for _ in range(ROW)]  

        for idx in range(COL):
            dfs(pacific_table, 0, idx, -1)
            dfs(atlantic_table, ROW-1, idx, -1)
        
        for idx in range(ROW):
            dfs(pacific_table, idx, 0, -1)
            dfs(atlantic_table, idx, COL-1, -1)   

        res = []
        for row in range(ROW):
            for col in range(COL):
                if pacific_table[row][col] and atlantic_table[row][col]:
                    res.append([row, col])
        return res


            