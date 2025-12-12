class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_curr = min_curr = max_prod = nums[0]

        for num in nums[1:]:
            if num < 0:
                max_curr ,min_curr = min_curr, max_curr
            max_curr = max(num, max_curr*num)
            min_curr = min(num, min_curr*num)
            max_prod = max(max_prod, max_curr)
        return max_prod

            
            