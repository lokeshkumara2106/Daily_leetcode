class Solution:
    def canAliceWin(self, n: int) -> bool:
        prev=11
        count=0
        while n>=(prev-1):
            n-=(prev-1)
            prev-=1
            count+=1
        return count%2==1