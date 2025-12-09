class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq ={}

        for i, num in enumerate(nums):
            c = target - num
            if c in freq:
                return [freq[c], i]
            freq[num] = i
        return []
