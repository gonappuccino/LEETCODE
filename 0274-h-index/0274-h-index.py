class Solution:
    def hIndex(self, citations: List[int]) -> int:
        freq = [0]*1001
        #[0,0,0,0]

        for i in range(len(citations)):
            for j in range(citations[i]+1):
                freq[j] += 1
        # print(freq[:6])

        for i in range(len(freq)):
            if freq[i] >= i:
                res = i
                # print(res)
        return res