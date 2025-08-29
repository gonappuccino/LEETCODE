class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_num = {0:1} 
        cnt = total = 0


        for num in nums:
            total += num
            if total - k in sub_num:
                cnt += sub_num[total-k]

            sub_num[total] = 1 + sub_num.get(total, 0)
        return cnt