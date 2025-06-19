class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = defaultdict(int)
        len = 0
        for c in s:
            freq[c] += 1
        flag = 0
        for c in freq:
            if freq[c] % 2 == 0:
                len += freq[c]
            else:
                if flag == 1:
                    len += (freq[c] - 1)
                else:
                    len += freq[c]
                    flag = 1
        return len