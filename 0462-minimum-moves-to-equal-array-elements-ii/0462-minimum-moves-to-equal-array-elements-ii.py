class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        total=0
        n=len(nums)
        mid=n//2
        v=nums[mid]
        for num in nums:
            total+= abs(v-num)
        return total