"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}
        q = deque([node])
        visited[node] = Node(node.val) #original = new (only val)

        while q:
            curr = q.popleft()
            for ngbr in curr.neighbors:
                if ngbr not in visited:
                    visited[ngbr] = Node(ngbr.val)
                    q.append(ngbr)
                visited[curr].neighbors.append(visited[ngbr])
        return visited[node]
