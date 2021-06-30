class Solution:
    def reverse(self, x: int) -> int:
        b = 2**31
        neg_b = -1*b
        rev = 0
        if x>0: 
            while x!=0:
                digit = x%10
                x//=10
                rev = rev*10 + digit
        else: 
            x = abs(x)
            while x!=0:
                digit=x%10
                x//=10
                rev=rev*10+digit
            rev*=-1
        if rev>b or rev<neg_b: return 0
        return rev