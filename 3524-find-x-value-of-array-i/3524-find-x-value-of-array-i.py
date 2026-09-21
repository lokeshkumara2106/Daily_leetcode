class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        dp=[[0]*k for _ in range(n)]
        for i in range(n):
            dp[i][nums[i]%k]+=1
            if i==0: continue
            for j in range(k):
                dp[i][(j*nums[i])%k]+=dp[i-1][j]
        res=[0]*k
        for i in range(n):
            for j in range(k):
                res[j]+=dp[i][j]
        return res