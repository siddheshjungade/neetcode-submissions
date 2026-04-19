from collections import deque
class Solution:
    def bfs(self, start, adj, vis):
        q = deque()
        q.append([start, -1])
        vis.add(start)
        while q:
            current = q.popleft()
            node = current[0]
            parent = current[1]
            for n in adj[node]:
                if n == parent:
                    continue
                if n not in vis:
                    q.append([n, node])
                    vis.add(n)

    # def dfs(self,node, parent, adj, vis):
    #     if node in vis:
    #         return
    #     vis.add(node)
    #     for n in adj[node]:
    #         if parent == n:
    #             continue
    #         else:
    #             self.dfs(n, node, adj, vis)
    #     return

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        vis = set()
        
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        count = 0
        for node in range(n):
            if node not in vis:
                self.bfs(node, adj, vis)
                count += 1
            
        return count