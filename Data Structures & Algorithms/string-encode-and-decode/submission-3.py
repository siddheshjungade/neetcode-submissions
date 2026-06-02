class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs:
            len(i)
            ans += f"{len(i)}#{i}"
        print(ans)
        return ans

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
        print(ans)
        return ans
