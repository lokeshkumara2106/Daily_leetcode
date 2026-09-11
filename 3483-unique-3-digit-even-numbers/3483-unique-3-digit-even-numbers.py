class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        d={}
        for num in digits:
            d[num]=d.get(num,0)+1
        def fun(path):
            if len(path)==3:
                if path[-1]%2==0:
                    return 1
                return 0
            ans=0
            for num in d:
                if d[num]==0:
                    continue
                if len(path)==0 and num==0:
                    continue
                d[num]-=1
                ans+=fun(path+[num])
                d[num]+=1
            return ans
        return fun([])