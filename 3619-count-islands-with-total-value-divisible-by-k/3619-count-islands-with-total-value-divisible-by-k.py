class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        visited=set()
        def fun(x,y):
            visited.add((x,y))
            ans=grid[x][y]
            for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and grid[nx][ny]!=0 and (nx,ny) not in visited:
                    ans+=+fun(nx,ny)
            return ans
        m=len(grid)
        n=len(grid[0])
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0 and (i,j) not in visited:
                    val=fun(i,j)
                    if val%k==0:
                        count+=1
        return count