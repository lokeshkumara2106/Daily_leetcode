class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if stack:
                if char==')' and stack[-1]=='(':
                    stack.pop(-1)
                elif char==']' and stack[-1]=='[':
                    stack.pop(-1)
                elif char=='}' and stack[-1]=='{':
                    stack.pop(-1)
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return False if stack else True
            