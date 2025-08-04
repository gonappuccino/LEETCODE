class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = math.sqrt((point[0])**2 + (point[1])**2)
            heapq.heappush(heap, (-dist, [point[0],point[1]]))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for element in heap:
            res.append(element[1])

        return res
            