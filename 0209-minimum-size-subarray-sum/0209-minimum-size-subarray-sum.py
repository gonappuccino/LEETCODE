class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_sum = float('inf')
        curr = 0

        for right in range(len(nums)):
            curr += nums[right]

            while curr >= target:
                min_sum = min(min_sum, right - left + 1)
                curr -= nums[left]
                left += 1
        return 0 if min_sum == float('inf') else min_sum


            
