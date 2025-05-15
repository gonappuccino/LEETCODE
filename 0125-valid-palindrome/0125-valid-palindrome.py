class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        s_letter = ''.join([ch for ch in s_lower if ch.isalnum()])
        left = 0
        right = len(s_letter)-1


        while left <= right:
            if s_letter[left] != s_letter[right]:
                return False
            left += 1
            right -= 1
        return True