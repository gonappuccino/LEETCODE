class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod_max = nums[0]
        curr_min = nums[0]
        curr_max = nums[0]

        for num in nums[1:]:
            if num < 0:
                curr_min, curr_max = curr_max, curr_min

            curr_min = min(num, num*curr_min)
            curr_max = max(num, num*curr_max)
            prod_max = max(prod_max, curr_max)
        return prod_max