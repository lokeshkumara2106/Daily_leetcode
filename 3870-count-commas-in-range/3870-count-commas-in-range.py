class Solution:
    def countCommas(self, n: int) -> int:
        start=1000
        total=0
        while start<=n:
            total+=(n-start+1)
            start*=1000
        return total