class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        m, n = len(p), len(s)
        if m > n:
            return []
        
        res = []
        need = Counter(p)
        window = Counter(s[:m])

        if window == need:
            res.append(0)


        left = 0 
        for right in range(m, n):
            window[s[right]] += 1
            window[s[left]] -= 1

            if window[s[left]] == 0:
                del window[s[left]]
            left += 1

            if window == need:
                res.append(left)
        return res
