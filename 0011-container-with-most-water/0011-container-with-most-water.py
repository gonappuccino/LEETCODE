class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(height) - 1

        while (l < r):
            maxArea = max(maxArea, (r-l)*min(height[r],height[l]))
            if (height[l] < height[r]):
                l += 1
            elif (height[l] > height[r]):
                r -= 1
            else:
                l += 1
                r -= 1
        return maxArea