class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROW, COL = len(grid), len(grid[0])
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '-2':
                    continue
                elif grid[r][c] == '1':
                    count += 1
                    # bfs
                    queue = deque([(r,c)])
                    grid[r][c] = "-2"
                    while queue:
                        for _ in range(len(queue)):
                            row, col = queue.popleft()
                            for ro, co in [(-1,0),(0,-1),(1,0),(0,1)]:
                                nr = row + ro
                                nc = col + co
                                if nr in range(ROW) and nc in range(COL) and grid[nr][nc] == '1':
                                    queue.append((nr, nc))
                                    grid[nr][nc] = "-2"
                else:
                    grid[r][c] = "-2"

        

        return count