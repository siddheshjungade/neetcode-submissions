class Solution:
    def dfs(self,node, adj, vis):
        if node in vis:
            return
        vis.add(node)
        for n in adj[node]:
            if n not in vis:
                self.dfs(n, adj, vis)
        return

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        vis = set()
        
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        count = 0
        for node in range(n):
            if node not in vis:
                self.dfs(node, adj, vis)
                count += 1
            
        return count