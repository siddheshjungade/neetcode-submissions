class Solution:
    def dfs(self,node, parent, adj, vis):
        if node in vis:
            return False
        vis.add(node)
        for n in adj[node]:
            if n == parent:
                continue
            elif self.dfs(n,node,adj,vis) == False:
                return False
        return True
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        vis = set()
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        
        return self.dfs(0,-1,adj, vis) and len(vis) == n
        