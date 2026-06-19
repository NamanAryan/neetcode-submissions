class Solution:
    def isPathCrossing(self, path: str) -> bool:
        direction = {
            "N" : (0, 1),
            "S" : (0, -1),
            "E" : (1, 0),
            "W" : (-1, 0)
        }

        visited = {(0, 0)}
        x, y = 0, 0
        for i in path:
            dx, dy = direction[i]
            x += dx
            y += dy

            if (x, y) in visited:
                return True

            visited.add((x, y))      

        return False  