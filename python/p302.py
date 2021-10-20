class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        x1, y1 = x, y
        x2, y2 = x, y
        n, m = len(image), len(image[0])
        for i in range(n):
            for j in range(m):
                if image[i][j] == "1":
                    x1, y1 = min(x1, i), min(y1, j)
                    x2, y2 = max(x2, i), max(y2, j)
        return (x2 - x1) * (y2 - y1)
