class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4,-1,-1,0,1,2]
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            complement = 0 - nums[i] #1
            left = i+1 #3
            right = len(nums)-1 #5
            #print(complement, left, right)
            while left < right:
                if nums[left] + nums[right] == complement:
                    #print('1')
                    res.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                    #print(res)
                elif nums[left] + nums[right] > complement:
                    #print('2')
                    right -= 1
                else:
                    #print('3')
                    left += 1
        return res