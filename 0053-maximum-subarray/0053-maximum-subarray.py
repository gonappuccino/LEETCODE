class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane's algorithm
        #지금까지의 합이 음수면 버려
        curr_sum = float('-inf')
        max_sum = float('-inf')

        for num in nums:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(curr_sum, max_sum)
        return max_sum

        
        