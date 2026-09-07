class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        len(nums)
        maxi=[0]*n
        mini=[0]*n
        maxi[0]=nums[0]
        res=float('inf')
        for i in range(1,n):
            maxi[i]=max(maxi[i-1],nums[i])
        mini[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            mini[i]=min(mini[i+1],nums[i])
        for i in range(n):
            score=maxi[i]-mini[i]
            if score<=k and i<res:
                res=i
        return res if res!=float('inf') else -1