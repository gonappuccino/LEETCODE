class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [0, 1, 2]
        # [[2, 1], [1, 0]]
        # cycle detection
        # bfs, node, num of prereq

        
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        cnt = 0

        while q:
            curr = q.popleft()
            cnt += 1

            for linked in graph[curr]:
                indegree[linked] -= 1
                if(indegree[linked] == 0):
                    q.append(linked)
        return numCourses == cnt



        
        




