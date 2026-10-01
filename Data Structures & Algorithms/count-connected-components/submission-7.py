class Solution:
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return False
        
        if self.rank[rootA] < self.rank[rootB]:
            rootA, rootB = rootB, rootA

        self.parent[rootB] = rootA

        if self.rank[rootA] == self.rank[rootB]:
            self.rank[rootA] += 1
        return True
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.parent = [i for i in range(n)]
        self.rank = [0] * (n)
        ans = 0
        for u , v in edges:
            
            self.union(u - 1, v -1)

        return max(ans, len(set([self.find(i) for i in self.parent])))
        
        