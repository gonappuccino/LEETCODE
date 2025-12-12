class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            sorted_s = sorted(s)
            sorted_s = ''.join(sorted_s)
            group[sorted_s].append(s)
        return list(group.values())

        
        