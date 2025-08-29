class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        res = float('inf')
        curr = 0

        for right in range(len(nums)):
            curr += nums[right]
            while curr >= target:
                res = min(res, right - left + 1)
                curr -= nums[left]
                left += 1
        return 0 if res == float('inf') else res
            
