class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = ((0,1), (0,-1), (1,0), (-1,0))

        def traverse(i, j):
            queue = deque([(i, j)])
            while queue:
                curr_i,curr_j = queue.popleft()
                if grid[curr_i][curr_j] == '0':
                    continue
                if (curr_i, curr_j) not in visited:
                    visited.add((curr_i, curr_j))

                    for direction in directions:
                        next_i, next_j = curr_i + direction[0], curr_j + direction[1]
                        if 0 <= next_i < rows and 0<= next_j < cols:
                            queue.append((next_i, next_j))
                    
        island = 0
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and (grid[i][j] == '1'):
                    traverse(i,j)
                    island += 1
        return island