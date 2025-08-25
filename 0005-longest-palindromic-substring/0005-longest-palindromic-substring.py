class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        def expand(l: int, r: int) -> list[int]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return [l + 1, r - 1]
        
        start = end = 0

        for i in range(len(s)):
            #odd
            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i + 1)

            if r1 - l1 > end - start:
                end, start = r1, l1
            if r2 - l2 > end - start:
                end, start = r2, l2
        return s[start: end + 1]

        
                