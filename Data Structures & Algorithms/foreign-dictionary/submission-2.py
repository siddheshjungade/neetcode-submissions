class Solution:
    def dfs(self,node,adj, st,vis):
        if node in vis:
            return vis[node]
        vis[node] = True
        for neighbor in adj[node]:
            if self.dfs(neighbor, adj, st, vis):
                return True
        st.append(node) 
        vis[node] = False   
        return False
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        vis = {}
        st = []
        for i in range(0,len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for i in range(minLen):
                if w1[i] != w2[i]:
                    adj[w1[i]].add(w2[i])
                    break

        for i in adj:
            if self.dfs(i, adj,st,vis):
                return ""
                
        print(st)
        return ''.join(st[::-1])



        