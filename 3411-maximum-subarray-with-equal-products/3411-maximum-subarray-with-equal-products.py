class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def fun1(a,b):
            while b:
                a,b=b,a%b
            return a
        n=len(nums)
        maxii=0
        for i in range(n):
            lcm=1
            gcd=0
            prod=1
            for j in range(i,n):
                x=nums[j]
                prod*=x
                gcd=fun1(gcd,x)
                lcm=(lcm*x)//fun1(lcm,x)
                if prod == (lcm*gcd):
                    maxii=max(maxii,j-i+1)
        return maxii