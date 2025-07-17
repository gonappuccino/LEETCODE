class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = [0] * 52
        cnt = 0
        first_odd = True
        
        for c in s:
            if 'a' <= c <= 'z':
                freq[ord(c) - ord('a')] += 1
            elif 'A' <= c <= 'Z':
                freq[ord(c) - ord('A') + 26] += 1
            

        for f in freq:
            if f % 2 == 0:
                cnt += f
            else:
                if first_odd:
                    cnt += f
                    first_odd = False
                else:
                    cnt += (f - 1)
        return cnt
                