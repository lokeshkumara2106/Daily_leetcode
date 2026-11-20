class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        d={}
        for num in nums:
            d[num+1]=max(d.get(num+1,0),d.get(num,0)+1)
            d[num]=max(d.get(num-1,0)+1,d.get(num,0))
        return max(d.values())