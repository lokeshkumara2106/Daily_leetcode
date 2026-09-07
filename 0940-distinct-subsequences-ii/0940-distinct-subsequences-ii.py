class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD=10**9 + 7
        curr=1
        dp={}
        for c in s:
            new_curr=2*curr
            if c in dp:
                new_curr-=dp[c]
            dp[c]=curr
            curr=new_curr%MOD
        return (curr-1)%MOD