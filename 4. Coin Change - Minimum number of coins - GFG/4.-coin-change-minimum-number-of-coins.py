#{ 
#Driver Code Starts
#Initial Template for Python 3


 # } Driver Code Ends
#User function Template for python3


import sys
class Solution:
    #Function to find the minimum number of coins to make the change 
    #for value using the coins of given denominations.
    def minimumNumberOfCoins(self,coins,numberOfCoins,value):
        
        # your code here
        dp = [sys.maxsize for i in range(value+1)]
        dp[0]=0
        for i in range(1,value+1):
            for j in range(numberOfCoins):
                if coins[j]<=i:
                    dp[i]=min(dp[i],dp[i-coins[j]]+1)
        if dp[-1]==sys.maxsize: return "Not Possible"
        else: return dp[-1]
#{ 
#Driver Code Starts.

import sys
sys.setrecursionlimit(10**6)

def main():
    testcases=int(input())
    while(testcases>0):
        value=int(input())
        numberOfCoins=int(input())
        coins=[int(x) for x in input().strip().split()]
        answer=Solution().minimumNumberOfCoins(coins,numberOfCoins,value)
        print("Not Possible") if answer == -1 else print(answer)
        testcases-=1

if __name__=="__main__":
    main()
    
#} Driver Code Ends