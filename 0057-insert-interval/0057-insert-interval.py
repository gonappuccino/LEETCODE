class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        inserted = False

        for interval in intervals:
            # outside - left
            if interval[1] < newInterval[0]:
                res.append(interval)
            # outside - right
            elif interval[0] > newInterval[1]:
                if not inserted:
                    res.append(newInterval)
                    inserted = True
                res.append(interval)
            # merge
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

            # newInterval = rightmost
        if not inserted:
            res.append(newInterval)
            
        return res

                
        