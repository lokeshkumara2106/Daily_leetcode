class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""

        ans = ""

        while sum >= 9 and len(ans) < num:
            ans += "9"
            sum -= 9

        if sum > 0 and len(ans) < num:
            ans += str(sum)

        ans += "0" * (num - len(ans))

        return ans