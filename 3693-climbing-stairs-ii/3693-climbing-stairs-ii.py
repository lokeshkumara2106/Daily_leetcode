class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        def fun(ind):
            if ind==n:
                return 0
            ans=float('inf')
            for j in range(1,4):
                nxt=ind+j
                if nxt<=n:
                    ans=min(ans,costs[nxt-1] + ((nxt-ind)**2) + fun(nxt))
            return ans
        # return fun(0)
        dp=[float('inf')]*(n+1)
        dp[n]=0
        for ind in range(n-1,-1,-1):
            ans=float('inf')
            for j in range(1,4):
                nxt=ind+j
                if nxt<=n:
                    ans=min(ans,costs[nxt-1] + ((nxt-ind)**2) + dp[nxt])
            dp[ind]=ans
        return dp[0]