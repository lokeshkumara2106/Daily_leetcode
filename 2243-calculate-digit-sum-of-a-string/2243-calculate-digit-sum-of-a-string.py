class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            temp=''
            for i in range(0,len(s),k):
                temp+=str(sum(int(val) for val in s[i:min(i+k,len(s))]))
            s=temp
        return s