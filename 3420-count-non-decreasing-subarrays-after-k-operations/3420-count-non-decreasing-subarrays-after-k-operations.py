class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        dq=deque()
        n=len(nums)
        op=0
        r=n-1
        res=0
        for l in range(n-1,-1,-1):
            nsize=1
            while dq and dq[-1][0]<nums[l]:
                height,size=dq.pop()
                op+=(nums[l]-height)*size
                nsize+=size
            dq.append([nums[l],nsize])
            while op>k:
                op-= dq[0][0]-nums[r]
                dq[0][1]-=1
                if dq[0][1]==0:
                    dq.popleft()
                r-=1
            res+= (r-l+1)
        return res