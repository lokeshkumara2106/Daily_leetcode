class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy = []
        available = SortedList(range(k))
        count = [0] * k
        for i in range(len(arrival)):
            while busy and busy[0][0] <= arrival[i]:
                end, server = heapq.heappop(busy)
                available.add(server)
            if not available:
                continue
            idx = available.bisect_left(i % k)
            if idx == len(available):
                idx = 0
            server = available.pop(idx)
            count[server] += 1
            heapq.heappush(busy,(arrival[i] + load[i], server))
        mx = max(count)
        return [i for i in range(k) if count[i] == mx]