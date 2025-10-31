class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        [1,5,3,4],6

        for i in range(len(nums)):
            comp = target - nums[i]
            if nums[i] in seen:
                return [seen[nums[i]], i]
            seen[comp] = i
        return []