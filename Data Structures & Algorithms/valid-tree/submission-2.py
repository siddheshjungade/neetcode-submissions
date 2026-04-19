from collections import deque

class Solution:
    def bfs(self,start, adj, vis):
        q = deque()
        q.append([start, -1])
        vis.add(start) 
        while q:
            current = q.popleft()
            node = current[0]
            parent = current[1]
            for neighbor in adj[node]:
                if neighbor not in vis:
                    q.append([neighbor,node])
                    vis.add(neighbor)
                elif neighbor != parent:
                    return False
        return True



    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        vis = set()
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)

        return self.bfs(0,adj, vis) and len(vis) == n
        