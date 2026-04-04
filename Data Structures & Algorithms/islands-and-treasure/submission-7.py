class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROW, COL = len(grid), len(grid[0])

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    # do bfs
                    queue = deque()
                    visited = set()
                    for neighbor in self.get_neighbor(grid, r, c, ROW, COL):
                        queue.append(neighbor)
                    step = 1
                    while queue:
                        length = len(queue)
                        for _ in range(length):
                            row, col = queue.popleft()
                            visited.add((row,col))
                            grid[row][col] = min(grid[row][col], step)
                            for neighbor in self.get_neighbor(grid, row, col, ROW, COL):
                                if neighbor not in visited:
                                    queue.append(neighbor)
                        step += 1

    
    def get_neighbor(self, grid, r, c, ROW, COL):
        neighbor_list = []
        for r_o, c_o in [(-1,0),(0,-1),(1,0),(0,1)]:
            n_r = r + r_o
            n_c = c + c_o
            if 0 <= n_r and n_r < ROW and 0 <= n_c and n_c < COL and grid[n_r][n_c] != -1 and grid[n_r][n_c] != 0:
                neighbor_list.append((n_r, n_c))
        return neighbor_list

