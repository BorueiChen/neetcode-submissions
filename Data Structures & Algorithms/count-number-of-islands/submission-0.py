class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROW, COL = len(grid), len(grid[0])
        count = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    # do bfs
                    queue = deque([(r,c)])
                    grid[r][c] = "-1"
                    while queue:
                        length = len(queue)
                        for _ in range(length):
                            node = queue.popleft()
                            # get valid neighbor of node
                            for row_offset, col_offset in zip([-1, 0, 1, 0], [0, -1, 0, 1]):
                                n_r = node[0]+row_offset
                                n_c = node[1]+col_offset
                                if n_r < ROW and 0 <= n_r and n_c < COL and 0 <= n_c and grid[n_r][n_c] == "1":
                                    queue.append((n_r, n_c))
                                    grid[n_r][n_c] = "-1"

                    count += 1
                elif grid[r][c] == "0":
                    grid[r][c] = "-1"
                else:
                    # do nothing
                    pass
        return count
