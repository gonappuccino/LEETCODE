class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n #[1,1,1,1]
        right = [1] * n #[1,1,1,1]
        

        
        aggr = 1
        for i in range(n-1):
            aggr *= nums[i]
            left[i+1] = aggr
           
        
        
        aggr = 1
        for i in range(n-1, 0, -1):
            aggr *= nums[i]
            left[i-1] = aggr * left[i-1]

        return left
