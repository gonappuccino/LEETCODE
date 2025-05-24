class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            dis = math.sqrt(point[0]**2 + point[1] **2)
            
            heapq.heappush(heap, (-dis, (point[0], point[1])))

            if len(heap) > k:
                heapq.heappop(heap)

        return [[point[1][0], point[1][1]] for point in heap]