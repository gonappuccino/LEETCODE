class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        cnt = [0] * (n+1)
        for c in citations:
            if c >= n:
                cnt[n] += 1
            else:
                cnt[c] += 1
        
        total = 0
        for h in range(n, -1, -1):
            total += cnt[h]
            if total >= h:
                return h