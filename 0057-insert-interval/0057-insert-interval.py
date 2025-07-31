class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        inserted = False


        for interval in intervals:
            # 왼쪽 벗어남
            if interval[1] < newInterval[0]:
                res.append(interval)
            # 오른쪽 벗어남 (new먼저 들어가고, interval append)
            elif interval[0] > newInterval[1]:
                if not inserted:
                    res.append(newInterval)
                    inserted = True
                res.append(interval)
            # merge needed
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        # new interval이 가장 오른쪽
        if not inserted:
            res.append(newInterval)
        return res

                
        