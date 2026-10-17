class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(num):
            return sum(map(int, str(num)))

        arr = sorted(
            [(digit_sum(num), num, i) for i, num in enumerate(nums)]
        )

        visited = [False] * len(nums)
        swaps = 0

        for i in range(len(nums)):
            if visited[i] or arr[i][2] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps