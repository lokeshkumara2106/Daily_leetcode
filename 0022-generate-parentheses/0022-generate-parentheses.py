class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def fun(s,left,right):
            if len(s)==2*n:
                res.append(s)
                return
            if left<n:
                fun(s+'(',left+1,right)
            if right<left:
                fun(s+')',left,right+1)
        fun('',0,0)
        return res
