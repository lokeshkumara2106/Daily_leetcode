class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target=sum(nums)-x
        if target==0:
            return len(nums)
        if target<0:
            return -1
        maxi=-1
        left=curr=0
        for right in range(len(nums)):
            curr+=nums[right]
            while curr>target:
                curr-=nums[left]
                left+=1
            if curr==target:
                maxi=max(maxi,right-left+1)
        if maxi==-1:
            return -1
        return len(nums)-maxi