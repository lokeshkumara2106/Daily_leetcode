class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        mini=float('inf')
        for i in range(n):
            total=0
            count=0
            for j in range(i,n):
                count+=1
                total+=nums[j]
                if count<l:
                    continue
                if count>r:
                    break
                if total>0:
                    mini=min(mini,total)
        return mini if mini!=float('inf') else -1