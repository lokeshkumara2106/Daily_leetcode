class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        mini,maxi=min(s),max(s)
        if all(a<=b for a,b in zip(s,s[1:])):
            return 0
        if n==2:
            return -1
        if s[0]==mini or s[-1]==maxi:
            return 1
        for i in range(1,n-1):
            if s[i]==maxi or s[i]==mini:
                return 2
        return 3