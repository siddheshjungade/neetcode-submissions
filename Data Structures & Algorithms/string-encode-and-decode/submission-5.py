class Solution:
    def encode(self, strs: List[str]) -> str:
        ans = []
        for i in strs:
            ans.append(f"{len(i)}#{i}")
        return ''.join(ans)

    def decode(self, s: str) -> List[str]:
        ans = []
        while s:
            wl = ""
            while s[0] != '#':
                wl += s[0]
                s = s[1:]
            wl = int(wl)
            s = s[1:]
            ans.append(s[:wl])
            s = s[wl:]
        
        return ans
