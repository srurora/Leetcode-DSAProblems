class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n==0: return 0
        x = math.factorial(n)
        x = str(x)
        print(x)
        ans=0
        if len(x)==1: return 0
        for i in range(len(x)-1,-1,-1):
            if x[i]=='0' and x[i-1]!='0': return ans+1
            elif x[i]=='0': ans+=1
        return ans
        