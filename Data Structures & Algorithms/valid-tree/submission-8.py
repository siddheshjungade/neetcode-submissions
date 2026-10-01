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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.parent = [i for i in range(n)]
        self.rank = [0] * (n)
        for u , v in edges:
            if self.union(u - 1, v -1) == False:
                return False
        

        return len(set([self.find(x) for x in self.parent])) == 1
        