class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=0
        n=len(s)
        i=0
        while i<n:
            if s[i]=='(':
                depth=1
                j=i+1
                maxi=max(maxi,depth)
                while depth:
                    if s[j]=='(':
                        depth+=1
                    elif s[j]==')':
                        depth-=1
                    maxi=max(maxi,depth)
                    j+=1
                i=j
            i+=1
        return maxi