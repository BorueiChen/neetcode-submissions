class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        def dfs(prev, row, col, table):
            if row < 0 or row == ROW or col < 0 or col == COL:
                return
            if table[row][col] == 1:
                return
            if heights[row][col] < prev:
                return
            
            table[row][col] = 1
            dfs(heights[row][col], row - 1, col, table)
            dfs(heights[row][col], row + 1, col, table)
            dfs(heights[row][col], row, col - 1, table)
            dfs(heights[row][col], row, col + 1, table)

        pacific_table = [[0 for _ in range(COL)] for _ in range(ROW)]
        atlantic_table = [[0 for _ in range(COL)] for _ in range(ROW)]
        for col in range(COL):
            dfs(-1, 0, col, pacific_table)
            dfs(-1, ROW - 1, col, atlantic_table)
        
        for row in range(ROW):
            dfs(-1, row, 0, pacific_table)
            dfs(-1, row, COL - 1, atlantic_table)
        
        ans = []
        for row in range(ROW):
            for col in range(COL):
                if pacific_table[row][col] and atlantic_table[row][col]:
                    ans.append([row, col])
        return ans
