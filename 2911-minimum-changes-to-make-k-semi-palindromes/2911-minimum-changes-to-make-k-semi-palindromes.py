class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                for d in range(1, length):
                    if length % d != 0:
                        continue
                    changes = 0
                    groups = length // d
                    for r in range(d):
                        for t in range(groups // 2):
                            left = i + r + t * d
                            right = i + r + (groups - 1 - t) * d
                            if s[left] != s[right]:
                                changes += 1
                    cost[i][j] = min(cost[i][j], changes)
        # Recursive DP
        @lru_cache(None)
        def solve(i, parts):
            if parts == 0:
                return 0 if i == 0 else INF
            ans = INF
            for p in range(i - 1):
                previous = solve(p, parts - 1)
                if previous == INF:
                    continue
                current = previous + cost[p][i - 1]
                ans = min(ans, current)
            return ans
        return solve(n, k)