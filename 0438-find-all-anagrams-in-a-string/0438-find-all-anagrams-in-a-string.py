class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls = len(s)
        lp = len(p)
        res = []

        if ls < lp:
            return []

        need = Counter(p)
        window = Counter(s[:lp])

        if window == need:
            res.append(0)

        left = 0

        for right in range(lp, ls):
            window[s[left]] -= 1
            window[s[right]] += 1

            if window[s[left]] == 0:
                del window[s[left]]
            left += 1

            if window == need:
                res.append(left)
        return res