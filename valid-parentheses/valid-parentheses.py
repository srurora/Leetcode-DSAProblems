class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s: 
            if i=='[' or i=='{' or i=='(': stack.append(i)
            else:
                if not stack: return False
                x = stack.pop(-1)
                if i==']' and x!='[': return False
                elif i=='}' and x!='{': return False
                elif i==')' and x!='(': return False
        if stack: return False
        else: return True
                