class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = []
        busy = []

        n = len(servers)

        for i in range(n):
            heapq.heappush(available, (servers[i], i))

        ans = []
        time = 0

        for i, task in enumerate(tasks):

            time = max(time, i)

            # Move completed servers to available heap
            while busy and busy[0][0] <= time:
                finish, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            # If no server is available, wait
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    finish, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))

            # Select the best available server
            weight, idx = heapq.heappop(available)

            ans.append(idx)

            # Mark server as busy
            heapq.heappush(
                busy,
                (time + task, weight, idx)
            )

        return ans