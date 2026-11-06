
class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])

        q = sorted((t, i) for i, t in enumerate(queries))

        freq = {}
        ans = [0] * len(queries)

        left = right = 0
        active = 0

        for time, idx in q:
            start = time - x

            # Add logs within the right boundary
            while right < len(logs) and logs[right][1] <= time:
                s = logs[right][0]
                freq[s] = freq.get(s, 0) + 1

                if freq[s] == 1:
                    active += 1

                right += 1

            # Remove logs before the left boundary
            while left < right and logs[left][1] < start:
                s = logs[left][0]
                freq[s] -= 1

                if freq[s] == 0:
                    active -= 1

                left += 1

            ans[idx] = n - active

        return ans
