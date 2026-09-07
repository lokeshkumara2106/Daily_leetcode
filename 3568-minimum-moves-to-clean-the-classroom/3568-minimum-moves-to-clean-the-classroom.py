from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        locations = {}
        count = 0
        sx = sy = -1

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'L':
                    locations[(i, j)] = count
                    count += 1
                elif classroom[i][j] == 'S':
                    sx, sy = i, j

        full = (1 << count) - 1

        q = deque()
        q.append((sx, sy, energy, 0, 0))

        visited = set()
        visited.add((sx, sy, energy, 0))

        while q:
            x, y, ene, mask, moves = q.popleft()

            if mask == full:
                return moves

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + dx
                ny = y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue

                if classroom[nx][ny] == 'X':
                    continue

                newene = ene - 1

                if newene < 0:
                    continue

                newmask = mask

                if classroom[nx][ny] == 'L':
                    idx = locations[(nx, ny)]
                    newmask |= 1 << idx

                if classroom[nx][ny] == 'R':
                    newene = energy

                state = (nx, ny, newene, newmask)

                if state not in visited:
                    visited.add(state)
                    q.append((nx, ny, newene, newmask, moves + 1))

        return -1