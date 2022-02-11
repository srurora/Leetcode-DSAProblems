#User function Template for python3

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        
        # code here
        dp = [-1 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        if n >= 2:
            dp[2] = 2
        if n >= 3:
            dp[3] = 4
        if n > 3:
            for i in range(4,n+1):
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
                
        return dp[n]%1000000007
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))
# } Driver Code Ends