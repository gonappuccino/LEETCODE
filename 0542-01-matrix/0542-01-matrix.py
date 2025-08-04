class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dist = [[float('inf')]*cols for _ in range(rows)]
        queue =deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))

        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while(queue):
            i , j = queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if(0 <= ni < rows and 0 <= nj < cols):
                    if dist[ni][nj] > dist[i][j] + 1:
                        dist[ni][nj] = dist[i][j] + 1
                        queue.append((ni, nj))
        return dist
