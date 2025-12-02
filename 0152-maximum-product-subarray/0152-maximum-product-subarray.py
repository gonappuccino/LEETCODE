class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod_max = curr_max = curr_min = nums[0]

        for num in nums[1:]:
            if num < 0:
                curr_max, curr_min = curr_min, curr_max
            curr_min = min(num, curr_min * num)
            curr_max = max(num, curr_max * num)
            prod_max = max(prod_max, max(curr_min, curr_max))
        return prod_max

            
            