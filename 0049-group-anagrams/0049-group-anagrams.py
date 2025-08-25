class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            new_s = "".join(sorted(s))
            if new_s in seen:
                seen[new_s].append(s)
            else:
                seen[new_s] = [s]
        
        res = []
        for v in seen.values():
            res.append(v)
        return res