from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return [[]]
        
        rows, cols = len(image), len(image[0])
        visited = set()
        directions = ((0,1), (0,-1), (-1,0), (1,0))
        original_color = image[sr][sc]

        if original_color == color:
            return image  # 색이 이미 같으면 작업 안 함

        def traverse(i, j):
            queue = deque([(i, j)])
            while queue:
                curr_i, curr_j = queue.popleft()
                if (curr_i, curr_j) in visited:
                    continue
                if image[curr_i][curr_j] != original_color:
                    continue

                visited.add((curr_i, curr_j))
                image[curr_i][curr_j] = color  # 여기서 색칠

                for direction in directions:
                    next_i, next_j = curr_i + direction[0], curr_j + direction[1]
                    if 0 <= next_i < rows and 0 <= next_j < cols:
                        queue.append((next_i, next_j))

        traverse(sr, sc)
        return image