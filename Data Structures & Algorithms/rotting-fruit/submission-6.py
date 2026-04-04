class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        found = set()

        ROW, COL = len(grid), len(grid[0])
        number_of_fresh = 0
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 2:
                    queue.append((row, col))
                if grid[row][col] == 1:
                    number_of_fresh += 1
        
        time = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for neighbor in self.get_neighbor(grid, row, col, ROW, COL):
                    if neighbor not in found:
                        queue.append(neighbor)
                        found.add(neighbor)
                        number_of_fresh -= 1
            if queue:
                time += 1
        return time if number_of_fresh == 0 else -1
    
    def get_neighbor(self, grid, row, col, ROW, COL):
        neighbor = []
        for ro, co in [(-1,0), (0,-1), (1,0), (0,1)]:
            if 0 <= row + ro and row + ro < ROW and\
            0 <= col + co and col + co < COL and\
            grid[row + ro][col + co] == 1:
                neighbor.append((row + ro, col + co))
        
        return neighbor
            
        