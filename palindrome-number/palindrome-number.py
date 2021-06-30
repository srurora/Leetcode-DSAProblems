class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        if x>0 and int(y[::-1])==x: return True
        elif x<0 :
            y = y[::-1]
            return y==str(x)
        elif x==0: return True
        else: return False
        