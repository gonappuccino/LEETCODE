class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        left = 0
        max_f = 0
        ans = 0

        for right, ch in enumerate(s):

            cnt[ch] += 1
            max_f = max(max_f, cnt[ch])

            while (right - left + 1) - max_f > k:
                cnt[s[left]] -= 1
                left += 1
            
            ans =max(ans, right - left + 1)
        return ans