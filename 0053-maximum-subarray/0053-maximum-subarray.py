class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = float('-inf')
        max_res = float('-inf')

        for num in nums:
            curr += num
            if curr <= num:
                curr = num
            max_res = max(max_res, curr)
        return max_res

        

