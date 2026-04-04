class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        ans = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == -1:
                    continue
                elif grid[r][c] == 1:
                    # bfs
                    area = self.bfs(grid, r, c, ROW, COL)
                    ans = max(ans, area)
                else:
                    grid[r][c] = -1
        
        return ans
    
    def bfs(self, grid, r, c, ROW, COL):
        queue = deque([(r,c)])
        grid[r][c] = -1
        area = 1
        while queue:
            length = len(queue)
            for _ in range(length):
                row, col = queue.popleft()
                for r_o, c_o in [(-1,0), (0,-1), (1,0), (0,1)]:
                    if 0 <= row + r_o and row + r_o < ROW and\
                    0 <= col + c_o and col + c_o < COL and\
                    grid[row + r_o][col + c_o] == 1:
                        queue.append((row + r_o, col + c_o))
                        grid[row + r_o][col + c_o] = -1
                        area += 1
        return area