class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return []
        
        rows, cols = len(mat), len(mat[0])
        dist=[[-1 for _ in range(cols)] for _ in range((rows))]
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i,j))

        while queue:
            i, j = queue.popleft()
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols and dist[next_i][next_j] == -1:
                    dist[next_i][next_j] = dist[i][j] + 1
                    queue.append((next_i, next_j))

        return dist