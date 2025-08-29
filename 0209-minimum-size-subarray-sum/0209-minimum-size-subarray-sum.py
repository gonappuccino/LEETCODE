class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_len = float('inf')
        curr_sums = 0

        for right in range(len(nums)):
            curr_sums += nums[right]
            while curr_sums >= target:
                min_len = min(min_len, right - left + 1)
                curr_sums -= nums[left]
                left += 1
        return 0 if min_len == float('inf') else min_len
