class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        if not rows or not cols:
            return 0
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    res += 1
                    grid[r][c] = '0'
                    q = deque([(r, c)])
                    while q:
                        i, j = q.popleft()

                        for di, dj in directions:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == '1':
                                grid[ni][nj] = '0'
                                q.append((ni, nj))
        return res
            

        