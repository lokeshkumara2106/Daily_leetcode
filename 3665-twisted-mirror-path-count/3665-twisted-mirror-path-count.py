class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7

        down = [[-1] * n for _ in range(m)]
        right = [[-1] * n for _ in range(m)]

        dp = [[0] * n for _ in range(m)]
        dp[m-1][n-1] = 1

        # Precompute mirror transitions
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):

                if grid[i][j] == 0:
                    continue

                # Entered from above: reflect right
                if j+1 < n:
                    if grid[i][j+1] == 0:
                        down[i][j] = (i, j+1)
                    else:
                        down[i][j] = right[i][j+1]

                # Entered from left: reflect down
                if i+1 < m:
                    if grid[i+1][j] == 0:
                        right[i][j] = (i+1, j)
                    else:
                        right[i][j] = down[i+1][j]

        # Bottom-up DP
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):

                if i == m-1 and j == n-1:
                    continue

                ans = 0

                # Move down
                if i+1 < m:
                    if grid[i+1][j] == 0:
                        ans += dp[i+1][j]
                    else:
                        pos = down[i+1][j]
                        if pos != -1:
                            x, y = pos
                            ans += dp[x][y]

                # Move right
                if j+1 < n:
                    if grid[i][j+1] == 0:
                        ans += dp[i][j+1]
                    else:
                        pos = right[i][j+1]
                        if pos != -1:
                            x, y = pos
                            ans += dp[x][y]

                dp[i][j] = ans % MOD

        return dp[0][0]

        # def fun(i,j):
        #     if i>=m or j>=n:
        #         return 0
        #     if i==m-1 and j==n-1:
        #         return 1
        #     ans=0
        #     for dx,dy in [[1,0],[0,1]]:
        #         nx,ny=i+dx,j+dy
        #         if 0<=nx<m and 0<=ny<n:
        #             if grid[nx][ny]==1:
        #                 x,y=check(nx,ny,dx,dy)
        #                 if x!=-1:
        #                     ans+=fun(x,y)
        #             else:
        #                 ans+=fun(nx,ny)
        #     return ans
        # return fun(0,0)

        def check(x,y,dx,dy):
            if x>=m or y>=n:
                return -1,-1
            if grid[x][y]!=1:
                return x,y
            if dx==0:
                return check(x+1,y,1,0)
            else:
                return check(x,y+1,0,1)

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    continue
                ans=0
                for dx,dy in [[1,0],[0,1]]:
                    nx,ny=i+dx,j+dy
                    if 0<=nx<m and 0<=ny<n:
                        if grid[nx][ny]==1:
                            x,y=check(nx,ny,dx,dy)
                            if x!=-1:
                                ans=(ans+dp[x][y])%MOD
                        else:
                            ans=(ans+dp[nx][ny])%MOD
                dp[i][j]=ans
        return dp[0][0]%MOD