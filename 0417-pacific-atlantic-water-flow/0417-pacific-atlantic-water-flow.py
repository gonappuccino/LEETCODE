class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # cells where water can reach both Pacific and Atlantic
        # BFS: start from the ocean edges
        # left, top = the Pacific
        # right, bottom = the Atlantic
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])

        pac_start = [(0, j) for j in range(n)] + [(i, 0) for i in range(m)]
        atl_start = [(m-1, j) for j in range(n)] + [(i, n-1) for i in range(m)]
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def bfs(starts):
            vis = [[False]*n for _ in range(m)]
            q = deque(starts)
            for r, c in starts:
                vis[r][c] = True
            
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m) and (0 <= nc < n) and not vis[nr][nc] and heights[r][c] <= heights[nr][nc] :
                        vis[nr][nc] = True
                        q.append((nr,nc))
            return vis
        pacific = bfs(pac_start)
        atlantic = bfs(atl_start)

        return [[r, c] for r in range(m) for c in range(n) if pacific[r][c] and atlantic[r][c]]

        
        