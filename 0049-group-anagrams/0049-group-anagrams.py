class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            curr = sorted(s)
            curr = ''.join(curr)
            if curr in seen:
                seen[curr].append(s)
            else:
                seen[curr] = [s]
        res = []
        for first in seen:
            res.append(seen[first])
        return res