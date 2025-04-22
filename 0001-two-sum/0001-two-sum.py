class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if hash_map.get(complement) != None:
                return [hash_map[complement], i]
            hash_map[nums[i]] = i
        return []