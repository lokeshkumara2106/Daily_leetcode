class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        # ans=[]
        # def fun(i,j,path):
        #     if i==m-1 and j ==n-1:
        #         ans.append(path[:])
        #         return
        #     for dx,dy in [[0,1],[1,0]]:
        #         nx,ny=i+dx,j+dy
        #         if 0<=nx<m and 0<=ny<n:
        #             fun(nx,ny,path+[grid[nx][ny]])
        # fun(0,0,[grid[0][0]])
        # mini=float('inf')
        # for sub in ans:
        #     xor=0
        #     for num in sub:
        #         xor^=num
        #     mini=min(mini,xor)
        # return mini

        dp=[[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])
        for i in range(m):
            for j in range(n):
                for val in dp[i][j]:
                    if i+1<m:
                        dp[i+1][j].add(val^grid[i+1][j])
                    if j+1<n:
                        dp[i][j+1].add(val^grid[i][j+1])
        return min(dp[m-1][n-1])