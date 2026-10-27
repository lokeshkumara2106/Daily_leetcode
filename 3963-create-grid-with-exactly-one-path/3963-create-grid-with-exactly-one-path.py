class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        arr = [['#'] * n for _ in range(m)]

        for j in range(n):
            arr[0][j] = '.'

        for i in range(m):
            arr[i][n - 1] = '.'

        return [''.join(row) for row in arr]