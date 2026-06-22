class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for r in range(ROWS):
            for c in range(COLS):
                
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        dist = 0
        while q:
            for _ in range(len(q)):
                R, C = q.popleft()
                grid[R][C] = dist
                
                for dr, dc in direction:
                    row = dr + R
                    col = dc + C
                    if (row < 0 or
                        col < 0 or
                        row >= ROWS or
                        col >= COLS or
                        grid[row][col] == -1 or
                        (row, col) in visit):
                        continue
                    visit.add((row, col))
                    q.append((row, col))
            dist += 1


