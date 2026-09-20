class Solution:
    def reverseDegree(self, s: str) -> int:
        total=0
        for i,c in enumerate(s,start=1):
            val=26-(ord(c)-ord('a'))
            total+=(i*val)
        return total