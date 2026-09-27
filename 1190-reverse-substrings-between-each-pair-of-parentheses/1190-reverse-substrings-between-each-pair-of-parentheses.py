class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for c in s:
            if c == ')':
                res=''
                while stack[-1]!='(':
                    res+=stack.pop()
                stack.pop()
                stack.append(res[::-1])
            else:
                stack.append(c)
        res=''
        while stack:
            v=stack.pop()
            res+=v
        return res[::-1]