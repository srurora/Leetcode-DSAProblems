#User function Template for python3

import sys
class Solution:
    
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        cuts = [x,y,z]
        dp = [-sys.maxsize for i in range(n+1)]
        dp[0]=0
        for i in range(n+1):
            for j in range(3):
                if cuts[j]<=i:
                    dp[i]=max(dp[i], dp[i-cuts[j]]+1)
        if dp[n]<0: return 0
        else: return dp[-1]
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        x,y,z=[int(x) for x in input().split()]
        
        print(Solution().maximizeTheCuts(n,x,y,z))
# } Driver Code Ends