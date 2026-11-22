class Solution:
    def checkString(self, s: str) -> bool:
        last_a=-1
        last_b=-1
        for i,c in enumerate(s):
            if c=='a' and last_b<i and last_b!=-1:
                return False
            if c=='a':
                last_a=i
            else:
                last_b=i
        return True