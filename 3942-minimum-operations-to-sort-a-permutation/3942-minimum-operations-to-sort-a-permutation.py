class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def check(arr):
            k = arr.index(0)

            for i in range(n):
                if arr[(k + i) % n] != i:
                    return -1

            return k

        # Option 1: Rotate the original array
        k = check(nums)
        ans = float('inf')

        if k != -1:
            ans = min(k, n - k + 2)

        # Option 2: Reverse, then rotate
        k = check(nums[::-1])

        if k != -1:
            ans = min(ans, min(k, n - k) + 1)

        return ans if ans != float('inf') else -1