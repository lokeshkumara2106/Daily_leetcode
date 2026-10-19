class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l=0
        r=len(nums)-1
        res=set()
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                res.add(m)
                for i in range(m+1,r+1):
                    if nums[i]==target:
                        res.add(i)
            if nums[m]<target:
                if nums[l]==target:
                    res.add(l)
                l=m+1
            else:
                if nums[r]==target:
                    res.add(r)
                r=m-1
        return sorted(list(res))