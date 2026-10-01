class Solution:
    def dfs(self, node , parent , adj, vis):
        if node in vis:
            return True
        vis.add(node)
        for n in adj[node]:
            if n == parent:
                continue
            else:
                if self.dfs(n, node, adj, vis):
                    return True
        return False
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)

        vis = set()
        if self.dfs(0, -1, adj, vis):
            return False

        return len(vis) == n 
        