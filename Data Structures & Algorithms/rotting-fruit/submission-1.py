class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        freshOranges = 0
        q = deque()
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        time = 0
        visit = set()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    freshOranges += 1
                elif grid[row][col] == 2:
                    q.append((row, col))
        
        while q and freshOranges > 0:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                for dr, dc in direction:
                    C, R = dc + c, dr + r
                    if (C < 0 or
                        R < 0 or
                        C >= COLS or
                        R >= ROWS or
                        (R, C) in visit or
                        grid[R][C] != 1) :
                        continue
                    
                    freshOranges -= 1
                    visit.add((R, C))
                    q.append((R, C))
                             
        return time if freshOranges == 0 else -1


        