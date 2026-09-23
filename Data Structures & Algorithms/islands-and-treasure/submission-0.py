from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        count_frequency = 0
        ROW, COL = len(grid), len(grid[0])
        q = deque()
        INF = 2147483647


        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    q.append((i,j))
                
        while q:
            count_frequency += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                if r - 1 >= 0 and grid[r-1][c] == INF:
                    grid[r-1][c] = count_frequency
                    q.append((r-1, c))
                
                if c - 1 >= 0 and grid[r][c-1] == INF:
                    grid[r][c-1] = count_frequency
                    q.append((r, c-1))
                
                if c + 1 < COL and grid[r][c+1] == INF:
                    grid[r][c+1] = count_frequency
                    q.append((r, c+1))
                
                if r + 1 < ROW and grid[r + 1][c] == INF:
                    grid[r + 1][c] = count_frequency
                    q.append((r+1, c))












