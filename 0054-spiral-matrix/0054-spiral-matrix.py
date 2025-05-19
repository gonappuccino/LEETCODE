class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # → 1. 왼 → 오
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1  # 위쪽 줄은 끝났으니까 한 칸 아래로

            # ↓ 2. 위 → 아래
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # 오른쪽 줄은 끝났으니까 한 칸 왼쪽으로

            # ← 3. 오 → 왼
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # ↑ 4. 아래 → 위
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result