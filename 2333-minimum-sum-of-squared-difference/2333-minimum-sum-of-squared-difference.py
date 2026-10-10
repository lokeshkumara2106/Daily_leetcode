class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        dif=[]
        for i in range(len(nums1)):
            dif.append(abs(nums1[i]-nums2[i]))
        m=max(dif)
        d=[0]*(m+1)
        for num in dif:
            d[num]+=1
        k=k1+k2
        for i in range(m,0,-1):
            moves=min(d[i],k)
            d[i]-=moves
            d[i-1]+=moves
            k-=moves
            if k==0:
                break
        res=0
        for i in range(m+1):
            res+= (i**2 * d[i])
        return res