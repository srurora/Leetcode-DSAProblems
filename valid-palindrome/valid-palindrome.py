class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = []
        for i in s: 
            if i.isalnum(): x.append(i)
        x = ''.join(str(e) for e in x)
        x=x.lower()
        return x[::-1]==x
        