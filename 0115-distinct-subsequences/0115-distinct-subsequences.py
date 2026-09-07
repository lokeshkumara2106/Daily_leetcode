class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        dp={}
        def fun(i,j):
            if j==n:
                return 1
            if i==m:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            take=0
            if s[i]==t[j]:
                take+=fun(i+1,j+1)+fun(i+1,j)
            nott=fun(i+1,j)
            dp[(i,j)]= max(take,nott)
            return dp[(i,j)]
        return fun(0,0)