class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*46
        dp[0]=1; dp[1]=2;dp[2]=3;
        if n<3: return dp[n-1]
        for i in range(3,n):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n-1]
            
        