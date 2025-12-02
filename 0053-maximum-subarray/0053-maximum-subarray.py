class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = max_res = nums[0]

        for num in nums[1:]:
            curr = max(num, curr + num)
            max_res = max(max_res, curr)
        return max_res

        

