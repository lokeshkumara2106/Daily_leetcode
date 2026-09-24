class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def getDigits(num):
            res=0
            while num>0:
                res+=num%10
                num//=10
            return res
        for i in range(len(nums)):
            if getDigits(nums[i])==i:
                return i
        return -1