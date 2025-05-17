class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        

        def backtracking(start: int, path: list[int]):
            #base case
            if len(path) == k:
                result.append(path[:])
                return
            
            for i in range(start, n+1):
                path.append(i)
                # second number
                backtracking(i+1, path)
                path.pop()
            
        backtracking(1, [])
        return result