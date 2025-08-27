class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        pac_start = [[0, j] for j in range(n)] + [[i, 0] for i in range(m)]
        atl_start = [[m-1, j] for j in range(n)] + [[i, n-1] for i in range(m)]

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def bfs(starts):
            vis = [[False]*n for _ in range(m)]
            q = deque(starts)
            for r, c in starts:
                if not vis[r][c]:
                    vis[r][c] = True
            
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m) and (0 <= nc < n) and not vis[nr][nc] and heights[nr][nc] >= heights[r][c]:
                        vis[nr][nc] = True
                        q.append((nr,nc))
            return vis
        
        pac = bfs(pac_start)
        atl = bfs(atl_start)

        return [[r,c] for r in range(m) for c in range(n) if pac[r][c] and atl[r][c]]