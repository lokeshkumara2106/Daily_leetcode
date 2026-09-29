class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m=len(grid)
        n=len(grid[0])
        dp={}
        def fun(i,j,path):
            if path<0:
                return False
            if i==m-1 and j==n-1:
                return path==0
            if (i,j,path) in dp:
                return dp[(i,j,path)]
            if i+1<m:
                val= 1 if grid[i+1][j]=='(' else -1
                if fun(i+1,j,path+val):
                    dp[(i,j,path)] =True
                    return dp[(i,j,path)]
            if j+1<n:
                val= 1 if grid[i][j+1]=='(' else -1
                if fun(i,j+1,path+val):
                    dp[(i,j,path)]= True
                    return dp[(i,j,path)]
            dp[(i,j,path)]=False
            return dp[(i,j,path)]
        val= 1 if grid[0][0]=='(' else -1
        return fun(0,0,val)