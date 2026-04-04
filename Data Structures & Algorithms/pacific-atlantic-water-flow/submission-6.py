class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        ans = []

        for r in range(ROW):
            for c in range(COL):
                is_pacific, is_atlantic = False, False
                visited = set()
                queue = deque([[r,c]])
                visited.add((r,c))
                while queue:
                    for _ in range(len(queue)):
                        row, col = queue.popleft()
                        for ro, co in [(-1,0),(0,-1),(1,0),(0,1)]:
                            n_row = row + ro
                            n_col = col + co
                            if n_row in range(ROW) and n_col in range(COL) and\
                            heights[row][col] >= heights[n_row][n_col] and \
                            (n_row,n_col) not in visited:
                                queue.append([n_row,n_col])
                                visited.add((n_row,n_col))
                            else:
                                if n_row < 0 or n_col < 0:
                                    is_pacific = True
                                if n_row >= ROW or n_col >= COL:
                                    is_atlantic = True

                if is_pacific and is_atlantic:
                    ans.append([r,c])
        
        return ans